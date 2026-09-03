# SpanGPU — Durable Codex Router

This is a router, not a one-time execution prompt. It must not choose or cache the
next action itself.

## Required route

1. Read `AGENTS.md`.
2. Read canonical `governance/PROJECT_STATE.yaml`.
3. Read `governance/12-machine-readable/governance-entrypoints.yaml`.
4. Follow only the `next_required_action` currently authorized by `PROJECT_STATE.yaml`.
5. Read further material only when the active-entrypoint registry or that authorized
   action identifies it as current.
6. Treat every path classified `historical_superseded` or `historical_evidence` as
   provenance only. A link or an existing file never grants execution authority.
7. Obey the Codex Verification Contract, the authority state, and the current
   repository policy before changing any material path.

`materialize-repositories.py --apply` is currently quarantined and is **NOT an active
route**. Do not execute any historical Bootstrap or materializer path merely because it
exists in this repository.

The current project state, including its authorization and phase/gate separation, is
the operational truth.
