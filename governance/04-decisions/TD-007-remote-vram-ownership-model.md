# TD-007 — Remote VRAM ownership model
**STATUS:** `PROOF_REQUIRED`

## Context
SpanGPU needs an explicit project-wide decision for remote vram ownership model.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-002, RF-009, RF-010, RF-016, RF-017

## Decision
Make remote host resource state authoritative; local mappings become explicit staging/shadow state rather than WAN-coherent memory.

## Consequences
- Implementation and review must preserve architecture invariants.
- Failure of the linked proof may supersede this decision through a new TD; never silently work around it.

## Risks
RISK-003

## Rejected alternatives
- Unavailable proprietary critical path
- Per-game/launcher-specific core integration
- Unproven assumption treated as accepted where status is PROOF_REQUIRED/PROVISIONAL

## Reversibility
Reversible by superseding TD with migration plan before dependent proof-gated phases proceed.

## Migration path
Stop dependent phase, preserve evidence, write superseding TD, update canonical sources/traceability, rerun affected gates.

## Proof requirement
`GATE-007`

## Affected requirements
VRAM-001, VRAM-002, VRAM-003, VRAM-004, VRAM-005, VRAM-006, VRAM-007, VRAM-008, VRAM-009, VRAM-010, VRAM-011, VRAM-012, MEM-001, MEM-002, MEM-003, MEM-004, MEM-005, MEM-006, MEM-007, MEM-008, MEM-009, MEM-010

## Structured unresolved decision
STATUS: PROOF_REQUIRED

DECISION_OWNER: Architecture/owning phase

BLOCKING_GATE: GATE-007

OPTIONS:
- Preserve current provisional decision if proof passes.
- Supersede via a new TD using researched/experimental evidence.

EVIDENCE_REQUIRED: Linked gate evidence plus fresh BREAKER review.
