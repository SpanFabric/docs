# PHASE-017 — Content-addressed resource cache

## STATUS
`NOT_STARTED`

## OBJECTIVE
Content-addressed resource cache

## WHY THIS PHASE EXISTS
Risk-first progression requires content-addressed resource cache before broader capability claims.

## REQUIREMENTS
CACHE-001, CACHE-002, CACHE-003, CACHE-004, CACHE-005, CACHE-006, CACHE-007, CACHE-008, CACHE-009, CACHE-010, CACHE-011, CACHE-012

## TECHNOLOGY DECISIONS
TD-009

## PREREQUISITE GATES
GATE-007

## REPOSITORIES ALLOWED
platform, host, evals

## FILES/AREAS EXPECTED
Only areas required by the implementation tasks and linked repository contracts.

## IMPLEMENTATION TASKS
- Implement content-addressed immutable resource cache
- Validate cache compatibility metadata and corruption handling
- Measure hit rate and upload avoidance

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
- Cache hit/miss/corruption tests
- dedup tests
- persistence/restart tests

## HARDWARE TESTS REQUIRED
`true`. If required hardware tests do not execute, status cannot become DONE.

## EXPECTED ARTIFACTS
- code/config changes
- test results
- attempt/evidence bundle
- phase report
- fresh BREAKER report

## PROOF GATE
`GATE-008`

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
