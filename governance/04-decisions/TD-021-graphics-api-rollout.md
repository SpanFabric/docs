# TD-021 — Graphics API rollout
**STATUS:** `ACCEPTED`

## Context
SpanGPU needs an explicit project-wide decision for graphics api rollout.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-001, RF-010, RF-012, RF-019, RF-027

## Decision
Prove D3D11 first, then Vulkan/OpenGL/legacy, with D3D12 isolated as a separate proof-heavy track on the same core architecture.

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
DX-001, DX-002, DX-003, DX-004, DX-005, DX-006, DX-007, DX-008, DX-009, DX-010, COMPAT-001, COMPAT-002, COMPAT-003, COMPAT-004, COMPAT-005, COMPAT-006, COMPAT-007, COMPAT-008, COMPAT-009, COMPAT-010, COMPAT-011, COMPAT-012, COMPAT-013
