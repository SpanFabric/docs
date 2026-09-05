# Fresh BREAKER handoff — F-007-RLINK-004 CommonMark governance-link parsing

## Exact review subject

- Repository: `SpanFabric/docs`
- Material commit: `2ac3c0151f7cec124cead286e518d632e03d7841`
- Review-Subject SHA-256: `660eddcf4defb6435c7017ede2515305c3e8cd084fb5c936bf40bf22d0ff6b3d`
- Builder evidence: `verification/reports/F007_RLINK004_COMMONMARK_BUILDER.json`
- Resolve PR #1's final head from GitHub immediately before review. Excluded state and report metadata may be a descendant of the material commit; the material commit and digest above are the review subject.

## Scope and invariants

The remediation removes the custom Markdown label/reference parser from `scripts/active_governance_semantics.py`. All Markdown route extraction must instead use the repository-vendored `markdown-it-py 4.2.0` CommonMark parser and parser tokens. `mdurl 0.1.2` is a required vendored dependency.

The only permitted authority chain is:

```text
Markdown -> vendored CommonMark parser tokens -> parser-derived destinations
-> SpanGPU canonical Git/POSIX resolver -> registry classification
-> SpanGPU authorization
```

CommonMark may recognize syntax; it must not classify a governance route, decide that a historical route is allowed, or authorize execution. No runtime `pip`, network lookup, system-package fallback, import shadowing, or preloaded foreign `markdown_it`/`mdurl` module may silently change parser authority. Missing or invalid vendor files must fail closed.

Every rendered active link to `governance/09-codex/PHASE000_RESUME_AFTER_PREAPPLY_BREAKER.md` must be parser-derived, canonicalized, classified `HISTORICAL_REFERENCE`, and rejected before it can expose a materializer `--apply` action. Raw HTML navigation is forbidden and must be rejected for both local and external destinations. Inline/fenced code is not Markdown navigation.

## Required independent attacks

Use the production extractor and resolver, not a test-only substitute. Attempt to bypass historical-reference rejection using:

- escaped closing brackets; escaped opening and closing brackets; balanced and multi-level nested labels;
- inline titles; full, collapsed, and shortcut reference forms; escaped labels;
- case folding, whitespace normalization, punctuation, duplicate definitions, and undefined definitions;
- relative, same-directory, repository-root, fragment, query, angle-destination, percent-encoded, backslash, root/unclassified, and external variants;
- inline code and fenced code, which must not become navigation;
- raw `a`, `area`, `base`, `form`, `button`, `input`, `iframe`, and `frame` navigation attributes;
- a missing vendor root, tampered RECORD payload, foreign `PYTHONPATH`/system package precedence, and a preloaded non-vendor `markdown_it` or `mdurl` module.

Confirm rendered duplicate-reference behavior follows the parser's CommonMark semantics rather than legacy custom-parser semantics. Verify that a false non-rendered or code-only form does not get reported as navigation, while a raw HTML navigation form is rejected rather than ignored.

## Reproduction and evidence required

```text
python -B -m unittest tests/verification/test_active_governance_semantics.py tests/verification/test_project_state_semantics.py -v
python -B scripts/active_governance_semantics.py --repo-root . --audit
python -B scripts/verify_review_state.py --check --base <exact-origin-main-40-hex-sha>
git diff --check origin/main...HEAD
git status --short
```

Run the materialized trusted runner specified in `verification/MANUAL_AUTHORITY.md` with the exact current `origin/main` SHA. Recompute the review-subject digest for the named material commit. State/report changes must not alter it; any material change must.

For the full discovery suite, this Builder host has a known environmental limitation: eight existing trusted-runner tests select the Windows WSL launcher via `shutil.which('bash')` and fail `E_ACCESSDENIED`; direct Git Bash is available. The Fresh BREAKER should distinguish that host-selection defect from an F-007 parsing finding and record the exact host/command used.

## Boundary and authority

The Builder result is only `INDEPENDENT_REVIEW_PENDING`. The Fresh BREAKER must be independent and must store a durable report binding its checked SHA/digest, scope, commands, attacks, confirmed constructions, any findings, and verdict. Do not infer Fresh BREAKER, Owner, merge, or post-merge authority from this Builder evidence or any green CI.
