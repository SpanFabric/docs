# TD-022 — D3D12 implementation path
**STATUS:** `PROOF_REQUIRED`

## Context
SpanGPU needs an explicit project-wide decision for d3d12 implementation path.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-019, RF-020

## Decision
Do not assume Triton D3D11 architecture automatically extends to D3D12; run a proof-only phase before committing to full implementation.

## Consequences
- Implementation and review must preserve architecture invariants.
- Failure of the linked proof may supersede this decision through a new TD; never silently work around it.

## Risks
RISK-006

## Rejected alternatives
- Unavailable proprietary critical path
- Per-game/launcher-specific core integration
- Unproven assumption treated as accepted where status is PROOF_REQUIRED/PROVISIONAL

## Reversibility
Reversible by superseding TD with migration plan before dependent proof-gated phases proceed.

## Migration path
Stop dependent phase, preserve evidence, write superseding TD, update canonical sources/traceability, rerun affected gates.

## Proof requirement
`GATE-024`

## Affected requirements
Governance/architecture-wide.

## Structured unresolved decision
STATUS: PROOF_REQUIRED

DECISION_OWNER: Architecture/owning phase

BLOCKING_GATE: GATE-024

OPTIONS:
- Preserve current provisional decision if proof passes.
- Supersede via a new TD using researched/experimental evidence.

EVIDENCE_REQUIRED: Linked gate evidence plus fresh BREAKER review.
