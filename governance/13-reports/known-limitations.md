# Known Limitations
- No SpanGPU production implementation exists yet.
- Windows secondary-adapter viability of the selected controlled fork is unproven until GATE-001.
- Legitimate Windows presentation is unproven until GATE-006.
- Remote VRAM/fence/recovery WAN semantics are proof-required.
- D3D12 is not assumed; GATE-024 may require architecture refinement while preserving core boundaries.
- Anti-cheat acceptance cannot be guaranteed technically and remains third-party controlled.
- Upstream exact SHAs/licenses are intentionally UNPINNED_REQUIRES_BOOTSTRAP until PHASE-001; no SHA is invented.
