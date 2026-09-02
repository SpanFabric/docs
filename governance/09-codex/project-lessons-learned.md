# Project-wide Codex Lessons Learned

- **LL-001 — Global reasoning, local implementation:** Implementation scope stays inside the current phase; reasoning must include the whole product and future-phase compatibility.
- **LL-002 — Global Impact Pass before coding:** Before implementation, enumerate affected requirements, invariants, repositories, producers/consumers, state machines, persistence, auth/trust, concurrency, recovery, migrations and future compatibility.
- **LL-003 — What are we missing before and after build:** Every phase begins and ends with an explicit missing-assumptions pass.
- **LL-004 — Boundary Audit for every changed interface:** Record producer guarantees, consumer assumptions, source of truth, validation/authorization owner, version owner, trust boundary, retry/idempotency, failure semantics and compatibility.
- **LL-005 — Green tests are not DONE:** Passing builder tests means INDEPENDENT_REVIEW_PENDING until fresh independent review and all required proof gates pass.
- **LL-006 — Fresh independent BREAKER:** A separate fresh Codex session receives requirements/invariants and resulting code/commit but not builder reasoning; it attempts to falsify the implementation.
- **LL-007 — Evidence-based merge blocking:** A blocking finding needs a concrete failure mechanism/sequence, violated requirement or invariant, realistic impact/severity, remediation, regression evidence and fresh verification.
- **LL-008 — Fix findings permanently:** Confirmed defects become regression tests and, where systemic, requirements/invariants/documentation so the same class does not recur.
- **LL-009 — Specialists are risk-triggered:** Security, driver, concurrency, database/transaction or performance specialist review is invoked only when the phase presents that risk signal.
- **LL-010 — Environment blockers remain blockers:** If required tests cannot execute because of Windows policy, signing, missing hardware or external services, phase status is BLOCKED_ENVIRONMENT/PROOF_NOT_ESTABLISHED—not DONE.
- **LL-011 — Recovery provenance must be explicit:** Recovery/retry uses unique attempt IDs, immutable evidence IDs and explicit baseline provenance; stale counters or prior-run state cannot silently carry forward.
- **LL-012 — Historical and publication baselines are distinct:** Source/historical evidence and current control-plane/publication state must have distinct identifiers and digests; never infer one from the other.
- **LL-013 — Allowed, required and observed sets are different:** Schemas and validators must distinguish allowed values, exact required values and observed values to avoid permissive-success bugs.
- **LL-014 — Retry and idempotency are designed, not assumed:** Every retryable operation has an idempotency owner/key and ambiguous completion semantics are explicitly tested.
- **LL-015 — Concurrency and transaction semantics need hostile tests:** Races and ambiguous commits can survive green unit suites; use fault injection, repeated parallel runs and explicit invariants.
- **LL-016 — Control plane is protected:** Governance, .github, requirements, TDs, schemas and gate definitions are controlled interfaces; changes require impact review and cross-repo contract checks.
- **LL-017 — No retry-until-green validation:** Validation may rerun after a concrete fix, but must not repeatedly mutate/retry until tests happen to pass.
- **LL-018 — Future scope is checked but not prematurely built:** Document future-phase incompatibility as a finding, but do not implement later features early merely to silence hypothetical concerns.
- **LL-019 — Source of truth must be singular per fact:** Every authoritative state has exactly one owner; caches and projections are explicitly non-authoritative.
- **LL-020 — Authorization and validation ownership are explicit:** Even where current v1 is single-user/single-tenant, trust/validation ownership is recorded so later multi-tenant work cannot inherit implicit trust.
- **LL-021 — Publication requires immutable evidence:** Gate PASS and phase DONE reference immutable evidence artifacts/logs/commit IDs; summaries are not evidence.
- **LL-022 — Independent review is stateful governance:** Project state records builder attempt, breaker attempt, findings, remediation attempt and fresh breaker result as separate immutable events.

These rules are governance inputs, not optional style preferences. Repeated confirmed findings must be converted into tests/requirements/invariants so future phases do not rediscover them from scratch.
