# PHASE-007 — Host daemon and vendor-backend boundary

## STATUS
`NOT_STARTED`

## OBJECTIVE
Host daemon and vendor-backend boundary

## WHY THIS PHASE EXISTS
Risk-first progression requires host daemon and vendor-backend boundary before broader capability claims.

## REQUIREMENTS
HOST-001, HOST-002, HOST-003, HOST-004, HOST-005, HOST-006, HOST-007, HOST-008, HOST-009, HOST-010, HOST-011, HOST-012, GPU-001, GPU-002, GPU-003, GPU-004, GPU-005, GPU-006, GPU-007, GPU-008, GPU-009, GPU-010

## TECHNOLOGY DECISIONS
TD-010, TD-013

## PREREQUISITE GATES
GATE-002

## REPOSITORIES ALLOWED
host, platform

## FILES/AREAS EXPECTED
Only areas required by the implementation tasks and linked repository contracts.

## IMPLEMENTATION TASKS
- Create host session skeleton and RGPU_BACKEND ABI
- Integrate first proof renderer/backend from controlled OSS baseline
- Record physical GPU/capability identity

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
- Backend contract tests
- Host capability tests

## HARDWARE TESTS REQUIRED
`false`. If required hardware tests do not execute, status cannot become DONE.

## EXPECTED ARTIFACTS
- code/config changes
- test results
- attempt/evidence bundle
- phase report
- fresh BREAKER report

## PROOF GATE
`GATE-003`

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
