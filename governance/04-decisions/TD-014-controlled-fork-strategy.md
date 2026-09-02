# TD-014 — Controlled fork strategy
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for controlled fork strategy.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-012, RF-015, RF-017, RF-026, RF-029

## Decision
Critical WDDM/UMD/host renderer code is maintained as controlled pinned forks with explicit patch queues and manual upstream adoption.

## Consequences
- Implementation and review must preserve architecture invariants.
- Failure of the linked proof may supersede this decision through a new TD; never silently work around it.

## Risks
RISK-007, RISK-008, RISK-018, RISK-020, RISK-024

## Rejected alternatives
- Unavailable proprietary critical path
- Per-game/launcher-specific core integration
- Unproven assumption treated as accepted where status is PROOF_REQUIRED/PROVISIONAL

## Reversibility
Reversible by superseding TD with migration plan before dependent proof-gated phases proceed.

## Migration path
Stop dependent phase, preserve evidence, write superseding TD, update canonical sources/traceability, rerun affected gates.

## Proof requirement
`GATE-000`

## Affected requirements
UPSTREAM-001, UPSTREAM-002, UPSTREAM-003, UPSTREAM-004, UPSTREAM-005, UPSTREAM-006, UPSTREAM-007, UPSTREAM-008, UPSTREAM-009, UPSTREAM-010, UPSTREAM-011, UPSTREAM-012, UPSTREAM-013, UPSTREAM-014
