# Fresh BREAKER handoff — F-007-RLINK-004 PyPI reproducibility follow-up

## Scope and authority

This is Builder-produced routing metadata only. It is neither a Fresh BREAKER
report nor a verdict, and it grants no Owner, merge, CI, post-merge, GATE-000,
or PHASE-001 authority.

Review subject:

- Material commit: `a3e85b7febeeb7c3e7c11fe44964efb3b1e6b60b`
- Review-subject digest: `64d0efa04f7747b55af394d665ef449075303d0e49c47188ab8d6c6fe6e79615`
- Required maximum lifecycle before independent review: `INDEPENDENT_REVIEW_PENDING`
- Base for history-derived verification: `origin/main` =
  `b622dd3d21cc1cebdf07d7de344ece1a32fb34bd`

The evidence envelope is intentionally excluded from the digest and must remain
an ordinary descendant of the material commit. Any material change invalidates
this handoff's subject binding.

## Builder inputs to independently distrust and reproduce

- The owner identified official PyPI wheels as the current authoritative source:
  `markdown_it_py-4.2.0-py3-none-any.whl` SHA-256
  `9f7ebbcd14fe59494226453aed97c1070d83f8d24b6fc3a3bcf9a38092641c4a`, and
  `mdurl-0.1.2-py3-none-any.whl` SHA-256
  `84008a41e51615a49fc9966191ff91509e3c40b939176e643fd50a5c2196b8f8`.
- The historical original wheel files remain unavailable. The Builder claims
  only current payload reproducibility from those current authoritative
  artifacts, not original-file identity.
- The superseding Builder record is
  `verification/reports/F007_RLINK004_PYPI_REPRODUCIBILITY_BUILDER_20261003.json`.
  The earlier conflicting wheel-hash claim remains immutable historical
  evidence and is superseded only for source-wheel provenance.
- Builder claims the production loader imports `markdown_it` and `mdurl` only
  from `scripts/_vendor`; validates canonical internal `RECORD` paths and
  content; and fails closed for missing, tampered, or external-record payloads.
- Builder claims CommonMark governs rendered link destinations only. SpanGPU
  still owns canonical path resolution, external/local classification,
  historical rejection, raw-HTML rejection, F-000-04 quarantine, and lifecycle
  decisions.

## Required independent attack plan

1. Establish the exact reviewed commit and recompute the digest before trusting
   any Builder statement or hosted check.
2. Independently download or otherwise authenticate the two specified PyPI
   wheels, compare their SHA-256 values, and compare fresh raw extraction to
   the committed vendor tree. Do not infer lost-original identity.
3. Attack escaped/balanced/nested labels, reference-label normalization,
   duplicate/undefined definitions, title-bearing links, code false positives,
   raw HTML navigation, canonical traversal and encoded-path cases. For every
   actual historical local target, prove token -> destination -> canonical path
   -> historical classification -> `allowed=False` -> semantic rejection.
4. Recheck the F-000-04 first boundary: active governance must reject the
   rendered historical target before any historical resume document can reach
   `materialize-repositories.py --apply`.
5. Verify the audit counters derive from parser-token routes and policy
   decisions. Do not accept a zero-route semantic pass or any disguised form of
   `ignored_recognized_local_markdown_references=0`.
6. Run the materialized Trusted Runner against the exact `origin/main` SHA and
   inspect its runner/validator Git object identities. Recheck the Windows
   Git-Bash selection repair without accepting a WSL launcher substitution.
7. Establish exact-head hosted CI after push. Builder tests, BuilderKit
   validators, clean mergeability, and CI are supporting technical evidence,
   not independent approval.

## Explicit non-conclusions

No Fresh BREAKER outcome is asserted here. A materially independent reviewer
must issue its own `BREAKER_FAILED`, `BREAKER_BLOCKED`, or
`READY_FOR_OWNER_ACCEPTANCE` outcome, if warranted, for this exact subject.
