# Boundary Audit
Boundary ID / change attempt / phase / commit

- Producer / producer guarantees
- Consumer / consumer assumptions
- Source of truth
- Validation owner
- Authorization/trust owner
- Version owner
- Concurrency/order model
- Transaction/atomicity model
- Retry/idempotency/ambiguous completion
- Failure semantics
- Migration/version skew/future-phase compatibility
- Security/resource limits
- Tests including negative/fault/retry/version-skew
- Changed requirements/TDs

Mandatory triggers are defined in `12-machine-readable/boundary-audit-schema.yaml`.
