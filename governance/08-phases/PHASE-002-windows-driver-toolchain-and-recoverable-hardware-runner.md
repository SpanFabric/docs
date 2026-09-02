# PHASE-002 — Windows driver toolchain and recoverable hardware runner

## STATUS
`NOT_STARTED`

## OBJECTIVE
Windows driver toolchain and recoverable hardware runner

## WHY THIS PHASE EXISTS
Risk-first progression requires windows driver toolchain and recoverable hardware runner before broader capability claims.

## REQUIREMENTS
OPS-001, OPS-002, OPS-003, OPS-004, OPS-005, OPS-006, OPS-007, OPS-008, OPS-009, OPS-010, OPS-011, OPS-012, EVIDENCE-004, LAB-001, LAB-002, LAB-003, LAB-004

## TECHNOLOGY DECISIONS
TD-020, TD-032

## PREREQUISITE GATES
GATE-000

## REPOSITORIES ALLOWED
windows, evals, docs

## FILES/AREAS EXPECTED
Only areas required by the implementation tasks and linked repository contracts.

## IMPLEMENTATION TASKS
- Establish WDK/SDK/VS/WinDbg/KD toolchain
- Provision sacrificial client runner with exclusive lease and recovery path
- Configure test-signing only in isolated development environment
- Automate reboot-safe log/dump/ETW collection and rollback guards

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
- Runner lease tests
- Environment fingerprint tests
- Rollback dry run
- Crash artifact persistence test

## HARDWARE TESTS REQUIRED
`true`. If required hardware tests do not execute, status cannot become DONE.

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
