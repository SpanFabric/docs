"""Cross-document regression coverage for active versus superseded governance.

The test deliberately uses only the standard library because it guards the same
portable verification surface as the Manual Verification Bridge.  It reads the small,
stable YAML shapes used by the registry and state projections instead of depending on a
runtime YAML package.
"""
from __future__ import annotations

import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


sys.dont_write_bytecode = True

REPO = Path(__file__).resolve().parents[2]
REGISTRY = Path("governance/12-machine-readable/governance-entrypoints.yaml")
PROJECT_STATE = Path("governance/PROJECT_STATE.yaml")
PROJECT_PROJECTION = Path("governance/12-machine-readable/project.yaml")
PHASES = Path("governance/12-machine-readable/phases.yaml")
PHASE_STATUS_SCHEMA = Path("governance/12-machine-readable/phase-status-schema.yaml")
PHASE_DOCUMENT = Path("governance/08-phases/PHASE-000-builderkit-organization-and-evidence-bootstrap.md")
PHASE_INDEX_YAML = Path("governance/08-phases/INDEX.yaml")
PHASE_INDEX_MD = Path("governance/08-phases/INDEX.md")
ROUTER = Path("governance/09-codex/FIRST_CODEX_PROMPT.md")

LEGACY_TOKENS = (
    "stage a",
    "stage b",
    "pre-apply",
    "materialize-repositories.py --apply",
    "gh repo create",
    "bootstrap-repos",
    "bootstrap-workspace",
    "ready_for_phase_00",
    "github mutation is forbidden",
)
DIRECTIVE = re.compile(r"\b(?:run|execute|start|resume|use|follow|create)\b", re.IGNORECASE)
NEUTRALIZERS = re.compile(
    r"\b(?:not|never|forbidden|quarantined|superseded|historical|provenance|cannot)\b",
    re.IGNORECASE,
)


def read(root: Path, relative: Path) -> str:
    path = (root / relative).resolve()
    if root.resolve() not in path.parents and path != root.resolve():
        raise AssertionError(f"path escapes repository root: {relative}")
    return path.read_text(encoding="utf-8")


def list_value(document: str, key: str) -> tuple[str, ...]:
    match = re.search(rf"(?m)^{re.escape(key)}:\n((?:^- [^\n]+\n?)+)", document)
    if not match:
        raise AssertionError(f"missing flat YAML list: {key}")
    return tuple(line[2:].strip() for line in match.group(1).splitlines() if line.strip())


def scalar(document: str, key: str, indent: int = 0) -> str:
    match = re.search(rf"(?m)^{' ' * indent}{re.escape(key)}: ([^\n]+)$", document)
    if not match:
        raise AssertionError(f"missing scalar {key}")
    return match.group(1).strip().strip("'")


def phase_block(document: str, phase_id: str) -> str:
    match = re.search(
        rf"(?ms)^- id: {re.escape(phase_id)}\n(.*?)(?=^- id:|\Z)", document
    )
    if not match:
        raise AssertionError(f"missing phase: {phase_id}")
    return match.group(0)


def phase_status(document: str, phase_id: str) -> str:
    return scalar(phase_block(document, phase_id), "status", indent=2)


def registry(root: Path) -> tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]:
    document = read(root, REGISTRY)
    return (
        list_value(document, "active_entrypoints"),
        list_value(document, "historical_superseded"),
        list_value(document, "historical_evidence"),
    )


def legacy_governance_paths(root: Path) -> set[str]:
    paths: set[str] = set()
    for path in (root / "governance").rglob("*"):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if any(token in text.lower() for token in LEGACY_TOKENS):
            paths.add(path.relative_to(root).as_posix())
    return paths


def active_execution_lines(root: Path, active: tuple[str, ...]) -> list[str]:
    failures: list[str] = []
    for relative in active:
        text = read(root, Path(relative))
        for number, line in enumerate(text.splitlines(), start=1):
            normalized = line.lower()
            if not any(token in normalized for token in LEGACY_TOKENS):
                continue
            if DIRECTIVE.search(line) and not NEUTRALIZERS.search(line):
                failures.append(f"{relative}:{number}: {line.strip()}")
    return failures


