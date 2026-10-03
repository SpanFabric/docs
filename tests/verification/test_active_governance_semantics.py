"""Regression coverage for the production active-governance semantic validator."""
from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import active_governance_semantics as governance_semantics
from scripts.active_governance_semantics import (
    GovernanceRouteError,
    audit_summary,
    audit_active_governance_references,
    assert_governance_semantics as validate_governance_semantics,
    markdown_references,
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

    def test_solo_owner_hosting_authority_rejects_weakened_controls(self):
        mutations = (
            ("mode: SOLO_OWNER", "mode: MULTI_OWNER"),
            ("authority: FRESH_BREAKER\n    required: true", "authority: FRESH_BREAKER\n    required: false"),
            ("authority: OWNER\n    required: true", "authority: OWNER\n    required: false"),
            ("required_approvals: 0", "required_approvals: 1"),
            ("force_push_allowed: false", "force_push_allowed: true"),
            ("deletion_allowed: false", "deletion_allowed: true"),
            ("admin_bypass_allowed: false", "admin_bypass_allowed: true"),
            ("require_up_to_date: false", "require_up_to_date: true"),
        )
        for before, after in mutations:
            with self.subTest(before=before, after=after):
                with self.fixture_root() as temporary:
                    root = Path(temporary)
                    path = root / PROJECT_STATE
                    path.write_text(
                        path.read_text(encoding="utf-8").replace(before, after, 1),
                        encoding="utf-8",
                    )
                    with self.assertRaisesRegex(GovernanceRouteError, "SOLO_OWNER hosting_authority"):
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
        self.assert_route_rejected("[resume](PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md\\\\resume)", "percent-encoded")

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
                ("../PROJECT_STATE.yaml#authorization", "governance/PROJECT_STATE.yaml", "ACTIVE"),
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

    def test_commonmark_corpus_extracts_every_actual_historical_link_then_rejects_it(self):
        historical = "PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md"
        cases = (
            ("escaped closing bracket", f"[resume\\]]({historical})"),
            ("balanced nested label", f"[resume [historical]]({historical})"),
            ("multiple nested labels", f"[a [b [c]]]({historical})"),
            ("escaped opening and closing brackets", f"[a \\[b\\] c]({historical})"),
            ("escaped closing bracket with title", f'[resume\\]]({historical} "title")'),
            ("balanced label with title", f'[resume [historical]]({historical} "title")'),
            ("full escaped reference", f"[resume\\]][id]\n\n[id]: {historical} 'title'"),
            ("collapsed escaped reference", f"[resume\\]][]\n\n[resume\\]]: {historical} \"title\""),
            ("shortcut escaped reference", f"[resume\\]]\n\n[resume\\]]: {historical}"),
            ("balanced full reference", f"[resume [historical]][id]\n\n[id]: {historical}"),
            ("case-normalized reference", f"[resume][HISTORICAL REF]\n\n[historical ref]: {historical}"),
            ("whitespace-normalized reference", f"[resume][historical   ref]\n\n[ Historical Ref ]: {historical}"),
            ("escaped punctuation reference", f"[resume\\!][id]\n\n[id]: {historical}"),
        )
        for name, addition in cases:
            with self.subTest(name=name):
                self.assert_historical_route_extracted_then_rejected(addition, historical)

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

    def test_malformed_local_link_syntax_that_commonmark_does_not_render_is_not_navigation(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(root, '[resume](PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md "unterminated)')
            self.append_router(root, '[legacy][id]\n\n[id]: PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md "unterminated')
            audit = assert_governance_semantics(self, root)
            self.assertFalse(any(item.classification.startswith("HISTORICAL") for item in audit), audit)

    def test_duplicate_reference_definitions_follow_commonmark_first_definition_semantics(self):
        historical = "PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md"
        self.assert_historical_route_extracted_then_rejected(
            f"[resume][id]\n\n[id]: {historical}\n[id]: ../PROJECT_STATE.yaml",
            historical,
        )

        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(root, f"[state][id]\n\n[id]: ../PROJECT_STATE.yaml\n[id]: {historical}")
            audit = assert_governance_semantics(self, root)
            self.assertIn(
                ("../PROJECT_STATE.yaml", "governance/PROJECT_STATE.yaml", "ACTIVE", True),
                {(item.raw_destination, item.canonical_target, item.classification, item.allowed) for item in audit},
            )

    def test_undefined_references_are_non_navigation_under_commonmark(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(root, "[resume][missing]")
            self.append_router(root, "[PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md]")
            audit = assert_governance_semantics(self, root)
            self.assertNotIn(
                "PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md",
                {item.raw_destination for item in audit},
            )

    def test_inline_and_fenced_code_are_not_navigation(self):
        historical = "PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md"
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(root, f"`[resume]({historical})`\n\n~~~md\n[resume]({historical})\n~~~")
            audit = assert_governance_semantics(self, root)
            self.assertNotIn(historical, {item.raw_destination for item in audit})

    def test_raw_html_navigation_is_rejected_before_span_gpu_path_authorization(self):
        cases = (
            ("local anchor", '<a href="PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md">resume</a>'),
            ("external anchor", '<a href="https://example.invalid/governance">documentation</a>'),
            ("form action", '<form action="PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md"><input type="submit"></form>'),
            ("base target", '<base href="PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md">'),
        )
        for name, addition in cases:
            with self.subTest(name=name):
                with self.fixture_root() as temporary:
                    root = Path(temporary)
                    self.append_router(root, addition)
                    audit = audit_active_governance_references(root)
                    raw_html = [item for item in audit if item.form == "raw-html-navigation"]
                    self.assertEqual(1, len(raw_html), audit)
                    self.assertEqual("REJECTED", raw_html[0].classification)
                    self.assertFalse(raw_html[0].allowed)
                    with self.assertRaisesRegex(GovernanceRouteError, "raw HTML navigation is forbidden"):
                        assert_governance_semantics(self, root)

    def test_audit_summary_counts_parser_tokens_and_policy_decisions(self):
        with self.fixture_root() as temporary:
            root = Path(temporary)
            self.append_router(
                root,
                "\n".join(
                    (
                        "[active](../PROJECT_STATE.yaml)",
                        "[external](https://example.invalid/governance)",
                        "[historical](PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md)",
                        "[unknown](unclassified-governance.md)",
                        '<a href="PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md">resume</a>',
                    )
                ),
            )
            audit = audit_active_governance_references(root)
            summary = audit_summary(audit, len(structured_provenance_references(root)))
            self.assertEqual(
                sum(item.form == "markdown-link" for item in audit),
                summary["parsed_navigable_markdown_links"],
            )
            self.assertEqual(
                sum(item.form == "markdown-link" and item.canonical_target is not None for item in audit),
                summary["parsed_local_markdown_links"],
            )
            self.assertEqual(
                sum(item.form == "markdown-link" and item.classification == "EXTERNAL_HTTP" for item in audit),
                summary["parsed_external_markdown_links"],
            )
            self.assertEqual(1, summary["rejected_historical_routes"])
            # The unclassified Markdown route and raw-HTML navigation are each
            # policy rejections; the latter is additionally exposed by its
            # dedicated counter below.
            self.assertEqual(2, summary["rejected_unclassified_or_unsafe_routes"])
            self.assertEqual(1, summary["raw_html_navigation_rejections"])
            self.assertNotIn("ignored_recognized_local_markdown_references", summary)

    def test_external_vendored_record_path_fails_closed(self):
        with tempfile.TemporaryDirectory(prefix="spangpu-vendor-record-") as temporary:
            root = Path(temporary)
            vendor = root / "_vendor"
            shutil.copytree(REPO / "scripts" / "_vendor", vendor)
            record = vendor / "markdown_it_py-4.2.0.dist-info" / "RECORD"
            record.write_text(
                record.read_text(encoding="utf-8")
                + "../../bin/markdown-it.exe,sha256=cTQ9ByxmWQthmPN5_odeSVwaqZm1MOXvuDJsvXqByrM,108327\n",
                encoding="utf-8",
            )
            with patch.object(governance_semantics, "__file__", str(root / "validator.py")), patch.object(
                governance_semantics, "VENDOR_ROOT", vendor
            ):
                with self.assertRaisesRegex(GovernanceRouteError, "non-canonical vendored CommonMark RECORD path"):
                    governance_semantics._validate_vendored_distribution("markdown_it")

    def test_tampered_vendored_payload_fails_closed(self):
        with tempfile.TemporaryDirectory(prefix="spangpu-vendor-tamper-") as temporary:
            root = Path(temporary)
            vendor = root / "_vendor"
            shutil.copytree(REPO / "scripts" / "_vendor", vendor)
            payload = vendor / "mdurl" / "__init__.py"
            payload.write_text(payload.read_text(encoding="utf-8") + "\n# tampered\n", encoding="utf-8")
            with patch.object(governance_semantics, "__file__", str(root / "validator.py")), patch.object(
                governance_semantics, "VENDOR_ROOT", vendor
            ):
                with self.assertRaisesRegex(GovernanceRouteError, "vendored CommonMark payload integrity mismatch"):
                    governance_semantics._validate_vendored_distribution("mdurl")

    def test_missing_vendored_commonmark_dependency_fails_without_fallback(self):
        with patch.object(governance_semantics, "VENDOR_ROOT", REPO / "scripts" / "missing-vendor"), patch.object(
            governance_semantics, "_COMMONMARK_PARSER", None
        ):
            with self.assertRaisesRegex(GovernanceRouteError, "vendored CommonMark dependency is missing"):
                markdown_references("governance/09-codex/FIRST_CODEX_PROMPT.md", "[state](../PROJECT_STATE.yaml)")

    def test_preloaded_non_vendored_commonmark_module_is_rejected_without_fallback(self):
        with patch.object(governance_semantics, "_COMMONMARK_PARSER", None), patch.dict(
            sys.modules, {"markdown_it": object()}
        ):
            with self.assertRaisesRegex(GovernanceRouteError, "non-vendored CommonMark module already loaded"):
                markdown_references("governance/09-codex/FIRST_CODEX_PROMPT.md", "[state](../PROJECT_STATE.yaml)")

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
