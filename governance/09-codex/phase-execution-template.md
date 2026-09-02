# Phase Execution
PHASE / target commit / builder attempt ID

## PLAN
Implementation scope; assumptions; files/repos; tests; rollback.

## GLOBAL IMPACT PASS
Requirements/invariants; boundaries; source-of-truth; validation/trust/version owners; concurrency/transactions; retry/idempotency; recovery; upstreams; future compatibility.

## WHAT ARE WE MISSING? — PRE
List missing assumptions or state none with evidence.

## BUILD + TEST
Exact commands and results. Skipped/blocked tests are explicit.

## BUILDER ASSUMPTION CHALLENGE
Attempt to falsify implementation and identify weak assumptions.

## BUILDER RESULT
`INDEPENDENT_REVIEW_PENDING` / FAILED / BLOCKED_* / PROOF_NOT_ESTABLISHED.

## HANDOFF
Produce Breaker handoff manifest; no builder reasoning history.
