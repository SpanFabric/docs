# Requirements
> Canonical source: `12-machine-readable/requirements.yaml`. This Markdown is a generated/validated view.

## ANTICHEAT-001 — No bypass development
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `anticheat`  
**Description:** Project shall not implement concealment, spoofing or anti-cheat bypass techniques.

**Rationale/evidence:** RF-028

**Acceptance criteria:**
- Evidence demonstrates: Project shall not implement concealment, spoofing or anti-cheat bypass techniques.
- Required negative/failure case for No bypass development is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-016
**Gates:** GATE-029
**Phases:** PHASE-040
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## ANTICHEAT-002 — Third-party acceptance separate status
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `anticheat`  
**Description:** Anti-cheat refusal shall be classified THIRD_PARTY_BLOCKED rather than SPANGPU_BUG unless SpanGPU violates its own requirements.

**Rationale/evidence:** RF-028

**Acceptance criteria:**
- Evidence demonstrates: Anti-cheat refusal shall be classified THIRD_PARTY_BLOCKED rather than SPANGPU_BUG unless SpanGPU violates its own requirements.
- Required negative/failure case for Third-party acceptance separate status is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-016
**Gates:** GATE-029
**Phases:** PHASE-040
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## ANTICHEAT-003 — Official pilot only
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `anticheat`  
**Description:** Automated/partner anti-cheat pilots shall occur only under permitted normal use or explicit vendor cooperation.

**Rationale/evidence:** RF-028

**Acceptance criteria:**
- Evidence demonstrates: Automated/partner anti-cheat pilots shall occur only under permitted normal use or explicit vendor cooperation.
- Required negative/failure case for Official pilot only is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-016
**Gates:** GATE-029
**Phases:** PHASE-040
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## ANTICHEAT-004 — Driver transparency
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `anticheat`  
**Description:** SpanGPU driver/device identity shall be stable and documentable rather than hidden as another vendor device.

**Rationale/evidence:** RF-028

**Acceptance criteria:**
- Evidence demonstrates: SpanGPU driver/device identity shall be stable and documentable rather than hidden as another vendor device.
- Required negative/failure case for Driver transparency is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-016
**Gates:** GATE-029
**Phases:** PHASE-040
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## ANTICHEAT-005 — Integrity-compatible architecture
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `anticheat`  
**Description:** Production direction shall preserve Secure Boot/signing/integrity compatibility.

**Rationale/evidence:** RF-028

**Acceptance criteria:**
- Evidence demonstrates: Production direction shall preserve Secure Boot/signing/integrity compatibility.
- Required negative/failure case for Integrity-compatible architecture is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-016
**Gates:** GATE-029
**Phases:** PHASE-040
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## ANTICHEAT-006 — No injection dependency
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `anticheat`  
**Description:** Anti-cheat compatibility strategy shall not depend on process injection.

**Rationale/evidence:** RF-028

**Acceptance criteria:**
- Evidence demonstrates: Anti-cheat compatibility strategy shall not depend on process injection.
- Required negative/failure case for No injection dependency is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-016
**Gates:** GATE-029
**Phases:** PHASE-040
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## ANTICHEAT-007 — Policy change monitoring
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `anticheat`  
**Description:** Known third-party compatibility policy changes shall be monitored as external dependency risk.

**Rationale/evidence:** RF-028

**Acceptance criteria:**
- Evidence demonstrates: Known third-party compatibility policy changes shall be monitored as external dependency risk.
- Required negative/failure case for Policy change monitoring is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-016
**Gates:** GATE-029
**Phases:** PHASE-040
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## ANTICHEAT-008 — Compatibility evidence preserves cause
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `anticheat`  
**Description:** Reports shall distinguish render failure, driver failure, DRM failure and anti-cheat policy refusal.

**Rationale/evidence:** RF-028

**Acceptance criteria:**
- Evidence demonstrates: Reports shall distinguish render failure, driver failure, DRM failure and anti-cheat policy refusal.
- Required negative/failure case for Compatibility evidence preserves cause is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-016
**Gates:** GATE-029
**Phases:** PHASE-040
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## BOUNDARY-001 — Boundary audit trigger
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** Any change to a stable cross-component, cross-process, cross-machine, privilege, persistence or repository contract shall require a boundary audit.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Any change to a stable cross-component, cross-process, cross-machine, privilege, persistence or repository contract shall require a boundary audit.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-029
**Gates:** GATE-BK-000
**Phases:** PHASE-000
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## BOUNDARY-002 — Boundary ownership fields
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** Boundary audits shall identify producer guarantees, consumer assumptions, source of truth, validation/trust/version owners, concurrency, transactionality, retry/idempotency, failure semantics and future compatibility.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Boundary audits shall identify producer guarantees, consumer assumptions, source of truth, validation/trust/version owners, concurrency, transactionality, retry/idempotency, failure semantics and future compatibility.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-029
**Gates:** GATE-BK-000
**Phases:** PHASE-000
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## BUILD-001 — Reproducible bootstrap
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `build`  
**Description:** Phase 00 shall establish repeatable setup instructions for all required toolchains and selected OSS baselines.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Phase 00 shall establish repeatable setup instructions for all required toolchains and selected OSS baselines.
- Required negative/failure case for Reproducible bootstrap is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## BUILD-002 — Windows WDK/SDK inventory
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `build`  
**Description:** Supported Visual Studio/WDK/SDK versions shall be recorded and validated.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Supported Visual Studio/WDK/SDK versions shall be recorded and validated.
- Required negative/failure case for Windows WDK/SDK inventory is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## BUILD-003 — Host toolchain inventory
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `build`  
**Description:** Linux host compiler/build-system versions shall be recorded and validated.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Linux host compiler/build-system versions shall be recorded and validated.
- Required negative/failure case for Host toolchain inventory is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## BUILD-004 — Generated code reproducible
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `build`  
**Description:** Protocol/generated bindings shall be reproducible from checked-in schemas/generators.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Protocol/generated bindings shall be reproducible from checked-in schemas/generators.
- Required negative/failure case for Generated code reproducible is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## BUILD-005 — No hidden local dependencies
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `build`  
**Description:** Build shall not rely on unrecorded developer-machine files or conversational context.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Build shall not rely on unrecorded developer-machine files or conversational context.
- Required negative/failure case for No hidden local dependencies is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## BUILD-006 — Build provenance
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `build`  
**Description:** Artifacts shall record source commit, toolchain and dependency baselines.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Artifacts shall record source commit, toolchain and dependency baselines.
- Required negative/failure case for Build provenance is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## BUILD-007 — Fork build smoke tests
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `build`  
**Description:** Every controlled fork shall have an automated baseline build smoke test before modification.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Every controlled fork shall have an automated baseline build smoke test before modification.
- Required negative/failure case for Fork build smoke tests is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## BUILD-008 — Debug/release separation
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `build`  
**Description:** Driver/service debug settings and release settings shall be explicit and non-ambiguous.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Driver/service debug settings and release settings shall be explicit and non-ambiguous.
- Required negative/failure case for Debug/release separation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## BUILD-009 — No secrets in builds
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `build`  
**Description:** Build scripts/config shall not contain tokens, signing private keys or personal credentials.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Build scripts/config shall not contain tokens, signing private keys or personal credentials.
- Required negative/failure case for No secrets in builds is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## BUILD-010 — Artifact naming includes identity
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `build`  
**Description:** Test artifacts shall identify component/version/commit/attempt sufficiently to avoid stale evidence confusion.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Test artifacts shall identify component/version/commit/attempt sufficiently to avoid stale evidence confusion.
- Required negative/failure case for Artifact naming includes identity is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## BUILD-011 — Clean-room checkout test
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `build`  
**Description:** A fresh workspace checkout shall be able to validate metadata and begin Phase 00 without hidden state.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: A fresh workspace checkout shall be able to validate metadata and begin Phase 00 without hidden state.
- Required negative/failure case for Clean-room checkout test is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CACHE-001 — Content-addressed immutable cache
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `cache`  
**Description:** Immutable resources shall support a content-addressed cache keyed by cryptographic digest and canonical metadata.

**Rationale/evidence:** RF-024

**Acceptance criteria:**
- Evidence demonstrates: Immutable resources shall support a content-addressed cache keyed by cryptographic digest and canonical metadata.
- Required negative/failure case for Content-addressed immutable cache is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-009
**Gates:** GATE-008
**Phases:** PHASE-017
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CACHE-002 — Session-local cache first
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `cache`  
**Description:** v1 may begin with session-local persistence but schema shall not preclude cross-session persistent cache.

**Rationale/evidence:** RF-024

**Acceptance criteria:**
- Evidence demonstrates: v1 may begin with session-local persistence but schema shall not preclude cross-session persistent cache.
- Required negative/failure case for Session-local cache first is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-009
**Gates:** GATE-008
**Phases:** PHASE-017
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CACHE-003 — Cache hit validation
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `cache`  
**Description:** A cache hit shall validate required metadata/capability compatibility before reuse.

**Rationale/evidence:** RF-024

**Acceptance criteria:**
- Evidence demonstrates: A cache hit shall validate required metadata/capability compatibility before reuse.
- Required negative/failure case for Cache hit validation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-009
**Gates:** GATE-008
**Phases:** PHASE-017
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CACHE-004 — Cache corruption detection
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `cache`  
**Description:** Corrupt cache entries shall be rejected and regenerated/reuploaded with evidence.

**Rationale/evidence:** RF-024

**Acceptance criteria:**
- Evidence demonstrates: Corrupt cache entries shall be rejected and regenerated/reuploaded with evidence.
- Required negative/failure case for Cache corruption detection is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-009
**Gates:** GATE-008
**Phases:** PHASE-017
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CACHE-005 — No cache as source of truth
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `cache`  
**Description:** Cache state shall never override authoritative resource generation/lifetime state.

**Rationale/evidence:** RF-024

**Acceptance criteria:**
- Evidence demonstrates: Cache state shall never override authoritative resource generation/lifetime state.
- Required negative/failure case for No cache as source of truth is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-009
**Gates:** GATE-008
**Phases:** PHASE-017
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CACHE-006 — Shader cache
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `cache`  
**Description:** Reusable shaders shall support remote cache identity where driver/API semantics permit.

**Rationale/evidence:** RF-024

**Acceptance criteria:**
- Evidence demonstrates: Reusable shaders shall support remote cache identity where driver/API semantics permit.
- Required negative/failure case for Shader cache is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-009
**Gates:** GATE-008
**Phases:** PHASE-017
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CACHE-007 — Pipeline cache
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `cache`  
**Description:** Pipelines/PSOs shall support cache identity/versioning where semantics permit.

**Rationale/evidence:** RF-024

**Acceptance criteria:**
- Evidence demonstrates: Pipelines/PSOs shall support cache identity/versioning where semantics permit.
- Required negative/failure case for Pipeline cache is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-009
**Gates:** GATE-008
**Phases:** PHASE-017
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CACHE-008 — Texture/buffer deduplication
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `cache`  
**Description:** Identical immutable payloads shall be transferable once and referenced by identity thereafter.

**Rationale/evidence:** RF-024

**Acceptance criteria:**
- Evidence demonstrates: Identical immutable payloads shall be transferable once and referenced by identity thereafter.
- Required negative/failure case for Texture/buffer deduplication is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-009
**Gates:** GATE-008
**Phases:** PHASE-017
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CACHE-009 — Delta update optional
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `cache`  
**Description:** Delta/range transfer may optimize mutable resources only when correctness and CPU cost are measured.

**Rationale/evidence:** RF-024

**Acceptance criteria:**
- Evidence demonstrates: Delta/range transfer may optimize mutable resources only when correctness and CPU cost are measured.
- Required negative/failure case for Delta update optional is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-009
**Gates:** GATE-008
**Phases:** PHASE-017
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CACHE-010 — Cache metrics
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `cache`  
**Description:** Hit/miss/bytes-saved/validation-failure/eviction metrics shall be captured.

**Rationale/evidence:** RF-024

**Acceptance criteria:**
- Evidence demonstrates: Hit/miss/bytes-saved/validation-failure/eviction metrics shall be captured.
- Required negative/failure case for Cache metrics is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-009
**Gates:** GATE-008
**Phases:** PHASE-017
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CACHE-011 — Cache invalidation versioned
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `cache`  
**Description:** Protocol/driver/backend capability changes shall invalidate incompatible cache entries deterministically.

**Rationale/evidence:** RF-024

**Acceptance criteria:**
- Evidence demonstrates: Protocol/driver/backend capability changes shall invalidate incompatible cache entries deterministically.
- Required negative/failure case for Cache invalidation versioned is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-009
**Gates:** GATE-008
**Phases:** PHASE-017
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CACHE-012 — Cache security boundary
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `cache`  
**Description:** Persistent cache shall prevent cross-user/session data disclosure according to configured tenancy model.

**Rationale/evidence:** RF-024

