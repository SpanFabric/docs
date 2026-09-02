# TD-018 — Observability contract
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for observability contract.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-030

## Decision
Every proof path emits correlation IDs, queue/fence timings, cache/resource metrics, network metrics, device-loss state and immutable evidence bundles.

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
PERF-001, PERF-002, PERF-003, PERF-004, PERF-005, PERF-006, PERF-007, PERF-008, PERF-009, PERF-010, PERF-011, PERF-012, PERF-013, PERF-014, OBS-001, OBS-002, OBS-003, OBS-004, OBS-005, OBS-006, OBS-007, OBS-008, OBS-009, OBS-010, OBS-011
