# TD-004 — Graphics command streaming model
**STATUS:** `PROVISIONAL`

## Context
SpanGPU needs an explicit project-wide decision for graphics command streaming model.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-001, RF-006, RF-008, RF-010, RF-012

## Decision
Use API-specific command namespaces above common object/resource/fence envelopes, borrowing from Neptune, Venus and gfxstream.

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
`GATE-005`

## Affected requirements
GFX-001, GFX-002, GFX-003, GFX-004, GFX-005, GFX-006, GFX-007, GFX-008, GFX-009, GFX-010, VK-001, VK-002, VK-003, VK-004, VK-005, VK-006, VK-007, VK-008, VK-009, VK-010, GL-001, GL-002, GL-003, GL-004, GL-005, GL-006, GL-007, GL-008

## Structured unresolved decision
STATUS: PROVISIONAL

DECISION_OWNER: Architecture/owning phase

BLOCKING_GATE: GATE-005

OPTIONS:
- Preserve current provisional decision if proof passes.
- Supersede via a new TD using researched/experimental evidence.

EVIDENCE_REQUIRED: Linked gate evidence plus fresh BREAKER review.
