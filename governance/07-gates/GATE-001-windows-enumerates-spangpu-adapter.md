# GATE-001 — Windows enumerates SpanGPU adapter
**STATUS:** `NOT_RUN`  
**KIND:** `implementation`

## OBJECTIVE
A Windows 11 test machine enumerates SpanGPU as a secondary hardware-accelerated adapter beside the local GPU without instability.

## RATIONALE
Windows enumerates SpanGPU adapter is a risk-first proof required before later claims depend on it.

## PREREQUISITES
GATE-000

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
A Windows 11 test machine enumerates SpanGPU as a secondary hardware-accelerated adapter beside the local GPU without instability.

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
