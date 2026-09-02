# Remote Host
## Components
- session/auth/capability manager;
- validated command/resource decoder;
- GPU scheduler (v1 may be one session/GPU);
- remote-authoritative VRAM/resource manager;
- content-addressed resource/cache service;
- vendor-neutral backend ABI;
- NVIDIA and AMD backend integrations using stock host drivers;
- frame export/encoder/return path;
- telemetry, quotas, fault containment and health/drain controls.

## Authority
The host is authoritative for remote resource generation, VRAM residency and physical execution completion. A client shadow/cache hit cannot overrule host state. Host restart changes the session epoch unless a later proof establishes durable recovery semantics.
