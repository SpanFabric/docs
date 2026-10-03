"""Regression coverage for the canonical post-bootstrap project-state claims.

The repository-local bridge intentionally has no YAML dependency.  These assertions
therefore validate the state claims that would be dangerous to regress while the
BuilderKit PyYAML schema validator remains an external bootstrap tool.
"""
from __future__ import annotations

from pathlib import Path
import re
import unittest


REPO = Path(__file__).resolve().parents[2]
STATE_PATHS = (
    REPO / "governance" / "PROJECT_STATE.yaml",
    REPO / "governance" / "12-machine-readable" / "project.yaml",
)
SCHEMA_PATH = REPO / "governance" / "12-machine-readable" / "project-state-schema.yaml"


def root_section(document: str, name: str) -> str:
    match = re.search(
        rf"(?ms)^{re.escape(name)}:\n(.*?)(?=^[^\s#][^:]*:|\Z)", document
    )
    if not match:
        raise AssertionError(f"missing root mapping {name}")
    return match.group(1)


def scalar(document: str, name: str, indent: int = 0) -> str:
    pattern = r"(?m)^" + re.escape(" " * indent) + re.escape(name) + r": ([^\n]+)$"
    match = re.search(pattern, document)
    if not match:
        raise AssertionError(f"missing scalar {' ' * indent}{name}")
    return match.group(1).strip().strip("'")


class ProjectStateSemanticsTests(unittest.TestCase):
    def test_canonical_and_machine_readable_projection_preserve_post_bootstrap_truth(self):
        for path in STATE_PATHS:
            with self.subTest(path=path.relative_to(REPO)):
                document = path.read_text(encoding="utf-8")
                project = root_section(document, "project")
                bootstrap = root_section(document, "phase_000_bootstrap")
                verification = root_section(document, "verification")
                hosting_authority = root_section(document, "hosting_authority")
                authorization = root_section(document, "authorization")

                self.assertEqual(scalar(project, "status", 2), "INDEPENDENT_REVIEW_PENDING")
                self.assertEqual(
                    scalar(project, "implementation_status", 2),
                    "BOOTSTRAP_INFRASTRUCTURE_ESTABLISHED",
                )
                self.assertEqual(scalar(project, "product_functionality_status", 2), "NOT_STARTED")
                self.assertEqual(scalar(document, "repositories_bootstrapped"), "true")
                self.assertEqual(scalar(verification, "status", 2), "INDEPENDENT_REVIEW_PENDING")
                self.assertEqual(scalar(document, "current_phase"), "PHASE-000")
                self.assertEqual(scalar(document, "current_gate"), "GATE-000")
                self.assertEqual(scalar(bootstrap, "status", 2), "SUPERSEDED")
                self.assertEqual(
                    scalar(bootstrap, "pre_apply_breaker_status", 2),
                    "NOT_RUN_SUPERSEDED",
                )
                self.assertEqual(
                    scalar(bootstrap, "github_mutation_allowed", 2),
                    "NOT_APPLICABLE_SUPERSEDED_PATH",
                )
                self.assertEqual(scalar(authorization, "next_action", 2), "FRESH_INDEPENDENT_BREAKER_REVIEW")
                self.assertEqual(scalar(authorization, "phase_001", 2), "NOT_AUTHORIZED")
                self.assertEqual(scalar(hosting_authority, "mode", 2), "SOLO_OWNER")
                self.assertIn(
                    "  independent_technical_review:\n    authority: FRESH_BREAKER\n    required: true",
                    hosting_authority,
                )
                self.assertIn(
                    "  owner_acceptance:\n    authority: OWNER\n    required: true\n    may_be_pr_author: true",
                    hosting_authority,
                )
                self.assertIn(
                    "  github_review:\n    human_approval_required: false\n    required_approvals: 0",
                    hosting_authority,
                )
                self.assertIn(
                    "  branch_protection:\n    pull_request_required: true\n    required_checks:\n    - verification-gate\n    - bootstrap-integrity\n    force_push_allowed: false\n    deletion_allowed: false\n    admin_bypass_allowed: false\n    require_up_to_date: false",
                    hosting_authority,
                )

                self.assertIn("PHASE-000: NOT_COMPLETED", document)
                self.assertIn("GATE-000: NOT_PASSED", document)
                self.assertIn("finding: F-000-04", document)
                self.assertIn("status: QUARANTINED", document)
                self.assertIn("authorization: FORBIDDEN", document)
                self.assertIn("FRESH_INDEPENDENT_BREAKER_REVIEW", document)

                self.assertNotIn("status: READY_FOR_PHASE_00", document)
                self.assertNotIn("implementation_status: NOT_STARTED", document)
                self.assertNotIn("github_mutation_allowed: false", document)
                self.assertNotRegex(document, r"pre_apply_breaker_status: NOT_RUN(?:\s|$)")
                self.assertNotIn("Execute PHASE-000 Stage A only", document)

    def test_schema_requires_the_five_separated_state_dimensions(self):
        schema = SCHEMA_PATH.read_text(encoding="utf-8")
        for field in (
            "repositories_bootstrapped",
            "verification",
            "hosting_authority",
            "phase_completion",
            "gate_completion",
            "authorization",
            "quarantined_items",
        ):
            self.assertRegex(schema, rf"(?m)^- {re.escape(field)}$")
        self.assertIn("original_builderkit_strategy: SUPERSEDED", schema)
        self.assertIn("actual_bootstrap: CONTROLLED_INITIAL_BASELINE_BOOTSTRAP", schema)
        self.assertIn("materializer_apply: QUARANTINED_F000_04", schema)
        self.assertIn("SOLO_OWNER keeps Fresh BREAKER", schema)


if __name__ == "__main__":
    unittest.main(verbosity=2)
