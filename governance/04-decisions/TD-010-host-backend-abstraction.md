# TD-010 — Host backend abstraction
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for host backend abstraction.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-002, RF-005, RF-007, RF-009, RF-018

## Decision
Decode SpanGPU commands into vendor-neutral host renderer interfaces and use stock NVIDIA/AMD host drivers behind them.

## Consequences
- Implementation and review must preserve architecture invariants.
- Failure of the linked proof may supersede this decision through a new TD; never silently work around it.

## Risks
RISK-011, RISK-017

## Rejected alternatives
- Unavailable proprietary critical path
- Per-game/launcher-specific core integration
- Unproven assumption treated as accepted where status is PROOF_REQUIRED/PROVISIONAL

## Reversibility
Reversible by superseding TD with migration plan before dependent proof-gated phases proceed.

## Migration path
Stop dependent phase, preserve evidence, write superseding TD, update canonical sources/traceability, rerun affected gates.

## Proof requirement
`GATE-025`

## Affected requirements
HOST-001, HOST-002, HOST-003, HOST-004, HOST-005, HOST-006, HOST-007, HOST-008, HOST-009, HOST-010, HOST-011, HOST-012, GPU-001, GPU-002, GPU-003, GPU-004, GPU-005, GPU-006, GPU-007, GPU-008, GPU-009, GPU-010
