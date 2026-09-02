# PHASE-038 — Compatibility database and representative engine/game matrix

## STATUS
`NOT_STARTED`

## OBJECTIVE
Compatibility database and representative engine/game matrix

## WHY THIS PHASE EXISTS
Risk-first progression requires compatibility database and representative engine/game matrix before broader capability claims.

## REQUIREMENTS
COMPAT-001, COMPAT-002, COMPAT-003, COMPAT-004, COMPAT-005, COMPAT-006, COMPAT-007, COMPAT-008, COMPAT-009, COMPAT-010, COMPAT-011, COMPAT-012, COMPAT-013

## TECHNOLOGY DECISIONS
TD-021

## PREREQUISITE GATES
GATE-028

## REPOSITORIES ALLOWED
platform, windows, host, evals, docs

## FILES/AREAS EXPECTED
Only areas required by the implementation tasks and linked repository contracts.

## IMPLEMENTATION TASKS
- Compatibility database and representative engine/game matrix

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
- Unity/Unreal/custom/legacy matrix
- taxonomy validation

## HARDWARE TESTS REQUIRED
`true`. If required hardware tests do not execute, status cannot become DONE.

## EXPECTED ARTIFACTS
- code/config changes
- test results
- attempt/evidence bundle
- phase report
- fresh BREAKER report

## PROOF GATE
`GATE-026`

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
