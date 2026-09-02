# GATE-028 — Signed/Secure Boot path
**STATUS:** `NOT_RUN`  
**KIND:** `implementation`

## OBJECTIVE
A production-like signed driver deployment path works under Secure Boot on designated hardware; test-signing is no longer the only path.

## RATIONALE
Signed/Secure Boot path is a risk-first proof required before later claims depend on it.

## PREREQUISITES
GATE-027

## ENVIRONMENT
As defined by owning phase and test matrix.

## HARDWARE
Required

## PROCEDURE
1. Execute all tests linked by owning phase(s).
2. Create immutable attempt/evidence bundle bound to target commit/environment/hardware.
3. Run Builder Assumption Challenge.
4. Run fresh independent BREAKER against the target commit/evidence.
5. Record gate verdict without mutating prior attempts.

## EXPECTED RESULT
A production-like signed driver deployment path works under Secure Boot on designated hardware; test-signing is no longer the only path.

## METRICS
- Gate-specific correctness metrics
- Crash/TDR/error counters where applicable
- Performance/network metrics where applicable

## ARTIFACTS
- attempt metadata
- raw logs/traces/dumps as applicable
- derived metrics with provenance
- builder report
- fresh BREAKER report
- gate report

## PASS RULE
All required acceptance criteria/tests execute and pass, no unresolved blocking findings remain, fresh BREAKER accepts, and immutable evidence references the exact target commit.

## FAIL RULE
Reproducible requirement/invariant violation, unresolved blocking finding or executed proof failing acceptance criteria produces FAIL.

## BLOCKED RULE
Required environment/hardware/upstream unavailable produces explicit BLOCKED_* or PROOF_NOT_ESTABLISHED, never PASS.

## NEXT ACTION
Proceed to next risk-first phase only after PASS.