**Acceptance criteria:**
- Evidence demonstrates: Persistent cache shall prevent cross-user/session data disclosure according to configured tenancy model.
- Required negative/failure case for Cache security boundary is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-009
**Gates:** GATE-008
**Phases:** PHASE-017
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CI-001 — PR CI baseline
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `ci`  
**Description:** Every PR shall run metadata validation, build/lint/unit/contract tests applicable to changed components.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Every PR shall run metadata validation, build/lint/unit/contract tests applicable to changed components.
- Required negative/failure case for PR CI baseline is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CI-002 — Hardware-required labeling
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `ci`  
**Description:** Changes requiring hardware evidence shall be machine-detectable/declared and cannot merge on software CI alone.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Changes requiring hardware evidence shall be machine-detectable/declared and cannot merge on software CI alone.
- Required negative/failure case for Hardware-required labeling is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CI-003 — Controlled fork CI
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `ci`  
**Description:** Fork update PRs shall run SpanGPU patch compatibility and selected hardware tests before adoption.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Fork update PRs shall run SpanGPU patch compatibility and selected hardware tests before adoption.
- Required negative/failure case for Controlled fork CI is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CI-004 — No automatic critical-fork merge
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `ci`  
**Description:** Critical upstream updates shall never auto-merge.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Critical upstream updates shall never auto-merge.
- Required negative/failure case for No automatic critical-fork merge is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CI-005 — Immutable artifacts
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `ci`  
**Description:** CI proof artifacts shall be associated with commit SHA and attempt ID.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: CI proof artifacts shall be associated with commit SHA and attempt ID.
- Required negative/failure case for Immutable artifacts is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CI-006 — Separate builder/reviewer status
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `ci`  
**Description:** CI/state shall distinguish builder green from independent review accepted.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: CI/state shall distinguish builder green from independent review accepted.
- Required negative/failure case for Separate builder/reviewer status is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CI-007 — Environment blocker status
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `ci`  
**Description:** Infrastructure inability to run required validation shall produce BLOCKED_ENVIRONMENT.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Infrastructure inability to run required validation shall produce BLOCKED_ENVIRONMENT.
- Required negative/failure case for Environment blocker status is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CI-008 — Matrix version pinning
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `ci`  
**Description:** Toolchain/OS/dependency versions used by CI shall be explicit and recorded.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Toolchain/OS/dependency versions used by CI shall be explicit and recorded.
- Required negative/failure case for Matrix version pinning is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CI-009 — Reproducible commands
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `ci`  
**Description:** Local and CI test commands shall be documented and as reproducible as practical.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Local and CI test commands shall be documented and as reproducible as practical.
- Required negative/failure case for Reproducible commands is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CI-010 — Branch protection evidence gates
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `ci`  
**Description:** Critical repositories shall require status checks representing mandatory review/gates appropriate to phase maturity.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Critical repositories shall require status checks representing mandatory review/gates appropriate to phase maturity.
- Required negative/failure case for Branch protection evidence gates is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CI-011 — No retry-until-green automation
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `ci`  
**Description:** CI bots shall not auto-rerun failing nondeterministic jobs until one passes.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: CI bots shall not auto-rerun failing nondeterministic jobs until one passes.
- Required negative/failure case for No retry-until-green automation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## CI-012 — Phase/gate state validation
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `ci`  
**Description:** CI shall validate project state and evidence references before phase completion PRs merge.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: CI shall validate project state and evidence references before phase completion PRs merge.
- Required negative/failure case for Phase/gate state validation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## COMPAT-001 — Machine-readable compatibility records
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `compat`  
**Description:** Each tested application/version shall produce a record matching the compatibility schema.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Each tested application/version shall produce a record matching the compatibility schema.
- Required negative/failure case for Machine-readable compatibility records is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-026
**Phases:** PHASE-038
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## COMPAT-002 — Result taxonomy fixed
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `compat`  
**Description:** Compatibility uses SUPPORTED, SUPPORTED_WITH_LIMITATIONS, SPANGPU_BUG, THIRD_PARTY_BLOCKED, UNSUPPORTED_ARCHITECTURE, UNKNOWN or NOT_TESTED.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Compatibility uses SUPPORTED, SUPPORTED_WITH_LIMITATIONS, SPANGPU_BUG, THIRD_PARTY_BLOCKED, UNSUPPORTED_ARCHITECTURE, UNKNOWN or NOT_TESTED.
- Required negative/failure case for Result taxonomy fixed is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-026
**Phases:** PHASE-038
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## COMPAT-003 — Application version captured
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `compat`  
**Description:** Compatibility evidence shall include application/game version/build.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Compatibility evidence shall include application/game version/build.
- Required negative/failure case for Application version captured is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-026
**Phases:** PHASE-038
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## COMPAT-004 — Engine captured
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `compat`  
**Description:** Known engine and version shall be recorded where determinable.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Known engine and version shall be recorded where determinable.
- Required negative/failure case for Engine captured is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-026
**Phases:** PHASE-038
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## COMPAT-005 — Launcher captured
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `compat`  
**Description:** Launcher shall be recorded but shall not be required for architecture integration.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Launcher shall be recorded but shall not be required for architecture integration.
- Required negative/failure case for Launcher captured is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-026
**Phases:** PHASE-038
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## COMPAT-006 — Graphics API captured
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `compat`  
**Description:** Actual API/path used shall be recorded rather than inferred solely from game marketing.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Actual API/path used shall be recorded rather than inferred solely from game marketing.
- Required negative/failure case for Graphics API captured is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-026
**Phases:** PHASE-038
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## COMPAT-007 — Client/host OS captured
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `compat`  
**Description:** Exact tested client and host OS versions shall be recorded.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Exact tested client and host OS versions shall be recorded.
- Required negative/failure case for Client/host OS captured is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-026
**Phases:** PHASE-038
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## COMPAT-008 — Driver versions captured
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `compat`  
**Description:** SpanGPU and vendor driver versions shall be recorded.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: SpanGPU and vendor driver versions shall be recorded.
- Required negative/failure case for Driver versions captured is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-026
**Phases:** PHASE-038
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## COMPAT-009 — Network profile captured
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `compat`  
**Description:** RTT/loss/jitter/bandwidth profile shall be part of result identity.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: RTT/loss/jitter/bandwidth profile shall be part of result identity.
- Required negative/failure case for Network profile captured is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-026
**Phases:** PHASE-038
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## COMPAT-010 — Local/remote GPU captured
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `compat`  
**Description:** Local adapter and selected remote GPU shall be recorded.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Local adapter and selected remote GPU shall be recorded.
- Required negative/failure case for Local/remote GPU captured is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-026
**Phases:** PHASE-038
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## COMPAT-011 — Evidence references immutable
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `compat`  
**Description:** Compatibility records shall link immutable logs/screenshots/traces/results where policy permits.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Compatibility records shall link immutable logs/screenshots/traces/results where policy permits.
- Required negative/failure case for Evidence references immutable is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-026
**Phases:** PHASE-038
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## COMPAT-012 — No unsupported extrapolation
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `compat`  
**Description:** A passing title/version/hardware combination shall not automatically imply all versions/APIs/anti-cheat modes are supported.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: A passing title/version/hardware combination shall not automatically imply all versions/APIs/anti-cheat modes are supported.
- Required negative/failure case for No unsupported extrapolation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-026
**Phases:** PHASE-038
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## COMPAT-013 — Representative engine matrix
**Priority:** `SHOULD`  
**Horizon:** `later`  
**Component:** `compat`  
**Description:** Long-term matrix shall include Unreal, Unity, custom engines, older DX, modern DX12, Vulkan and RT workloads.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Long-term matrix shall include Unreal, Unity, custom engines, older DX, modern DX12, Vulkan and RT workloads.
- Required negative/failure case for Representative engine matrix is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-026
**Phases:** PHASE-038
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DOC-001 — BuilderKit self-contained
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `doc`  
**Description:** A fresh Codex session shall understand project intent, architecture, rules and current state from repository artifacts alone.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: A fresh Codex session shall understand project intent, architecture, rules and current state from repository artifacts alone.
- Required negative/failure case for BuilderKit self-contained is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DOC-002 — Architecture documents normative labels
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `doc`  
**Description:** Documents shall distinguish normative requirements/invariants/TDs from explanatory research notes.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Documents shall distinguish normative requirements/invariants/TDs from explanatory research notes.
- Required negative/failure case for Architecture documents normative labels is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DOC-003 — Research evidence preserved
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `doc`  
**Description:** Research-derived choices shall link finding IDs and source URLs/summaries.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Research-derived choices shall link finding IDs and source URLs/summaries.
- Required negative/failure case for Research evidence preserved is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DOC-004 — Uncertainty structured
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `doc`  
**Description:** Unresolved decisions shall use PROOF_REQUIRED with owner, gate, options and evidence needed.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Unresolved decisions shall use PROOF_REQUIRED with owner, gate, options and evidence needed.
- Required negative/failure case for Uncertainty structured is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DOC-005 — No hidden conversation references
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `doc`  
**Description:** Project docs shall not rely on phrases such as prior chat/context for essential meaning.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Project docs shall not rely on phrases such as prior chat/context for essential meaning.
- Required negative/failure case for No hidden conversation references is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DOC-006 — Interface docs versioned
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `doc`  
**Description:** Stable cross-component interfaces shall have owner/version/failure/trust semantics documented.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Stable cross-component interfaces shall have owner/version/failure/trust semantics documented.
- Required negative/failure case for Interface docs versioned is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DOC-007 — Phase specs Codex-ready
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `doc`  
**Description:** Every phase file shall be executable from repository state without requiring a human to reconstruct scope.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Every phase file shall be executable from repository state without requiring a human to reconstruct scope.
- Required negative/failure case for Phase specs Codex-ready is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DOC-008 — Gate specs evidence-ready
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `doc`  
**Description:** Every gate shall specify environment, procedure, metrics, artifacts and pass/fail/blocked rules.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Every gate shall specify environment, procedure, metrics, artifacts and pass/fail/blocked rules.
- Required negative/failure case for Gate specs evidence-ready is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DOC-009 — Known limitations explicit
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `doc`  
**Description:** Unsupported/unproven API, RTT, vendor, trust and anti-cheat states shall be documented.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Unsupported/unproven API, RTT, vendor, trust and anti-cheat states shall be documented.
- Required negative/failure case for Known limitations explicit is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DOC-010 — ADR/TD index authoritative
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `doc`  
**Description:** Technology decision status/index shall be machine-readable and match individual files.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Technology decision status/index shall be machine-readable and match individual files.
- Required negative/failure case for ADR/TD index authoritative is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DOC-011 — Architecture diagrams source-controlled
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `doc`  
**Description:** System/flow/trust/failure diagrams shall be stored in text-source format.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: System/flow/trust/failure diagrams shall be stored in text-source format.
- Required negative/failure case for Architecture diagrams source-controlled is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DOC-012 — Contributor terminology stable
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `doc`  
**Description:** Core terms such as resource authority, attempt, evidence, gate, breaker and session epoch shall have canonical definitions.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Core terms such as resource authority, attempt, evidence, gate, breaker and session epoch shall have canonical definitions.
- Required negative/failure case for Contributor terminology stable is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DOC-013 — Normative governance source of truth
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** After Phase 00, requirements, TDs, phases, gates and architecture metadata shall have a single authoritative home in the docs repository; mirrors/generated views are non-authoritative.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: After Phase 00, requirements, TDs, phases, gates and architecture metadata shall have a single authoritative home in the docs repository; mirrors/generated views are non-authoritative.
- Machine-readable validators reject contradictory/overwritten state.

**Verification:** Metadata validator plus Project Steward policy tests.
**Dependencies:** None
**TDs:** TD-027
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Prior attempts or review states can be mistaken for current evidence, enabling fake completion or stale-state recovery.

## DOC-014 — Append-only attempt history
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** Builder, gate, reviewer, remediation and recovery attempts shall be recorded as distinct append-only events rather than overwriting a single status record.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Builder, gate, reviewer, remediation and recovery attempts shall be recorded as distinct append-only events rather than overwriting a single status record.
- Machine-readable validators reject contradictory/overwritten state.

**Verification:** Metadata validator plus Project Steward policy tests.
**Dependencies:** None
**TDs:** TD-028
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Prior attempts or review states can be mistaken for current evidence, enabling fake completion or stale-state recovery.

## DOC-015 — Builder and breaker identities separated
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** Evidence metadata shall distinguish builder session/attempt from independent breaker session/attempt.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Evidence metadata shall distinguish builder session/attempt from independent breaker session/attempt.
- Machine-readable validators reject contradictory/overwritten state.

**Verification:** Metadata validator plus Project Steward policy tests.
**Dependencies:** None
**TDs:** TD-028
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Prior attempts or review states can be mistaken for current evidence, enabling fake completion or stale-state recovery.

## DOC-016 — Gate PASS references immutable evidence
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** A gate PASS record shall reference commit SHA plus immutable artifact/log identifiers and the successful attempt ID.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: A gate PASS record shall reference commit SHA plus immutable artifact/log identifiers and the successful attempt ID.
- Machine-readable validators reject contradictory/overwritten state.

**Verification:** Metadata validator plus Project Steward policy tests.
**Dependencies:** None
**TDs:** TD-028
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Prior attempts or review states can be mistaken for current evidence, enabling fake completion or stale-state recovery.

## DOC-017 — Phase DONE references accepted review
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** A phase DONE record shall reference required gate PASS and the fresh BREAKER acceptance attempt.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: A phase DONE record shall reference required gate PASS and the fresh BREAKER acceptance attempt.
- Machine-readable validators reject contradictory/overwritten state.

**Verification:** Metadata validator plus Project Steward policy tests.
**Dependencies:** None
**TDs:** TD-028
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Prior attempts or review states can be mistaken for current evidence, enabling fake completion or stale-state recovery.

## DOC-018 — Finding lifecycle explicit
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** Findings shall move through OPEN, ACCEPTED, FIXED_PENDING_REVIEW, VERIFIED or REJECTED_WITH_EVIDENCE without being deleted from history.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Findings shall move through OPEN, ACCEPTED, FIXED_PENDING_REVIEW, VERIFIED or REJECTED_WITH_EVIDENCE without being deleted from history.
- Machine-readable validators reject contradictory/overwritten state.

**Verification:** Metadata validator plus Project Steward policy tests.
**Dependencies:** None
**TDs:** TD-028
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Prior attempts or review states can be mistaken for current evidence, enabling fake completion or stale-state recovery.

## DX-001 — DX9 long-term support
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `dx`  
**Description:** Architecture shall retain a supported path for unmodified Direct3D 9 applications.

**Rationale/evidence:** RF-003, RF-019, RF-020

**Acceptance criteria:**
- Evidence demonstrates: Architecture shall retain a supported path for unmodified Direct3D 9 applications.
- Required negative/failure case for DX9 long-term support is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-005
**Phases:** PHASE-012, PHASE-031
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DX-002 — DX10 long-term support
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `dx`  
**Description:** Architecture shall retain a supported path for unmodified Direct3D 10 applications.

**Rationale/evidence:** RF-003, RF-019, RF-020

**Acceptance criteria:**
- Evidence demonstrates: Architecture shall retain a supported path for unmodified Direct3D 10 applications.
- Required negative/failure case for DX10 long-term support is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-005
**Phases:** PHASE-012, PHASE-031
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DX-003 — DX11 v1 proof path
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `dx`  
**Description:** D3D11 shall be the first full graphics proof path using Triton/Neptune-derived OSS where validated.

**Rationale/evidence:** RF-003, RF-019, RF-020

**Acceptance criteria:**
- Evidence demonstrates: D3D11 shall be the first full graphics proof path using Triton/Neptune-derived OSS where validated.
- Required negative/failure case for DX11 v1 proof path is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-005
**Phases:** PHASE-012
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DX-004 — DX11 third-party proof
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `dx`  
**Description:** At least one unmodified third-party D3D11 application shall pass before game scaling.

**Rationale/evidence:** RF-003, RF-019, RF-020

**Acceptance criteria:**
- Evidence demonstrates: At least one unmodified third-party D3D11 application shall pass before game scaling.
- Required negative/failure case for DX11 third-party proof is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-005
**Phases:** PHASE-012, PHASE-011
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DX-005 — DX11 real-game proof
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `dx`  
**Description:** At least one unmodified D3D11 game shall pass the defined game gate.

**Rationale/evidence:** RF-003, RF-019, RF-020

**Acceptance criteria:**
- Evidence demonstrates: At least one unmodified D3D11 game shall pass the defined game gate.
- Required negative/failure case for DX11 real-game proof is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-005
**Phases:** PHASE-012, PHASE-014
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DX-006 — DX12 separate proof decision
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `dx`  
**Description:** D3D12 shall not be marked supported until the bounded architecture proof establishes compatibility with the common core.

**Rationale/evidence:** RF-003, RF-019, RF-020

**Acceptance criteria:**
- Evidence demonstrates: D3D12 shall not be marked supported until the bounded architecture proof establishes compatibility with the common core.
- Required negative/failure case for DX12 separate proof decision is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-005
**Phases:** PHASE-012, PHASE-032, PHASE-033
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DX-007 — DX12 no hidden fallback
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `dx`  
**Description:** D3D12 support shall not silently route through per-game wrappers/injection to claim success.

**Rationale/evidence:** RF-003, RF-019, RF-020

**Acceptance criteria:**
- Evidence demonstrates: D3D12 support shall not silently route through per-game wrappers/injection to claim success.
- Required negative/failure case for DX12 no hidden fallback is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-005
**Phases:** PHASE-012, PHASE-032, PHASE-033
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DX-008 — DX feature level reporting
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `dx`  
**Description:** Exposed D3D feature levels shall not exceed remotely supported semantics.

**Rationale/evidence:** RF-003, RF-019, RF-020

**Acceptance criteria:**
- Evidence demonstrates: Exposed D3D feature levels shall not exceed remotely supported semantics.
- Required negative/failure case for DX feature level reporting is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-005
**Phases:** PHASE-012
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DX-009 — DX device removal mapping
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `dx`  
**Description:** Remote failures shall map to valid D3D device-removal behavior with diagnostics.

**Rationale/evidence:** RF-003, RF-019, RF-020

**Acceptance criteria:**
- Evidence demonstrates: Remote failures shall map to valid D3D device-removal behavior with diagnostics.
- Required negative/failure case for DX device removal mapping is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-005
**Phases:** PHASE-012
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## DX-010 — DX debug-layer test coverage
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `dx`  
**Description:** Where available, Direct3D debug/validation layers shall run in proof and regression tests.

**Rationale/evidence:** RF-003, RF-019, RF-020

