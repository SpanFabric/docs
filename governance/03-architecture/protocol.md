# SpanGPU Protocol
## Stable layers
- `RGPU_SESSION`: version/capability/auth/session epoch.
- `RGPU_OBJECT`: object identity/type/lifetime envelope.
- `RGPU_RESOURCE`: create/version/upload/readback/evict/cache identity.
- `RGPU_COMMAND_STREAM(api)`: API-specific encoded command batches.
- `RGPU_FENCE`: queue-scoped signals, waits, timeline/completions.
- `RGPU_PRESENT`: present surface/frame metadata and return coordination.
- `RGPU_TELEMETRY`: versioned metrics/events/evidence correlation.

## Channel model
Control is reliable/ordered. Command ordering is **per required GPU queue**, not global. Resources use parallel bulk streams. Fence/completion messages are small and prioritized. Telemetry may permit lossy delivery where it is not correctness evidence. Frame return has independent congestion/latency handling.

## Version and capability model
Handshake records `allowed`, `required`, and `observed/negotiated` capability sets separately. Mandatory unknown semantics fail closed. Session epochs invalidate stale messages and handles. Retryable mutations require idempotency/sequence semantics.

## Serialization
TD-006 remains PROOF_REQUIRED. No final wire format is frozen until GATE-003 benchmarks and compatibility tests prove a concrete encoding.
