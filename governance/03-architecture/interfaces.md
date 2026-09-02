# Stable Interface Contracts
| Interface | Producer → Consumer | Source of truth | Version owner | Failure/retry/idempotency |
|---|---|---|---|---|
| RGPU_DRIVER_ABI | KMD/UMD ↔ client service | Windows driver/object state + explicit service messages | windows repo | bounded local queues; version mismatch fails closed; no blind retry |
| RGPU_SESSION | client service ↔ host | negotiated session/epoch | platform | reconnect creates/revalidates epoch; auth required |
| RGPU_OBJECT | frontends ↔ host decoders | object owner by type | platform | stale epoch rejected; create/destroy sequence explicit |
| RGPU_RESOURCE | client resource mgr ↔ host VRAM mgr | **host** for remote resource/residency | platform | idempotent content lookup; mutation generation/sequence explicit |
| RGPU_COMMAND_STREAM | API frontend ↔ API decoder | API semantics + queue order | platform + owning API component | batch sequence/queue order; invalid command fails session/work item safely |
| RGPU_FENCE | queues ↔ completion manager | remote GPU execution completion | platform | duplicate completion safe; stale rejected; waits explicit |
| RGPU_PRESENT | host frame return ↔ Windows presentation | selected present state machine | windows+host via TD-012 | loss maps to bounded device/present failure |
| RGPU_BACKEND | host core ↔ renderer/vendor backend | host negotiated capability/resource state | host | backend errors map to structured GPU/device loss |
| RGPU_TRANSPORT | protocol ↔ MsQuic/RDMA plugin | protocol session semantics, not transport internals | platform | connection retries cannot replay mutations without idempotency |
| RGPU_CACHE | resource manager ↔ cache | host resource generation is authoritative; cache is projection | platform/host | digest validation; corrupt/stale entry becomes miss |
| RGPU_TELEMETRY | all components → evidence | component state; evidence store immutable | evals/docs schema | telemetry loss cannot fabricate correctness PASS |

Every interface change must execute the Boundary Audit in `09-codex/boundary-audit-template.md`.
