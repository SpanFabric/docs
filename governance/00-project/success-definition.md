# Success definition
The full North Star is achieved when unmodified representative Windows applications across the targeted graphics APIs can select a normal SpanGPU adapter, execute on remote NVIDIA/AMD hardware with remote-authoritative VRAM over realistic WAN profiles, present correctly on the local desktop, coexist with the local GPU, survive defined failures safely, and operate without a proprietary black-box critical data plane. Third-party anti-cheat acceptance remains an external compatibility dimension and is never conflated with rendering correctness.

A v1 can ship earlier only if it is architecture-valid: D3D11-first is acceptable; replacing the WDDM/semantic-WAN/remote-VRAM architecture later is not.
