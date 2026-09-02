# TD-031 — Finding and waiver lifecycle
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for finding and waiver lifecycle.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-003, RF-004, RF-005, RF-006, RF-007

## Decision
Findings and waivers are append-only state machines; waivers cannot fabricate proof and fixed findings require fresh independent verification.

## Consequences
- Implementation and review must preserve architecture invariants.
- Failure of the linked proof may supersede this decision through a new TD; never silently work around it.

## Risks
RISK-023, RISK-025, RISK-026

## Rejected alternatives
- Unavailable proprietary critical path
- Per-game/launcher-specific core integration
- Unproven assumption treated as accepted where status is PROOF_REQUIRED/PROVISIONAL

## Reversibility
Reversible by superseding TD with migration plan before dependent proof-gated phases proceed.

## Migration path
Stop dependent phase, preserve evidence, write superseding TD, update canonical sources/traceability, rerun affected gates.

## Proof requirement
`GATE-BK-000`

## Affected requirements
FINDING-001, FINDING-002, FINDING-003, WAIVER-001, WAIVER-002
