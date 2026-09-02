# TD-027 — Governance source of truth
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for governance source of truth.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-005, RF-006, RF-011, RF-024

## Decision
Before bootstrap the BuilderKit is authoritative; after Phase 00 the SpanGPU/docs repository owns requirements, TDs, gates, phases and architecture metadata, while .github owns organization policy/workflows and never duplicates normative state.

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
DOC-013
