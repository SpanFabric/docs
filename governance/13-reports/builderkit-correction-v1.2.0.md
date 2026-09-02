# BuilderKit correction — v1.2.0

This release corrects two confirmed Phase-00 control-plane blockers found by the first Codex bootstrap attempt:

1. `bootstrap-repos.ps1` could print the correct all-missing dry-run plan but return exit code 1 because the final expected failed `gh repo view` remained in `$LASTEXITCODE`. The script now captures absence as data and explicitly exits 0 on a successful dry run; a regression contract test enforces this.
2. Phase 00 required governance/AGENTS/CI/Steward/evidence materialization and project-state/Steward tests without supplying a canonical implementation. This release adds a machine-readable materialization map, idempotent fail-closed materializer, repository skeletons, executable semantic tests, pre-bootstrap evidence sealing and recovery semantics.

Additional corrections pin the validator dependency (`PyYAML==6.0.3`) and make Phase 00 sequencing unambiguous: Stage A dry-run/evidence → fresh pre-apply BREAKER → Stage B mutation/materialization → final fresh BREAKER.
