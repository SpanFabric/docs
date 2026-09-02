# TD-001 — Client abstraction boundary
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for client abstraction boundary.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-003, RF-013, RF-017, RF-018

## Decision
Use a normal WDDM adapter with API UMD/ICDs above a common SpanGPU session/resource layer; no launcher/game integration.

## Consequences
- Implementation and review must preserve architecture invariants.
- Failure of the linked proof may supersede this decision through a new TD; never silently work around it.

## Risks
RISK-001

## Rejected alternatives
- Unavailable proprietary critical path
- Per-game/launcher-specific core integration
- Unproven assumption treated as accepted where status is PROOF_REQUIRED/PROVISIONAL

## Reversibility
Reversible by superseding TD with migration plan before dependent proof-gated phases proceed.

## Migration path
Stop dependent phase, preserve evidence, write superseding TD, update canonical sources/traceability, rerun affected gates.

## Proof requirement
`GATE-001`

## Affected requirements
VISION-001, VISION-002, VISION-003, VISION-004, VISION-005, VISION-006, VISION-007, VISION-008, VISION-009, VISION-010, FUNC-001, FUNC-002, FUNC-003, FUNC-004, FUNC-005, FUNC-006, FUNC-007, FUNC-008, FUNC-009, FUNC-010
