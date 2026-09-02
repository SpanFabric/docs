# TD-028 — Evidence and attempt state model
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for evidence and attempt state model.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-003, RF-004, RF-005, RF-006, RF-007

## Decision
Gate/phase/review state is append-only by attempt: builder attempt, validation evidence, breaker attempt, findings, remediation and fresh breaker are separate records linked to immutable commits/artifacts.

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
DOC-014, DOC-015, DOC-016, DOC-017, DOC-018
