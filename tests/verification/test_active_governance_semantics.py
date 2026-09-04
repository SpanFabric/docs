"""Regression coverage for the production active-governance semantic validator."""
from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.active_governance_semantics import (
    GovernanceRouteError,
    assert_governance_semantics as validate_governance_semantics,
)


sys.dont_write_bytecode = True

REPO = Path(__file__).resolve().parents[2]
REGISTRY = Path("governance/12-machine-readable/governance-entrypoints.yaml")
PROJECT_STATE = Path("governance/PROJECT_STATE.yaml")
PHASES = Path("governance/12-machine-readable/phases.yaml")
PHASE_DOCUMENT = Path("governance/08-phases/PHASE-000-builderkit-organization-and-evidence-bootstrap.md")
ROUTER = Path("governance/09-codex/FIRST_CODEX_PROMPT.md")


def assert_governance_semantics(test: unittest.TestCase, root: Path):
    """Invoke the production semantic validator used by every adversarial fixture."""
    return validate_governance_semantics(root)


class ActiveGovernanceSemanticsTests(unittest.TestCase):
    def fixture_root(self) -> tempfile.TemporaryDirectory[str]:
        temporary = tempfile.TemporaryDirectory(prefix="spangpu-active-governance-")
        root = Path(temporary.name)
        shutil.copytree(REPO / "governance", root / "governance")
        shutil.copy2(REPO / "AGENTS.md", root / "AGENTS.md")
        shutil.copytree(REPO / ".steward", root / ".steward")
        shutil.copytree(REPO / "verification", root / "verification")
        return temporary

    def append_router(self, root: Path, addition: str) -> None:
        path = root / ROUTER
        path.write_text(path.read_text(encoding="utf-8") + "\n" + addition, encoding="utf-8")

    def assert_route_rejected(self, addition: str, expected: str) -> None:
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(root, addition)
            with self.assertRaisesRegex(GovernanceRouteError, expected):
                assert_governance_semantics(self, root)

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

    def test_same_directory_markdown_historical_route_is_rejected(self):
        self.assert_route_rejected("[resume](PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md)", "historical target")

    def test_explicit_same_directory_markdown_historical_route_is_rejected(self):
        self.assert_route_rejected("[resume](./PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md)", "historical target")

    def test_normalized_parent_markdown_historical_route_is_rejected(self):
        self.assert_route_rejected("[resume](../09-codex/PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md)", "historical target")

    def test_repository_relative_historical_route_is_rejected(self):
        self.assert_route_rejected(
            "[resume](governance/09-codex/PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md)",
            "historical target",
        )

    def test_fragment_cannot_hide_historical_target_identity(self):
        self.assert_route_rejected(
            "[resume](governance/09-codex/PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md#resume)",
            "historical target",
        )

    def test_query_cannot_hide_historical_target_identity(self):
        self.assert_route_rejected(
            "[resume](governance/09-codex/PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md?mode=resume)",
            "historical target",
        )

    def test_reference_style_historical_route_is_rejected(self):
        self.assert_route_rejected(
            "[resume][legacy]\n\n[legacy]: PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md",
            "historical target",
        )

    def test_shortcut_reference_style_historical_route_is_rejected(self):
        self.assert_route_rejected(
            "[legacy]\n\n[legacy]: PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md",
            "historical target",
        )

    def test_historical_evidence_route_is_rejected(self):
        self.assert_route_rejected("[sealed](governance/13-reports/validation-report.json)", "historical target")

    def test_root_escape_or_unclassified_local_target_fails_closed(self):
        self.assert_route_rejected("[outside](../../outside.md)", "unclassified internal executable governance target")

    def test_backslash_repository_path_is_rejected(self):
        self.assert_route_rejected("[resume](PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md\\\\resume)", "backslash repository path")

    def test_percent_encoded_traversal_or_separator_is_rejected(self):
        self.assert_route_rejected(
            "[resume](..%2F09-codex%2FPHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md)",
            "percent-encoded",
        )

    def test_angle_bracket_markdown_destination_is_resolved_and_rejected_when_historical(self):
        self.assert_route_rejected("[resume](<PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md>)", "historical target")

    def test_normal_active_to_active_repository_route_is_allowed(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(root, "[project-state](../PROJECT_STATE.yaml)")
            audit = assert_governance_semantics(self, root)
            self.assertIn(
                ("../PROJECT_STATE.yaml", "governance/PROJECT_STATE.yaml", "ACTIVE"),
                {(item.raw_destination, item.canonical_target, item.classification) for item in audit},
            )

    def test_external_https_documentation_link_is_separate_and_allowed(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(root, "[documentation](https://example.invalid/governance)")
            audit = assert_governance_semantics(self, root)
            self.assertIn(
                ("https://example.invalid/governance", None, "EXTERNAL_HTTP"),
                {(item.raw_destination, item.canonical_target, item.classification) for item in audit},
            )

    def test_fragment_on_active_target_is_allowed(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(root, "[project-state](<../PROJECT_STATE.yaml#authorization>)")
            audit = assert_governance_semantics(self, root)
            self.assertIn(
                ("<../PROJECT_STATE.yaml#authorization>", "governance/PROJECT_STATE.yaml", "ACTIVE"),
                {(item.raw_destination, item.canonical_target, item.classification) for item in audit},
            )

    def test_explicit_registry_provenance_citation_is_nonoperative_and_allowed(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(root, "[sealed-record](../13-reports/validation-report.json)")
            path = root / REGISTRY
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "explicit_provenance_references: []",
                    "explicit_provenance_references:\n"
                    "- source: governance/09-codex/FIRST_CODEX_PROMPT.md\n"
                    "  target: governance/13-reports/validation-report.json",
                ),
                encoding="utf-8",
            )
            audit = assert_governance_semantics(self, root)
            self.assertIn(
                ("HISTORICAL_EVIDENCE", "explicit non-operative provenance reference"),
                {(item.classification, item.reason) for item in audit},
            )

    def test_direct_repository_anchored_governance_reference_is_resolved(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(root, "Read `governance/PROJECT_STATE.yaml` before proceeding.")
            audit = assert_governance_semantics(self, root)
            self.assertIn(
                ("direct-governance", "governance/PROJECT_STATE.yaml", "ACTIVE"),
                {(item.form, item.canonical_target, item.classification) for item in audit},
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
