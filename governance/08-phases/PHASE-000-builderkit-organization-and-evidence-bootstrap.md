# PHASE-000 — BuilderKit, organization and evidence bootstrap

## STATUS
`NOT_STARTED`

## OBJECTIVE
Create the reproducible organization/repository/governance/evidence baseline without implementing GPU functionality.

## WHY THIS PHASE EXISTS
Repository creation is a cross-repository control-plane mutation. A broken bootstrap can create durable partial state before any runtime code exists, so Phase 00 is split into a reviewed pre-apply stage and a post-acceptance apply stage.

## REQUIREMENTS
VISION-001, VISION-002, VISION-003, VISION-004, VISION-005, VISION-006, VISION-007, VISION-008, VISION-009, VISION-010, TEST-001, TEST-002, TEST-003, TEST-004, TEST-005, TEST-006, TEST-007, TEST-008, TEST-009, TEST-010, TEST-011, TEST-012, TEST-013, TEST-014, TEST-015, TEST-016, TEST-017, TEST-018, CI-001, CI-002, CI-003, CI-004, CI-005, CI-006, CI-007, CI-008, CI-009, CI-010, CI-011, CI-012, LICENSE-001, LICENSE-002, LICENSE-003, LICENSE-004, LICENSE-005, LICENSE-006, LICENSE-007, LICENSE-008, LICENSE-009, LICENSE-010, BUILD-001, BUILD-002, BUILD-003, BUILD-004, BUILD-005, BUILD-006, BUILD-007, BUILD-008, BUILD-009, BUILD-010, BUILD-011, DOC-001, DOC-002, DOC-003, DOC-004, DOC-005, DOC-006, DOC-007, DOC-008, DOC-009, DOC-010, DOC-011, DOC-012, DOC-013, DOC-014, DOC-015, DOC-016, DOC-017, DOC-018, EVIDENCE-001, EVIDENCE-002, EVIDENCE-003, EVIDENCE-005, EVIDENCE-006, EVIDENCE-007, EVIDENCE-008, EVIDENCE-009, FINDING-001, FINDING-002, FINDING-003, WAIVER-001, WAIVER-002, BOUNDARY-001, BOUNDARY-002, SOURCE-001, SOURCE-002

## TECHNOLOGY DECISIONS
TD-001, TD-003, TD-020, TD-025, TD-026, TD-027, TD-028, TD-029, TD-030, TD-031

## PREREQUISITE GATES
`GATE-BK-000` must be PASS. No SpanGPU runtime proof prerequisite.

## REPOSITORIES ALLOWED
platform, windows, host, evals, docs, .github

## STAGE A — PRE-APPLY BUILDER
1. Extract the exact BuilderKit ZIP and record its SHA-256/version.
2. PLAN + GLOBAL IMPACT + pre-build “What are we missing?”.
3. Create the isolated validator environment using the pinned dependency file under `D:\Projekte\SpanGPU\.tooling`; this is the only permitted pre-dry-run local tooling mutation.
4. Run BuilderKit, traceability, upstream and Phase-000 semantic tests.
5. Verify local `gh` identity and active `SpanFabric` authorization read-only.
6. Rediscover GitHub repository state and local workspace state.
7. Create a unique pre-bootstrap attempt directory under `_evidence-prebootstrap`.
8. Run organization, repository and workspace bootstrap in DRY RUN only. Run materialization in DRY RUN against a temporary six-repository directory or, if repositories already exist locally, against the verified workspace.
9. Capture exact commands/stdout/stderr/exit codes/environment and seal the attempt manifest.
10. Stop with `INDEPENDENT_REVIEW_PENDING` and hand the sealed inputs to a fresh **PRE-APPLY BREAKER**.

**GitHub mutation is forbidden during Stage A.**

## PRE-APPLY BREAKER BARRIER
The fresh breaker must independently accept the exact sealed Stage-A attempt before repository creation. A failed or blocked breaker creates findings/new attempt; it never authorizes apply by implication.

