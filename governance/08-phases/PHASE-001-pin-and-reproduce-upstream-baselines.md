# PHASE-001 — Pin and reproduce upstream baselines

## STATUS
`NOT_STARTED`

## OBJECTIVE
Pin and reproduce upstream baselines

## WHY THIS PHASE EXISTS
Risk-first progression requires pin and reproduce upstream baselines before broader capability claims.

## REQUIREMENTS
UPSTREAM-001, UPSTREAM-002, UPSTREAM-003, UPSTREAM-004, UPSTREAM-005, UPSTREAM-006, UPSTREAM-007, UPSTREAM-008, UPSTREAM-009, UPSTREAM-010, UPSTREAM-011, UPSTREAM-012, UPSTREAM-013, UPSTREAM-014

## TECHNOLOGY DECISIONS
TD-014

## PREREQUISITE GATES
GATE-000

## REPOSITORIES ALLOWED
docs, .github, upstream-forks

## FILES/AREAS EXPECTED
Only areas required by the implementation tasks and linked repository contracts.

## IMPLEMENTATION TASKS
- Resolve UNPINNED upstream baselines to exact commits/tags
- Verify source license at selected baseline
- Build/smoke-test selected OSS baselines from clean checkout
- Record SBOM/upstream metadata and patch baseline

## OUT OF SCOPE
- Unrelated future phases
- Product GUI/marketplace/account polish unless explicitly named

## FORBIDDEN SHORTCUTS
- Per-game patches
- Launcher-specific integration
- DLL injection as primary architecture
- Hidden local GPU fallback presented as remote success
- Skipping required hardware proof

## TESTS REQUIRED
- Clean-room upstream builds
- License manifest validation
- Upstream registry validation

## HARDWARE TESTS REQUIRED
`false`. If required hardware tests do not execute, status cannot become DONE.

## EXPECTED ARTIFACTS
- code/config changes
- test results
- attempt/evidence bundle
- phase report
- fresh BREAKER report

## PROOF GATE
`GATE-000`

## DONE CRITERIA
- All linked requirements in phase scope meet acceptance criteria.
- All required tests executed and passed.
- Builder Assumption Challenge completed.
- Fresh independent BREAKER accepted the target commit.
- Proof gate PASS with immutable evidence where this phase owns/advances the gate.

## FAILURE CONDITIONS
- Required test not executed
- Environment/upstream blocker prevents proof
- Fresh BREAKER finds unresolved blocking defect
- Architecture invariant would be violated

## ROLLBACK
Revert phase changes or restore last known-good driver/runtime build; preserve failed-attempt evidence.

## BLOCKER REPORTING
Use BLOCKED_ENVIRONMENT, BLOCKED_ARCHITECTURE, BLOCKED_UPSTREAM, FAILED or PROOF_NOT_ESTABLISHED with evidence; never DONE by inference.

## REVIEW REQUIREMENTS
- Builder Assumption Challenge
- Fresh BREAKER
- Boundary Audit for every changed stable interface

## NEXT PHASE CONDITIONS
- Current proof gate PASS and all blocking findings VERIFIED
