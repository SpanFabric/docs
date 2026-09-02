# TD-009 — Persistent resource caching
**STATUS:** `PROVISIONAL`

## Context
SpanGPU needs an explicit project-wide decision for persistent resource caching.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-006, RF-024

## Decision
Use content-addressed immutable payload identities plus versioned mutable resource metadata; begin session-local, preserve persistent-cache compatibility.

## Consequences
- Implementation and review must preserve architecture invariants.
- Failure of the linked proof may supersede this decision through a new TD; never silently work around it.

## Risks
RISK-009

## Rejected alternatives
- Unavailable proprietary critical path
- Per-game/launcher-specific core integration
- Unproven assumption treated as accepted where status is PROOF_REQUIRED/PROVISIONAL

## Reversibility
Reversible by superseding TD with migration plan before dependent proof-gated phases proceed.

## Migration path
Stop dependent phase, preserve evidence, write superseding TD, update canonical sources/traceability, rerun affected gates.

## Proof requirement
`GATE-008`

## Affected requirements
CACHE-001, CACHE-002, CACHE-003, CACHE-004, CACHE-005, CACHE-006, CACHE-007, CACHE-008, CACHE-009, CACHE-010, CACHE-011, CACHE-012

## Structured unresolved decision
STATUS: PROVISIONAL

DECISION_OWNER: Architecture/owning phase

BLOCKING_GATE: GATE-008

OPTIONS:
- Preserve current provisional decision if proof passes.
- Supersede via a new TD using researched/experimental evidence.

EVIDENCE_REQUIRED: Linked gate evidence plus fresh BREAKER review.
