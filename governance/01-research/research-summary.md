# Research Summary
This is a frozen planning summary of SpanGPU Research 1–3. Implementation must not silently replace these findings; new contradictory evidence requires a TD/research amendment.

## RF-001 — GPU-PV validates transparent Windows GPU paravirtualization
Microsoft WDDM GPU-PV keeps application graphics runtimes unchanged while virtualizing GPU execution.
**Evidence/source:** https://learn.microsoft.com/en-us/windows-hardware/drivers/display/gpu-paravirtualization

## RF-002 — GPU-PV mirrors selected state locally
Microsoft deliberately keeps some object state local to avoid expensive host communication; SpanGPU needs the same principle across WAN.
**Evidence/source:** https://learn.microsoft.com/en-us/windows-hardware/drivers/display/gpu-paravirtualization

## RF-003 — Triton provides an OSS Windows WDDM D3D11 starting point
UTM/osy Triton combines a virtio-derived WDDM KMD with a Mesa-based D3D UMD and is the closest open Windows client starting point found.
**Evidence/source:** https://blog.getutm.app/2026/introducing-triton-directx-11-driver-for-qemu/

## RF-004 — Triton is experimental and VM-local
Triton/Neptune proves important pieces but assumes VM-local virtio transport and cannot be treated as a WAN-ready production driver.
**Evidence/source:** https://github.com/osy/kvm-guest-drivers-windows/tree/neptune

## RF-005 — Neptune supplies a matching host-side D3D virtualization path
UTM Neptune/virglrenderer and DXVK-native provide a source-available host path for the Triton D3D11 prototype.
**Evidence/source:** https://blog.getutm.app/2026/introducing-neptune-direct3d-virtualization-for-qemu/

## RF-006 — virtio-gpu is a useful device/resource/fence model
virtio-gpu defines device, resource, command and fence concepts that are useful at the Windows boundary.
**Evidence/source:** https://www.qemu.org/docs/master/system/devices/virtio/virtio-gpu.html

## RF-007 — Unmodified virtio transport is WAN-hostile
Virtqueue/shared-memory/blob assumptions target VM-local latency and cannot be tunneled packet-for-packet over WAN.
**Evidence/source:** https://www.qemu.org/docs/master/system/devices/virtio/virtio-gpu.html

## RF-008 — Venus provides reusable Vulkan object and command serialization
Mesa Venus serializes Vulkan over virtio-gpu and offers strong object-lifetime/queue patterns.
**Evidence/source:** https://docs.mesa3d.org/drivers/venus.html

## RF-009 — Venus memory transport needs replacement
Venus relies on host-visible/blob/shared memory semantics unsuitable for remote-authoritative WAN VRAM.
**Evidence/source:** https://docs.mesa3d.org/drivers/venus.html

## RF-010 — gfxstream provides mature graphics command-streaming patterns
gfxstream offers API encoding/decoding, code generation and end-to-end test patterns useful for SpanGPU.
**Evidence/source:** https://github.com/google/gfxstream

## RF-011 — LUPINE proves modern open GPU-over-IP for compute
LUPINE demonstrates source-available network GPU sessions/handle remoting for CUDA/NVML and is valuable for session and RPC patterns.
**Evidence/source:** https://github.com/lupinemachines/lupine

## RF-012 — Juice is not an independent OSS core
The public Juice repository does not contain the complete graphics/GPU data plane required for an independent fork.
**Evidence/source:** https://github.com/Juice-Labs/Juice-Labs

## RF-013 — Juice Windows path uses proprietary/injection components
The public Windows launcher calls unavailable/proprietary juiceclient.dll and launch.exe and uses injection/ICD mechanisms, conflicting with the North Star.
**Evidence/source:** https://github.com/Juice-Labs/Juice-Labs

## RF-014 — MsQuic is a strong default WAN transport building block
MsQuic provides maintained cross-platform QUIC/TLS with streams and is appropriate as a replaceable transport dependency.
**Evidence/source:** https://github.com/microsoft/msquic