**Acceptance criteria:**
- Evidence demonstrates: Where available, Direct3D debug/validation layers shall run in proof and regression tests.
- Required negative/failure case for DX debug-layer test coverage is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-021
**Gates:** GATE-005
**Phases:** PHASE-012
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## EVIDENCE-001 — Unique attempt identity
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** Every builder, breaker, gate, recovery, hardware and release execution shall receive a globally unique immutable attempt_id.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Every builder, breaker, gate, recovery, hardware and release execution shall receive a globally unique immutable attempt_id.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-030
**Gates:** GATE-BK-000
**Phases:** PHASE-000
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## EVIDENCE-002 — Commit-bound evidence
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** Evidence shall record the exact commit SHA/build identity under test and may not be reused as proof for a different commit.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Evidence shall record the exact commit SHA/build identity under test and may not be reused as proof for a different commit.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-030
**Gates:** GATE-BK-000
**Phases:** PHASE-000
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## EVIDENCE-003 — Environment fingerprint
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `evals`  
**Description:** Every non-unit proof shall record OS/build, toolchain, driver, dependency and relevant runtime versions.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Every non-unit proof shall record OS/build, toolchain, driver, dependency and relevant runtime versions.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-030
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## EVIDENCE-004 — Hardware fingerprint
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `evals`  
**Description:** Hardware-gated evidence shall record stable client, GPU host, local GPU, remote GPU, firmware and relevant PCI/device identities.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Hardware-gated evidence shall record stable client, GPU host, local GPU, remote GPU, firmware and relevant PCI/device identities.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-032
**Gates:** GATE-000
**Phases:** PHASE-002
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## EVIDENCE-005 — Raw evidence immutability
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `evals`  
**Description:** Raw logs, dumps, traces and benchmark outputs used for a verdict shall be content-hashed and append-only.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Raw logs, dumps, traces and benchmark outputs used for a verdict shall be content-hashed and append-only.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-030
**Gates:** GATE-BK-000
**Phases:** PHASE-000
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## EVIDENCE-006 — Derived metrics provenance
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `evals`  
**Description:** Derived metrics shall record the raw artifact hashes and exact derivation tool/version that produced them.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Derived metrics shall record the raw artifact hashes and exact derivation tool/version that produced them.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-030
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## EVIDENCE-007 — Evidence staleness rules
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** Evidence shall declare applicability constraints and become stale when commit, protocol, relevant driver/OS/hardware baseline or acceptance criteria change.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Evidence shall declare applicability constraints and become stale when commit, protocol, relevant driver/OS/hardware baseline or acceptance criteria change.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-030
**Gates:** GATE-BK-000
**Phases:** PHASE-000
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## EVIDENCE-008 — Supersession is append-only
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** New evidence may supersede old evidence but shall never mutate or delete the historical record.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: New evidence may supersede old evidence but shall never mutate or delete the historical record.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-030
**Gates:** GATE-BK-000
**Phases:** PHASE-000
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## EVIDENCE-009 — Builder and breaker evidence separation
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** Builder and fresh BREAKER evidence bundles shall be separate and independently attributable.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Builder and fresh BREAKER evidence bundles shall be separate and independently attributable.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-025
**Gates:** GATE-BK-000
**Phases:** PHASE-000
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## FINDING-001 — Finding lifecycle persistence
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** Every review finding shall retain identity and lifecycle history across sessions and remediation attempts.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Every review finding shall retain identity and lifecycle history across sessions and remediation attempts.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-031
**Gates:** GATE-BK-000
**Phases:** PHASE-000
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## FINDING-002 — Merge-blocking evidence threshold
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** A merge-blocking finding shall include failure mechanism/sequence, violated requirement/invariant, impact/severity, remediation and regression proof expectation.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: A merge-blocking finding shall include failure mechanism/sequence, violated requirement/invariant, impact/severity, remediation and regression proof expectation.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-031
**Gates:** GATE-BK-000
**Phases:** PHASE-000
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## FINDING-003 — Fresh verification after remediation
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** A fixed blocking finding shall not become VERIFIED until a fresh BREAKER attempt validates the remediation and regression evidence.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: A fixed blocking finding shall not become VERIFIED until a fresh BREAKER attempt validates the remediation and regression evidence.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-031
**Gates:** GATE-BK-000
**Phases:** PHASE-000
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## FUNC-001 — No game modification
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `func`  
**Description:** Primary operation shall not require patching or modifying game binaries, assets or source.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Primary operation shall not require patching or modifying game binaries, assets or source.
- Required negative/failure case for No game modification is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## FUNC-002 — No per-game core plugin
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `func`  
**Description:** Primary operation shall not require a SpanGPU plugin authored for each game or engine.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Primary operation shall not require a SpanGPU plugin authored for each game or engine.
- Required negative/failure case for No per-game core plugin is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## FUNC-003 — No launcher integration
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `func`  
**Description:** Launchers shall not need SpanGPU-specific extensions or account linking for core graphics operation.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Launchers shall not need SpanGPU-specific extensions or account linking for core graphics operation.
- Required negative/failure case for No launcher integration is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-001
**Phases:** PHASE-004, PHASE-015
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## FUNC-004 — No DLL injection core path
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `func`  
**Description:** DLL injection/hooking shall not be required for normal SpanGPU rendering.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: DLL injection/hooking shall not be required for normal SpanGPU rendering.
- Required negative/failure case for No DLL injection core path is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## FUNC-005 — Adapter selectable by normal OS/application mechanisms
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `func`  
**Description:** Applications shall discover/select SpanGPU through normal Windows graphics adapter enumeration mechanisms.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Applications shall discover/select SpanGPU through normal Windows graphics adapter enumeration mechanisms.
- Required negative/failure case for Adapter selectable by normal OS/application mechanisms is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-001
**Phases:** PHASE-004, PHASE-013
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## FUNC-006 — Session establishment independent of application
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `func`  
**Description:** SpanGPU session lifecycle shall be managed by driver/service/host components rather than application-specific code.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: SpanGPU session lifecycle shall be managed by driver/service/host components rather than application-specific code.
- Required negative/failure case for Session establishment independent of application is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-001
**Phases:** PHASE-004, PHASE-015
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## FUNC-007 — Graceful unsupported-feature reporting
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `func`  
**Description:** Unsupported graphics capabilities shall fail with explicit capability diagnostics rather than undefined behavior.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Unsupported graphics capabilities shall fail with explicit capability diagnostics rather than undefined behavior.
- Required negative/failure case for Graceful unsupported-feature reporting is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## FUNC-008 — Local GPU remains usable
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `func`  
**Description:** SpanGPU activation shall not disable the local GPU or prevent normal local graphics use.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: SpanGPU activation shall not disable the local GPU or prevent normal local graphics use.
- Required negative/failure case for Local GPU remains usable is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## FUNC-009 — One-host one-session v1 permitted
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `func`  
**Description:** v1 may constrain scheduling to one GPU/session while preserving interfaces for later sharing/multitenancy.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: v1 may constrain scheduling to one GPU/session while preserving interfaces for later sharing/multitenancy.
- Required negative/failure case for One-host one-session v1 permitted is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## FUNC-010 — Non-game application compatibility path
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `func`  
**Description:** Architecture shall not encode assumptions that exclude Blender, CAD/rendering or later compute workloads.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Architecture shall not encode assumptions that exclude Blender, CAD/rendering or later compute workloads.
- Required negative/failure case for Non-game application compatibility path is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GFX-001 — Common graphics object namespace
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gfx`  
**Description:** SpanGPU shall define stable identities for devices, queues, resources, pipelines and synchronization objects independent of transport handles.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: SpanGPU shall define stable identities for devices, queues, resources, pipelines and synchronization objects independent of transport handles.
- Required negative/failure case for Common graphics object namespace is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-003
**Phases:** PHASE-009
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GFX-002 — API namespace isolation
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gfx`  
**Description:** D3D, Vulkan and OpenGL command namespaces shall be separable so API evolution does not change generic resource/transport semantics.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: D3D, Vulkan and OpenGL command namespaces shall be separable so API evolution does not change generic resource/transport semantics.
- Required negative/failure case for API namespace isolation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-003
**Phases:** PHASE-009
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GFX-003 — Capability negotiation
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gfx`  
**Description:** Client shall receive authoritative host GPU/API capability data before exposing unsupported functionality.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Client shall receive authoritative host GPU/API capability data before exposing unsupported functionality.
- Required negative/failure case for Capability negotiation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-003
**Phases:** PHASE-009
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GFX-004 — Deterministic unsupported caps
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gfx`  
**Description:** Capability gaps shall be deterministic and reproducible across runs with the same negotiated profile.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Capability gaps shall be deterministic and reproducible across runs with the same negotiated profile.
- Required negative/failure case for Deterministic unsupported caps is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-003
**Phases:** PHASE-009
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GFX-005 — Shader lifecycle modeled
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gfx`  
**Description:** Shader create/cache/use/destroy behavior shall have stable remote identity and evidence.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Shader create/cache/use/destroy behavior shall have stable remote identity and evidence.
- Required negative/failure case for Shader lifecycle modeled is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-003
**Phases:** PHASE-009
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GFX-006 — Pipeline lifecycle modeled
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gfx`  
**Description:** Pipeline/PSO-like objects shall support remote creation/cache/reuse without per-frame recreation where API semantics permit.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Pipeline/PSO-like objects shall support remote creation/cache/reuse without per-frame recreation where API semantics permit.
- Required negative/failure case for Pipeline lifecycle modeled is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-003
**Phases:** PHASE-009
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GFX-007 — Descriptor/binding semantics preserved
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gfx`  
**Description:** Descriptor/binding updates shall preserve API-visible ordering and lifetime.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Descriptor/binding updates shall preserve API-visible ordering and lifetime.
- Required negative/failure case for Descriptor/binding semantics preserved is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-003
**Phases:** PHASE-009
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GFX-008 — Resource format negotiation
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gfx`  
**Description:** Formats/tiling/export constraints shall be negotiated or rejected explicitly rather than guessed.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Formats/tiling/export constraints shall be negotiated or rejected explicitly rather than guessed.
- Required negative/failure case for Resource format negotiation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-003
**Phases:** PHASE-009
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GFX-009 — No generic protocol vendor opcode leakage
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gfx`  
**Description:** Vendor-private commands shall be extension-scoped, not part of mandatory generic protocol.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Vendor-private commands shall be extension-scoped, not part of mandatory generic protocol.
- Required negative/failure case for No generic protocol vendor opcode leakage is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004, TD-013
**Gates:** GATE-003
**Phases:** PHASE-009
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GFX-010 — Feature profile recorded in evidence
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gfx`  
**Description:** Every compatibility result shall record negotiated graphics feature/capability profile.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Every compatibility result shall record negotiated graphics feature/capability profile.
- Required negative/failure case for Feature profile recorded in evidence is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-003
**Phases:** PHASE-009
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GL-001 — OpenGL normal ICD path
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `gl`  
**Description:** OpenGL support shall be exposed through a normal Windows OpenGL driver/ICD path where feasible.

**Rationale/evidence:** RF-021

**Acceptance criteria:**
- Evidence demonstrates: OpenGL support shall be exposed through a normal Windows OpenGL driver/ICD path where feasible.
- Required negative/failure case for OpenGL normal ICD path is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-022
**Phases:** PHASE-030
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GL-002 — Zink consolidation evaluated
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `gl`  
**Description:** Mesa/Zink shall be evaluated as the preferred OpenGL-over-Vulkan consolidation path before creating a separate remote GL backend.

**Rationale/evidence:** RF-021

**Acceptance criteria:**
- Evidence demonstrates: Mesa/Zink shall be evaluated as the preferred OpenGL-over-Vulkan consolidation path before creating a separate remote GL backend.
- Required negative/failure case for Zink consolidation evaluated is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-022
**Phases:** PHASE-030
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GL-003 — Legacy GL compatibility tracked
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `gl`  
**Description:** Compatibility matrix shall distinguish core/compatibility profiles and extension gaps.

**Rationale/evidence:** RF-021

**Acceptance criteria:**
- Evidence demonstrates: Compatibility matrix shall distinguish core/compatibility profiles and extension gaps.
- Required negative/failure case for Legacy GL compatibility tracked is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-022
**Phases:** PHASE-030
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GL-004 — GL context lifetime remote-safe
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `gl`  
**Description:** Context creation/sharing/destruction shall preserve remote object ownership.

**Rationale/evidence:** RF-021

**Acceptance criteria:**
- Evidence demonstrates: Context creation/sharing/destruction shall preserve remote object ownership.
- Required negative/failure case for GL context lifetime remote-safe is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-022
**Phases:** PHASE-030
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GL-005 — GL synchronization mapped
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `gl`  
**Description:** glFinish/glFlush/fence-like operations shall be profiled for RTT and implemented with correct semantics.

**Rationale/evidence:** RF-021

**Acceptance criteria:**
- Evidence demonstrates: glFinish/glFlush/fence-like operations shall be profiled for RTT and implemented with correct semantics.
- Required negative/failure case for GL synchronization mapped is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-022
**Phases:** PHASE-030
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GL-006 — GL mapped resource behavior explicit
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `gl`  
**Description:** Persistent/coherent mappings shall be staged/emulated/rejected explicitly rather than assumed coherent over WAN.

**Rationale/evidence:** RF-021

**Acceptance criteria:**
- Evidence demonstrates: Persistent/coherent mappings shall be staged/emulated/rejected explicitly rather than assumed coherent over WAN.
- Required negative/failure case for GL mapped resource behavior explicit is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-022
**Phases:** PHASE-030
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GL-007 — GL extension exposure truthful
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `gl`  
**Description:** Reported extensions shall match effective semantics on the remote backend.

**Rationale/evidence:** RF-021

**Acceptance criteria:**
- Evidence demonstrates: Reported extensions shall match effective semantics on the remote backend.
- Required negative/failure case for GL extension exposure truthful is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-022
**Phases:** PHASE-030
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GL-008 — GL third-party app proof
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `gl`  
**Description:** At least one unmodified third-party OpenGL application shall pass before support status becomes SUPPORTED.

**Rationale/evidence:** RF-021

