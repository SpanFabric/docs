# TD-032 — Hardware runner isolation model
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for hardware runner isolation model.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-017, RF-026

## Decision
Use exclusive runner leases, environment fingerprints, reset/contamination checks and out-of-band recovery before hardware evidence is admissible.

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
EVIDENCE-004, LAB-001, LAB-002, LAB-003, LAB-004, LAB-005
