# TD-008 — Synchronization model
**STATUS:** `PROOF_REQUIRED`

## Context
SpanGPU needs an explicit project-wide decision for synchronization model.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-006

## Decision
Use queue-scoped ordering and virtual timeline/fence completions with asynchronous completion propagation; block only when API semantics require it.

## Consequences
- Implementation and review must preserve architecture invariants.
- Failure of the linked proof may supersede this decision through a new TD; never silently work around it.

## Risks
RISK-004

## Rejected alternatives
- Unavailable proprietary critical path
- Per-game/launcher-specific core integration
- Unproven assumption treated as accepted where status is PROOF_REQUIRED/PROVISIONAL

## Reversibility
Reversible by superseding TD with migration plan before dependent proof-gated phases proceed.

## Migration path
Stop dependent phase, preserve evidence, write superseding TD, update canonical sources/traceability, rerun affected gates.

## Proof requirement
`GATE-009`

## Affected requirements
SYNC-001, SYNC-002, SYNC-003, SYNC-004, SYNC-005, SYNC-006, SYNC-007, SYNC-008, SYNC-009, SYNC-010, SYNC-011, SYNC-012

## Structured unresolved decision
STATUS: PROOF_REQUIRED

DECISION_OWNER: Architecture/owning phase

BLOCKING_GATE: GATE-009

OPTIONS:
- Preserve current provisional decision if proof passes.
- Supersede via a new TD using researched/experimental evidence.

EVIDENCE_REQUIRED: Linked gate evidence plus fresh BREAKER review.