def assert_governance_semantics(test: unittest.TestCase, root: Path) -> None:
    active, superseded, evidence = registry(root)
    historical = set(superseded) | set(evidence)

    test.assertTrue(active, "registry must declare active entrypoints")
    test.assertTrue(superseded, "registry must retain superseded operational provenance")
    test.assertFalse(set(active) & historical, "a historical path cannot be active")

    expected_active = {
        "AGENTS.md",
        PROJECT_STATE.as_posix(),
        PROJECT_PROJECTION.as_posix(),
        REGISTRY.as_posix(),
        PHASES.as_posix(),
        PHASE_DOCUMENT.as_posix(),
        ROUTER.as_posix(),
    }
    test.assertTrue(expected_active <= set(active), "current routing model is incomplete")

    for relative in superseded:
        banner = read(root, Path(relative)).splitlines()[:4]
        test.assertEqual(
            banner,
            ["# HISTORICAL / SUPERSEDED", "", "**NOT AN ACTIVE ENTRYPOINT — DO NOT EXECUTE.**", ""],
            f"superseded operational document lacks a durable banner: {relative}",
        )

    classified = set(active) | historical
    unclassified = legacy_governance_paths(root) - classified
    test.assertFalse(
        unclassified,
        f"every obsolete governance occurrence must be classified: {sorted(unclassified)}",
    )
    test.assertFalse(
        active_execution_lines(root, active),
        "active governance must not direct a superseded Bootstrap operation",
    )

    for active_path in set(active) - {REGISTRY.as_posix()}:
        text = read(root, Path(active_path))
        for historical_path in historical:
            test.assertNotIn(
                historical_path,
                text,
                f"active entrypoint links historical document as an execution source: {active_path}",
            )

    state = read(root, PROJECT_STATE)
    projection = read(root, PROJECT_PROJECTION)
    for document in (state, projection):
        test.assertEqual(scalar(document, "repositories_bootstrapped"), "true")
        test.assertIn("status: INDEPENDENT_REVIEW_PENDING", document)
        test.assertIn("PHASE-000: NOT_COMPLETED", document)
        test.assertIn("GATE-000: NOT_PASSED", document)
        test.assertIn("phase_001: NOT_AUTHORIZED", document)
        test.assertIn("finding: F-000-04", document)
        test.assertIn("status: QUARANTINED", document)
        test.assertIn("authorization: FORBIDDEN", document)
        test.assertIn("current_boundary: NORMAL_PR_AND_MANUAL_AUTHORITY_FLOW", document)
        test.assertNotIn("github_mutation_allowed: false", document)
    test.assertEqual(state, projection, "PROJECT_STATE and machine projection diverged")

    allowed_phase_statuses = set(list_value(read(root, PHASE_STATUS_SCHEMA), "allowed_phase_status"))
    machine_phase_status = phase_status(read(root, PHASES), "PHASE-000")
    index_phase_status = phase_status(read(root, PHASE_INDEX_YAML), "PHASE-000")
    phase_document = read(root, PHASE_DOCUMENT)
    test.assertIn("## STATUS\n`IN_PROGRESS`", phase_document)
    test.assertEqual(machine_phase_status, "IN_PROGRESS")
    test.assertEqual(machine_phase_status, index_phase_status)
    test.assertIn("`IN_PROGRESS`", read(root, PHASE_INDEX_MD).splitlines()[4])
    test.assertIn(machine_phase_status, allowed_phase_statuses)
    test.assertNotEqual(machine_phase_status, "NOT_STARTED")
    test.assertIn("CONTROLLED_INITIAL_BASELINE_BOOTSTRAP", phase_document)
    test.assertIn("`SUPERSEDED`", phase_document)
    test.assertIn("`QUARANTINED`", phase_document)
    test.assertIn("PHASE-000 is `NOT_COMPLETED`", phase_document)
    test.assertIn("GATE-000 is `NOT_PASSED`", phase_document)
    test.assertIn("PHASE-001 is\n`NOT_AUTHORIZED`", phase_document)

    router = read(root, ROUTER)
    for required in (
        "AGENTS.md",
        "PROJECT_STATE.yaml",
        "governance-entrypoints.yaml",
        "next_required_action",
        "historical_superseded",
        "Codex Verification Contract",
        "materialize-repositories.py --apply",
        "quarantined",
        "NOT an active",
    ):
        test.assertIn(required, router)