**Acceptance criteria:**
- Evidence demonstrates: At least one unmodified third-party OpenGL application shall pass before support status becomes SUPPORTED.
- Required negative/failure case for GL third-party app proof is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-022
**Phases:** PHASE-030
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GPU-001 — NVIDIA host hardware acceleration
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gpu`  
**Description:** At least one NVIDIA GPU path shall use real hardware acceleration and normal host vendor stack.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: At least one NVIDIA GPU path shall use real hardware acceleration and normal host vendor stack.
- Required negative/failure case for NVIDIA host hardware acceleration is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GPU-002 — AMD host hardware acceleration
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gpu`  
**Description:** At least one AMD GPU path shall use real hardware acceleration and normal host vendor stack.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: At least one AMD GPU path shall use real hardware acceleration and normal host vendor stack.
- Required negative/failure case for AMD host hardware acceleration is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007, PHASE-034
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GPU-003 — No software-renderer success substitution
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gpu`  
**Description:** A hardware gate shall not PASS when the workload silently falls back to software rendering.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: A hardware gate shall not PASS when the workload silently falls back to software rendering.
- Required negative/failure case for No software-renderer success substitution is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GPU-004 — Physical GPU identity recorded
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gpu`  
**Description:** Evidence shall record vendor/device/driver/capability data for the remote GPU.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Evidence shall record vendor/device/driver/capability data for the remote GPU.
- Required negative/failure case for Physical GPU identity recorded is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GPU-005 — GPU reset detection
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gpu`  
**Description:** Host shall detect/reset/session-fail on physical GPU reset with explicit evidence.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Host shall detect/reset/session-fail on physical GPU reset with explicit evidence.
- Required negative/failure case for GPU reset detection is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GPU-006 — GPU capability negotiation
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gpu`  
**Description:** Ray tracing, formats, queue features and other capabilities shall be negotiated from effective backend support.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Ray tracing, formats, queue features and other capabilities shall be negotiated from effective backend support.
- Required negative/failure case for GPU capability negotiation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010, TD-013
**Gates:** GATE-003
**Phases:** PHASE-007, PHASE-034
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GPU-007 — Vendor extensions scoped
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gpu`  
**Description:** Vendor-specific optimizations shall be optional negotiated extensions.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Vendor-specific optimizations shall be optional negotiated extensions.
- Required negative/failure case for Vendor extensions scoped is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010, TD-013
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GPU-008 — Hardware ray tracing future path
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gpu`  
**Description:** Architecture shall permit real remote hardware ray tracing where API/backend support exists.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Architecture shall permit real remote hardware ray tracing where API/backend support exists.
- Required negative/failure case for Hardware ray tracing future path is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GPU-009 — Compute extension boundary
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gpu`  
**Description:** Optional future compute APIs shall use separate negotiated backend/frontend modules rather than distort graphics core.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Optional future compute APIs shall use separate negotiated backend/frontend modules rather than distort graphics core.
- Required negative/failure case for Compute extension boundary is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007, PHASE-041
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## GPU-010 — No client vendor-driver dependency baseline
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `gpu`  
**Description:** v1 shall not require stock NVIDIA/AMD Windows client driver to bind to a fake remote PCI device.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: v1 shall not require stock NVIDIA/AMD Windows client driver to bind to a fake remote PCI device.
- Required negative/failure case for No client vendor-driver dependency baseline is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## HOST-001 — Host session manager
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `host`  
**Description:** Host shall authenticate, negotiate and isolate SpanGPU sessions.

**Rationale/evidence:** RF-005, RF-018

**Acceptance criteria:**
- Evidence demonstrates: Host shall authenticate, negotiate and isolate SpanGPU sessions.
- Required negative/failure case for Host session manager is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## HOST-002 — Host command decoder
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `host`  
**Description:** Host shall decode validated API command streams into backend operations.

**Rationale/evidence:** RF-005, RF-018

**Acceptance criteria:**
- Evidence demonstrates: Host shall decode validated API command streams into backend operations.
- Required negative/failure case for Host command decoder is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## HOST-003 — Host resource manager
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `host`  
**Description:** Host shall own resource objects, metadata, residency and cache references.

**Rationale/evidence:** RF-005, RF-018

**Acceptance criteria:**
- Evidence demonstrates: Host shall own resource objects, metadata, residency and cache references.
- Required negative/failure case for Host resource manager is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## HOST-004 — Host GPU scheduler
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `host`  
**Description:** Host shall schedule session work with explicit queue ownership and extensible fairness controls.

**Rationale/evidence:** RF-005, RF-018

**Acceptance criteria:**
- Evidence demonstrates: Host shall schedule session work with explicit queue ownership and extensible fairness controls.
- Required negative/failure case for Host GPU scheduler is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## HOST-005 — Host fault containment
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `host`  
**Description:** Malformed client input or a failed session shall not corrupt unrelated sessions/host daemon state.

**Rationale/evidence:** RF-005, RF-018

**Acceptance criteria:**
- Evidence demonstrates: Malformed client input or a failed session shall not corrupt unrelated sessions/host daemon state.
- Required negative/failure case for Host fault containment is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## HOST-006 — Host restart semantics
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `host`  
**Description:** Host restart shall invalidate or recover sessions according to protocol epoch rules.

**Rationale/evidence:** RF-005, RF-018

**Acceptance criteria:**
- Evidence demonstrates: Host restart shall invalidate or recover sessions according to protocol epoch rules.
- Required negative/failure case for Host restart semantics is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## HOST-007 — Host metrics
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `host`  
**Description:** GPU utilization, queue depth, VRAM, command decode, cache, encode and errors shall be observable.

**Rationale/evidence:** RF-005, RF-018

**Acceptance criteria:**
- Evidence demonstrates: GPU utilization, queue depth, VRAM, command decode, cache, encode and errors shall be observable.
- Required negative/failure case for Host metrics is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## HOST-008 — Host one-session v1
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `host`  
**Description:** Initial host may support one active GPU session while interfaces preserve future multi-session extension.

**Rationale/evidence:** RF-005, RF-018

**Acceptance criteria:**
- Evidence demonstrates: Initial host may support one active GPU session while interfaces preserve future multi-session extension.
- Required negative/failure case for Host one-session v1 is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## HOST-009 — Host OS abstraction
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `host`  
**Description:** Stable protocol shall not expose Linux-specific file descriptors/handles as mandatory semantics.

**Rationale/evidence:** RF-005, RF-018

**Acceptance criteria:**
- Evidence demonstrates: Stable protocol shall not expose Linux-specific file descriptors/handles as mandatory semantics.
- Required negative/failure case for Host OS abstraction is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## HOST-010 — Host capability inventory
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `host`  
**Description:** Session negotiation shall derive capabilities from actual backend/vendor driver, not hardcoded GPU names.

**Rationale/evidence:** RF-005, RF-018

**Acceptance criteria:**
- Evidence demonstrates: Session negotiation shall derive capabilities from actual backend/vendor driver, not hardcoded GPU names.
- Required negative/failure case for Host capability inventory is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## HOST-011 — Host resource quotas
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `host`  
**Description:** Protocol/host design shall allow bounded VRAM/resource/command quotas for future isolation.

**Rationale/evidence:** RF-005, RF-018

**Acceptance criteria:**
- Evidence demonstrates: Protocol/host design shall allow bounded VRAM/resource/command quotas for future isolation.
- Required negative/failure case for Host resource quotas is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## HOST-012 — Host graceful drain
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `host`  
**Description:** Maintenance/restart shall support a defined drain/deny-new-session behavior.

**Rationale/evidence:** RF-005, RF-018

**Acceptance criteria:**
- Evidence demonstrates: Maintenance/restart shall support a defined drain/deny-new-session behavior.
- Required negative/failure case for Host graceful drain is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-010
**Gates:** GATE-003
**Phases:** PHASE-007
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## LAB-001 — Exclusive hardware lease
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `evals`  
**Description:** Hardware tests shall use an exclusive renewable lease so concurrent jobs cannot contaminate driver/GPU/network state.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Hardware tests shall use an exclusive renewable lease so concurrent jobs cannot contaminate driver/GPU/network state.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-032
**Gates:** GATE-000
**Phases:** PHASE-002
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## LAB-002 — Out-of-band recovery
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `evals`  
**Description:** The driver test client shall have an out-of-band or equivalent recovery path capable of power-cycle/boot recovery after a broken driver deployment.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: The driver test client shall have an out-of-band or equivalent recovery path capable of power-cycle/boot recovery after a broken driver deployment.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-032
**Gates:** GATE-000
**Phases:** PHASE-002
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## LAB-003 — Environment reset and contamination detection
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `evals`  
**Description:** Hardware runners shall validate/reset driver, service, network profile, GPU state and pending reboot state before accepting a test attempt.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Hardware runners shall validate/reset driver, service, network profile, GPU state and pending reboot state before accepting a test attempt.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-032
**Gates:** GATE-000
**Phases:** PHASE-002
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## LAB-004 — Crash artifacts survive reboot
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `evals`  
**Description:** Crash dumps, ETW/WPR traces and test metadata shall be persisted off-machine or collected automatically after reboot before cleanup.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Crash dumps, ETW/WPR traces and test metadata shall be persisted off-machine or collected automatically after reboot before cleanup.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-032
**Gates:** GATE-000
**Phases:** PHASE-002
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## LAB-005 — Flaky hardware quarantine
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `evals`  
**Description:** Repeated unexplained hardware-runner failures shall quarantine the runner and prevent it from producing acceptance evidence until requalified.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Repeated unexplained hardware-runner failures shall quarantine the runner and prevent it from producing acceptance evidence until requalified.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-032
**Gates:** GATE-026
**Phases:** PHASE-035
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## LICENSE-001 — Project license decided by evidence
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `license`  
**Description:** SpanGPU project license shall be selected only after controlled-fork/file-level compatibility review.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: SpanGPU project license shall be selected only after controlled-fork/file-level compatibility review.
- Required negative/failure case for Project license decided by evidence is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-026
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## LICENSE-002 — File-level notices preserved
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `license`  
**Description:** Copied/adapted source shall retain required copyright/license notices.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Copied/adapted source shall retain required copyright/license notices.
- Required negative/failure case for File-level notices preserved is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-026
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## LICENSE-003 — No invented license assumptions
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `license`  
**Description:** Unknown/mixed-license components shall remain reference/dependency until verified.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Unknown/mixed-license components shall remain reference/dependency until verified.
- Required negative/failure case for No invented license assumptions is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-026
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## LICENSE-004 — GPL boundary explicit
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `license`  
**Description:** GPL components such as QEMU shall remain external test/development dependencies unless an accepted licensing TD permits a different integration.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: GPL components such as QEMU shall remain external test/development dependencies unless an accepted licensing TD permits a different integration.
- Required negative/failure case for GPL boundary explicit is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-026
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## LICENSE-005 — Proprietary terms isolated
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `license`  
**Description:** Vendor/proprietary reference materials shall not be copied into distributable source unless permitted.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Vendor/proprietary reference materials shall not be copied into distributable source unless permitted.
- Required negative/failure case for Proprietary terms isolated is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-026
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## LICENSE-006 — Juice separation
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `license`  
**Description:** Juice public MIT code and separate proprietary binaries/terms shall be treated distinctly; proprietary data plane shall not enter core.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Juice public MIT code and separate proprietary binaries/terms shall be treated distinctly; proprietary data plane shall not enter core.
- Required negative/failure case for Juice separation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-026
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## LICENSE-007 — License manifest
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `license`  
**Description:** Used dependencies/forks shall have machine-readable license metadata and source URL.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Used dependencies/forks shall have machine-readable license metadata and source URL.
- Required negative/failure case for License manifest is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-026
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## LICENSE-008 — License changes reviewed
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `license`  
**Description:** Upstream license or notice changes shall require explicit adoption review.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Upstream license or notice changes shall require explicit adoption review.
- Required negative/failure case for License changes reviewed is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-026
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## LICENSE-009 — Distribution obligations tested
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `license`  
**Description:** Release checklist shall validate required notices/source/offers where applicable.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Release checklist shall validate required notices/source/offers where applicable.
- Required negative/failure case for Distribution obligations tested is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-026
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## LICENSE-010 — No proprietary source redistribution
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `license`  
**Description:** BuilderKit and repositories shall not include proprietary vendor source or binaries without explicit redistribution rights.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: BuilderKit and repositories shall not include proprietary vendor source or binaries without explicit redistribution rights.
- Required negative/failure case for No proprietary source redistribution is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-026
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## MEM-001 — Client shadow state non-authoritative
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `mem`  
**Description:** Local resource shadows/cache metadata shall be explicitly non-authoritative unless a TD identifies a local-owned class.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: Local resource shadows/cache metadata shall be explicitly non-authoritative unless a TD identifies a local-owned class.
- Required negative/failure case for Client shadow state non-authoritative is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## MEM-002 — Staging buffers explicit
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `mem`  
**Description:** CPU-visible staging resources shall have clear ownership and transfer completion semantics.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: CPU-visible staging resources shall have clear ownership and transfer completion semantics.
- Required negative/failure case for Staging buffers explicit is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## MEM-003 — Memory coherence policy documented
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `mem`  
**Description:** Each memory/resource class shall state coherence, visibility and invalidation rules.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: Each memory/resource class shall state coherence, visibility and invalidation rules.
- Required negative/failure case for Memory coherence policy documented is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## MEM-004 — Dirty-range tracking
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `mem`  
**Description:** Mutable upload paths shall support tracking changed ranges where beneficial without weakening correctness.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: Mutable upload paths shall support tracking changed ranges where beneficial without weakening correctness.
- Required negative/failure case for Dirty-range tracking is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## MEM-005 — Read-modify-write ordering
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `mem`  
**Description:** Partial updates shall preserve API-visible ordering against GPU use.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: Partial updates shall preserve API-visible ordering against GPU use.
- Required negative/failure case for Read-modify-write ordering is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## MEM-006 — Memory pressure behavior
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `mem`  
**Description:** Client and host memory pressure shall produce bounded eviction/backpressure rather than silent corruption.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: Client and host memory pressure shall produce bounded eviction/backpressure rather than silent corruption.
- Required negative/failure case for Memory pressure behavior is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## MEM-007 — Allocation size validation
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `mem`  
**Description:** Protocol shall validate sizes/offsets/alignments before host allocation/use.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: Protocol shall validate sizes/offsets/alignments before host allocation/use.
- Required negative/failure case for Allocation size validation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## MEM-008 — Integer overflow hardening
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `mem`  
**Description:** All cross-boundary size/range calculations shall be overflow-safe and fuzz-tested.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: All cross-boundary size/range calculations shall be overflow-safe and fuzz-tested.
- Required negative/failure case for Integer overflow hardening is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## MEM-009 — No cross-session resource confusion
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `mem`  
**Description:** Resource IDs shall include enough session/epoch context to reject stale/cross-session references.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: Resource IDs shall include enough session/epoch context to reject stale/cross-session references.
- Required negative/failure case for No cross-session resource confusion is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## MEM-010 — Zero-copy is optional optimization
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `mem`  
**Description:** No correctness requirement shall depend on zero-copy across WAN.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: No correctness requirement shall depend on zero-copy across WAN.
- Required negative/failure case for Zero-copy is optional optimization is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## MULTIGPU-001 — Local adapter coexistence
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `multigpu`  
**Description:** Local GPU and SpanGPU shall coexist without adapter enumeration conflicts.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Local GPU and SpanGPU shall coexist without adapter enumeration conflicts.
- Required negative/failure case for Local adapter coexistence is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-011
**Gates:** GATE-012
**Phases:** PHASE-028, PHASE-013
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## MULTIGPU-002 — Explicit workload adapter selection
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `multigpu`  
**Description:** Tests shall verify normal Windows/application adapter preference mechanisms where supported.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Tests shall verify normal Windows/application adapter preference mechanisms where supported.
- Required negative/failure case for Explicit workload adapter selection is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-011
**Gates:** GATE-012
**Phases:** PHASE-028
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## MULTIGPU-003 — No transparent mid-frame failover claim
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `multigpu`  
**Description:** Architecture shall not promise live adapter migration/failover unless an API-specific proof exists.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Architecture shall not promise live adapter migration/failover unless an API-specific proof exists.
- Required negative/failure case for No transparent mid-frame failover claim is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-011
**Gates:** GATE-012
**Phases:** PHASE-028
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## MULTIGPU-004 — Fallback semantics documented
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `multigpu`  
**Description:** If remote device is lost, fallback may require application restart; behavior shall be truthful and deterministic.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: If remote device is lost, fallback may require application restart; behavior shall be truthful and deterministic.
- Required negative/failure case for Fallback semantics documented is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-011
**Gates:** GATE-012
**Phases:** PHASE-028
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## MULTIGPU-005 — Remote multi-GPU extensible
**Priority:** `SHOULD`  
**Horizon:** `later`  
**Component:** `multigpu`  
**Description:** Protocol shall allow multiple remote GPU offers/capability sets later without changing identity model.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Protocol shall allow multiple remote GPU offers/capability sets later without changing identity model.
- Required negative/failure case for Remote multi-GPU extensible is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-011
**Gates:** GATE-012
**Phases:** PHASE-028
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## MULTIGPU-006 — Host GPU selection explicit
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `multigpu`  
**Description:** Session shall bind to an authoritative selected host GPU/backend identity.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Session shall bind to an authoritative selected host GPU/backend identity.
- Required negative/failure case for Host GPU selection explicit is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-011
**Gates:** GATE-012
**Phases:** PHASE-028
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## MULTIGPU-007 — Cross-GPU resource copies explicit
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `multigpu`  
**Description:** Any local↔remote or remote↔remote GPU transfer shall have explicit synchronization/ownership.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Any local↔remote or remote↔remote GPU transfer shall have explicit synchronization/ownership.
- Required negative/failure case for Cross-GPU resource copies explicit is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-011
**Gates:** GATE-012
**Phases:** PHASE-028
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## MULTIGPU-008 — Mixed-vendor evidence
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `multigpu`  
**Description:** Compatibility evidence shall record local and remote vendor combination.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Compatibility evidence shall record local and remote vendor combination.
- Required negative/failure case for Mixed-vendor evidence is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-011
**Gates:** GATE-012
**Phases:** PHASE-028, PHASE-034
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OBS-001 — End-to-end correlation
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `obs`  
**Description:** Client KMD/service, transport and host logs shall share session/attempt/correlation identifiers.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Client KMD/service, transport and host logs shall share session/attempt/correlation identifiers.
- Required negative/failure case for End-to-end correlation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OBS-002 — Structured logs
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `obs`  
**Description:** Machine-relevant events shall be emitted as structured data with stable event IDs.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Machine-relevant events shall be emitted as structured data with stable event IDs.
- Required negative/failure case for Structured logs is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OBS-003 — No log-only correctness oracle
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `obs`  
**Description:** Logs support diagnosis but PASS requires explicit test assertions/evidence.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Logs support diagnosis but PASS requires explicit test assertions/evidence.
- Required negative/failure case for No log-only correctness oracle is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OBS-004 — Command batch metrics
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `obs`  
**Description:** Batch size, command count and queue assignment shall be observable without logging sensitive payloads.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Batch size, command count and queue assignment shall be observable without logging sensitive payloads.
- Required negative/failure case for Command batch metrics is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OBS-005 — Resource metrics
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `obs`  
**Description:** Create/upload/readback/cache/evict bytes and counts shall be observable.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Create/upload/readback/cache/evict bytes and counts shall be observable.
- Required negative/failure case for Resource metrics is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OBS-006 — Network metrics
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `obs`  
**Description:** RTT, congestion, loss/retransmit and throughput shall be observable.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: RTT, congestion, loss/retransmit and throughput shall be observable.
- Required negative/failure case for Network metrics is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OBS-007 — Device-loss timeline
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `obs`  
**Description:** Failures shall produce a timestamped state-transition timeline.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Failures shall produce a timestamped state-transition timeline.
- Required negative/failure case for Device-loss timeline is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OBS-008 — TDR/crash linkage
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `obs`  
**Description:** Windows crash/TDR artifacts shall include the SpanGPU attempt/evidence identifiers where possible.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Windows crash/TDR artifacts shall include the SpanGPU attempt/evidence identifiers where possible.
- Required negative/failure case for TDR/crash linkage is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OBS-009 — Evidence retention policy
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `obs`  
**Description:** Gate/release evidence retention shall be defined and separated from transient developer logs.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Gate/release evidence retention shall be defined and separated from transient developer logs.
- Required negative/failure case for Evidence retention policy is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OBS-010 — Telemetry versioning
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `obs`  
**Description:** Telemetry schema shall be versioned independently from protocol where appropriate.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Telemetry schema shall be versioned independently from protocol where appropriate.
- Required negative/failure case for Telemetry versioning is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OBS-011 — Performance counter overhead bounded
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `obs`  
**Description:** Instrumentation overhead shall be measured and configurable without removing mandatory correctness evidence.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Instrumentation overhead shall be measured and configurable without removing mandatory correctness evidence.
- Required negative/failure case for Performance counter overhead bounded is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OPS-001 — Client service lifecycle
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `ops`  
**Description:** Install/start/stop/update behavior for client service shall be deterministic and observable.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Install/start/stop/update behavior for client service shall be deterministic and observable.
- Required negative/failure case for Client service lifecycle is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-002
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OPS-002 — Host daemon lifecycle
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `ops`  
**Description:** Host daemon shall support deterministic startup, health check, drain and shutdown.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Host daemon shall support deterministic startup, health check, drain and shutdown.
- Required negative/failure case for Host daemon lifecycle is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-002
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OPS-003 — Health endpoints
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `ops`  
**Description:** Client/host shall expose bounded health/status diagnostics separate from correctness PASS.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Client/host shall expose bounded health/status diagnostics separate from correctness PASS.
- Required negative/failure case for Health endpoints is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-002
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OPS-004 — Safe driver deployment workflow
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `ops`  
**Description:** Driver deployment automation shall default dry-run and require explicit apply/confirmation on designated test machines.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Driver deployment automation shall default dry-run and require explicit apply/confirmation on designated test machines.
- Required negative/failure case for Safe driver deployment workflow is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-002
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OPS-005 — Automated rollback guard
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `ops`  
**Description:** Test machines shall have a recovery route after failed driver deployment or boot.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Test machines shall have a recovery route after failed driver deployment or boot.
- Required negative/failure case for Automated rollback guard is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-002
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OPS-006 — No destructive default
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `ops`  
**Description:** Bootstrap/maintenance scripts shall default to non-destructive dry-run.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Bootstrap/maintenance scripts shall default to non-destructive dry-run.
- Required negative/failure case for No destructive default is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-002
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OPS-007 — Evidence storage layout
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `ops`  
**Description:** Logs/traces/dumps/benchmarks/gate reports shall have deterministic attempt-scoped storage paths.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Logs/traces/dumps/benchmarks/gate reports shall have deterministic attempt-scoped storage paths.
- Required negative/failure case for Evidence storage layout is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-002
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OPS-008 — Host GPU inventory
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `ops`  
**Description:** Operations shall report detected GPU/vendor/driver capabilities before allocating a session.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Operations shall report detected GPU/vendor/driver capabilities before allocating a session.
- Required negative/failure case for Host GPU inventory is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-002
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OPS-009 — Network profile tooling
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `ops`  
**Description:** WAN emulation profiles shall be scripted and revertible.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: WAN emulation profiles shall be scripted and revertible.
- Required negative/failure case for Network profile tooling is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-002
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OPS-010 — Time synchronization awareness
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `ops`  
**Description:** Evidence timestamps shall record clock source/offset assumptions for cross-machine latency analysis.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Evidence timestamps shall record clock source/offset assumptions for cross-machine latency analysis.
- Required negative/failure case for Time synchronization awareness is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-002
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OPS-011 — Release rollback
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `ops`  
**Description:** Published client/host versions shall have documented rollback/compatibility behavior.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Published client/host versions shall have documented rollback/compatibility behavior.
- Required negative/failure case for Release rollback is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-002
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## OPS-012 — No cloud control-plane dependency
**Priority:** `SHOULD`  
**Horizon:** `v0/proof`  
**Component:** `ops`  
**Description:** Core client↔host operation shall be possible without a proprietary SpanGPU cloud marketplace/control service.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Core client↔host operation shall be possible without a proprietary SpanGPU cloud marketplace/control service.
- Required negative/failure case for No cloud control-plane dependency is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-002
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PERF-001 — Frame-time measurement
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `perf`  
**Description:** Every performance gate shall capture CPU frame time, remote GPU time and end-to-end present latency where measurable.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Every performance gate shall capture CPU frame time, remote GPU time and end-to-end present latency where measurable.
- Required negative/failure case for Frame-time measurement is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PERF-002 — Bytes per frame
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `perf`  
**Description:** Transport telemetry shall report command/resource/frame-return bytes per frame or interval.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Transport telemetry shall report command/resource/frame-return bytes per frame or interval.
- Required negative/failure case for Bytes per frame is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PERF-003 — RTT-sensitive operation count
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `perf`  
**Description:** Instrumentation shall count and classify operations that induce synchronous network waits.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Instrumentation shall count and classify operations that induce synchronous network waits.
- Required negative/failure case for RTT-sensitive operation count is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020, PHASE-021
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PERF-004 — Cache hit rate
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `perf`  
**Description:** Performance tests shall measure cache hit/miss and avoided upload volume.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Performance tests shall measure cache hit/miss and avoided upload volume.
- Required negative/failure case for Cache hit rate is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PERF-005 — Queue depth
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `perf`  
**Description:** Client and host command/resource queue depths shall be measurable to diagnose backpressure.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Client and host command/resource queue depths shall be measurable to diagnose backpressure.
- Required negative/failure case for Queue depth is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PERF-006 — Fence latency
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `perf`  
**Description:** Submission-to-completion and wait latency shall be measured by queue/fence.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Submission-to-completion and wait latency shall be measured by queue/fence.
- Required negative/failure case for Fence latency is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PERF-007 — CPU overhead
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `perf`  
**Description:** Client service/UMD/KMD and host decode CPU overhead shall be measured.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Client service/UMD/KMD and host decode CPU overhead shall be measured.
- Required negative/failure case for CPU overhead is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PERF-008 — GPU utilization
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `perf`  
**Description:** Remote physical GPU utilization shall be captured to distinguish network/CPU bottlenecks.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Remote physical GPU utilization shall be captured to distinguish network/CPU bottlenecks.
- Required negative/failure case for GPU utilization is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PERF-009 — No benchmark-only semantics
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `perf`  
**Description:** Optimizations shall not special-case benchmark names/workloads in ways unavailable to normal applications.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Optimizations shall not special-case benchmark names/workloads in ways unavailable to normal applications.
- Required negative/failure case for No benchmark-only semantics is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PERF-010 — Performance regression thresholds
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `perf`  
**Description:** Stable benchmark cases shall define alert thresholds and require investigation for material regressions.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Stable benchmark cases shall define alert thresholds and require investigation for material regressions.
- Required negative/failure case for Performance regression thresholds is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PERF-011 — Correctness gate before perf acceptance
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `perf`  
**Description:** A faster result with failed correctness/graphics validation shall never count as performance success.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: A faster result with failed correctness/graphics validation shall never count as performance success.
- Required negative/failure case for Correctness gate before perf acceptance is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PERF-012 — Latency tier publication
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `perf`  
**Description:** Published WAN performance expectations shall name RTT/bandwidth/hardware/workload, not claim one universal FPS.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Published WAN performance expectations shall name RTT/bandwidth/hardware/workload, not claim one universal FPS.
- Required negative/failure case for Latency tier publication is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020, PHASE-022, PHASE-023
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PERF-013 — Frame-return codec cost measured
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `perf`  
**Description:** Encoding/decoding and copy latency shall be reported separately from GPU execution.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Encoding/decoding and copy latency shall be reported separately from GPU execution.
- Required negative/failure case for Frame-return codec cost measured is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PERF-014 — Startup/resource warmup measured
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `perf`  
**Description:** Cold and warm cache startup behavior shall be separately benchmarked.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Cold and warm cache startup behavior shall be separately benchmarked.
- Required negative/failure case for Startup/resource warmup measured is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-018
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PROTO-001 — Protocol major/minor versioning
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `proto`  
**Description:** Every cross-machine protocol message shall be interpreted under a negotiated protocol version and feature set.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Every cross-machine protocol message shall be interpreted under a negotiated protocol version and feature set.
- Required negative/failure case for Protocol major/minor versioning is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-019
**Gates:** GATE-003
**Phases:** PHASE-008, PHASE-006
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PROTO-002 — Fail-closed incompatible major version
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `proto`  
**Description:** Client and host with incompatible mandatory major versions shall refuse session establishment with explicit diagnostics.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Client and host with incompatible mandatory major versions shall refuse session establishment with explicit diagnostics.
- Required negative/failure case for Fail-closed incompatible major version is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-019
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PROTO-003 — Control/data separation
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `proto`  
**Description:** Control/session messages shall be logically separable from high-volume command/resource/frame data.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Control/session messages shall be logically separable from high-volume command/resource/frame data.
- Required negative/failure case for Control/data separation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-019
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PROTO-004 — Command/resource separation
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `proto`  
**Description:** Graphics commands and resource payloads shall use independent flow-control paths to avoid bulk-transfer head-of-line blocking.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Graphics commands and resource payloads shall use independent flow-control paths to avoid bulk-transfer head-of-line blocking.
- Required negative/failure case for Command/resource separation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-019
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PROTO-005 — Fence/completion priority
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `proto`  
**Description:** Completion/fence notifications shall have a latency-prioritized path independent of bulk resource uploads.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Completion/fence notifications shall have a latency-prioritized path independent of bulk resource uploads.
- Required negative/failure case for Fence/completion priority is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-019
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PROTO-006 — Message length validation
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `proto`  
**Description:** Every message shall include validated bounded lengths before allocation or parsing.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Every message shall include validated bounded lengths before allocation or parsing.
- Required negative/failure case for Message length validation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-019
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PROTO-007 — Unknown optional message handling
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `proto`  
**Description:** Unknown optional extensions shall be safely ignorable/rejectable according to negotiated feature rules.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Unknown optional extensions shall be safely ignorable/rejectable according to negotiated feature rules.
- Required negative/failure case for Unknown optional message handling is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-019
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PROTO-008 — Unknown mandatory message rejection
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `proto`  
**Description:** Unknown mandatory semantics shall fail the session rather than being guessed.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Unknown mandatory semantics shall fail the session rather than being guessed.
- Required negative/failure case for Unknown mandatory message rejection is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-019
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PROTO-009 — Correlation IDs
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `proto`  
**Description:** Requests, batches, resources, completions and errors shall carry correlation identifiers sufficient for end-to-end evidence.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Requests, batches, resources, completions and errors shall carry correlation identifiers sufficient for end-to-end evidence.
- Required negative/failure case for Correlation IDs is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-019
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PROTO-010 — Session epoch
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `proto`  
**Description:** Every protocol session shall have an epoch/attempt identifier used to reject stale messages after reconnect.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Every protocol session shall have an epoch/attempt identifier used to reject stale messages after reconnect.
- Required negative/failure case for Session epoch is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-019
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PROTO-011 — Idempotency metadata
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `proto`  
**Description:** Retryable state mutations shall have explicit idempotency keys or monotonic sequence semantics.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Retryable state mutations shall have explicit idempotency keys or monotonic sequence semantics.
- Required negative/failure case for Idempotency metadata is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-019
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PROTO-012 — Protocol schemas machine-readable
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `proto`  
**Description:** Stable protocol envelopes/capability schemas shall have machine-readable definitions and compatibility tests.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Stable protocol envelopes/capability schemas shall have machine-readable definitions and compatibility tests.
- Required negative/failure case for Protocol schemas machine-readable is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-019
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## PROTO-013 — Allowed/required/observed capabilities separate
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `proto`  
**Description:** Negotiation schemas shall represent capabilities allowed by implementation, required by peer/workload and actually negotiated as distinct sets.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Negotiation schemas shall represent capabilities allowed by implementation, required by peer/workload and actually negotiated as distinct sets.
- Required negative/failure case for Allowed/required/observed capabilities separate is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-019
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## RECOVERY-001 — Unique attempt IDs
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `recovery`  
**Description:** Every gate/session/recovery attempt shall receive a unique immutable attempt ID.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Every gate/session/recovery attempt shall receive a unique immutable attempt ID.
- Required negative/failure case for Unique attempt IDs is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-017
**Gates:** GATE-018
**Phases:** PHASE-025, PHASE-027
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## RECOVERY-002 — Recovery epoch changes
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `recovery`  
**Description:** A successful reconnect/recovery shall use a new session/recovery epoch unless protocol proves state continuity.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: A successful reconnect/recovery shall use a new session/recovery epoch unless protocol proves state continuity.
- Required negative/failure case for Recovery epoch changes is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-017
**Gates:** GATE-018
**Phases:** PHASE-025, PHASE-027
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## RECOVERY-003 — No stale counter carryover
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `recovery`  
**Description:** Retry counters/state from prior attempts shall not silently satisfy current attempt requirements.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Retry counters/state from prior attempts shall not silently satisfy current attempt requirements.
- Required negative/failure case for No stale counter carryover is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-017
**Gates:** GATE-018
**Phases:** PHASE-025
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## RECOVERY-004 — Historical evidence immutable
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `recovery`  
**Description:** Prior failure/success evidence shall remain immutable and separately addressable.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Prior failure/success evidence shall remain immutable and separately addressable.
- Required negative/failure case for Historical evidence immutable is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-017
**Gates:** GATE-018
**Phases:** PHASE-025
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## RECOVERY-005 — Recovery baseline provenance
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `recovery`  
**Description:** Recovery shall record exactly which commit/config/protocol/resource baseline it used.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Recovery shall record exactly which commit/config/protocol/resource baseline it used.
- Required negative/failure case for Recovery baseline provenance is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-017
**Gates:** GATE-018
**Phases:** PHASE-025
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## RECOVERY-006 — Ambiguous completion resolved
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `recovery`  
**Description:** Operations whose remote completion is unknown at disconnect shall be classified and resolved by idempotency/reconciliation rules.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Operations whose remote completion is unknown at disconnect shall be classified and resolved by idempotency/reconciliation rules.
- Required negative/failure case for Ambiguous completion resolved is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-017
**Gates:** GATE-018
**Phases:** PHASE-025, PHASE-027
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## RECOVERY-007 — Controlled device loss fallback
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `recovery`  
**Description:** When safe recovery is impossible, client shall expose controlled device loss and require restart rather than guess state.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: When safe recovery is impossible, client shall expose controlled device loss and require restart rather than guess state.
- Required negative/failure case for Controlled device loss fallback is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-017
**Gates:** GATE-018
**Phases:** PHASE-025, PHASE-026
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## RECOVERY-008 — Resource revalidation
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `recovery`  
**Description:** Recovered sessions shall revalidate authoritative resource/cache state before reuse.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Recovered sessions shall revalidate authoritative resource/cache state before reuse.
- Required negative/failure case for Resource revalidation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-017
**Gates:** GATE-018
**Phases:** PHASE-025, PHASE-027
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## RECOVERY-009 — Recovery timeout bounded
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `recovery`  
**Description:** Recovery attempts shall have bounded timeout/cancellation semantics.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Recovery attempts shall have bounded timeout/cancellation semantics.
- Required negative/failure case for Recovery timeout bounded is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-017
**Gates:** GATE-018
**Phases:** PHASE-025
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## RECOVERY-010 — Recovery loop bounded
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `recovery`  
**Description:** Automation shall prevent infinite reconnect/recovery loops.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Automation shall prevent infinite reconnect/recovery loops.
- Required negative/failure case for Recovery loop bounded is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-017
**Gates:** GATE-018
**Phases:** PHASE-025
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## RECOVERY-011 — Crash evidence before rollback
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `recovery`  
**Description:** Driver/service failures shall capture diagnostics before automated rollback when possible.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Driver/service failures shall capture diagnostics before automated rollback when possible.
- Required negative/failure case for Crash evidence before rollback is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-017
**Gates:** GATE-018
**Phases:** PHASE-025, PHASE-026
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## RECOVERY-012 — Recovery regression suite
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `recovery`  
**Description:** Every confirmed recovery defect shall become a deterministic or stress/fault regression test.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Every confirmed recovery defect shall become a deterministic or stress/fault regression test.
- Required negative/failure case for Recovery regression suite is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-017
**Gates:** GATE-018
**Phases:** PHASE-025
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## RELEASE-001 — Development and production signing separation
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `release`  
**Description:** Test signing/development credentials and production release signing identities/keys shall be isolated by policy and tooling.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Test signing/development credentials and production release signing identities/keys shall be isolated by policy and tooling.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-033
**Gates:** GATE-028
**Phases:** PHASE-037
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## RELEASE-002 — Release evidence bundle
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `release`  
**Description:** Every public driver/runtime release shall bind source commit, reproducible build provenance, SBOM, license manifest, test/gate evidence, signatures and compatibility metadata.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Every public driver/runtime release shall bind source commit, reproducible build provenance, SBOM, license manifest, test/gate evidence, signatures and compatibility metadata.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-034
**Gates:** GATE-028
**Phases:** PHASE-042
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## RELEASE-003 — Protocol compatibility window
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `release`  
**Description:** Every release shall state supported client/host protocol version ranges and rollback compatibility.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Every release shall state supported client/host protocol version ranges and rollback compatibility.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-034
**Gates:** GATE-028
**Phases:** PHASE-042
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## RELEASE-004 — Staged release and rollback
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `release`  
**Description:** Public releases shall support staged rollout, explicit rollback and revocation/withdrawal procedures for unsafe driver/runtime builds.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Public releases shall support staged rollout, explicit rollback and revocation/withdrawal procedures for unsafe driver/runtime builds.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-034
**Gates:** GATE-028
**Phases:** PHASE-042
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## SEC-001 — Authenticated client identity
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sec`  
**Description:** Host shall authenticate the client/service identity before granting GPU session access.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Host shall authenticate the client/service identity before granting GPU session access.
- Required negative/failure case for Authenticated client identity is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-027
**Phases:** PHASE-036
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SEC-002 — Authenticated host identity
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sec`  
**Description:** Client shall authenticate the intended SpanGPU host before transmitting resource/command data.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Client shall authenticate the intended SpanGPU host before transmitting resource/command data.
- Required negative/failure case for Authenticated host identity is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-027
**Phases:** PHASE-036
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SEC-003 — Encryption in transit
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sec`  
**Description:** All WAN control/command/resource/completion channels shall use approved authenticated encryption.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: All WAN control/command/resource/completion channels shall use approved authenticated encryption.
- Required negative/failure case for Encryption in transit is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-027
**Phases:** PHASE-036
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SEC-004 — Replay resistance
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sec`  
**Description:** Session protocol shall reject replayed control and mutation messages across epochs.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Session protocol shall reject replayed control and mutation messages across epochs.
- Required negative/failure case for Replay resistance is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-027
**Phases:** PHASE-036
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SEC-005 — Parser hardening
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sec`  
**Description:** All network-facing decoders shall validate bounds, enums, counts, nesting and resource references before use.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: All network-facing decoders shall validate bounds, enums, counts, nesting and resource references before use.
- Required negative/failure case for Parser hardening is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-027
**Phases:** PHASE-036
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SEC-006 — Least privilege services
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sec`  
**Description:** Client and host user-mode services shall run with the minimum privileges required for their responsibilities.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Client and host user-mode services shall run with the minimum privileges required for their responsibilities.
- Required negative/failure case for Least privilege services is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-027
**Phases:** PHASE-036
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SEC-007 — Kernel input minimization
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sec`  
**Description:** KMD-facing input from user/network components shall be narrowly typed, bounded and validated.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: KMD-facing input from user/network components shall be narrowly typed, bounded and validated.
- Required negative/failure case for Kernel input minimization is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-027
**Phases:** PHASE-036
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SEC-008 — Session isolation
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sec`  
**Description:** One session shall not access resources, cache entries or telemetry belonging to another unauthorized session.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: One session shall not access resources, cache entries or telemetry belonging to another unauthorized session.
- Required negative/failure case for Session isolation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-027
**Phases:** PHASE-036
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SEC-009 — Resource quota enforcement
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sec`  
**Description:** Host shall support enforceable bounds for resource count, memory size, command size and outstanding work.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Host shall support enforceable bounds for resource count, memory size, command size and outstanding work.
- Required negative/failure case for Resource quota enforcement is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-027
**Phases:** PHASE-036
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SEC-010 — Fuzz mandatory decoders
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sec`  
**Description:** Protocol, capability, resource and command envelope decoders shall have continuous fuzz coverage.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Protocol, capability, resource and command envelope decoders shall have continuous fuzz coverage.
- Required negative/failure case for Fuzz mandatory decoders is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-027
**Phases:** PHASE-036
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SEC-011 — Security event evidence
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sec`  
**Description:** Authentication failures, malformed input and policy denials shall produce structured security evidence without secrets.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Authentication failures, malformed input and policy denials shall produce structured security evidence without secrets.
- Required negative/failure case for Security event evidence is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-027
**Phases:** PHASE-036
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SEC-012 — No secret logging
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sec`  
**Description:** Logs/evidence bundles shall redact credentials, private keys and session secrets.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Logs/evidence bundles shall redact credentials, private keys and session secrets.
- Required negative/failure case for No secret logging is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-027
**Phases:** PHASE-036
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SEC-013 — Dependency vulnerability monitoring
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sec`  
**Description:** Runtime and controlled-fork dependencies shall be monitored for known security issues with risk-based adoption.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Runtime and controlled-fork dependencies shall be monitored for known security issues with risk-based adoption.
- Required negative/failure case for Dependency vulnerability monitoring is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-027
**Phases:** PHASE-036
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SEC-014 — Secure update provenance
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sec`  
**Description:** Release artifacts shall be traceable to source commit, build workflow and signing identity.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Release artifacts shall be traceable to source commit, build workflow and signing identity.
- Required negative/failure case for Secure update provenance is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-027
**Phases:** PHASE-036
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SOURCE-001 — Canonical machine-readable governance source
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** Requirements, TDs, gates, phases, risks, upstreams and repository contracts shall each have one canonical machine-readable source; Markdown views are generated or validated projections.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Requirements, TDs, gates, phases, risks, upstreams and repository contracts shall each have one canonical machine-readable source; Markdown views are generated or validated projections.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-029
**Gates:** GATE-BK-000
**Phases:** PHASE-000
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## SOURCE-002 — Generated-view drift detection
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** CI shall fail when generated Markdown/JSON views differ from the canonical governance source.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: CI shall fail when generated Markdown/JSON views differ from the canonical governance source.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-029
**Gates:** GATE-BK-000
**Phases:** PHASE-000
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## SYNC-001 — Per-queue ordering
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sync`  
**Description:** Commands in a graphics queue shall preserve required order without imposing unrelated global ordering.

