# Windows Client
## Components
1. **WDDM KMD:** adapter/device/allocation/submission/fence/device-loss integration. It contains no general WAN protocol stack.
2. **API UMD/ICDs:** D3D11 first from Triton/Mesa; later Vulkan via Venus-derived logic, OpenGL via Mesa strategy, legacy/D3D12 by gated tracks.
3. **SpanGPU client service:** authenticated session, transport, batching, resource transfer/cache, telemetry, recovery orchestration.
4. **Local shadow/resource manager:** object identities, staged CPU-visible data, dirty ranges and cache inventory; non-authoritative for remote VRAM.
5. **Presentation client path:** PROOF_REQUIRED under TD-012/GATE-006.
6. **Diagnostics/runner:** ETW, event logs, dump capture, driver health and attempt/evidence identity.

## Client trust boundary
Network data never reaches KMD as raw unbounded packets. The user-mode service validates protocol/session state and exposes a narrow versioned local ABI; KMD still validates all user-mode inputs it consumes.

## Coexistence
SpanGPU must enumerate as an additional adapter. Local GPU remains usable for the desktop and, where the chosen presentation architecture permits, decode/composition. Live workload failover is not assumed.
