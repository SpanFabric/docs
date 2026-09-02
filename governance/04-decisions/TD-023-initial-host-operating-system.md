# TD-023 — Initial host operating system
**STATUS:** `PROVISIONAL`

## Context
SpanGPU needs an explicit project-wide decision for initial host operating system.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-002, RF-005, RF-007, RF-009, RF-016

## Decision
Use Linux as the first reference host because Neptune/Vulkan OSS paths are strongest there, but keep host OS outside protocol semantics.

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
Governance/architecture-wide.

## Structured unresolved decision
STATUS: PROVISIONAL

DECISION_OWNER: Architecture/owning phase

BLOCKING_GATE: GATE-003

OPTIONS:
- Preserve current provisional decision if proof passes.
- Supersede via a new TD using researched/experimental evidence.

EVIDENCE_REQUIRED: Linked gate evidence plus fresh BREAKER review.
