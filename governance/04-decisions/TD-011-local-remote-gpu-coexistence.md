# TD-011 — Local/remote GPU coexistence
**STATUS:** `PROOF_REQUIRED`

## Context
SpanGPU needs an explicit project-wide decision for local/remote gpu coexistence.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-001, RF-002, RF-006, RF-008, RF-010

## Decision
SpanGPU enumerates as an additional adapter; local GPU remains available for desktop/decode/fallback where application semantics permit.

## Consequences
- Implementation and review must preserve architecture invariants.
- Failure of the linked proof may supersede this decision through a new TD; never silently work around it.

## Risks
Tracked by architecture risk register.

## Rejected alternatives
- Unavailable proprietary critical path
- Per-game/launcher-specific core integration
- Unproven assumption treated as accepted where status is PROOF_REQUIRED/PROVISIONAL

## Reversibility
Reversible by superseding TD with migration plan before dependent proof-gated phases proceed.

## Migration path
Stop dependent phase, preserve evidence, write superseding TD, update canonical sources/traceability, rerun affected gates.

## Proof requirement
`GATE-012`

## Affected requirements
MULTIGPU-001, MULTIGPU-002, MULTIGPU-003, MULTIGPU-004, MULTIGPU-005, MULTIGPU-006, MULTIGPU-007, MULTIGPU-008

## Structured unresolved decision
STATUS: PROOF_REQUIRED

DECISION_OWNER: Architecture/owning phase

BLOCKING_GATE: GATE-012

OPTIONS:
- Preserve current provisional decision if proof passes.
- Supersede via a new TD using researched/experimental evidence.

EVIDENCE_REQUIRED: Linked gate evidence plus fresh BREAKER review.
