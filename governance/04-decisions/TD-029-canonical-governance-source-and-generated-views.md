# TD-029 — Canonical governance source and generated views
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for canonical governance source and generated views.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-030

## Decision
Use canonical YAML under 12-machine-readable for governance entities; Markdown/JSON projections are generated/validated to prevent drift.

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
BOUNDARY-001, BOUNDARY-002, SOURCE-001, SOURCE-002
