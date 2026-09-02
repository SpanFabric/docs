# TD-024 — Stock-client-driver PCIe research branch
**STATUS:** `PROVISIONAL`

## Context
SpanGPU needs an explicit project-wide decision for stock-client-driver pcie research branch.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-016

## Decision
Keep PCIe-over-network/libvfio-user as an isolated future research track; it must not block or contaminate the semantic WAN architecture.

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
`GATE-030`

## Affected requirements
Governance/architecture-wide.

## Structured unresolved decision
STATUS: PROVISIONAL

DECISION_OWNER: Architecture/owning phase

BLOCKING_GATE: GATE-030

OPTIONS:
- Preserve current provisional decision if proof passes.
- Supersede via a new TD using researched/experimental evidence.

EVIDENCE_REQUIRED: Linked gate evidence plus fresh BREAKER review.
