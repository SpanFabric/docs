# Fresh BREAKER Handoff — WINDOWS_TRUSTED_RUNNER_HOST_SELECTION

Producer: BUILDER  
Authority: MANUAL_AUTHORITY  
Lifecycle: INDEPENDENT_REVIEW_PENDING only

## Persisted failed finding

`WINDOWS_TRUSTED_RUNNER_HOST_SELECTION` was persisted as P1/HIGH Fresh BREAKER evidence for the failed subjects. Its evidence remains retained as historical in all six repositories. The direct defect was in `platform`, `windows`, `host`, `evals`, and `.github`: PATH-selected `C:\WINDOWS\system32\bash.exe` could win over installed Git Bash. `docs` was the known-good Git-Bash-first helper reference.

## Remediation and Windows CI contract

- The five affected helpers now select `C:\Program Files\Git\bin\bash.exe`, then `C:\Program Files\Git\usr\bin\bash.exe`, then PATH.
- Regressions cover Git bin priority, usr/bin fallback, non-WSL PATH fallback, deterministic missing-host failure, non-Windows behavior, and the historical WSL-launcher case.
- All six Verification gate workflows add `windows-trusted-runner` on `windows-latest`; `verification-gate` has `needs: windows-trusted-runner` and retains its stable required-context name.
- The Windows job selects Git Bash explicitly, converts `GITHUB_WORKSPACE` and `RUNNER_TEMP` using `cygpath -u`, materializes `HEAD:scripts/trusted_verify_review_state.sh` from Git objects, executes that immutable runner, then runs the native verification suite. It contains no WSL path.

## Exact material subjects and validated PR heads

| Repository | Material commit | Review-subject digest | Exact CI validation head | Verification gate run / Windows job |
|---|---|---|---|---|
| SpanFabric/platform | `6761c585e9700a407de9b2d87dbfab1f9fc48053` | `c52830149dc99491517ccddf1559550d87ada7e8e8c82550982231d9bddbd729` | `2e12120a89e3e10d1050dc48390c2a4d7a007b4d` | `37157281055 / 111303166485` |
| SpanFabric/windows | `ec3989285af71b1e4025b35a937c54c72cf045ee` | `f30f3334c9591802b6431e539fa532bdb63ada00499235a5b043004a8349b68d` | `27092fa89cf9dca4dd48633817205ad257b9e853` | `37157283583 / 111303174067` |
| SpanFabric/host | `8e2d4f59da25f83124ee964c45cf56ab7bb69254` | `c723d9c74c08c08324478b2f3848f6deaeed82f3388292d76c2a9e3d8f52bec5` | `b3c2d092677904adaf700ea4ef45298470eb37af` | `37157285208 / 111303179276` |
| SpanFabric/evals | `4f6c61bbee92b2385c1ee7b217cac7fb09e4d283` | `021132a430c3a12cf07b15cbe6ee817e985b47bdce5150528502b03bb4b0a5d3` | `7266e041b1ed3ec596752a15642a181ddc3b6cf5` | `37157287246 / 111303185371` |
| SpanFabric/docs | `e743945d26abfee8a5cc33bfe60acd292ba4bcc7` | `fbf04ed7d4201097c9a7cffaba882168f3107bd72a817828e74a6163e16cad44` | `4e333bee09825ad80b610e47521103d980ed983e` | `37157289548 / 111303191996` |
| SpanFabric/.github | `95e888267f4540be6f88274bfeb994debb97fbe7` | `f071b2b406c11b83280f276ab7a8552c52007b0dc7952ee588e27687a1156522d` | `9127cbe4bfda45b71bb9a4029982d28097393608` | `37157291243 / 111303197629` |

All listed exact-head Verification gate and integrity workflows succeeded. Every hosted Windows job selected `C:\Program Files\Git\bin\bash.exe`, logged valid Git-Bash POSIX paths, reported `WINDOWS_TRUSTED_RUNNER_EXIT=0`, and reported `WINDOWS_VERIFICATION_TESTS=PASS`.

## Required independent attacks

Fresh BREAKER must independently test Git Bash non-executability, WSL/PATH precedence, host PATH variance, conversion of temporary runner paths, immutable-object execution, Windows job dependency into `verification-gate`, stable required-context preservation, one-repository drift, Docs known-good behavior, stale evidence invalidation, and the separation of Builder, Fresh BREAKER, and Owner authority.

## Non-regression targets

Verify F-001 through F-006, immutable trusted execution, closed authority matrix, merge/post-merge SHA binding, SOLO_OWNER Fresh BREAKER requirement, Docs F-007 and RLINK-001 through RLINK-004, and F-000-04 remains QUARANTINED/FORBIDDEN.

This handoff does not assert Fresh BREAKER, Owner Acceptance, merge, post-merge verification, GATE-000, PHASE-000 completion, or PHASE-001 authorization.
