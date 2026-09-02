# TD-003 — virtio reuse boundary
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for virtio reuse boundary.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-003, RF-004, RF-006, RF-007, RF-008

## Decision
Reuse virtio/Triton device, object and WDDM patterns, but do not expose virtqueue/shared-memory semantics as the public WAN protocol.

## Consequences
- Implementation and review must preserve architecture invariants.
- Failure of the linked proof may supersede this decision through a new TD; never silently work around it.

## Risks
RISK-010, RISK-021

## Rejected alternatives
- Unavailable proprietary critical path
- Per-game/launcher-specific core integration
- Unproven assumption treated as accepted where status is PROOF_REQUIRED/PROVISIONAL

## Reversibility
Reversible by superseding TD with migration plan before dependent proof-gated phases proceed.

## Migration path
Stop dependent phase, preserve evidence, write superseding TD, update canonical sources/traceability, rerun affected gates.

## Proof requirement
`GATE-003`

## Affected requirements
VISION-009, WDDM-012, TRANSPORT-011
