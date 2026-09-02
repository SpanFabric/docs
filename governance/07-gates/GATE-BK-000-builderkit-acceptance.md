# GATE-BK-000 — BuilderKit acceptance
**STATUS:** `PASS`  
**KIND:** `builderkit`

## OBJECTIVE
Prove the packaged BuilderKit is self-contained, internally consistent, semantically traceable, safe to bootstrap and free of hidden-conversation dependencies.

## RATIONALE
The BuilderKit is project control-plane infrastructure. Partial generation or stale metadata would recreate known Codex failure modes before implementation begins.

## PREREQUISITES
None.

## ENVIRONMENT
Clean local workspace with Python 3 and PyYAML; no GPU hardware required.

## HARDWARE
None.

## PROCEDURE
1. Run validate-builderkit.py
2. Run validate-traceability.py
3. Run validate-upstreams.py
4. Parse all YAML/JSON
5. Verify source-view synchronization
6. Scan placeholders/secrets/binaries/zero-byte/temp files
7. Verify ZIP integrity and SHA-256
8. Run fresh semantic consistency checks over North Star, invariants, phases and proof gates.
9. Run Phase-00 control-plane tests for bootstrap exit semantics, project state, Steward policy and materialization idempotency/conflict handling.
10. Verify pinned validator dependency specification and pre-bootstrap evidence tooling exist.

## EXPECTED RESULT
All fatal validation rules pass; only explicitly structured PROOF_REQUIRED decisions remain unresolved.

## METRICS
- validator exit codes
- entity counts
- unresolved reference count
- placeholder count
- secret scan count
- ZIP CRC errors

## ARTIFACTS
- validation-report.json
- builderkit-manifest.json
- SpanGPU-BuilderKit.zip
- SpanGPU-BuilderKit.zip.sha256

## PASS RULE
All fatal validators exit 0, ZIP integrity passes, manifest hashes match and no prohibited content/secret/proprietary binary is present.

## FAIL RULE
Any fatal semantic/reference/packaging/source-of-truth violation or unsafe script default produces FAIL and BuilderKit is not distributable.

## BLOCKED RULE
Missing Python/PyYAML/ZIP support is BLOCKED_ENVIRONMENT; do not report PASS.

## NEXT ACTION
Set PROJECT_STATE current_phase=PHASE-000 and current_gate=GATE-000.