**Rationale/evidence:** RF-023, RF-002

**Acceptance criteria:**
- Evidence demonstrates: Commands in a graphics queue shall preserve required order without imposing unrelated global ordering.
- Required negative/failure case for Per-queue ordering is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-008
**Gates:** GATE-009
**Phases:** PHASE-018
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SYNC-002 — Virtual fence identity
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sync`  
**Description:** Client-visible synchronization objects shall map to epoch-scoped remote identities.

**Rationale/evidence:** RF-023, RF-002

**Acceptance criteria:**
- Evidence demonstrates: Client-visible synchronization objects shall map to epoch-scoped remote identities.
- Required negative/failure case for Virtual fence identity is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-008
**Gates:** GATE-009
**Phases:** PHASE-018
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SYNC-003 — Asynchronous completion
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sync`  
**Description:** Completion notifications shall flow asynchronously and update local shadow state without blocking unrelated work.

**Rationale/evidence:** RF-023, RF-002

**Acceptance criteria:**
- Evidence demonstrates: Completion notifications shall flow asynchronously and update local shadow state without blocking unrelated work.
- Required negative/failure case for Asynchronous completion is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-008
**Gates:** GATE-009
**Phases:** PHASE-018
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SYNC-004 — Semantic wait only
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sync`  
**Description:** A WAN blocking wait shall occur only when application/API semantics require observation of completion/data.

**Rationale/evidence:** RF-023, RF-002

**Acceptance criteria:**
- Evidence demonstrates: A WAN blocking wait shall occur only when application/API semantics require observation of completion/data.
- Required negative/failure case for Semantic wait only is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-008
**Gates:** GATE-009
**Phases:** PHASE-018
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SYNC-005 — Timeline monotonicity
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sync`  
**Description:** Timeline/fence values shall never regress or be reused ambiguously within an epoch.

