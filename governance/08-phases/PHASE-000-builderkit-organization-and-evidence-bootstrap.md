# PHASE-000 — BuilderKit, organization and evidence bootstrap

## STATUS
`IN_PROGRESS`

## OBJECTIVE
Complete the post-bootstrap verification and integration chain without implementing GPU
functionality or replaying repository creation.

## WHY THIS PHASE EXISTS
The repository, governance, CI and evidence baselines already exist through
`CONTROLLED_INITIAL_BASELINE_BOOTSTRAP`. That existence proves neither Phase completion
nor a gate result. The remaining work is exact-head verification, independent review,
authority-controlled integration and post-merge proof.

## REQUIREMENTS
VISION-001, VISION-002, VISION-003, VISION-004, VISION-005, VISION-006, VISION-007, VISION-008, VISION-009, VISION-010, TEST-001, TEST-002, TEST-003, TEST-004, TEST-005, TEST-006, TEST-007, TEST-008, TEST-009, TEST-010, TEST-011, TEST-012, TEST-013, TEST-014, TEST-015, TEST-016, TEST-017, TEST-018, CI-001, CI-002, CI-003, CI-004, CI-005, CI-006, CI-007, CI-008, CI-009, CI-010, CI-011, CI-012, LICENSE-001, LICENSE-002, LICENSE-003, LICENSE-004, LICENSE-005, LICENSE-006, LICENSE-007, LICENSE-008, LICENSE-009, LICENSE-010, BUILD-001, BUILD-002, BUILD-003, BUILD-004, BUILD-005, BUILD-006, BUILD-007, BUILD-008, BUILD-009, BUILD-010, BUILD-011, DOC-001, DOC-002, DOC-003, DOC-004, DOC-005, DOC-006, DOC-007, DOC-008, DOC-009, DOC-010, DOC-011, DOC-012, DOC-013, DOC-014, DOC-015, DOC-016, DOC-017, DOC-018, EVIDENCE-001, EVIDENCE-002, EVIDENCE-003, EVIDENCE-005, EVIDENCE-006, EVIDENCE-007, EVIDENCE-008, EVIDENCE-009, FINDING-001, FINDING-002, FINDING-003, WAIVER-001, WAIVER-002, BOUNDARY-001, BOUNDARY-002, SOURCE-001, SOURCE-002

## TECHNOLOGY DECISIONS
TD-001, TD-003, TD-020, TD-025, TD-026, TD-027, TD-028, TD-029, TD-030, TD-031

## PREREQUISITE GATES
`GATE-BK-000` must be PASS. No SpanGPU runtime proof prerequisite.

## REPOSITORIES ALLOWED
platform, windows, host, evals, docs, .github

## CURRENT OPERATIONAL SEMANTICS

### Historical context, not an execution route
The original two-stage BuilderKit apply strategy is `SUPERSEDED`. The actual method was
`CONTROLLED_INITIAL_BASELINE_BOOTSTRAP`. Its preserved prompts, reports and findings are
provenance only, as classified by `12-machine-readable/governance-entrypoints.yaml`.

F-000-04 keeps the BuilderKit materializer Apply capability `QUARANTINED` and
`FORBIDDEN`. It is not required or authorized for the current completion route. The old
global pre-bootstrap GitHub-mutation prohibition is also superseded; the current
boundary is the normal PR and `MANUAL_AUTHORITY` flow.

### Remaining completion route
1. Resolve the exact current heads and review-subject digests for the six open PRs.
2. Obtain a fresh independent BREAKER review of those exact subjects.
3. Complete the required external GitHub protections, required checks and independent
   review controls under `MANUAL_AUTHORITY`; repository text alone cannot assert them.
4. Obtain Owner Acceptance without inferring it from Builder, CI, or BREAKER work.
5. Cross the controlled merge boundary and record the exact resulting merge SHA.
6. Run post-merge verification against that resulting merge SHA.
7. Evaluate `GATE-000` from its own required evidence.
8. Mark PHASE-000 complete only after the preceding conditions are actually satisfied;
   only then may the authorization for PHASE-001 be reconsidered.

At present, PHASE-000 is `NOT_COMPLETED`, GATE-000 is `NOT_PASSED`, and PHASE-001 is
`NOT_AUTHORIZED`.