class ActiveGovernanceSemanticsTests(unittest.TestCase):
    def fixture_root(self) -> tempfile.TemporaryDirectory[str]:
        temporary = tempfile.TemporaryDirectory(prefix="spangpu-active-governance-")
        root = Path(temporary.name)
        shutil.copytree(REPO / "governance", root / "governance")
        shutil.copy2(REPO / "AGENTS.md", root / "AGENTS.md")
        shutil.copytree(REPO / ".steward", root / ".steward")
        shutil.copytree(REPO / "verification", root / "verification")
        return temporary

    def test_current_governance_has_one_coherent_route(self):
        assert_governance_semantics(self, REPO)

    def test_router_stage_a_regression_is_rejected(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            path = root / ROUTER
            path.write_text("# Router\nStart Stage A now.\n", encoding="utf-8")
            with self.assertRaisesRegex(AssertionError, "superseded Bootstrap operation"):
                assert_governance_semantics(self, root)

    def test_active_phase_materializer_apply_regression_is_rejected(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            path = root / PHASE_DOCUMENT
            path.write_text(path.read_text(encoding="utf-8") + "\nRun materialize-repositories.py --apply.\n", encoding="utf-8")
            with self.assertRaisesRegex(AssertionError, "superseded Bootstrap operation"):
                assert_governance_semantics(self, root)

    def test_bootstrapped_phase_cannot_revert_to_not_started(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            path = root / PHASES
            path.write_text(path.read_text(encoding="utf-8").replace("status: IN_PROGRESS", "status: NOT_STARTED", 1), encoding="utf-8")
            with self.assertRaisesRegex(AssertionError, "NOT_STARTED"):
                assert_governance_semantics(self, root)

    def test_active_registry_cannot_link_a_historical_resume_prompt(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            path = root / REGISTRY
            text = path.read_text(encoding="utf-8")
            text = text.replace(
                "- AGENTS.md\n",
                "- AGENTS.md\n- governance/09-codex/PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md\n",
                1,
            )
            path.write_text(text, encoding="utf-8")
            with self.assertRaisesRegex(AssertionError, "historical path cannot be active"):
                assert_governance_semantics(self, root)

    def test_unallowlisted_historical_execution_document_is_rejected(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            path = root / REGISTRY
            text = path.read_text(encoding="utf-8")
            text = text.replace("- governance/09-codex/pre-apply-breaker-template.md\n", "", 1)
            path.write_text(text, encoding="utf-8")
            with self.assertRaisesRegex(AssertionError, "every obsolete governance occurrence"):
                assert_governance_semantics(self, root)

    def test_f00004_quarantine_cannot_coexist_with_an_active_apply_instruction(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            path = root / ROUTER
            path.write_text(path.read_text(encoding="utf-8") + "\nRun materialize-repositories.py --apply.\n", encoding="utf-8")
            with self.assertRaisesRegex(AssertionError, "superseded Bootstrap operation"):
                assert_governance_semantics(self, root)

    def test_phase001_cannot_be_authorized_prematurely(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            path = root / PROJECT_STATE
            path.write_text(path.read_text(encoding="utf-8").replace("phase_001: NOT_AUTHORIZED", "phase_001: AUTHORIZED", 1), encoding="utf-8")
            with self.assertRaisesRegex(AssertionError, "phase_001: NOT_AUTHORIZED"):
                assert_governance_semantics(self, root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
