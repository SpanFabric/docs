# Landscape Summary
## Strongest reusable families
- **Triton/virtio-win Windows WDDM:** closest open Windows adapter/KMD/UMD start; experimental and VM-local.
- **Neptune/virglrenderer + DXVK Native:** matching D3D11 host proof path.
- **Mesa Venus:** strong Vulkan object/command serialization but local/shared-memory renderer assumptions must be replaced.
- **gfxstream:** mature generated graphics command encode/decode and testing patterns.
- **MsQuic:** default replaceable QUIC/TLS WAN transport.
- **LUPINE:** modern OSS GPU-over-IP compute/session concepts, not a WDDM graphics solution.
- **QEMU/virtio-gpu:** device/resource/fence reference and development harness, not the WAN wire protocol.
- **libvfio-user / PCIe-over-network:** future stock-driver research only.

## Commercial/proprietary references
Microsoft GPU-PV, NVIDIA vGPU and AMD virtualization are architectural references. Their existence validates virtualization patterns but does not give SpanGPU an independent OSS data path.

## Rejected critical foundation
Juice Labs is not used as the critical runtime foundation. Research found the public repository does not contain the complete GPU/data plane, while Windows launching uses unavailable/proprietary binaries/injection/ICD mechanisms. Its product behavior remains a useful competitive/reference target only.
