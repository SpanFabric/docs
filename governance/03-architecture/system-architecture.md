# System Architecture
## Selected architecture candidate
A normal Windows SpanGPU adapter is implemented with a controlled Triton/virtio-derived WDDM frontend. A privileged **user-mode SpanGPU client service** owns session management, QUIC/TLS, command batching, resource transfer/cache metadata and reconnect logic. The wire protocol is semantic and versioned; it does not expose virtqueues or local shared-memory assumptions. The remote host owns VRAM/resources and decodes graphics command streams into vendor-neutral renderer backends that use stock NVIDIA/AMD host drivers.

```text
LOCAL WINDOWS
Application → DX/Vulkan/OpenGL runtime → API UMD/ICD → WDDM KMD
                                      ↘ local shadow/object state
KMD → versioned local ABI/rings → SpanGPU Client Service
Client Service → command/resource/fence streams → QUIC → Host

REMOTE HOST
Session → validated decoder → GPU scheduler + VRAM/resource/cache authority
        → vendor-neutral renderer backend → stock NVIDIA/AMD host driver → physical GPU
        → present/frame return → local presentation path
```

## Planes and paths
- **Control plane:** auth, session/capability/version negotiation, health, configuration, drain/teardown.
- **Data plane:** graphics command batches, resource payloads/readbacks, frame return.
- **Fast path:** already-known resources + queued command batches + asynchronous completion updates.
- **Slow path:** resource creation/upload/readback, cache miss, capability change, recovery, shader/pipeline cold creation.

## State ownership
- **Authoritative local:** application CPU/RAM/storage/input; local GPU; client policy/config; current WDDM object handles as Windows owns them.
- **Authoritative remote:** remote VRAM residency, remote resource generations, physical-GPU execution/completion.
- **Shadow local:** remote object metadata, fence/completion snapshots, cache inventory, staged resource data.
- **Persistent cache:** content payloads/metadata validated against protocol/backend capability; never resource-lifetime authority.

## Architecture proof rule
The candidate remains provisional where TDs say PROOF_REQUIRED. Failure of a blocker gate triggers an architecture revision TD before feature expansion; Codex may not hide a blocker behind a per-game/API interception shortcut.
