# Architecture Invariants

## INV-001 — Unmodified applications
**Statement:** Games and applications MUST NOT require source/binary modification to use the primary SpanGPU architecture.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-002 — Launcher independence
**Statement:** Steam, Epic, GOG, Battle.net and other launchers MUST NOT require SpanGPU-specific integration.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-003 — No injection foundation
**Statement:** DLL injection/API hooking MUST NOT become the primary runtime architecture.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-004 — Normal Windows adapter
**Statement:** Windows MUST expose SpanGPU as a hardware-accelerated graphics adapter through supported WDDM mechanisms.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-005 — WAN first-class
**Statement:** Architecture decisions MUST remain correct at WAN latency/loss; LAN-only assumptions require explicit containment.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-006 — Remote-authoritative VRAM
**Statement:** GPU resources designated resident remotely MUST have explicit remote ownership/lifetime; WAN shared-memory illusion is forbidden.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-007 — Minimize synchronous RTT
**Statement:** No hot-path design may require a synchronous WAN round trip per draw, dispatch, ordinary submit, resource reference or fence poll.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-008 — Transport/API separation
**Statement:** Transport framing MUST remain separate from graphics command semantics and resource semantics.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-009 — API extensibility
**Statement:** The common architecture MUST allow DX9/10/11/12, Vulkan and OpenGL frontends without replacing the core WAN/resource model.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-010 — Local GPU coexistence
**Statement:** The local GPU MUST remain usable as another adapter; SpanGPU MUST NOT require exclusive graphics ownership.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-011 — Vendor backend boundary
**Statement:** NVIDIA/AMD-specific behavior MUST stay behind a stable host backend interface where technically practical.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-012 — Open critical path
**Statement:** Fundamental runtime operation MUST NOT depend on unavailable proprietary binaries or a proprietary hosted service.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-013 — Controlled upstreams
**Statement:** Critical upstream forks MUST be pinned, auditable, replaceable and never auto-merged.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-014 — Versioned protocol
**Statement:** All cross-machine and KMD↔service ABIs MUST be explicitly versioned with compatibility negotiation.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-015 — Correctness before optimization
**Statement:** Caching, batching, speculation and compression MUST NOT silently alter observable graphics/synchronization semantics.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-016 — Fail-safe kernel boundary
**Statement:** Network/TLS/cache complexity MUST remain outside the KMD unless a TD with proof shows kernel placement is required.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-017 — Controlled failure
**Statement:** Host/network failure MUST produce bounded, diagnosable device-loss/recovery behavior, never silent corruption.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-018 — No anti-cheat evasion
**Statement:** Anti-cheat compatibility MUST use legitimate signing/attestation/cooperation and MUST NOT use concealment or bypass.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-019 — Externally constrained truth
**Statement:** Third-party policy acceptance MUST be reported separately from SpanGPU rendering correctness.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-020 — Evidence-gated completion
**Statement:** Hardware/proof-gated phases MUST NOT be DONE without the required evidence.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-021 — Fresh independent verification
**Statement:** Builder success MUST be followed by a fresh independent BREAKER before acceptance for non-trivial phases.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-022 — Boundary ownership
**Statement:** Every stable interface MUST document producer, consumer, source of truth, validation, trust, versioning, retry/idempotency and failure semantics.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-023 — Attempt provenance
**Statement:** Retries, recovery runs and gate executions MUST have unique attempt/evidence IDs and immutable provenance.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-024 — Reason globally, implement locally
**Statement:** A phase MUST consider global impact but MUST NOT implement future scope outside its explicit implementation boundary.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-025 — Single source of truth
**Statement:** Every authoritative state item MUST have one named owner; caches/projections MUST never silently become authoritative.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-026 — No ambiguous success
**Statement:** Blocked or skipped required validation MUST produce BLOCKED/PROOF_NOT_ESTABLISHED states, never implicit PASS.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-027 — Allowed/required/observed separation
**Statement:** Schemas MUST distinguish allowed, required and observed sets where exact-set semantics matter.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-028 — No retry-until-green
**Statement:** Automated workflows MUST NOT mutate/retry repeatedly solely to obtain green status without a diagnosed failure and concrete remediation.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-029 — Builder/BREAKER isolation
**Statement:** Fresh BREAKER review MUST NOT receive Builder reasoning history; it receives requirements, invariants, target commit/diff and relevant evidence only.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-030 — Immutable evidence
**Statement:** Acceptance evidence MUST be append-only, content-hashed and bound to attempt/commit/environment/hardware identity.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-031 — Canonical governance source
**Statement:** Requirements, TDs, gates, phases, risks, upstreams and contracts MUST each have exactly one canonical machine-readable definition; generated views MUST NOT become independent sources.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-032 — Waivers do not create PASS
**Statement:** Risk/requirement waivers MUST NOT convert failed, blocked or unexecuted proof into PASS/DONE.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-033 — Exclusive hardware proof
**Statement:** Hardware evidence used for acceptance MUST originate from an exclusively leased, fingerprinted and contamination-checked runner.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-034 — Signing identity isolation
**Statement:** Development/test signing and production release signing identities/keys MUST remain operationally isolated.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.

## INV-035 — Release provenance
**Statement:** Public release artifacts MUST be traceable to immutable source, build provenance, dependency/SBOM, license and acceptance evidence.

**Rationale:** Preserves the researched North Star, correctness, independence or evidence integrity.

**Violation examples:** introducing a shortcut that contradicts the statement; claiming success while the invariant is unproven.

**Automated enforcement:** schema/architecture-guard checks where possible, plus fresh BREAKER semantic review.

**Review gate:** `STOP → architecture violation report → do not implement workaround → escalate`.
