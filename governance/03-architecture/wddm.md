# WDDM Strategy
Triton `viogpu3d` is a **controlled starting fork**, not an assertion that its VM-local design is already SpanGPU-correct. Reuse DDI/lifecycle/allocation/submission scaffolding where source-level review confirms compatibility. Replace or isolate assumptions about virtqueues, QEMU, local blob/shared memory and cheap completion.

## Mandatory WDDM proofs
- adapter enumerates beside local GPU;
- allocation lifecycle and GPUVA/resource mapping are defined;
- command submission can cross a user-mode service boundary safely;
- remote completion/TDR timing does not deadlock Windows;
- presentation integrates with a legitimate Windows path;
- disconnect maps to controlled device loss/recovery rather than kernel corruption.

## Kernel rule
If a desired optimization requires moving QUIC/cache/reconnect logic into KMD, stop and open a TD. Kernel code is deliberately minimized because every parsing/concurrency failure has BSOD blast radius.