**Rationale/evidence:** RF-023, RF-002

**Acceptance criteria:**
- Evidence demonstrates: Timeline/fence values shall never regress or be reused ambiguously within an epoch.
- Required negative/failure case for Timeline monotonicity is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-008
**Gates:** GATE-009
**Phases:** PHASE-018
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SYNC-006 — Duplicate completion safe
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sync`  
**Description:** Duplicate/retransmitted completion messages shall be idempotent.

**Rationale/evidence:** RF-023, RF-002

**Acceptance criteria:**
- Evidence demonstrates: Duplicate/retransmitted completion messages shall be idempotent.
- Required negative/failure case for Duplicate completion safe is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-008
**Gates:** GATE-009
**Phases:** PHASE-018
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SYNC-007 — Stale completion rejected
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sync`  
**Description:** Completions from an old session/recovery epoch shall be rejected.

**Rationale/evidence:** RF-023, RF-002

**Acceptance criteria:**
- Evidence demonstrates: Completions from an old session/recovery epoch shall be rejected.
- Required negative/failure case for Stale completion rejected is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-008
**Gates:** GATE-009
**Phases:** PHASE-018
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SYNC-008 — Cross-queue dependencies explicit
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sync`  
**Description:** Cross-queue synchronization shall be encoded as explicit dependency edges.

**Rationale/evidence:** RF-023, RF-002

**Acceptance criteria:**
- Evidence demonstrates: Cross-queue synchronization shall be encoded as explicit dependency edges.
- Required negative/failure case for Cross-queue dependencies explicit is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-008
**Gates:** GATE-009
**Phases:** PHASE-018
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SYNC-009 — Fence timeout diagnostic
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sync`  
**Description:** Timeouts shall identify queue/fence/correlation state and network/host context.

**Rationale/evidence:** RF-023, RF-002

**Acceptance criteria:**
- Evidence demonstrates: Timeouts shall identify queue/fence/correlation state and network/host context.
- Required negative/failure case for Fence timeout diagnostic is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-008
**Gates:** GATE-009
**Phases:** PHASE-018
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SYNC-010 — Synchronization stress tests
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sync`  
**Description:** Randomized dependency graphs, multi-threaded submits and fault injection shall test ordering.

**Rationale/evidence:** RF-023, RF-002

**Acceptance criteria:**
- Evidence demonstrates: Randomized dependency graphs, multi-threaded submits and fault injection shall test ordering.
- Required negative/failure case for Synchronization stress tests is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-008
**Gates:** GATE-009
**Phases:** PHASE-018
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SYNC-011 — No optimistic success
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sync`  
**Description:** Local fence completion shall never be signaled before the authoritative completion condition is satisfied.

**Rationale/evidence:** RF-023, RF-002

**Acceptance criteria:**
- Evidence demonstrates: Local fence completion shall never be signaled before the authoritative completion condition is satisfied.
- Required negative/failure case for No optimistic success is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-008
**Gates:** GATE-009
**Phases:** PHASE-018
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## SYNC-012 — Recovery fence policy
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `sync`  
**Description:** On device loss/reconnect, outstanding fence states shall follow documented fail/rebuild rules rather than silent reuse.

**Rationale/evidence:** RF-023, RF-002

**Acceptance criteria:**
- Evidence demonstrates: On device loss/reconnect, outstanding fence states shall follow documented fail/rebuild rules rather than silent reuse.
- Required negative/failure case for Recovery fence policy is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-008
**Gates:** GATE-009
**Phases:** PHASE-018
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TEST-001 — Unit tests
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `test`  
**Description:** Pure resource/protocol/cache/state components shall have deterministic unit tests.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Pure resource/protocol/cache/state components shall have deterministic unit tests.
- Required negative/failure case for Unit tests is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TEST-002 — Contract tests
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `test`  
**Description:** Stable component and cross-repo interfaces shall have producer/consumer contract tests.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Stable component and cross-repo interfaces shall have producer/consumer contract tests.
- Required negative/failure case for Contract tests is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TEST-003 — Protocol roundtrip tests
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `test`  
**Description:** Encode/decode/version/capability negotiation shall have deterministic roundtrip/negative tests.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Encode/decode/version/capability negotiation shall have deterministic roundtrip/negative tests.
- Required negative/failure case for Protocol roundtrip tests is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TEST-004 — Property tests
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `test`  
**Description:** Resource/fence/state machines shall use property-based tests for invariants and generated sequences.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Resource/fence/state machines shall use property-based tests for invariants and generated sequences.
- Required negative/failure case for Property tests is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TEST-005 — Fuzz tests
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `test`  
**Description:** Untrusted decoders and parsers shall be fuzzed continuously.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Untrusted decoders and parsers shall be fuzzed continuously.
- Required negative/failure case for Fuzz tests is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TEST-006 — Driver tests
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `test`  
**Description:** Adapter/allocation/submission/device-loss driver behavior shall be tested on isolated Windows runners.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Adapter/allocation/submission/device-loss driver behavior shall be tested on isolated Windows runners.
- Required negative/failure case for Driver tests is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TEST-007 — Graphics API tests
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `test`  
**Description:** Each claimed graphics API shall have API-specific correctness tests before compatibility claims.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Each claimed graphics API shall have API-specific correctness tests before compatibility claims.
- Required negative/failure case for Graphics API tests is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TEST-008 — Integration tests
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `test`  
**Description:** Client-service-host end-to-end tests shall run with deterministic fake and real backends where useful.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Client-service-host end-to-end tests shall run with deterministic fake and real backends where useful.
- Required negative/failure case for Integration tests is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TEST-009 — Hardware tests
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `test`  
**Description:** Claims involving WDDM/vendor GPU/presentation shall require designated hardware tests.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Claims involving WDDM/vendor GPU/presentation shall require designated hardware tests.
- Required negative/failure case for Hardware tests is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TEST-010 — Game tests
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `test`  
**Description:** Representative unmodified games shall be used only after underlying API/presentation gates pass.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Representative unmodified games shall be used only after underlying API/presentation gates pass.
- Required negative/failure case for Game tests is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TEST-011 — WAN tests
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `test`  
**Description:** Network profiles/faults shall be reproducible and recorded.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Network profiles/faults shall be reproducible and recorded.
- Required negative/failure case for WAN tests is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TEST-012 — Recovery tests
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `test`  
**Description:** Host crash, service crash, cable pull, timeout and reconnect shall be tested.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Host crash, service crash, cable pull, timeout and reconnect shall be tested.
- Required negative/failure case for Recovery tests is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TEST-013 — Security tests
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `test`  
**Description:** Auth/replay/malformed-input/isolation and fuzz tests shall gate security claims.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Auth/replay/malformed-input/isolation and fuzz tests shall gate security claims.
- Required negative/failure case for Security tests is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TEST-014 — Soak tests
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `test`  
**Description:** Long-duration resource churn and session loops shall detect leaks/races.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Long-duration resource churn and session loops shall detect leaks/races.
- Required negative/failure case for Soak tests is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TEST-015 — Regression permanence
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `test`  
**Description:** Every confirmed merge-blocking defect shall gain regression evidence or an equivalent durable oracle.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Every confirmed merge-blocking defect shall gain regression evidence or an equivalent durable oracle.
- Required negative/failure case for Regression permanence is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TEST-016 — Fresh breaker required
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `test`  
**Description:** Non-trivial phases require independent review after builder validation.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Non-trivial phases require independent review after builder validation.
- Required negative/failure case for Fresh breaker required is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TEST-017 — No skipped-test pass
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `test`  
**Description:** A required skipped/not-run test prevents PASS/DONE.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: A required skipped/not-run test prevents PASS/DONE.
- Required negative/failure case for No skipped-test pass is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TEST-018 — Flake investigation
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `test`  
**Description:** Repeated reruns are not an acceptable flake policy; nondeterminism must be diagnosed and tracked.

**Rationale/evidence:** LL-005, LL-006, LL-010, LL-011, LL-021

