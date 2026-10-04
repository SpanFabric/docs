# Fresh BREAKER handoff — F-007 active-governance remediation

## Role and independence

Act as a fresh independent BREAKER. Do not rely on Builder reasoning or create
an acceptance verdict by inference. Inspect the exact repository states and
return a durable report with the checked SHA, scope, commands, attacks,
findings, confirmed constructions, and a verdict.

## Required review subjects

All six open PRs use branch `codex/bootstrap-verification-bridge`. The PR tip
may contain excluded `verification/state.yaml` and `verification/reports/**`
metadata. Review the listed material subject/digest and independently resolve
the current PR tip from GitHub immediately before review.

| Repository | Exact open-PR head | Material review-subject commit | Review-subject SHA-256 |
| --- | --- | --- | --- |
| `platform` | `e625c13d89752254b4422e67be49ef2edadfde8d` | `956fefe9d883ba38814db126bc90bf1eddcb4d1b` | `d2eea8950925dbe76a2b9427895d8a13a1a66f00fdd55d038e1b94a8ae6b2860` |
| `windows` | `93d9caaf236eb515bd67015040100c7ba4ae0efd` | `9d1c94ad9ca46232fdb7aa9e79e81cbebd14b27f` | `5cb75656059ff0337572e4db9dfdb2e65335a9c3386f9d6d6133be918819c9a1` |
| `host` | `74c187738ca523e051871c41dad68765df82cba0` | `57f2260c47bc49f9eba4a7abc63afbe5b507a206` | `efad6bcbafb92a2b8fc71badbbaa652f6e40d0ed9e4734e0f918390fa4406889` |
| `evals` | `a33176c1420ff6273c7ddf683eee7b3c650072cc` | `cc096783e5d921aad4fb00a59379365d378b47dc` | `359fb9f22ba468e053abc2bb4adae196a2cbbffef8c64d6d42c2426253801b47` |
| `docs` | resolve final excluded-metadata tip before review | `4e00e9d1af3c072d511cf9c9c9d78290e1083080` | `5cd27488ef984beb3374175770c6e965193b84dab35b08f819f6c1bf1bceaab0` |
| `.github` | `89031b9f7a6efe479886b5e627a9cc35c6934fb4` | `e98a1ab51cc5e86469e0a1b35c6253dd9831982e` | `5dbd5019fda84a58ae9adceba71b4827bfe5c668f6c9eddda61fd65e5268729b` |

The Docs material subject above is the F-007 active-governance remediation.
The subsequent Docs evidence envelope is intentionally excluded from its own
digest; it must be an ordinary descendant of this material commit and must
contain active Builder evidence bound to the listed digest.

## Docs scope and invariants to verify

1. `governance/PROJECT_STATE.yaml` is canonical and its
   `12-machine-readable/project.yaml` projection has the same post-bootstrap
   semantic claims.
2. Repository/bootstrap infrastructure existence (`repositories_bootstrapped`)
   is distinct from `verification.status`, `phase_completion`,
   `gate_completion`, and `authorization`.
3. All six repositories may exist and the bridge may be established while
   `PHASE-000` remains `NOT_COMPLETED`, `GATE-000` remains `NOT_PASSED`, and
   `PHASE-001` remains `NOT_AUTHORIZED`.
4. The entrypoint registry and durable router establish one operational route through
   `PROJECT_STATE.yaml`. Historical BuilderKit prompts/reports are classified provenance
   only and cannot direct legacy execution or a global GitHub-mutation ban.
5. `F-000-04` still quarantines and forbids
   `materialize-repositories.py --apply`. The state must not imply that the
   materializer was accepted or used.
6. The Manual Verification Bridge remains R2, `MANUAL_AUTHORITY`, and
   `INDEPENDENT_REVIEW_PENDING`; Builder evidence and CI cannot substitute for
   fresh BREAKER, Owner, merge, or post-merge authority.

## Reproduction commands

```text
python -m unittest discover -s tests/verification -p 'test_*.py' -v
python scripts/verify_review_state.py --check --base <canonical-origin-main-40-hex-sha>
git diff --check origin/main...HEAD
git status --short
```

For the authoritative check, use the materialize-then-run command in
`verification/MANUAL_AUTHORITY.md` with the exact `origin/main` SHA. Confirm
that the review-subject digest remains
`5cd27488ef984beb3374175770c6e965193b84dab35b08f819f6c1bf1bceaab0` for
state/report-only changes and changes for a material modification.

## Required outcome

Do not merge. A passing BREAKER may move only to
`READY_FOR_OWNER_ACCEPTANCE` under the policy and must preserve
`MANUAL_AUTHORITY` limitations. Verify GitHub protection/required-check and
required-review settings as external authority conditions before any later
Owner/merge recommendation. If a finding is confirmed, document its failure
sequence, violated invariant, impact, severity, remediation, and fresh
regression evidence.