## REQUIREMENT IMPACT
This correction preserves the safety intent of reproducibility, bounded mutations,
recovery, evidence, independent review and authorization. It changes only the obsolete
Bootstrap mechanism: existing repositories are now governed through normal PR and
authority controls. No linked product requirement is weakened, and no product intent is
changed.

## OUT OF SCOPE
WDDM/KMD/UMD feature work; GPU transport/rendering; remote VRAM runtime; graphics APIs; production signing; controlled upstream forks; product GUI/account/marketplace work.

## FORBIDDEN SHORTCUTS
No ad-hoc copying of governance; no retry-until-green; no automatic deletion rollback; no repository repurposing; no per-game/launcher/injection architecture; no hidden local-GPU success substitution.

## RETAINED BUILDERKIT VALIDATION PROVENANCE — NOT CURRENT EXECUTION

The following test names preserve the linked historical safety evidence for
reproducibility, fixed targets, zero-write conflict handling and recovery. They do not
authorize a historical Bootstrap action, do not define the current completion route,
and cannot clear F-000-04 quarantine.
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

## CURRENT VALIDATION REQUIRED
- Complete repository-local Manual Verification Bridge suite.
- Active-governance semantic regression suite and its adversarial fixtures.
- PROJECT_STATE semantic and schema validation, phase/gate schema validation, and
  traceability validation.
- Authoritative trusted-runner validation against the canonical `origin/main` base.
- Exact-head CI results for the required verification and bootstrap-integrity subjects.
- Fresh BREAKER, then the external authority and merge/post-merge checks described above.

## HARDWARE TESTS REQUIRED
`false`

## HISTORICAL BUILDERKIT ARTIFACT PROVENANCE — NOT CURRENT EXECUTION
Sealed pre-apply evidence + breaker verdict; repositories/clones if authorized; materialization states; canonical governance commits; CI/Steward baseline; sealed post-apply evidence; boundary audits; final breaker handoff.

## CURRENT EXPECTED ARTIFACTS
Exact review-subject digests; Builder evidence; CI results; Fresh BREAKER report;
external authority records; exact merge-SHA and post-merge evidence; gate evaluation;
boundary audits; final acceptance evidence.

## PROOF GATE
`GATE-000`

## DONE CRITERIA
All linked scope criteria and current validation pass; a fresh BREAKER accepts the exact
current PR subjects; external protection/review controls and Owner Acceptance are
completed; the resulting merge SHA is verified post-merge; and `GATE-000` passes with
immutable evidence. Historical BuilderKit checks remain provenance and do not substitute
for any current authority boundary.

## HISTORICAL BUILDERKIT FAILURE PROVENANCE — NOT CURRENT EXECUTION
Any required test does not execute; dry-run nonzero/unexpected scope; unmanaged materialization conflict; environment/upstream blocker; unresolved blocking breaker finding; architecture invariant violation.

## CURRENT FAILURE CONDITIONS
Any required current validation does not execute; exact-head CI, Fresh BREAKER,
external authority, merge-SHA, post-merge verification, or GATE-000 evidence is absent;
an unresolved blocking finding exists; or an architecture invariant would be violated.

## HISTORICAL BUILDERKIT RECOVERY PROVENANCE — NOT CURRENT EXECUTION
Preserve partial repositories and evidence. Never delete automatically. New attempt rediscovers state, verifies origins/managed hashes and continues only missing safe operations. See `11-bootstrap/bootstrap-recovery.md`.

## CURRENT ROLLBACK / RECOVERY
Preserve the existing repository and evidence history. Never delete automatically. A
failed review or integration produces a new bounded remediation subject and fresh
verification; it does not replay historical bootstrap actions.

## BLOCKER REPORTING
Use FAILED, BLOCKED_ENVIRONMENT, BLOCKED_ARCHITECTURE, BLOCKED_UPSTREAM or PROOF_NOT_ESTABLISHED with evidence. Green builder tests are only INDEPENDENT_REVIEW_PENDING.

## REVIEW REQUIREMENTS
Builder Assumption Challenge; Boundary Audit for changed stable interfaces; Fresh BREAKER;
external protection/review authority; Owner Acceptance; merge and post-merge verification.

## NEXT PHASE CONDITIONS
`GATE-000` must PASS and all blocking findings must be VERIFIED. PHASE-001 remains
unauthorized until those conditions are met.
