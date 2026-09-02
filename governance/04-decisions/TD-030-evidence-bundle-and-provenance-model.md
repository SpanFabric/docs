# TD-030 — Evidence bundle and provenance model
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for evidence bundle and provenance model.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-030

## Decision
Every proof/review/recovery attempt emits immutable content-hashed evidence bound to commit, environment, hardware and invocation identity.

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
EVIDENCE-001, EVIDENCE-002, EVIDENCE-003, EVIDENCE-005, EVIDENCE-006, EVIDENCE-007, EVIDENCE-008
