# Scope
## In scope
Windows WDDM client adapter; API UMD/ICDs; user-mode client networking service; versioned semantic command/resource/fence protocol; QUIC WAN transport; remote-authoritative VRAM/resource/cache; host renderer/backend; NVIDIA+AMD host acceleration; presentation return; diagnostics; fault/recovery; signing/trust path; compatibility evidence; controlled upstream forks; optional later compute.

## v1-valid narrowing
Windows 11, D3D11 first, Linux reference host, one GPU/session allowed, session-local cache allowed if persistent-cache-compatible, test signing during development. These constraints may narrow implementation but may not alter the core boundaries.
