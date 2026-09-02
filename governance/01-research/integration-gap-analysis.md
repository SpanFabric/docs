# Integration / Gap Analysis
The leading architecture family is a **hybrid WDDM/virtio-derived frontend with semantic WAN command/resource/fence transport**. It scored best in Research 3 because it combines Windows compatibility potential, WAN control, remote-VRAM semantics and OSS independence.

## Highest-risk greenfield/adaptation gaps
1. Stable modern secondary WDDM adapter.
2. Clean KMD↔user-service boundary without VM-bus dependency.
3. Windows Present/DWM path for remote-rendered surfaces.
4. Remote-authoritative VRAM/GPUVA/resource semantics.
5. Virtual fences/queue ordering without synchronous WAN serialization.
6. Controlled TDR/device-loss/reconnect semantics.
7. D3D12 on the same architectural core.
8. Vendor-neutral host capability/backend model.
9. Production signing/Secure Boot/trust.
10. Evidence-backed compatibility and third-party anti-cheat classification.

## Reuse estimate
- direct OSS: **30–35%** of final code;
- modified/controlled OSS: **35–40%**;
- greenfield: **25–35%**.
Engineering effort is risk-heavier than those code percentages because most hard correctness work is at WDDM, memory, synchronization, presentation and recovery boundaries.
