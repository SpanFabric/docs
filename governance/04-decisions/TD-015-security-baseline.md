# TD-015 — Security baseline
**STATUS:** `PROVISIONAL`

## Context
SpanGPU needs an explicit project-wide decision for security baseline.

## Researched alternatives
- Research 1–3 alternatives relevant to this boundary
- Greenfield implementation where reuse assumptions fail
- Defer behind proof gate rather than assume capability

## Evidence
RF-015, RF-017

## Decision
Mutual authenticated encryption, least-privilege service boundaries, replay resistance and session isolation are mandatory before hostile-network claims.

## Consequences
- Implementation and review must preserve architecture invariants.
- Failure of the linked proof may supersede this decision through a new TD; never silently work around it.

## Risks
RISK-013

## Rejected alternatives
- Unavailable proprietary critical path
- Per-game/launcher-specific core integration
- Unproven assumption treated as accepted where status is PROOF_REQUIRED/PROVISIONAL

## Reversibility
Reversible by superseding TD with migration plan before dependent proof-gated phases proceed.

## Migration path
Stop dependent phase, preserve evidence, write superseding TD, update canonical sources/traceability, rerun affected gates.

## Proof requirement
`GATE-027`

## Affected requirements
SEC-001, SEC-002, SEC-003, SEC-004, SEC-005, SEC-006, SEC-007, SEC-008, SEC-009, SEC-010, SEC-011, SEC-012, SEC-013, SEC-014, TRUST-001, TRUST-002, TRUST-003, TRUST-004, TRUST-005, TRUST-006, TRUST-007, TRUST-008, TRUST-009, TRUST-010

## Structured unresolved decision
STATUS: PROVISIONAL

DECISION_OWNER: Architecture/owning phase

BLOCKING_GATE: GATE-027

OPTIONS:
- Preserve current provisional decision if proof passes.
- Supersede via a new TD using researched/experimental evidence.

EVIDENCE_REQUIRED: Linked gate evidence plus fresh BREAKER review.
