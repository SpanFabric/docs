# PHASE-016 — Remote-authoritative VRAM model

## STATUS
`NOT_STARTED`

## OBJECTIVE
Remote-authoritative VRAM model

## WHY THIS PHASE EXISTS
Risk-first progression requires remote-authoritative vram model before broader capability claims.

## REQUIREMENTS
VRAM-001, VRAM-002, VRAM-003, VRAM-004, VRAM-005, VRAM-006, VRAM-007, VRAM-008, VRAM-009, VRAM-010, VRAM-011, VRAM-012, MEM-001, MEM-002, MEM-003, MEM-004, MEM-005, MEM-006, MEM-007, MEM-008, MEM-009, MEM-010

## TECHNOLOGY DECISIONS
TD-007

## PREREQUISITE GATES
GATE-011

## REPOSITORIES ALLOWED
platform, windows, host, evals

## FILES/AREAS EXPECTED
Only areas required by the implementation tasks and linked repository contracts.

## IMPLEMENTATION TASKS
- Implement formal remote-authoritative resource/VRAM state machine
- Add explicit staging/readback/residency/OOM semantics
- Introduce resource generations and epoch-scoped IDs

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
- Resource state-machine property tests
- OOM tests
- stale ID/epoch tests
- readback correctness

## HARDWARE TESTS REQUIRED
`true`. If required hardware tests do not execute, status cannot become DONE.

## EXPECTED ARTIFACTS
- code/config changes
- test results
- attempt/evidence bundle
- phase report
- fresh BREAKER report

## PROOF GATE
`GATE-007`

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
