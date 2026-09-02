# PHASE-029 — Vulkan frontend using common SpanGPU core

## STATUS
`NOT_STARTED`

## OBJECTIVE
Vulkan frontend using common SpanGPU core

## WHY THIS PHASE EXISTS
Risk-first progression requires vulkan frontend using common spangpu core before broader capability claims.

## REQUIREMENTS
VK-001, VK-002, VK-003, VK-004, VK-005, VK-006, VK-007, VK-008, VK-009, VK-010

## TECHNOLOGY DECISIONS
TD-004

## PREREQUISITE GATES
GATE-012

## REPOSITORIES ALLOWED
platform, windows, host, evals, docs

## FILES/AREAS EXPECTED
Only areas required by the implementation tasks and linked repository contracts.

## IMPLEMENTATION TASKS
- Vulkan frontend on common resource/session core

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
- Vulkan CTS-inspired subset
- unmodified Vulkan app

## HARDWARE TESTS REQUIRED
`true`. If required hardware tests do not execute, status cannot become DONE.

## EXPECTED ARTIFACTS
- code/config changes
- test results
- attempt/evidence bundle
- phase report
- fresh BREAKER report

## PROOF GATE
`GATE-021`

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
