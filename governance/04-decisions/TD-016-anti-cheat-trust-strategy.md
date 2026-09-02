# TD-016 — Anti-cheat trust strategy
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for anti-cheat trust strategy.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-028

## Decision
Pursue only documented drivers, signing, Secure Boot/attestation and vendor cooperation; third-party rejection is a compatibility state, never a bypass trigger.

## Consequences
- Implementation and review must preserve architecture invariants.
- Failure of the linked proof may supersede this decision through a new TD; never silently work around it.

## Risks
RISK-016

## Rejected alternatives
- Unavailable proprietary critical path
- Per-game/launcher-specific core integration
- Unproven assumption treated as accepted where status is PROOF_REQUIRED/PROVISIONAL

## Reversibility
Reversible by superseding TD with migration plan before dependent proof-gated phases proceed.

## Migration path
Stop dependent phase, preserve evidence, write superseding TD, update canonical sources/traceability, rerun affected gates.

## Proof requirement
`GATE-029`

## Affected requirements
ANTICHEAT-001, ANTICHEAT-002, ANTICHEAT-003, ANTICHEAT-004, ANTICHEAT-005, ANTICHEAT-006, ANTICHEAT-007, ANTICHEAT-008
