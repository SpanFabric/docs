# TD-033 — Driver signing separation
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for driver signing separation.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-004, RF-016, RF-017, RF-018, RF-026

## Decision
Keep development/test signing completely separate from production driver signing; BuilderKit contains policy only, never production signing secrets.

## Consequences
- Implementation and review must preserve architecture invariants.
- Failure of the linked proof may supersede this decision through a new TD; never silently work around it.

## Risks
RISK-027

## Rejected alternatives
- Unavailable proprietary critical path
- Per-game/launcher-specific core integration
- Unproven assumption treated as accepted where status is PROOF_REQUIRED/PROVISIONAL

## Reversibility
Reversible by superseding TD with migration plan before dependent proof-gated phases proceed.

## Migration path
Stop dependent phase, preserve evidence, write superseding TD, update canonical sources/traceability, rerun affected gates.

## Proof requirement
`GATE-028`

## Affected requirements
RELEASE-001
