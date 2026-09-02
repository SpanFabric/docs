# Traceability
Canonical traceability is `12-machine-readable/traceability-graph.json`. The required chain is:
`RESEARCH/LESSON → REQUIREMENT → TD → COMPONENT/REPOSITORY → PHASE → TEST → GATE → EVIDENCE`.
Validators reject orphaned requirements, proof-required TDs without gates, phases without requirements/completion criteria, gates without owning tests/phases, controlled forks without update policies and critical risks without mitigation/proof.
