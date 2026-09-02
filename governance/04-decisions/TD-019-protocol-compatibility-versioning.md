# TD-019 — Protocol compatibility/versioning
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for protocol compatibility/versioning.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-030

## Decision
Handshake negotiates protocol, feature, API and backend capabilities; incompatible major versions fail closed with explicit diagnostics.

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
PROTO-001, PROTO-002, PROTO-003, PROTO-004, PROTO-005, PROTO-006, PROTO-007, PROTO-008, PROTO-009, PROTO-010, PROTO-011, PROTO-012, PROTO-013
