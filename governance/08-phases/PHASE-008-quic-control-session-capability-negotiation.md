# PHASE-008 — QUIC control/session/capability negotiation

## STATUS
`NOT_STARTED`

## OBJECTIVE
QUIC control/session/capability negotiation

## WHY THIS PHASE EXISTS
Risk-first progression requires quic control/session/capability negotiation before broader capability claims.

## REQUIREMENTS
PROTO-001, PROTO-002, PROTO-003, PROTO-004, PROTO-005, PROTO-006, PROTO-007, PROTO-008, PROTO-009, PROTO-010, PROTO-011, PROTO-012, PROTO-013, TRANSPORT-001, TRANSPORT-002, TRANSPORT-003, TRANSPORT-004, TRANSPORT-005, TRANSPORT-006, TRANSPORT-007, TRANSPORT-008, TRANSPORT-009, TRANSPORT-010, TRANSPORT-011

## TECHNOLOGY DECISIONS
TD-003, TD-005, TD-019

## PREREQUISITE GATES
GATE-003

## REPOSITORIES ALLOWED
platform, host, windows

## FILES/AREAS EXPECTED
Only areas required by the implementation tasks and linked repository contracts.

## IMPLEMENTATION TASKS
- Implement MsQuic session/auth/capability negotiation behind RGPU_TRANSPORT
- Separate allowed/required/observed capability sets
- Implement session epochs and bounded reconnect-free initial behavior

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
- Protocol negotiation tests
- Version-skew tests
- mTLS/session tests
- malformed input fuzzing

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
