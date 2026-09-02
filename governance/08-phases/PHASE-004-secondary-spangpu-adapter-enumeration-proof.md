# PHASE-004 — Secondary SpanGPU adapter enumeration proof

## STATUS
`NOT_STARTED`

## OBJECTIVE
Secondary SpanGPU adapter enumeration proof

## WHY THIS PHASE EXISTS
Risk-first progression requires secondary spangpu adapter enumeration proof before broader capability claims.

## REQUIREMENTS
FUNC-001, FUNC-002, FUNC-003, FUNC-004, FUNC-005, FUNC-006, FUNC-007, FUNC-008, FUNC-009, FUNC-010, WIN-001, WIN-002, WIN-003, WIN-004, WIN-005, WIN-006, WIN-007, WIN-008, WIN-009, WIN-010, WDDM-001, WDDM-002, WDDM-003, WDDM-004, WDDM-005, WDDM-006, WDDM-007, WDDM-008, WDDM-009, WDDM-010, WDDM-011, WDDM-012

## TECHNOLOGY DECISIONS
TD-001, TD-002, TD-003

## PREREQUISITE GATES
GATE-000

## REPOSITORIES ALLOWED
windows, evals

## FILES/AREAS EXPECTED
Only areas required by the implementation tasks and linked repository contracts.

## IMPLEMENTATION TASKS
- Minimize/adapt Triton-derived WDDM adapter for secondary enumeration
- Install only on sacrificial test machine through guarded runner
- Capture Device Manager/dxdiag/DXGI enumeration and crash evidence

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
- Adapter enumeration integration test
- Install/uninstall/rollback test

## HARDWARE TESTS REQUIRED
`true`. If required hardware tests do not execute, status cannot become DONE.

## EXPECTED ARTIFACTS
- code/config changes
- test results
- attempt/evidence bundle
- phase report
- fresh BREAKER report

## PROOF GATE
`GATE-001`

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
