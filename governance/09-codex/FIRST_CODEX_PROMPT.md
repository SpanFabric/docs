# SpanGPU — PHASE-000 STAGE A RETRY ON BUILDERKIT v1.2.3

Start a NEW PHASE-000 Stage-A attempt. Historical v1.2.0, v1.2.1 and v1.2.2 attempts/findings remain immutable historical evidence and are never rewritten or promoted.

## Fixed inputs
- Organization: `SpanFabric`
- Product: `SpanGPU`
- Local root: `D:\Projekte\SpanGPU`
- BuilderKit: `%USERPROFILE%\Downloads\SpanGPU-BuilderKit-v1.2.3.zip` (or the exact attached v1.2.3 archive; record actual path/hash)
- Expected version: `2026.09.02-v1.2.3-spanfabric`
- Fixed mutation policy: `11-bootstrap/fixed-targets.json`
- Planned repos: `platform`, `windows`, `host`, `evals`, `docs`, `.github`

Execute Stage A only. No GitHub repository creation, clone/apply, real materialization, controlled forks, push/merge, or GPU implementation.

## Mandatory sequence
1. Hash archive; extract into a NEW version/hash-specific path; verify `BUILDERKIT_VERSION` and embedded manifest.
2. Read `README_START_HERE.md`, all mandatory reading, and `13-reports/v1.2.3-correction.md`.
3. PLAN + GLOBAL IMPACT PASS + pre-build “What are we missing?”.
4. Prepare/reuse only the declared isolated validator venv; no global package mutation.
5. Run BuilderKit, traceability, upstream validators and **all Phase-000 semantic tests**, including `test_manual_verification_bridge.py`. On Windows, the PowerShell 5.1 empty-org regression, fixed-target rejection regression, and byte-safe capture path MUST execute, not skip.
6. Independently prove F-000-03 remediation: a real/fake empty `gh repo list ... --json name` result `[]` must normalize to zero records under Windows PowerShell 5.1 and `bootstrap-repos.ps1 -DryRun` must exit 0 with exactly six planned repo actions. Also prove a partial-existing JSON array remains idempotent.
7. Read-only rediscover `gh` identity, direct active admin membership in `SpanFabric`, GitHub repo pre-state and local pre-state.
8. Create a NEW prebootstrap evidence attempt.
9. Run `bootstrap-org.ps1 -DryRun`, `bootstrap-repos.ps1 -DryRun`, and `bootstrap-workspace.ps1 -DryRun` only with canonical targets. All must exit 0.
10. Run materializer dry-run against a NEW isolated six-repository fixture.
11. Run the supplied materialization conflict and recovery semantics tests.
12. Verify the Manual Verification Bridge materialization contract for all six repo skeletons. This is pre-push/pre-merge governance; do not push anything in Stage A.
13. Capture exact commands/results/environment/BuilderKit identity; seal and verify the new evidence bundle. Never redirect seal output into the directory being sealed.
14. BUILDER ASSUMPTION CHALLENGE + post-build “What are we missing?”.
15. STOP at `INDEPENDENT_REVIEW_PENDING`; produce a fresh PRE-APPLY BREAKER handoff.

## Forbidden
- patching the extracted BuilderKit;
- reusing historical attempt IDs or evidence as current proof;
- `gh repo create`, cloning/apply bootstrap, real governance materialization;
- push, PR, merge or acceptance;
- changing the fixed target allowlist;
- retry-until-green;
- PHASE-000 DONE/GATE-000 claims.

A mutation-capable Stage B is authorized only by a NEW fresh breaker accepting the exact sealed v1.2.3 Stage-A attempt. Before the first repository push in Stage B, the repository-local Manual Verification Bridge v1 must be materialized, tested, and represented truthfully in repository state.
