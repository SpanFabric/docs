# OSS Reuse Map

| ID | Project | Classification | License | Used components | Rationale |
|---|---|---|---|---|---|
| UP-001 | Triton KMD / osy kvm-guest-drivers-windows | CONTROLLED FORK | BSD-3-Clause | viogpu/viogpu3d, viogpu/shared | Critical WDDM starting point; heavy SpanGPU boundary modifications expected. |
| UP-002 | Triton Mesa UMD | CONTROLLED FORK | MIT-family Mesa licensing; verify file-level notices | D3D10/11 UMD/Gallium frontend | D3D11 client starting point; keep patch provenance. |
| UP-003 | Neptune virglrenderer | CONTROLLED FORK | MIT | Neptune D3D host decoding, renderer integration | Host D3D proof path; transport-local assumptions must be separated. |
| UP-004 | DXVK Native UTM/osy branch | CONTROLLED FORK | zlib/libpng family; verify branch file licenses | native/headless D3D-to-Vulkan host support | Initially pinned/forked because branch-specific behavior may be needed. |
| UP-005 | upstream virtio-win | REFERENCE IMPLEMENTATION ONLY | BSD-3-Clause | upstream Windows virtio driver changes | Monitor and selectively backport into controlled KMD fork. |
| UP-006 | Mesa / Venus / Zink | VENDORED/ADAPTED COMPONENT | MIT and component notices | Venus Vulkan frontend/object model, Zink/OpenGL, common Mesa utilities | Prefer bounded patch queue/component adaptation; avoid unnecessary full fork divergence. |
| UP-007 | virglrenderer upstream | REFERENCE IMPLEMENTATION ONLY | MIT | renderer architecture, Venus host | Track upstream against Neptune fork. |
| UP-008 | gfxstream | VENDORED/ADAPTED COMPONENT | Apache-2.0 | API codegen, encoder/decoder patterns, end-to-end test patterns | Selective reuse/adaptation behind SpanGPU protocol. |
| UP-009 | MsQuic | DIRECT DEPENDENCY | MIT | QUIC/TLS transport | Normal replaceable dependency; protocol must not depend on MsQuic internals. |
| UP-010 | libfabric | DIRECT DEPENDENCY | BSD/GPL component mix; verify selected provider/files | optional controlled-network/RDMA transport | Optional fast-path dependency, not WAN correctness baseline. |
| UP-011 | QEMU | DIRECT DEPENDENCY | GPL-2.0-or-later and component licenses | development/test harness, virtio-gpu reference device | External dev/test dependency; do not copy GPL core into permissive SpanGPU code without explicit TD. |
| UP-012 | LUPINE | VENDORED/ADAPTED COMPONENT | Apache-2.0 | GPU-over-IP sessions, RPC/handle patterns, future compute ideas | Selective code/architecture source, not graphics client core. |
| UP-013 | libvfio-user | REFERENCE IMPLEMENTATION ONLY | BSD-3-Clause | future PCIe/device remoting research | Reference/experimental branch only. |
| UP-014 | Microsoft GPU-PV | REFERENCE IMPLEMENTATION ONLY | Proprietary Windows platform documentation/API | WDDM virtualization architecture concepts | Architectural reference, not redistributable dependency. |
| UP-015 | NVIDIA vGPU | REFERENCE IMPLEMENTATION ONLY | Proprietary/commercial | scheduler/trust/virtualization concepts | Reference only; do not make required dependency. |
| UP-016 | AMD virtualization / SR-IOV | REFERENCE IMPLEMENTATION ONLY | Vendor-specific/proprietary components | host virtualization concepts | Reference only. |
| UP-017 | Virtio specification | REFERENCE IMPLEMENTATION ONLY | OASIS specification terms | device/protocol concepts | Normative reference for reused virtio semantics only. |
| UP-018 | PCIe-over-network 2026 prototype | REFERENCE IMPLEMENTATION ONLY | Research publication; source availability/license must be verified | future stock-driver research | Do not treat blog proof as production code. |
| UP-019 | Juice Labs public repository | REJECTED | MIT for public repo; separate proprietary terms/binaries | none in critical runtime | Reference/competitive analysis only; incomplete proprietary GPU/data plane and injection-based Windows path conflict with core requirements. |
| UP-020 | wgpu-remote | REFERENCE IMPLEMENTATION ONLY | VERIFY_AT_BOOTSTRAP | QUIC graphics RPC ideas | Research reference only; application API mismatch. |
