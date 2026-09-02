# Risk Register

> Canonical source: `12-machine-readable/risk-register.yaml`.

- **RISK-001 [BLOCKER]** Triton-derived adapter cannot operate safely as a normal secondary Windows adapter — proof `GATE-001` — mitigation: Fall back to a new minimal WDDM adapter while retaining the same service/protocol boundaries; do not tunnel launcher/API hooks.
- **RISK-002 [BLOCKER]** Presentation cannot integrate remote-rendered surfaces into a legitimate Windows path — proof `GATE-006` — mitigation: Evaluate render-only cross-adapter/virtual display alternatives behind TD-012; if none preserve North Star, architecture must be revised before game scaling.
- **RISK-003 [HIGH]** Remote VRAM/GPUVA semantics conflict with WDDM allocation expectations — proof `GATE-007` — mitigation: Use explicit staging/shadow allocations and narrow supported mapping modes; document unsupported zero-copy semantics.
- **RISK-004 [BLOCKER]** Fence/scheduler semantics force synchronous RTT in common workloads — proof `GATE-009` — mitigation: Redesign command granularity/queue proxy; set explicit supported RTT limit if unavoidable.
- **RISK-005 [HIGH]** Hard disconnect triggers TDR loop, hang or BSOD — proof `GATE-019` — mitigation: Fail closed to device removal, isolate network logic from KMD, automate rollback and crash-dump analysis.
- **RISK-006 [HIGH]** D3D12 requires incompatible WDDM/UMD architecture — proof `GATE-024` — mitigation: Keep D3D12 proof isolated; if core replacement is required, revise TD-021 before full implementation rather than layering hacks.
- **RISK-007 [HIGH]** Controlled forks diverge beyond maintainability — proof `GATE-000` — mitigation: Patch ownership, divergence metrics, upstream monitoring and takeover policy; minimize changes outside owned seams.
- **RISK-008 [HIGH]** Upstream license/provenance conflicts prevent intended redistribution — proof `GATE-000` — mitigation: File-level license inventory and license TD before copying/adapting code; dependency/reference when copying is unsafe.
- **RISK-009 [HIGH]** Persistent cache returns stale/corrupt resources — proof `GATE-008` — mitigation: Content hashes, immutable payloads, versioned mutable metadata, corruption/fault tests and authoritative host validation.
- **RISK-010 [HIGH]** Protocol version skew silently corrupts state — proof `GATE-003` — mitigation: Fail-closed capability/version negotiation; compatibility tests for N/N-1 where supported.
- **RISK-011 [HIGH]** Different GPU capability sets change observable graphics semantics — proof `GATE-025` — mitigation: Explicit capability negotiation, deterministic feature rejection and per-backend conformance matrix.
- **RISK-012 [HIGH]** Client/host retry creates duplicate or ambiguous mutations — proof `GATE-017` — mitigation: Attempt IDs, idempotency keys, monotonic sequence/epoch model and ambiguous-completion tests.
- **RISK-013 [HIGH]** Host/client trust boundary exposes DMA-like or protocol attack surface — proof `GATE-027` — mitigation: No raw client memory authority; bounded parsers, fuzzing, auth, least privilege and per-session quotas.
- **RISK-014 [MEDIUM]** 40 ms WAN cannot deliver acceptable gaming latency — proof `GATE-016` — mitigation: Keep correctness; characterize workload support honestly, optimize pipeline, and define latency tiers rather than fake universal performance.
- **RISK-015 [HIGH]** Windows update breaks WDDM fork — proof `GATE-026` — mitigation: Version matrix, signed rollback packages, upstream tracking and staged release rings.
- **RISK-016 [HIGH]** Anti-cheat rejects virtual adapter despite technically correct driver — proof `GATE-029` — mitigation: Report THIRD_PARTY_BLOCKED, pursue official cooperation; never conceal adapter.
- **RISK-017 [MEDIUM]** Linux-first host assumptions leak into protocol — proof `GATE-025` — mitigation: Backend contract tests and no host-OS-specific fields in stable protocol.
- **RISK-018 [HIGH]** Codex marks phases complete without hardware proof — proof `GATE-000` — mitigation: Machine-readable state machine, required evidence references, fresh breaker and Project Steward rejection of incomplete proof.
- **RISK-019 [HIGH]** Recovery reuses stale session/resource state from prior attempt — proof `GATE-020` — mitigation: Unique attempt/session epochs, immutable evidence/provenance and fail-closed resource revalidation.
- **RISK-020 [HIGH]** Builder and reviewer share assumptions and miss systemic defect — proof `GATE-000` — mitigation: Fresh independent BREAKER with no builder reasoning history and explicit assumption challenge.
- **RISK-021 [HIGH]** Allowed capability set is confused with exact required capability set — proof `GATE-003` — mitigation: Schemas separate allowed/required/observed capabilities and contract tests assert exact negotiation rules.
- **RISK-022 [HIGH]** Retry-until-green hides nondeterministic race — proof `GATE-026` — mitigation: Record attempt history, forbid blind reruns, require diagnosed mechanism and regression proof before rerun acceptance.
- **RISK-023 [HIGH]** Generated Markdown/YAML/JSON governance views drift and Codex follows stale copy — proof `GATE-BK-000` — mitigation: Canonical YAML + generated/validated views; CI source-view drift check.
- **RISK-024 [HIGH]** Hardware evidence is contaminated by concurrent job or stale driver/network state — proof `GATE-000` — mitigation: Exclusive leases, fingerprint/reset checks, contamination detection and runner quarantine.
- **RISK-025 [HIGH]** Fresh BREAKER unintentionally receives builder reasoning and reproduces builder assumptions — proof `GATE-BK-000` — mitigation: Explicit handoff manifest containing only requirements/invariants/commit/diff/evidence; separate session/attempt identity.
- **RISK-026 [HIGH]** Waiver/exception is used to mask missing proof — proof `GATE-BK-000` — mitigation: Waiver schema prohibits PASS override; validators and Steward enforce.
- **RISK-027 [HIGH]** Release/test signing credentials cross trust boundary — proof `GATE-028` — mitigation: Separate signing identities, no secrets in BuilderKit, release key isolation and audit.
