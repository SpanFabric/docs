# Builder → Fresh BREAKER Handoff Contract
## Include
Target commit/full diff; active requirements/invariants; active phase/gate; linked TDs; relevant architecture/contracts; test commands/results/raw evidence hashes; environment/hardware fingerprint; known blockers/failures; changed files.

## Deliberately exclude
Builder chain-of-thought/reasoning narrative, confidence statements, intended review conclusion, previous BREAKER reasoning unless it is a persisted finding record required to verify remediation.

The BREAKER receives a new attempt ID and independently derives its attack plan.

## Pre-apply Phase 00 exception
Before the initial repository mutation, a fresh breaker reviews the sealed Stage-A dry-run attempt. It receives no builder reasoning history and may authorize apply only by an explicit ACCEPTED verdict tied to the attempt manifest hash. This pre-apply acceptance does not replace the final Phase-00 breaker.
