# Fresh BREAKER handoff — F-007-RLINK-001 canonical link resolution

## Exact subject

- Repository: `SpanFabric/docs`
- Material commit: `9da0b7567aba797d62eb248c8ef63d030a2e3227`
- Review-Subject SHA-256: `7d2c7ec656004680e43beb049b401ce34062265ab0ae068663081ffb8d7a8f79`
- Builder evidence: `verification/reports/F007_RLINK001_CANONICAL_LINK_RESOLUTION_BUILDER.json`
- Resolve the final PR #1 head from GitHub immediately before review; excluded state/report metadata may be a descendant of the material commit.

## Scope and invariants

The correction replaces active-governance raw full-path substring detection with one canonical Git/POSIX resolver. It must preserve active/historical registry separation, the durable `FIRST_CODEX_PROMPT.md` router, `PROJECT_STATE.yaml` next-action authority, PHASE-000 `IN_PROGRESS`, GATE-000 `NOT_PASSED`, PHASE-001 `NOT_AUTHORIZED`, `CONTROLLED_INITIAL_BASELINE_BOOTSTRAP` history, the superseded Stage-A/Stage-B route, and F-000-04 as `QUARANTINED`/`FORBIDDEN`.

No active operational/normative route may resolve to `HISTORICAL_REFERENCE` or `HISTORICAL_EVIDENCE`. Historical citation is allowed only through an exact structured `explicit_provenance_references` source/target pair, and is non-operative.

## Required attacks

Use the production resolver, not a test helper, against same-directory, `./`, normalized `../`, repository-root, fragment, query, angle-bracket, explicit/collapsed/shortcut reference-style, backslash, percent-encoded, absolute, root/unclassified, and historical-evidence variants. Confirm external HTTP(S) and active-to-active links remain allowed. Try to make an explicit provenance pair authorize execution rather than a citation. Confirm the direct materializer Apply regression remains rejected.

## Reproduction

```text
python -B -m unittest tests/verification/test_active_governance_semantics.py -v
python -B -m unittest tests/verification/test_project_state_semantics.py -v
python -B -m unittest discover -s tests/verification -p 'test_*.py'
python -B scripts/active_governance_semantics.py --repo-root . --audit
python -B scripts/verify_review_state.py --check --base <exact-origin-main-40-hex-sha>
git diff --check origin/main...HEAD
git status --short
```

Run the materialized trusted runner specified in `verification/MANUAL_AUTHORITY.md` with the exact current `origin/main` SHA. Recompute the digest for the named material commit; state/report changes must not alter it, material changes must.

## Boundary and authority

The Builder result is only `INDEPENDENT_REVIEW_PENDING`. The Fresh BREAKER must produce an independent durable report with checked SHA, scope, executed commands, attacks, confirmed constructions, findings, and verdict. Do not infer Fresh BREAKER, Owner, merge, or post-merge authority from Builder evidence or green CI.
