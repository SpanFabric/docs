# Fresh BREAKER Handoff — SOLO_OWNER governance

## Review subject

Review these six exact immutable material subjects. The later Builder-evidence commits
change only `verification/state.yaml` and `verification/reports/**`, which are explicit
review-subject exclusions; their material digests therefore remain the values below.

| Repository | Material commit | Review-subject SHA-256 | Final Builder-evidence head |
| --- | --- | --- | --- |
| platform | `04c960d55e84927d6d54d14b58079903dff14a48` | `a389d70b4d4370261505f41e886be2fbcaafa85c1a72ea83e088607ef1aa01e5` | `14715541c8927a685391794b6957c6b3fab9703a` |
| windows | `574b270b2e008935bfa217387aa1f8f43e9931e9` | `4aaeb5a1e212aebe641dcd739c8efd7575dd76a8c878e0d5fce32ac628352986` | `bf101e0d45df26efb82cbd08726bc022e8df2d8c` |
| host | `2717d083688e80d8a94e0b0be79fba9deb28361d` | `954356953fd2800321a18dd3d0a3c017b8ad1d0b89d22962aaf762381a834edc` | `be34b359006525bb569346e18ab1033ceee83514` |
| evals | `457fd42664c56dbc6ad4f7f8ab0f333d18c1d2f4` | `f40e4be92a1bbadcb06425902f4e9c1d54f2ab7eb8d50e43c2e998d3b7cc13f5` | `cf977cd24ddbabef89085150c1460c110538baf6` |
| docs | `5eebafd863abea78a2fc8a0f2e96485f1da2eaa2` | `c40d0678cfe26dd01d8fcf3808e09da97dba80da7b19df349388a952b7735cd2` | `c69d74286e77d96b6ed6bdcde38fde69a3148b32` |
| .github | `ca14508cb97a4d67b128614c1a3d7fce95f48e78` | `239effb4223039bf4db76ddafd22ed42ee266fc69f8d25c4549ae411a229de7b` | `cedf0d240daff98ef6e243782326b9119825e940` |

## Authority model to verify

- `SOLO_OWNER` means GitHub required human approvals are zero; it does **not** mean
  no technical review.
- Fresh BREAKER is required independent technical authority for the exact subject.
- Owner Acceptance remains a separate human authority. The sole Owner may be PR author.
- Builder and CI cannot create Fresh BREAKER or Owner evidence; GitHub approval is never
  Fresh BREAKER evidence.
- The shared bridge now permits `READY_FOR_OWNER_ACCEPTANCE → BUILDING` only for
  `BUILDER` when material changes occur before Owner Acceptance. The old Docs
  Fresh-BREAKER verdict remains immutable historical evidence for
  `a3e85b7febeeb7c3e7c11fe44964efb3b1e6b60b` /
  `64d0efa04f7747b55af394d665ef449075303d0e49c47188ab8d6c6fe6e79615`; it is inactive
  for the subjects above.

## Required adversarial attacks

1. Attempt to weaken SOLO_OWNER so Fresh BREAKER, Owner Acceptance, required checks,
   PR protection, force-push prohibition, deletion prohibition, or admin-bypass
   prohibition becomes optional; each must fail closed.
2. Attempt to count PR-author Owner Acceptance, a GitHub approval, Builder evidence, or
   CI as Fresh BREAKER evidence; each must fail.
3. Attempt to carry an accepted exact-subject BREAKER record across a material head/base
   change while `require_up_to_date: false`; it must fail. A new material commit requires
   Builder validation, exact-head CI, new Fresh BREAKER, and new Owner Acceptance.
4. Attempt the material-change reopen from `READY_FOR_OWNER_ACCEPTANCE` with an authority
   other than Builder, and attempt Builder transition directly to `ACCEPTED`; both must
   fail. Historical evidence must remain readable but inactive.
5. Recheck F-001 through F-007, F-007-RLINK-001 through F-007-RLINK-004, and the
   F-000-04 `QUARANTINED` / `FORBIDDEN` boundary. No historical evidence is rewritten.
6. Independently confirm that the two metadata paths are the only material-to-final-head
   delta, then recompute each review-subject digest with the trusted runner.

## Required future hosting controls — not applied by this Builder task

For each default `main` branch: require PR; require `verification-gate` and
`bootstrap-integrity`; set required approvals to `0`; do not require latest-push human
approval; do not require up-to-date/strict status checks; prohibit force push and branch
deletion; enforce administrators; and allow no broad bypass. In `.github`, the integrity
workflow display name is **Steward baseline integrity**, while the required context is
`bootstrap-integrity`.

Before a Hosting Controls Operator claims these controls established, it must inspect
organization-level rulesets with sufficient read authority and enumerate inherited
bypasses. This Builder task did not configure, accept, merge, or post-merge verify any
hosting state.

## Exact-head CI observed

For each final Builder-evidence head above, `verification-gate` and
`bootstrap-integrity` completed successfully. These CI results are supporting evidence
only and do not replace the required Fresh BREAKER or Owner Acceptance boundaries.

## Builder limit

Current lifecycle is `INDEPENDENT_REVIEW_PENDING` in all six repositories. This handoff
requests an independent Fresh BREAKER verdict; it does not issue one.
