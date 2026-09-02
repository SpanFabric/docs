# Source-Code Deep Dive Summary
## Triton / virtio-win
Source inspection identified `viogpu/viogpu3d` and shared virtio GPU structures as the primary Windows KMD starting point, plus osy `virtio-win-mesa` for D3D UMD work. Reusable areas include adapter lifecycle, DDI structure, allocation/command scaffolding and guest/host object concepts. Major refactor zones are shared-memory/blob assumptions, completion/fence latency and any QEMU/virtqueue-specific transport coupling.

## Neptune / virglrenderer
Neptune provides the matching D3D host decode/render path and is valuable for the first D3D11 proof. It remains VM-local; SpanGPU must introduce a transport-neutral semantic boundary instead of extending rings/virtqueues directly over WAN.

## Mesa Venus
The reusable core is Vulkan object lifetime, queue/command handling and serialization. `vn_renderer_virtgpu`-style local kernel/mmap integration is reference material, not a WAN transport.

## gfxstream
High-value reuse: API code generation, encoder/decoder patterns and end-to-end testing. Low-value for SpanGPU: assuming its existing guest/hypervisor transport is the final Windows/WAN architecture.

## LUPINE
High-value ideas: session routing, remote handles, generated API RPC and multi-GPU/compute experience. It does not supply WDDM graphics adapter/presentation semantics.

## Juice
Public orchestration code is not the missing SpanGPU data plane. Its Windows path references `juiceclient.dll`/`launch.exe` and injection; therefore no dependency on those components is allowed.

## Source-level bootstrap requirement
Phase 00/01 must pin exact commits and create a file/symbol/license inventory before copying/adapting source. This BuilderKit intentionally does not invent unverified commit SHAs or exact file-license claims.
