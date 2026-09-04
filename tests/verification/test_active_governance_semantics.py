"""Regression coverage for the production active-governance semantic validator."""
from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.active_governance_semantics import (
    GovernanceRouteError,
    audit_active_governance_references,
    assert_governance_semantics as validate_governance_semantics,
    structured_provenance_references,
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

    def add_structured_provenance(self, root: Path, target: str) -> None:
        path = root / REGISTRY
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "structured_provenance: []",
                "structured_provenance:\n"
                "- source: governance/09-codex/FIRST_CODEX_PROMPT.md\n"
                f"  historical_target: {target}\n"
                "  relationship: provenance",
            ),
            encoding="utf-8",
        )

    def assert_route_rejected(self, addition: str, expected: str) -> None:
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(root, addition)
            with self.assertRaisesRegex(GovernanceRouteError, expected):
                assert_governance_semantics(self, root)

    def assert_historical_route_extracted_then_rejected(
        self,
        addition: str,
        raw_destination: str,
        classification: str = "HISTORICAL_REFERENCE",
        provenance: bool = False,
    ) -> None:
        with self.fixture_root() as temporary:
            root = Path(temporary)
            if provenance:
                self.add_structured_provenance(
                    root,
                    "governance/09-codex/PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md",
                )
            self.append_router(root, addition)
            audit = audit_active_governance_references(root)
            matching = [item for item in audit if item.raw_destination == raw_destination]
            self.assertEqual(1, len(matching), audit)
            reference = matching[0]
            self.assertEqual("governance/09-codex/PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md", reference.canonical_target)
            self.assertEqual(classification, reference.classification)
            self.assertFalse(reference.allowed)
            with self.assertRaisesRegex(GovernanceRouteError, "historical target"):
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

    def test_structured_provenance_is_valid_without_a_navigable_historical_route(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.add_structured_provenance(
                root,
                "governance/13-reports/validation-report.json",
            )
            audit = assert_governance_semantics(self, root)
            self.assertFalse(
                any(item.classification.startswith("HISTORICAL") for item in audit),
                audit,
            )
            self.assertEqual(
                [("governance/09-codex/FIRST_CODEX_PROMPT.md", "governance/13-reports/validation-report.json", "provenance")],
                [
                    (item.source, item.historical_target, item.relationship)
                    for item in structured_provenance_references(root)
                ],
            )

    def test_title_bearing_historical_links_are_extracted_and_rejected(self):
        historical = "PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md"
        cases = (
            ("double quoted inline", f'[resume]({historical} "retained historical record")', "inline"),
            ("single quoted inline", f"[resume]({historical} 'retained historical record')", "inline"),
            ("parenthesized inline", f"[resume]({historical} (retained historical record))", "inline"),
            ("angle destination with title", f'[resume](<{historical}> "retained historical record")', "inline"),
            ("explicit reference definition", f'[legacy][id]\n\n[id]: {historical} "retained historical record"', "reference"),
            ("collapsed reference definition", f'[legacy][]\n\n[legacy]: {historical} \'retained historical record\'', "reference"),
            ("shortcut reference definition", f'[legacy]\n\n[legacy]: <{historical}> "retained historical record"', "reference"),
        )
        for name, addition, form in cases:
            with self.subTest(name=name):
                with self.fixture_root() as temporary:
                    root = Path(temporary)
                    self.append_router(root, addition)
                    audit = audit_active_governance_references(root)
                    matching = [item for item in audit if item.canonical_target == "governance/09-codex/PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md"]
                    self.assertEqual(1, len(matching), audit)
                    self.assertEqual(form, matching[0].form)
                    self.assertEqual("HISTORICAL_REFERENCE", matching[0].classification)
                    self.assertFalse(matching[0].allowed)
                    with self.assertRaisesRegex(GovernanceRouteError, "historical target"):
                        assert_governance_semantics(self, root)

    def test_title_is_not_part_of_active_or_external_target_identity(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(root, '[project-state](../PROJECT_STATE.yaml "active target")')
            self.append_router(root, "[documentation](https://example.invalid/governance 'external title')")
            audit = assert_governance_semantics(self, root)
            self.assertIn(
                ("../PROJECT_STATE.yaml", "governance/PROJECT_STATE.yaml", "ACTIVE", True),
                {(item.raw_destination, item.canonical_target, item.classification, item.allowed) for item in audit},
            )
            self.assertIn(
                ("https://example.invalid/governance", None, "EXTERNAL_HTTP", True),
                {(item.raw_destination, item.canonical_target, item.classification, item.allowed) for item in audit},
            )

    def test_malformed_local_title_syntax_fails_closed_in_the_production_extractor(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(root, '[resume](PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md "unterminated)')
            with self.assertRaisesRegex(GovernanceRouteError, "malformed or unsupported local Markdown reference"):
                audit_active_governance_references(root)

    def test_malformed_local_reference_definition_fails_closed_in_the_production_extractor(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(root, '[legacy][id]\n\n[id]: PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md "unterminated')
            with self.assertRaisesRegex(GovernanceRouteError, "malformed or unsupported local Markdown reference"):
                audit_active_governance_references(root)

    def test_duplicate_reference_definitions_fail_deterministically(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(
                root,
                '[state][id]\n\n[id]: ../PROJECT_STATE.yaml "first"\n[id]: ../PROJECT_STATE.yaml \'second\'',
            )
            with self.assertRaisesRegex(GovernanceRouteError, "duplicate reference definition"):
                audit_active_governance_references(root)

    def test_undefined_reference_label_fails_and_undefined_shortcut_is_not_a_path(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(root, "[resume][missing]")
            with self.assertRaisesRegex(GovernanceRouteError, "undefined reference label"):
                audit_active_governance_references(root)
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(root, "[PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md]")
            audit = assert_governance_semantics(self, root)
            self.assertNotIn(
                "PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md",
                {item.raw_destination for item in audit},
            )

    def test_title_content_cannot_create_a_second_hidden_route(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(
                root,
                '[project-state](../PROJECT_STATE.yaml "ignored [resume](PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md)")',
            )
            audit = assert_governance_semantics(self, root)
            self.assertIn(
                ("../PROJECT_STATE.yaml", "governance/PROJECT_STATE.yaml", "ACTIVE"),
                {(item.raw_destination, item.canonical_target, item.classification) for item in audit},
            )
            self.assertNotIn(
                "PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md",
                {item.raw_destination for item in audit},
            )

    def test_structured_provenance_never_authorizes_historical_navigation_aliases(self):
        historical = "PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md"
        cases = (
            ("same directory", f"[resume]({historical})"),
            ("dot relative", f"[resume](./{historical})"),
            ("parent relative", f"[resume](../09-codex/{historical})"),
            ("repository root", f"[resume](governance/09-codex/{historical})"),
            ("fragment", f"[resume](./{historical}#stage-b)"),
            ("query", f"[resume](../09-codex/{historical}?mode=apply)"),
            ("title", f'[resume]({historical} "historical")'),
            ("reference", f"[resume][id]\n\n[id]: {historical} 'historical'"),
            ("collapsed", f"[resume][]\n\n[resume]: {historical} \"historical\""),
            ("shortcut", f"[resume]\n\n[resume]: <{historical}> \"historical\""),
        )
        for name, addition in cases:
            with self.subTest(name=name):
                with self.fixture_root() as temporary:
                    root = Path(temporary)
                    self.add_structured_provenance(
                        root,
                        "governance/09-codex/PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md",
                    )
                    self.append_router(root, addition)
                    audit = audit_active_governance_references(root)
                    historical_routes = [item for item in audit if item.classification.startswith("HISTORICAL")]
                    self.assertEqual(1, len(historical_routes), audit)
                    self.assertFalse(historical_routes[0].allowed)
                    self.assertEqual(
                        "governance/09-codex/PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md",
                        historical_routes[0].canonical_target,
                    )
                    with self.assertRaisesRegex(GovernanceRouteError, "historical target"):
                        assert_governance_semantics(self, root)

    def test_structured_provenance_aliases_and_wildcards_fail_closed(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.add_structured_provenance(root, "./PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md")
            with self.assertRaisesRegex(GovernanceRouteError, "non-canonical registry path"):
                assert_governance_semantics(self, root)
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.add_structured_provenance(root, "governance/09-codex/*")
            with self.assertRaisesRegex(GovernanceRouteError, "classified historical path"):
                assert_governance_semantics(self, root)

    def test_f00004_is_unreachable_at_the_first_active_to_historical_boundary(self):
        self.assert_historical_route_extracted_then_rejected(
            "[resume](PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md)",
            "PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md",
        )

    def test_every_current_navigable_local_reference_is_classified_and_allowed(self):
        audit = assert_governance_semantics(self, REPO)
        local = [item for item in audit if item.classification != "EXTERNAL_HTTP"]
        self.assertTrue(local)
        self.assertTrue(all(item.canonical_target is not None for item in local))
        self.assertTrue(all(item.classification == "ACTIVE" and item.allowed for item in local))

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
