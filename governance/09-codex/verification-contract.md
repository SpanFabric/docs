# Codex Verification Contract
## Mandatory flow
1. PLAN.
2. GLOBAL IMPACT PASS.
3. “What are we missing?” pre-build.
4. BUILD + TEST within phase scope.
5. BUILDER ASSUMPTION CHALLENGE.
6. Builder result becomes `INDEPENDENT_REVIEW_PENDING` when its own tests are green.
7. Start a **fresh independent BREAKER** session with no builder reasoning history.
8. If valid findings: FIX → regression evidence → new fresh BREAKER.
9. Specialist review only when a concrete risk signal exists.
10. ACCEPT only after required gate/evidence/review conditions pass.

## Global impact topics
Requirements/invariants; producer/consumer boundaries; source of truth; validation/authorization/trust/version ownership; concurrency; transactions; retry/idempotency; failure semantics; migrations; recovery epochs; upstreams; future-phase compatibility.

## Merge-blocking finding quality
Concrete failure mechanism/sequence; violated requirement/invariant; realistic impact/severity; remediation; regression test/equivalent evidence; fresh verification after fix. Hypothetical concern without mechanism is documented but does not create ritual review loops.
