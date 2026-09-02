# Central Project Steward
One organization-level Steward consumes canonical governance from `docs` and project evidence/status across repositories. It is not copied as an independent full policy engine into every repo.

## Evaluates
Requirement/invariant/TD drift; cross-repo contracts; phase/gate state; missing/skipped tests; evidence freshness; unresolved findings/waivers; dependency/fork drift; security/license changes; compatibility/performance regressions; claims of success without admissible evidence.

## Triggers
PR; important push touching protected boundaries; phase completion; gate result; upstream change; release candidate; scheduled review.

## Outputs
`ACCEPTABLE`, `INDEPENDENT_REVIEW_PENDING`, `FINDINGS`, `BLOCKED_*`, `PROOF_NOT_ESTABLISHED`, `ARCHITECTURE_VIOLATION`. Reports link exact IDs/evidence and never mutate historical attempts.

## Machine-readable baseline
`12-machine-readable/steward-policy.yaml` is the bootstrap policy source used by the Phase-00 Steward policy test. The runtime in `.github` consumes canonical governance from `docs`; it does not own normative requirements/TDs.
