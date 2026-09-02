# TD-002 — WDDM client strategy
**STATUS:** `PROOF_REQUIRED`

## Context
SpanGPU needs an explicit project-wide decision for wddm client strategy.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-001, RF-003, RF-013, RF-016, RF-017

## Decision
Start from Triton/virtio-win WDDM code as a controlled fork and prove it can operate as a stable secondary render adapter outside its original VM-local assumptions.

## Consequences
- Implementation and review must preserve architecture invariants.
- Failure of the linked proof may supersede this decision through a new TD; never silently work around it.

## Risks
RISK-001

## Rejected alternatives
- Unavailable proprietary critical path
- Per-game/launcher-specific core integration
- Unproven assumption treated as accepted where status is PROOF_REQUIRED/PROVISIONAL

## Reversibility
Reversible by superseding TD with migration plan before dependent proof-gated phases proceed.

## Migration path
Stop dependent phase, preserve evidence, write superseding TD, update canonical sources/traceability, rerun affected gates.

## Proof requirement
`GATE-001`

## Affected requirements
WIN-001, WIN-002, WIN-003, WIN-004, WIN-005, WIN-006, WIN-007, WIN-008, WIN-009, WIN-010, WDDM-001, WDDM-002, WDDM-003, WDDM-004, WDDM-005, WDDM-006, WDDM-007, WDDM-008, WDDM-009, WDDM-010, WDDM-011, WDDM-012

## Structured unresolved decision
STATUS: PROOF_REQUIRED

DECISION_OWNER: Architecture/owning phase

BLOCKING_GATE: GATE-001

OPTIONS:
- Preserve current provisional decision if proof passes.
- Supersede via a new TD using researched/experimental evidence.

EVIDENCE_REQUIRED: Linked gate evidence plus fresh BREAKER review.
