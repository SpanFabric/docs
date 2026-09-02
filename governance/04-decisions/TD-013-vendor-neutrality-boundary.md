# TD-013 — Vendor neutrality boundary
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for vendor neutrality boundary.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-017, RF-018, RF-028

## Decision
Protocol/core resource semantics stay vendor-neutral; capability negotiation exposes vendor-specific optional features without leaking them into generic transport.

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
GFX-009, GPU-006, GPU-007
