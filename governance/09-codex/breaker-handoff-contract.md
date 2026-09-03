# Builder → Fresh BREAKER Handoff Contract
## Include
Target commit/full diff; active requirements/invariants; active phase/gate; linked TDs; relevant architecture/contracts; test commands/results/raw evidence hashes; environment/hardware fingerprint; known blockers/failures; changed files.

## Deliberately exclude
Builder chain-of-thought/reasoning narrative, confidence statements, intended review conclusion, previous BREAKER reasoning unless it is a persisted finding record required to verify remediation.

The BREAKER receives a new attempt ID and independently derives its attack plan.

## Superseded Bootstrap provenance
The historical BuilderKit pre-bootstrap review route is not a current exception to this
contract. It is classified in `12-machine-readable/governance-entrypoints.yaml` as
historical provenance and cannot grant mutation or phase authority. Current BREAKER
work starts only from the `next_required_action` in `PROJECT_STATE.yaml`.