**Acceptance criteria:**
- Evidence demonstrates: Repeated reruns are not an acceptable flake policy; nondeterminism must be diagnosed and tracked.
- Required negative/failure case for Flake investigation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-020
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRANSPORT-001 — QUIC baseline
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `transport`  
**Description:** WAN baseline transport shall be QUIC through a replaceable transport interface.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: WAN baseline transport shall be QUIC through a replaceable transport interface.
- Required negative/failure case for QUIC baseline is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRANSPORT-002 — Mutual authentication support
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `transport`  
**Description:** Transport/session layer shall support authenticated client and host identities.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: Transport/session layer shall support authenticated client and host identities.
- Required negative/failure case for Mutual authentication support is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRANSPORT-003 — Encrypted WAN data
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `transport`  
**Description:** SpanGPU WAN traffic shall be encrypted in transit by default.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: SpanGPU WAN traffic shall be encrypted in transit by default.
- Required negative/failure case for Encrypted WAN data is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRANSPORT-004 — Independent logical streams
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `transport`  
**Description:** Control, command, resource, completion and telemetry traffic shall support independent stream/priority behavior.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: Control, command, resource, completion and telemetry traffic shall support independent stream/priority behavior.
- Required negative/failure case for Independent logical streams is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRANSPORT-005 — No global ordering requirement
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `transport`  
**Description:** Transport shall not impose global ordering where only per-queue or per-resource ordering is required.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: Transport shall not impose global ordering where only per-queue or per-resource ordering is required.
- Required negative/failure case for No global ordering requirement is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRANSPORT-006 — Bulk transfer parallelism
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `transport`  
**Description:** Large resources shall support parallel transfer without blocking small control/completion messages.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: Large resources shall support parallel transfer without blocking small control/completion messages.
- Required negative/failure case for Bulk transfer parallelism is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRANSPORT-007 — Connection migration semantics explicit
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `transport`  
**Description:** QUIC connection migration/rebinding shall be accepted only if session identity and trust remain valid.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: QUIC connection migration/rebinding shall be accepted only if session identity and trust remain valid.
- Required negative/failure case for Connection migration semantics explicit is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRANSPORT-008 — RDMA optional plugin
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `transport`  
**Description:** RDMA/libfabric transport may be added without changing graphics/resource protocol semantics.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: RDMA/libfabric transport may be added without changing graphics/resource protocol semantics.
- Required negative/failure case for RDMA optional plugin is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRANSPORT-009 — Backpressure propagation
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `transport`  
**Description:** Transport congestion/backpressure shall feed the command/resource schedulers with bounded queues.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: Transport congestion/backpressure shall feed the command/resource schedulers with bounded queues.
- Required negative/failure case for Backpressure propagation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRANSPORT-010 — Transport metrics
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `transport`  
**Description:** RTT, loss, retransmission, throughput, queueing and stream stalls shall be observable.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: RTT, loss, retransmission, throughput, queueing and stream stalls shall be observable.
- Required negative/failure case for Transport metrics is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRANSPORT-011 — Transport replacement contract
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `transport`  
**Description:** A transport implementation shall satisfy a documented RGPU_TRANSPORT contract and conformance tests.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: A transport implementation shall satisfy a documented RGPU_TRANSPORT contract and conformance tests.
- Required negative/failure case for Transport replacement contract is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005, TD-003
**Gates:** GATE-003
**Phases:** PHASE-008
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRUST-001 — Driver signing roadmap
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `trust`  
**Description:** Development, attestation/test signing and production signing paths shall be separately documented.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Development, attestation/test signing and production signing paths shall be separately documented.
- Required negative/failure case for Driver signing roadmap is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-028
**Phases:** PHASE-037
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRUST-002 — Secure Boot compatibility target
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `trust`  
**Description:** Production client architecture shall not require disabling Secure Boot.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Production client architecture shall not require disabling Secure Boot.
- Required negative/failure case for Secure Boot compatibility target is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-028
**Phases:** PHASE-037
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRUST-003 — TPM/attestation extensibility
**Priority:** `SHOULD`  
**Horizon:** `later`  
**Component:** `trust`  
**Description:** Trust protocol shall permit later client/host attestation without changing graphics command semantics.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Trust protocol shall permit later client/host attestation without changing graphics command semantics.
- Required negative/failure case for TPM/attestation extensibility is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-028
**Phases:** PHASE-037
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRUST-004 — Host software identity
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `trust`  
**Description:** Session evidence shall record host daemon/backend/vendor-driver build identities.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Session evidence shall record host daemon/backend/vendor-driver build identities.
- Required negative/failure case for Host software identity is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-028
**Phases:** PHASE-037
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRUST-005 — Client software identity
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `trust`  
**Description:** Session evidence shall record KMD/UMD/service build identities.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Session evidence shall record KMD/UMD/service build identities.
- Required negative/failure case for Client software identity is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-028
**Phases:** PHASE-037
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRUST-006 — Trust policy separate from transport
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `trust`  
**Description:** Authentication/attestation policy shall be separable from QUIC implementation details.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Authentication/attestation policy shall be separable from QUIC implementation details.
- Required negative/failure case for Trust policy separate from transport is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-028
**Phases:** PHASE-037
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRUST-007 — Trust downgrade visible
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `trust`  
**Description:** Any development mode, test signing or disabled attestation shall be explicitly reflected in evidence/compatibility status.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Any development mode, test signing or disabled attestation shall be explicitly reflected in evidence/compatibility status.
- Required negative/failure case for Trust downgrade visible is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-028
**Phases:** PHASE-037
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRUST-008 — No trust by GPU name
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `trust`  
**Description:** A claimed GPU model string shall not alone establish host trust or capability.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: A claimed GPU model string shall not alone establish host trust or capability.
- Required negative/failure case for No trust by GPU name is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-028
**Phases:** PHASE-037
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRUST-009 — Signed evidence metadata
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `trust`  
**Description:** Release/gate evidence may be cryptographically signed/attested where infrastructure supports it.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Release/gate evidence may be cryptographically signed/attested where infrastructure supports it.
- Required negative/failure case for Signed evidence metadata is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-028
**Phases:** PHASE-037
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## TRUST-010 — Vendor cooperation optional to core
**Priority:** `SHOULD`  
**Horizon:** `later`  
**Component:** `trust`  
**Description:** Core rendering shall not require anti-cheat/vendor cooperation, while trust integration may later use it.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Core rendering shall not require anti-cheat/vendor cooperation, while trust integration may later use it.
- Required negative/failure case for Vendor cooperation optional to core is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-015
**Gates:** GATE-028
**Phases:** PHASE-037
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## UPSTREAM-001 — Machine-readable upstream registry
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `upstream`  
**Description:** Every controlled fork/dependency/reference shall have an upstream registry entry with classification and provenance.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Every controlled fork/dependency/reference shall have an upstream registry entry with classification and provenance.
- Required negative/failure case for Machine-readable upstream registry is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-014
**Gates:** GATE-000
**Phases:** PHASE-001
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## UPSTREAM-002 — Pinned critical baselines
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `upstream`  
**Description:** Controlled forks shall pin a specific upstream ref during bootstrap; unpinned status blocks implementation depending on that baseline.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Controlled forks shall pin a specific upstream ref during bootstrap; unpinned status blocks implementation depending on that baseline.
- Required negative/failure case for Pinned critical baselines is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-014
**Gates:** GATE-000
**Phases:** PHASE-001
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## UPSTREAM-003 — Upstream remote retained
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `upstream`  
**Description:** Controlled forks shall retain an upstream remote separate from SpanGPU origin.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Controlled forks shall retain an upstream remote separate from SpanGPU origin.
- Required negative/failure case for Upstream remote retained is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-014
**Gates:** GATE-000
**Phases:** PHASE-001
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## UPSTREAM-004 — Patch ownership
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `upstream`  
**Description:** Each SpanGPU-specific patch area shall have an owner/rationale and affected contracts.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Each SpanGPU-specific patch area shall have an owner/rationale and affected contracts.
- Required negative/failure case for Patch ownership is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-014
**Gates:** GATE-000
**Phases:** PHASE-001
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## UPSTREAM-005 — Divergence tracking
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `upstream`  
**Description:** Automation shall report commits/patches ahead/behind upstream and touched critical files.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Automation shall report commits/patches ahead/behind upstream and touched critical files.
- Required negative/failure case for Divergence tracking is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-014
**Gates:** GATE-000
**Phases:** PHASE-001
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## UPSTREAM-006 — Scheduled upstream monitoring
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `upstream`  
**Description:** Critical upstreams shall be checked on a scheduled cadence and on known release/security events.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Critical upstreams shall be checked on a scheduled cadence and on known release/security events.
- Required negative/failure case for Scheduled upstream monitoring is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-014
**Gates:** GATE-000
**Phases:** PHASE-001
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## UPSTREAM-007 — Automated impact packet
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `upstream`  
**Description:** Detected upstream change shall produce metadata, diff summary, license/security signals and selected test plan for review.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Detected upstream change shall produce metadata, diff summary, license/security signals and selected test plan for review.
- Required negative/failure case for Automated impact packet is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-014
**Gates:** GATE-000
**Phases:** PHASE-001
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## UPSTREAM-008 — Manual adoption gate
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `upstream`  
**Description:** Critical upstream changes require human/steward adoption after Codex review and tests.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Critical upstream changes require human/steward adoption after Codex review and tests.
- Required negative/failure case for Manual adoption gate is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-014
**Gates:** GATE-000
**Phases:** PHASE-001
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## UPSTREAM-009 — Abandonment policy
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `upstream`  
**Description:** If an upstream becomes abandoned, project shall document takeover/freeze/replace decision without silently drifting.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: If an upstream becomes abandoned, project shall document takeover/freeze/replace decision without silently drifting.
- Required negative/failure case for Abandonment policy is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-014
**Gates:** GATE-000
**Phases:** PHASE-001
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## UPSTREAM-010 — Replacement strategy
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `upstream`  
**Description:** Every critical dependency/fork shall name a plausible replacement/ownership strategy.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Every critical dependency/fork shall name a plausible replacement/ownership strategy.
- Required negative/failure case for Replacement strategy is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-014
**Gates:** GATE-000
**Phases:** PHASE-001
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## UPSTREAM-011 — No proprietary critical fork
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `upstream`  
**Description:** Unavailable proprietary binaries shall not be registered as a controlled fork or mandatory critical runtime component.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Unavailable proprietary binaries shall not be registered as a controlled fork or mandatory critical runtime component.
- Required negative/failure case for No proprietary critical fork is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-014
**Gates:** GATE-000
**Phases:** PHASE-001
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## UPSTREAM-012 — Fork provenance preserved
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `upstream`  
**Description:** Fork commit history and upstream baseline metadata shall remain auditable through releases.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Fork commit history and upstream baseline metadata shall remain auditable through releases.
- Required negative/failure case for Fork provenance preserved is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-014
**Gates:** GATE-000
**Phases:** PHASE-001
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## UPSTREAM-013 — Upstream license change gate
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `upstream`  
**Description:** License changes in used components shall block adoption until compatibility review completes.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: License changes in used components shall block adoption until compatibility review completes.
- Required negative/failure case for Upstream license change gate is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-014
**Gates:** GATE-000
**Phases:** PHASE-001
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## UPSTREAM-014 — SBOM integration
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `upstream`  
**Description:** Release/dependency metadata shall include an SBOM or equivalent machine-readable dependency inventory.

**Rationale/evidence:** RF-012, RF-013, RF-029

**Acceptance criteria:**
- Evidence demonstrates: Release/dependency metadata shall include an SBOM or equivalent machine-readable dependency inventory.
- Required negative/failure case for SBOM integration is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-014
**Gates:** GATE-000
**Phases:** PHASE-001
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VISION-001 — Universal remote GPU abstraction
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `vision`  
**Description:** SpanGPU shall let ordinary local Windows applications consume physically remote GPU execution without application awareness of the network boundary.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: SpanGPU shall let ordinary local Windows applications consume physically remote GPU execution without application awareness of the network boundary.
- Required negative/failure case for Universal remote GPU abstraction is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VISION-002 — Local application execution
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `vision`  
**Description:** Application/game process execution shall remain on the client machine.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Application/game process execution shall remain on the client machine.
- Required negative/failure case for Local application execution is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VISION-003 — Local CPU ownership
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `vision`  
**Description:** Application CPU execution shall remain on the client CPU.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Application CPU execution shall remain on the client CPU.
- Required negative/failure case for Local CPU ownership is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VISION-004 — Local system RAM ownership
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `vision`  
**Description:** Application system RAM shall remain client-local except explicit serialized/staged GPU resource transfers.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Application system RAM shall remain client-local except explicit serialized/staged GPU resource transfers.
- Required negative/failure case for Local system RAM ownership is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VISION-005 — Local storage ownership
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `vision`  
**Description:** Application binaries, assets and ordinary filesystem state shall remain on client storage.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Application binaries, assets and ordinary filesystem state shall remain on client storage.
- Required negative/failure case for Local storage ownership is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VISION-006 — Local input ownership
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `vision`  
**Description:** Keyboard, mouse, controller and other application input shall remain handled by the local OS/application.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Keyboard, mouse, controller and other application input shall remain handled by the local OS/application.
- Required negative/failure case for Local input ownership is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VISION-007 — Remote GPU execution
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `vision`  
**Description:** Graphics and supported compute commands selected for SpanGPU shall execute on the remote physical GPU.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Graphics and supported compute commands selected for SpanGPU shall execute on the remote physical GPU.
- Required negative/failure case for Remote GPU execution is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VISION-008 — Remote VRAM first-class
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `vision`  
**Description:** Remote GPU memory shall be modeled as first-class authoritative resource state rather than incidental renderer memory.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: Remote GPU memory shall be modeled as first-class authoritative resource state rather than incidental renderer memory.
- Required negative/failure case for Remote VRAM first-class is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VISION-009 — No architecture dead end
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `vision`  
**Description:** v0/v1 shortcuts shall preserve the ability to reach the full North Star without replacing the fundamental client/protocol/host boundaries.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: v0/v1 shortcuts shall preserve the ability to reach the full North Star without replacing the fundamental client/protocol/host boundaries.
- Required negative/failure case for No architecture dead end is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001, TD-003
**Gates:** GATE-000
**Phases:** PHASE-000, PHASE-041
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VISION-010 — Long-lived OSS independence
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `vision`  
**Description:** The project shall remain operable when any non-essential upstream service or proprietary vendor offering is discontinued.

**Rationale/evidence:** RF-030

**Acceptance criteria:**
- Evidence demonstrates: The project shall remain operable when any non-essential upstream service or proprietary vendor offering is discontinued.
- Required negative/failure case for Long-lived OSS independence is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-001
**Gates:** GATE-000
**Phases:** PHASE-000
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VK-001 — Vulkan ICD integration
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `vk`  
**Description:** Vulkan support shall use a normal Windows ICD path rather than application injection.

**Rationale/evidence:** RF-008, RF-009

**Acceptance criteria:**
- Evidence demonstrates: Vulkan support shall use a normal Windows ICD path rather than application injection.
- Required negative/failure case for Vulkan ICD integration is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-021
**Phases:** PHASE-029
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VK-002 — Venus reuse evaluated at source level
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `vk`  
**Description:** Mesa Venus encoder/object logic shall be reused only where its transport/memory assumptions are explicitly separated.

**Rationale/evidence:** RF-008, RF-009

**Acceptance criteria:**
- Evidence demonstrates: Mesa Venus encoder/object logic shall be reused only where its transport/memory assumptions are explicitly separated.
- Required negative/failure case for Venus reuse evaluated at source level is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-021
**Phases:** PHASE-029
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VK-003 — Vulkan object identity
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `vk`  
**Description:** Vk object lifetimes crossing the remote boundary shall have deterministic SpanGPU identities.

**Rationale/evidence:** RF-008, RF-009

**Acceptance criteria:**
- Evidence demonstrates: Vk object lifetimes crossing the remote boundary shall have deterministic SpanGPU identities.
- Required negative/failure case for Vulkan object identity is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-021
**Phases:** PHASE-029
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VK-004 — Vulkan queue ordering
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `vk`  
**Description:** Queue submit, semaphore and fence semantics shall preserve Vulkan ordering under WAN delay.

**Rationale/evidence:** RF-008, RF-009

**Acceptance criteria:**
- Evidence demonstrates: Queue submit, semaphore and fence semantics shall preserve Vulkan ordering under WAN delay.
- Required negative/failure case for Vulkan queue ordering is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-021
**Phases:** PHASE-029
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VK-005 — Vulkan memory mapping rules explicit
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `vk`  
**Description:** Host-visible/mapped memory behavior shall be explicitly supported, staged or rejected; WAN shared mmap shall not be implied.

**Rationale/evidence:** RF-008, RF-009

**Acceptance criteria:**
- Evidence demonstrates: Host-visible/mapped memory behavior shall be explicitly supported, staged or rejected; WAN shared mmap shall not be implied.
- Required negative/failure case for Vulkan memory mapping rules explicit is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-021
**Phases:** PHASE-029
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VK-006 — Vulkan capability filtering
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `vk`  
**Description:** Physical-device properties/extensions shall reflect the effective remote capability set.

**Rationale/evidence:** RF-008, RF-009

**Acceptance criteria:**
- Evidence demonstrates: Physical-device properties/extensions shall reflect the effective remote capability set.
- Required negative/failure case for Vulkan capability filtering is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-021
**Phases:** PHASE-029
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VK-007 — Vulkan CTS subset before game claims
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `vk`  
**Description:** A defined CTS/conformance-oriented subset shall pass before Vulkan game support claims.

**Rationale/evidence:** RF-008, RF-009

**Acceptance criteria:**
- Evidence demonstrates: A defined CTS/conformance-oriented subset shall pass before Vulkan game support claims.
- Required negative/failure case for Vulkan CTS subset before game claims is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-021
**Phases:** PHASE-029
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VK-008 — Vulkan external memory scoped
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `vk`  
**Description:** External memory/semaphore features shall be capability-gated and must not assume same-host handles.

**Rationale/evidence:** RF-008, RF-009

**Acceptance criteria:**
- Evidence demonstrates: External memory/semaphore features shall be capability-gated and must not assume same-host handles.
- Required negative/failure case for Vulkan external memory scoped is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-021
**Phases:** PHASE-029
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VK-009 — Vulkan device lost mapping
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `vk`  
**Description:** Remote failure shall produce deterministic Vulkan device-lost/recovery behavior.

