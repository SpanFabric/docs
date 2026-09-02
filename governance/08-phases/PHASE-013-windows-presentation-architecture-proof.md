# PHASE-013 — Windows presentation architecture proof

## STATUS
`NOT_STARTED`

## OBJECTIVE
Windows presentation architecture proof

## WHY THIS PHASE EXISTS
Risk-first progression requires windows presentation architecture proof before broader capability claims.

## REQUIREMENTS
FUNC-005, MULTIGPU-001

## TECHNOLOGY DECISIONS
No new decision ownership; existing architecture invariants still apply.

## PREREQUISITE GATES
GATE-005

## REPOSITORIES ALLOWED
windows, host, evals

## FILES/AREAS EXPECTED
Only areas required by the implementation tasks and linked repository contracts.

## IMPLEMENTATION TASKS
- Prototype legitimate Windows presentation path per TD-012 candidates
- Measure remote render→return→present stages
- Reject streaming-window-only hacks as proof

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
- Presentation correctness test
- DWM/display integration test
- resize/fullscreen/device-loss cases

## HARDWARE TESTS REQUIRED
`true`. If required hardware tests do not execute, status cannot become DONE.

## EXPECTED ARTIFACTS
- code/config changes
- test results
- attempt/evidence bundle
- phase report
- fresh BREAKER report

## PROOF GATE
`GATE-006`

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