## RF-015 — RDMA/RoCE can be an optional controlled-network fast path
RDMA/libfabric may benefit datacenter/LAN deployment but cannot be the WAN correctness baseline.
**Evidence/source:** https://github.com/ofiwg/libfabric

## RF-016 — PCIe-over-network is a research path, not the primary WAN design
A 2026 prototype initialized a remote RTX via stock Linux NVIDIA driver, but did not prove Windows WDDM, DMA, gaming or WAN frame-time viability.
**Evidence/source:** https://leoustc.com/blog-2026-08-16-pcie-over-network/

## RF-017 — Stock vendor driver on the client is not a safe baseline assumption
NVIDIA/AMD client hardware interfaces are proprietary and vendor-controlled; SpanGPU must not depend on reverse-emulating them for v1.
**Evidence/source:** https://docs.nvidia.com/vgpu/

## RF-018 — Stock vendor drivers are feasible on the host
Host rendering can target normal NVIDIA/AMD Vulkan/OpenGL/vendor stacks behind a SpanGPU backend abstraction.
**Evidence/source:** https://docs.mesa3d.org/

## RF-019 — D3D11 is the lowest-risk first graphics proof
Existing Triton/Neptune code makes D3D11 the cheapest architecture-valid proof before D3D12.
**Evidence/source:** https://blog.getutm.app/2026/introducing-triton-directx-11-driver-for-qemu/

## RF-020 — D3D12 remains a major greenfield risk
No researched drop-in open D3D12 WDDM path meets the target; D3D12 requires its own proof gate.
**Evidence/source:** https://blog.getutm.app/2026/introducing-triton-directx-11-driver-for-qemu/

## RF-021 — OpenGL can likely consolidate through Mesa/Zink
Zink can implement desktop OpenGL over Vulkan, reducing independent host backend complexity where compatibility permits.
**Evidence/source:** https://docs.mesa3d.org/drivers/zink.html

## RF-022 — Remote VRAM must be remote-authoritative
A WAN design cannot pretend remote VRAM is synchronously shared local memory; explicit ownership, upload, eviction and readback semantics are required.
**Evidence/source:** Research 1–3 synthesis

## RF-023 — Fence virtualization is a central WAN correctness problem
Synchronous fence waits become catastrophic at 5–40 ms RTT; completions must be asynchronous unless application semantics require blocking.
**Evidence/source:** Research 1–3 synthesis

## RF-024 — Persistent content-addressed caching is essential for WAN viability
Stable resources, shaders and pipelines should be uploaded once and subsequently referenced by IDs/hashes.
**Evidence/source:** Research 1–3 synthesis

## RF-025 — Presentation is an independent architecture proof
Rendering a remote frame is insufficient; a normal Windows/DWM-compatible presentation path must be proven without a streaming-window hack.
**Evidence/source:** Research 1–3 synthesis

## RF-026 — Disconnect must degrade to controlled device loss
WAN failure must not corrupt driver state or cause a BSOD; TDR/device-removal/recovery semantics require explicit design and hardware testing.
**Evidence/source:** Research 1–3 synthesis

## RF-027 — Local and remote GPUs must coexist
SpanGPU should enumerate as an additional adapter and preserve the local GPU for desktop, decode and fallback where the API/application permits.
**Evidence/source:** Research 1–3 synthesis

## RF-028 — Anti-cheat acceptance is externally constrained
Signing, Secure Boot, attestation and vendor cooperation improve trust but cannot force EAC/BattlEye/Vanguard or any third party to accept the adapter.
**Evidence/source:** Research 1–3 synthesis

## RF-029 — Critical path should remain open or controlled
Architecture independence requires controlled forks/replaceable dependencies and excludes unavailable proprietary data-plane binaries.
**Evidence/source:** Research 1–3 synthesis

## RF-030 — Full North Star is mostly reuse plus high-risk adaptation
Estimated code reuse: 30–35% direct OSS, 35–40% modified/forked OSS, 25–35% greenfield; engineering risk is concentrated in modified/greenfield boundaries.
**Evidence/source:** Research 3 engineering estimate
