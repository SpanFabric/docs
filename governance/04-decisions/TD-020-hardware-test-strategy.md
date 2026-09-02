# TD-020 — Hardware test strategy
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for hardware test strategy.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-010, RF-017, RF-026, RF-028

## Decision
Kernel/graphics claims require isolated recoverable Windows hardware runners and separate GPU hosts; CI-only simulation cannot substitute required hardware evidence.

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
TEST-001, TEST-002, TEST-003, TEST-004, TEST-005, TEST-006, TEST-007, TEST-008, TEST-009, TEST-010, TEST-011, TEST-012, TEST-013, TEST-014, TEST-015, TEST-016, TEST-017, TEST-018, BUILD-001, BUILD-002, BUILD-003, BUILD-004, BUILD-005, BUILD-006, BUILD-007, BUILD-008, BUILD-009, BUILD-010, BUILD-011, OPS-001, OPS-002, OPS-003, OPS-004, OPS-005, OPS-006, OPS-007, OPS-008, OPS-009, OPS-010, OPS-011, OPS-012
