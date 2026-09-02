# TD-017 — Failure and recovery semantics
**STATUS:** `PROOF_REQUIRED`

## Context
SpanGPU needs an explicit project-wide decision for failure and recovery semantics.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-003, RF-004, RF-005, RF-006, RF-007

## Decision
Network/host loss must converge to controlled device loss or bounded recovery with attempt-scoped provenance, no stale-state reuse and no BSOD.

## Consequences
- Implementation and review must preserve architecture invariants.
- Failure of the linked proof may supersede this decision through a new TD; never silently work around it.

## Risks
RISK-019

## Rejected alternatives
- Unavailable proprietary critical path
- Per-game/launcher-specific core integration
- Unproven assumption treated as accepted where status is PROOF_REQUIRED/PROVISIONAL

## Reversibility
Reversible by superseding TD with migration plan before dependent proof-gated phases proceed.

## Migration path
Stop dependent phase, preserve evidence, write superseding TD, update canonical sources/traceability, rerun affected gates.

## Proof requirement
`GATE-020`

## Affected requirements
RECOVERY-001, RECOVERY-002, RECOVERY-003, RECOVERY-004, RECOVERY-005, RECOVERY-006, RECOVERY-007, RECOVERY-008, RECOVERY-009, RECOVERY-010, RECOVERY-011, RECOVERY-012

## Structured unresolved decision
STATUS: PROOF_REQUIRED

DECISION_OWNER: Architecture/owning phase

BLOCKING_GATE: GATE-020

OPTIONS:
- Preserve current provisional decision if proof passes.
- Supersede via a new TD using researched/experimental evidence.

EVIDENCE_REQUIRED: Linked gate evidence plus fresh BREAKER review.
