# PHASE-025 — Remote-host failure semantics

## STATUS
`NOT_STARTED`

## OBJECTIVE
Remote-host failure semantics

## WHY THIS PHASE EXISTS
Risk-first progression requires remote-host failure semantics before broader capability claims.

## REQUIREMENTS
RECOVERY-001, RECOVERY-002, RECOVERY-003, RECOVERY-004, RECOVERY-005, RECOVERY-006, RECOVERY-007, RECOVERY-008, RECOVERY-009, RECOVERY-010, RECOVERY-011, RECOVERY-012

## TECHNOLOGY DECISIONS
TD-017

## PREREQUISITE GATES
GATE-017

## REPOSITORIES ALLOWED
platform, windows, host, evals, docs

## FILES/AREAS EXPECTED
Only areas required by the implementation tasks and linked repository contracts.

## IMPLEMENTATION TASKS
- Controlled host crash/reset semantics

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
- Host kill/reset tests
- device-loss evidence

## HARDWARE TESTS REQUIRED
`true`. If required hardware tests do not execute, status cannot become DONE.

## EXPECTED ARTIFACTS
- code/config changes
- test results
- attempt/evidence bundle
- phase report
- fresh BREAKER report

## PROOF GATE
`GATE-018`

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
