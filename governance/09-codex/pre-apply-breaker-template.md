# HISTORICAL / SUPERSEDED

**NOT AN ACTIVE ENTRYPOINT — DO NOT EXECUTE.**

This retained template documents the superseded BuilderKit route. Current
authorization is owned by `PROJECT_STATE.yaml`; use `FIRST_CODEX_PROMPT.md` and
`12-machine-readable/governance-entrypoints.yaml` to find the active route.

---

# PHASE-000 PRE-APPLY FRESH BREAKER

Start in a fresh Codex session. Do not receive builder reasoning history.

## Inputs allowed
- exact BuilderKit ZIP/hash/version;
- PHASE-000, project state, invariants, repository/materialization contracts;
- sealed pre-bootstrap attempt bundle and manifest hash;
- read-only GitHub pre-state and exact dry-run stdout/stderr/exit codes;
- environment/tooling fingerprint;
- known blockers stated as facts.

## Deliberately excluded
Builder chain-of-thought, confidence, desired conclusion, unpublished workaround ideas.

## Task
Independently verify that dry-run outputs are scoped to `SpanFabric` and `D:\Projekte\SpanGPU`, all expected bootstrap commands exit cleanly, no unexpected mutation is required, materialization rules are deterministic/idempotent, and evidence is sealed. Return `ACCEPTED` only if repository creation/apply is safe. Otherwise produce concrete findings.