## STAGE B — APPLY AFTER PRE-APPLY ACCEPTANCE
1. Verify the accepted breaker attempt/evidence reference.
2. Rediscover GitHub/local state immediately before mutation.
3. Create only missing planned repositories with explicit `-Apply`/`--apply`.
4. Clone/verify repositories under `D:\Projekte\SpanGPU`; existing paths must be Git repos with the expected origin.
5. Run `materialize-repositories.py --apply --attempt-id <current-stage-b-attempt-id>` using the canonical manifest. A global read-only preflight must succeed before any write; unmanaged conflicts or managed-file drift fail with zero materialization writes. Preserve the append-only apply journal for any later recovery.
6. Materialize and validate the repository-local Manual Verification Bridge v1 in every repository (`.steward/verification-policy.yaml`, `verification/state.yaml`, `verification/reports/`, `scripts/verify_review_state.py`, `tests/verification/`, and `.github/workflows/verification-gate.yml`) together with repo-local `AGENTS.md`, CI skeletons and Steward runtime baseline. No repository may be pushed or merged before its bridge tests pass. `docs` becomes normative only after the materialization commit hashes are recorded.
7. Import verified sealed pre-bootstrap evidence into `evals/evidence/prebootstrap/<attempt_id>/` and commit it without altering original bytes.
8. Run BuilderKit/traceability/upstream validators, project-state schema tests, Steward policy tests, materialization/idempotency tests and repository topology checks.
9. Perform Builder Assumption Challenge and all required boundary audits.
10. Seal post-apply evidence tied to exact commits and stop at `INDEPENDENT_REVIEW_PENDING` for the final fresh BREAKER.

## OUT OF SCOPE
WDDM/KMD/UMD feature work; GPU transport/rendering; remote VRAM runtime; graphics APIs; production signing; controlled upstream forks; product GUI/account/marketplace work.

## FORBIDDEN SHORTCUTS
No ad-hoc copying of governance; no retry-until-green; no automatic deletion rollback; no repository repurposing; no per-game/launcher/injection architecture; no hidden local-GPU success substitution.

## TESTS REQUIRED
- BuilderKit validator
- Traceability validator
- Upstream registry validator
- `11-bootstrap/tests/test_bootstrap_repos_contract.py`
- `11-bootstrap/tests/test_bootstrap_target_constraints.py`
- `11-bootstrap/tests/test_project_state.py`
- `11-bootstrap/tests/test_steward_policy.py`
- `11-bootstrap/tests/test_materialization_manifest.py`
- `11-bootstrap/tests/test_materialization_recovery.py`
- `11-bootstrap/tests/test_manual_verification_bridge.py`
- per-repository `python scripts/verify_review_state.py --check` and `python -m unittest discover -s tests/verification -p "test_*.py"` before first push
- clean repository/workspace/materialization dry runs
- post-apply topology and source-hash verification

## HARDWARE TESTS REQUIRED
`false`

## EXPECTED ARTIFACTS
Sealed pre-apply evidence + breaker verdict; repositories/clones if authorized; materialization states; canonical governance commits; CI/Steward baseline; sealed post-apply evidence; boundary audits; final breaker handoff.

## PROOF GATE
`GATE-000`

## DONE CRITERIA
All linked scope criteria and tests pass; Stage-A pre-apply BREAKER accepted before mutation; Stage-B builder evidence is complete; final fresh BREAKER accepts exact target commits; `GATE-000` passes with immutable evidence.

## FAILURE CONDITIONS
Any required test does not execute; dry-run nonzero/unexpected scope; unmanaged materialization conflict; environment/upstream blocker; unresolved blocking breaker finding; architecture invariant violation.

## ROLLBACK / RECOVERY
Preserve partial repositories and evidence. Never delete automatically. New attempt rediscovers state, verifies origins/managed hashes and continues only missing safe operations. See `11-bootstrap/bootstrap-recovery.md`.

## BLOCKER REPORTING
Use FAILED, BLOCKED_ENVIRONMENT, BLOCKED_ARCHITECTURE, BLOCKED_UPSTREAM or PROOF_NOT_ESTABLISHED with evidence. Green builder tests are only INDEPENDENT_REVIEW_PENDING.

## REVIEW REQUIREMENTS
Fresh pre-apply BREAKER; Builder Assumption Challenge; Boundary Audit for changed stable interfaces; final fresh BREAKER.

## NEXT PHASE CONDITIONS
PHASE-000 accepted and `GATE-000` PASS. Do not proceed otherwise.