**Rationale/evidence:** RF-008, RF-009

**Acceptance criteria:**
- Evidence demonstrates: Remote failure shall produce deterministic Vulkan device-lost/recovery behavior.
- Required negative/failure case for Vulkan device lost mapping is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-021
**Phases:** PHASE-029
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VK-010 — Vulkan evidence captures driver stack
**Priority:** `SHOULD`  
**Horizon:** `v1.x`  
**Component:** `vk`  
**Description:** Compatibility evidence shall record client ICD and host vendor driver versions.

**Rationale/evidence:** RF-008, RF-009

**Acceptance criteria:**
- Evidence demonstrates: Compatibility evidence shall record client ICD and host vendor driver versions.
- Required negative/failure case for Vulkan evidence captures driver stack is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-004
**Gates:** GATE-021
**Phases:** PHASE-029
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VRAM-001 — Host is VRAM authority
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `vram`  
**Description:** Host VRAM manager shall be authoritative for remote-resident allocation identity, residency and eviction.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: Host VRAM manager shall be authoritative for remote-resident allocation identity, residency and eviction.
- Required negative/failure case for Host is VRAM authority is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VRAM-002 — Stable resource IDs
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `vram`  
**Description:** Remote resources shall use session/epoch-scoped stable IDs independent of client pointer values.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: Remote resources shall use session/epoch-scoped stable IDs independent of client pointer values.
- Required negative/failure case for Stable resource IDs is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VRAM-003 — Immutable payload hashing
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `vram`  
**Description:** Immutable resource payloads shall support cryptographic content identities for cache lookup/integrity.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: Immutable resource payloads shall support cryptographic content identities for cache lookup/integrity.
- Required negative/failure case for Immutable payload hashing is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VRAM-004 — Mutable resource versioning
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `vram`  
**Description:** Mutable resources shall carry explicit generation/version state.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: Mutable resources shall carry explicit generation/version state.
- Required negative/failure case for Mutable resource versioning is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VRAM-005 — No pointer serialization
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `vram`  
**Description:** Raw client virtual pointers shall never be treated as durable remote resource identity.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: Raw client virtual pointers shall never be treated as durable remote resource identity.
- Required negative/failure case for No pointer serialization is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VRAM-006 — Explicit upload ranges
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `vram`  
**Description:** Buffer/texture uploads shall identify exact affected ranges/subresources.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: Buffer/texture uploads shall identify exact affected ranges/subresources.
- Required negative/failure case for Explicit upload ranges is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VRAM-007 — Explicit readback
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `vram`  
**Description:** GPU-to-CPU readback shall be modeled as a potentially blocking data transfer with measurable latency.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: GPU-to-CPU readback shall be modeled as a potentially blocking data transfer with measurable latency.
- Required negative/failure case for Explicit readback is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VRAM-008 — Eviction protocol
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `vram`  
**Description:** Host eviction shall have deterministic client-visible metadata/update rules.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: Host eviction shall have deterministic client-visible metadata/update rules.
- Required negative/failure case for Eviction protocol is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VRAM-009 — Residency telemetry
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `vram`  
**Description:** VRAM usage, residency, evictions and upload volume shall be observable per session.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: VRAM usage, residency, evictions and upload volume shall be observable per session.
- Required negative/failure case for Residency telemetry is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VRAM-010 — Resource lifetime after disconnect
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `vram`  
**Description:** Post-disconnect resource retention/reuse shall be controlled by session epoch and security policy, never assumed.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: Post-disconnect resource retention/reuse shall be controlled by session epoch and security policy, never assumed.
- Required negative/failure case for Resource lifetime after disconnect is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VRAM-011 — Cache/VRAM distinction
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `vram`  
**Description:** Persistent cache presence shall not imply current GPU VRAM residency.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: Persistent cache presence shall not imply current GPU VRAM residency.
- Required negative/failure case for Cache/VRAM distinction is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## VRAM-012 — VRAM quota extensible
**Priority:** `MUST`  
**Horizon:** `v1`  
**Component:** `vram`  
**Description:** Object model shall permit per-session VRAM limits even if v1 is single tenant.

**Rationale/evidence:** RF-009, RF-022, RF-024

**Acceptance criteria:**
- Evidence demonstrates: Object model shall permit per-session VRAM limits even if v1 is single tenant.
- Required negative/failure case for VRAM quota extensible is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-007
**Gates:** GATE-007
**Phases:** PHASE-016
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WAIVER-001 — Structured waiver lifecycle
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** Any accepted exception shall have owner, scope, rationale, expiry/review date and affected requirements/risks; waivers are append-only governance records.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: Any accepted exception shall have owner, scope, rationale, expiry/review date and affected requirements/risks; waivers are append-only governance records.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-031
**Gates:** GATE-BK-000
**Phases:** PHASE-000
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## WAIVER-002 — Waiver cannot fabricate proof
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `governance`  
**Description:** A waiver may permit risk acceptance but shall never convert an unexecuted or failed proof gate into PASS.

**Rationale/evidence:** LL-005, LL-006, LL-011, LL-021, LL-022

**Acceptance criteria:**
- Evidence demonstrates: A waiver may permit risk acceptance but shall never convert an unexecuted or failed proof gate into PASS.
- Negative/failure semantics defined and exercised where applicable.

**Verification:** Machine-readable validator and linked proof/hardware gate as applicable.
**Dependencies:** None
**TDs:** TD-031
**Gates:** GATE-BK-000
**Phases:** PHASE-000
**Risk if violated:** Can create stale evidence, false completion, cross-attempt contamination, unsafe release or unowned interface semantics.

## WAN-001 — WAN baseline profiles
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `wan`  
**Description:** CI/hardware tests shall include deterministic LAN, 1, 5, 10, 20, 30 and 40 ms RTT profiles.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: CI/hardware tests shall include deterministic LAN, 1, 5, 10, 20, 30 and 40 ms RTT profiles.
- Required negative/failure case for WAN baseline profiles is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-013
**Phases:** PHASE-020, PHASE-021
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WAN-002 — Jitter profile
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `wan`  
**Description:** WAN tests shall include reproducible jitter distributions.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: WAN tests shall include reproducible jitter distributions.
- Required negative/failure case for Jitter profile is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-013
**Phases:** PHASE-020, PHASE-024
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WAN-003 — Loss profile
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `wan`  
**Description:** WAN tests shall include bounded packet-loss profiles appropriate to the transport.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: WAN tests shall include bounded packet-loss profiles appropriate to the transport.
- Required negative/failure case for Loss profile is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-013
**Phases:** PHASE-020, PHASE-024
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WAN-004 — Bandwidth caps
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `wan`  
**Description:** WAN tests shall include constrained bandwidth profiles for resource-heavy workloads.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: WAN tests shall include constrained bandwidth profiles for resource-heavy workloads.
- Required negative/failure case for Bandwidth caps is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-013
**Phases:** PHASE-020, PHASE-024
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WAN-005 — Temporary disconnect
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `wan`  
**Description:** Tests shall include temporary connectivity loss with bounded duration.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: Tests shall include temporary connectivity loss with bounded duration.
- Required negative/failure case for Temporary disconnect is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WAN-006 — Hard disconnect
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `wan`  
**Description:** Tests shall include hard link loss without graceful close.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: Tests shall include hard link loss without graceful close.
- Required negative/failure case for Hard disconnect is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WAN-007 — No per-draw RTT
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `wan`  
**Description:** Hot path shall demonstrate no mandatory synchronous roundtrip per draw.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: Hot path shall demonstrate no mandatory synchronous roundtrip per draw.
- Required negative/failure case for No per-draw RTT is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WAN-008 — No per-submit RTT
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `wan`  
**Description:** Ordinary queue submit shall not require a WAN ack before the next independent submit can be prepared.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: Ordinary queue submit shall not require a WAN ack before the next independent submit can be prepared.
- Required negative/failure case for No per-submit RTT is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WAN-009 — Readback stalls attributed
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `wan`  
**Description:** Required CPU-visible readbacks shall be identified as RTT-sensitive and visible in telemetry.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: Required CPU-visible readbacks shall be identified as RTT-sensitive and visible in telemetry.
- Required negative/failure case for Readback stalls attributed is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WAN-010 — WAN support tiers evidence-based
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `wan`  
**Description:** Latency support tiers shall be published from measured evidence, not assumed universal.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: Latency support tiers shall be published from measured evidence, not assumed universal.
- Required negative/failure case for WAN support tiers evidence-based is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-013
**Phases:** PHASE-020, PHASE-022, PHASE-023
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WAN-011 — Frame-return independent congestion control
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `wan`  
**Description:** Presentation/frame return shall not share a single blocking queue with command/resource control.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: Presentation/frame return shall not share a single blocking queue with command/resource control.
- Required negative/failure case for Frame-return independent congestion control is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-013
**Phases:** PHASE-020
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WAN-012 — Network fault does not corrupt resource graph
**Priority:** `SHOULD`  
**Horizon:** `v1`  
**Component:** `wan`  
**Description:** Loss/reordering/reconnect shall not produce valid-looking but incorrect resource/object state.

**Rationale/evidence:** RF-014, RF-015, RF-023

**Acceptance criteria:**
- Evidence demonstrates: Loss/reordering/reconnect shall not produce valid-looking but incorrect resource/object state.
- Required negative/failure case for Network fault does not corrupt resource graph is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-005
**Gates:** GATE-013
**Phases:** PHASE-020, PHASE-024
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WDDM-001 — WDDM KMD boundary
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `wddm`  
**Description:** A SpanGPU KMD shall own adapter/device/allocation/submission interfaces required by the selected WDDM model.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: A SpanGPU KMD shall own adapter/device/allocation/submission interfaces required by the selected WDDM model.
- Required negative/failure case for WDDM KMD boundary is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WDDM-002 — UMD/KMD contract versioned
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `wddm`  
**Description:** The client graphics UMD/KMD contract shall be explicit and versioned where SpanGPU-owned structures cross the boundary.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: The client graphics UMD/KMD contract shall be explicit and versioned where SpanGPU-owned structures cross the boundary.
- Required negative/failure case for UMD/KMD contract versioned is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004, PHASE-006
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WDDM-003 — KMD network minimization
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `wddm`  
**Description:** KMD shall not own general WAN/TLS/cache logic unless a later accepted TD proves it necessary.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: KMD shall not own general WAN/TLS/cache logic unless a later accepted TD proves it necessary.
- Required negative/failure case for KMD network minimization is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WDDM-004 — WDDM allocation lifecycle correctness
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `wddm`  
**Description:** Allocation create/open/close/destroy paths shall preserve WDDM lifetime rules under remote execution.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: Allocation create/open/close/destroy paths shall preserve WDDM lifetime rules under remote execution.
- Required negative/failure case for WDDM allocation lifecycle correctness is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004, PHASE-005
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WDDM-005 — GPUVA model explicit
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `wddm`  
**Description:** GPU virtual-address behavior and any translation to remote resource identity shall be formally specified before broad API support.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: GPU virtual-address behavior and any translation to remote resource identity shall be formally specified before broad API support.
- Required negative/failure case for GPUVA model explicit is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004, PHASE-005
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WDDM-006 — Submission ordering preserved
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `wddm`  
**Description:** WDDM submission order and preemption/fence expectations shall map deterministically to SpanGPU queue semantics.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: WDDM submission order and preemption/fence expectations shall map deterministically to SpanGPU queue semantics.
- Required negative/failure case for Submission ordering preserved is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WDDM-007 — TDR behavior bounded
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `wddm`  
**Description:** Remote stalls/disconnects shall not create unbounded TDR loops or kernel deadlocks.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: Remote stalls/disconnects shall not create unbounded TDR loops or kernel deadlocks.
- Required negative/failure case for TDR behavior bounded is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004, PHASE-026
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WDDM-008 — Device removal semantics
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `wddm`  
**Description:** Irrecoverable remote failures shall surface through documented Windows device-loss/removal semantics.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: Irrecoverable remote failures shall surface through documented Windows device-loss/removal semantics.
- Required negative/failure case for Device removal semantics is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WDDM-009 — Power/suspend behavior explicit
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `wddm`  
**Description:** Sleep/hibernate/power transitions shall be unsupported explicitly or tested with defined restore behavior; silent state reuse is forbidden.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: Sleep/hibernate/power transitions shall be unsupported explicitly or tested with defined restore behavior; silent state reuse is forbidden.
- Required negative/failure case for Power/suspend behavior explicit is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WDDM-010 — WDDM version ownership
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `wddm`  
**Description:** Supported WDDM/DDI versions shall be centrally declared and changed only through a TD and compatibility evidence.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: Supported WDDM/DDI versions shall be centrally declared and changed only through a TD and compatibility evidence.
- Required negative/failure case for WDDM version ownership is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WDDM-011 — Cross-adapter behavior tested
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `wddm`  
**Description:** Any cross-adapter resource/present mechanism shall have explicit ownership and synchronization tests.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: Any cross-adapter resource/present mechanism shall have explicit ownership and synchronization tests.
- Required negative/failure case for Cross-adapter behavior tested is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WDDM-012 — No assumption of VM bus
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `wddm`  
**Description:** Client WDDM design shall not require a hypervisor/VM bus in normal SpanGPU deployment.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: Client WDDM design shall not require a hypervisor/VM bus in normal SpanGPU deployment.
- Required negative/failure case for No assumption of VM bus is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002, TD-003
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WIN-001 — Windows 11 baseline
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `win`  
**Description:** Initial supported client baseline shall be a documented Windows 11 build family validated in the hardware matrix.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: Initial supported client baseline shall be a documented Windows 11 build family validated in the hardware matrix.
- Required negative/failure case for Windows 11 baseline is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WIN-002 — Secondary adapter enumeration
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `win`  
**Description:** SpanGPU shall enumerate alongside an existing local adapter.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: SpanGPU shall enumerate alongside an existing local adapter.
- Required negative/failure case for Secondary adapter enumeration is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WIN-003 — Device Manager diagnostics
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `win`  
**Description:** Driver installation/state/errors shall be diagnosable through standard Windows driver/device mechanisms and SpanGPU diagnostics.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: Driver installation/state/errors shall be diagnosable through standard Windows driver/device mechanisms and SpanGPU diagnostics.
- Required negative/failure case for Device Manager diagnostics is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WIN-004 — No desktop takeover requirement
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `win`  
**Description:** SpanGPU shall not require becoming the sole display adapter to provide render acceleration.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: SpanGPU shall not require becoming the sole display adapter to provide render acceleration.
- Required negative/failure case for No desktop takeover requirement is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WIN-005 — Windows update compatibility matrix
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `win`  
**Description:** Supported Windows builds shall be explicitly tracked and regression-tested.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: Supported Windows builds shall be explicitly tracked and regression-tested.
- Required negative/failure case for Windows update compatibility matrix is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WIN-006 — Test-signing isolated to development
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `win`  
**Description:** Development may use test signing only on designated test hardware; production claims require the signing gate.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: Development may use test signing only on designated test hardware; production claims require the signing gate.
- Required negative/failure case for Test-signing isolated to development is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WIN-007 — Driver rollback package
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `win`  
**Description:** Every deployable driver test build shall have a documented automatic/manual rollback route.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: Every deployable driver test build shall have a documented automatic/manual rollback route.
- Required negative/failure case for Driver rollback package is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WIN-008 — Crash dump preservation
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `win`  
**Description:** Kernel/driver failures shall preserve crash dumps and correlation metadata before test environment restoration.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: Kernel/driver failures shall preserve crash dumps and correlation metadata before test environment restoration.
- Required negative/failure case for Crash dump preservation is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WIN-009 — ETW/event log capture
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `win`  
**Description:** Windows driver/service test runs shall collect relevant ETW/Event Log evidence.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: Windows driver/service test runs shall collect relevant ETW/Event Log evidence.
- Required negative/failure case for ETW/event log capture is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.

## WIN-010 — No unsupported kernel patching
**Priority:** `MUST`  
**Horizon:** `v0/proof`  
**Component:** `win`  
**Description:** Client operation shall not depend on patching Windows kernel binaries or disabling platform integrity outside documented development test modes.

**Rationale/evidence:** RF-001, RF-003, RF-004

**Acceptance criteria:**
- Evidence demonstrates: Client operation shall not depend on patching Windows kernel binaries or disabling platform integrity outside documented development test modes.
- Required negative/failure case for No unsupported kernel patching is exercised or explicitly proven not applicable.

**Verification:** Automated test/validator where possible plus the linked proof gate; hardware evidence is mandatory when the linked gate declares hardware.
**Dependencies:** None
**TDs:** TD-002
**Gates:** GATE-001
**Phases:** PHASE-004
**Risk if violated:** Can invalidate compatibility, correctness, safety, independence or evidence integrity depending on component.
