# TD-025 — Codex verification workflow
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for codex verification workflow.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-030

## Decision
Every non-trivial implementation phase follows PLAN/GLOBAL IMPACT → build/test → builder assumption challenge → fresh independent BREAKER → fix/regression → fresh BREAKER → acceptance.

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
CI-001, CI-002, CI-003, CI-004, CI-005, CI-006, CI-007, CI-008, CI-009, CI-010, CI-011, CI-012, DOC-001, DOC-002, DOC-003, DOC-004, DOC-005, DOC-006, DOC-007, DOC-008, DOC-009, DOC-010, DOC-011, DOC-012, EVIDENCE-009
