# TD-005 — Default WAN transport
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for default wan transport.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-002, RF-004, RF-007, RF-009, RF-014

## Decision
Use MsQuic as the default replaceable QUIC/TLS transport; keep transport ABI independent of graphics protocol.

## Consequences
- Implementation and review must preserve architecture invariants.
- Failure of the linked proof may supersede this decision through a new TD; never silently work around it.

## Risks
Tracked by architecture risk register.

## Rejected alternatives
- Unavailable proprietary critical path
- Per-game/launcher-specific core integration
- Unproven assumption treated as accepted where status is PROOF_REQUIRED/PROVISIONAL

## Reversibility
Reversible by superseding TD with migration plan before dependent proof-gated phases proceed.

## Migration path
Stop dependent phase, preserve evidence, write superseding TD, update canonical sources/traceability, rerun affected gates.

## Proof requirement
`GATE-014`

## Affected requirements
TRANSPORT-001, TRANSPORT-002, TRANSPORT-003, TRANSPORT-004, TRANSPORT-005, TRANSPORT-006, TRANSPORT-007, TRANSPORT-008, TRANSPORT-009, TRANSPORT-010, TRANSPORT-011, WAN-001, WAN-002, WAN-003, WAN-004, WAN-005, WAN-006, WAN-007, WAN-008, WAN-009, WAN-010, WAN-011, WAN-012
