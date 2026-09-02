# F-000-04 — BuilderKit materializer Apply path is quarantined

**Status:** CONFIRMED historical finding; remediation not implemented in this
bootstrap.

## Failure mechanism

The BuilderKit `materialize-repositories.py --apply` path is not sufficiently
bound to the fixed workspace and canonical manifest identity boundary for this
project bootstrap. Invoking it could therefore apply a plan outside the
intended fixed-target contract rather than proving that every write is bound to
the exact `D:\Projekte\SpanGPU` workspace, canonical manifest, and six-repo
topology.

## Violated requirement and impact

The fixed target boundary permits writes only to `SpanFabric/{platform,
windows,host,evals,docs,.github}` and their matching local paths. An
insufficiently bound Apply path could misdirect or partially materialize
governance/CI files. This is an R3 data-integrity and workspace-boundary risk,
not an authorization to rerun bootstrap packaging.

## Mandatory disposition

`materialize-repositories.py --apply` is prohibited for SpanGPU until
repository-controlled code has all of the following and passes fresh review:

1. fixed-target workspace validation;
2. canonical manifest identity validation;
3. a six-repository allowlist;
4. traversal rejection; and
5. regression tests for each condition.

This finding does not block the safe manual creation of the six repositories
or the manual import recorded in `governance/IMPORT_PROVENANCE.md`. No new
BuilderKit archive is created or patched as part of this disposition.
