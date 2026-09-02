# Vendor Backends
`RGPU_BACKEND` isolates renderer/vendor specifics from session/resource/transport logic. Initial D3D11 host proof may use Neptune/virglrenderer + DXVK Native/Vulkan. Vulkan may use virglrenderer/Venus/gfxstream-derived paths. NVIDIA/AMD capabilities are negotiated, not hardcoded.

Vendor-specific extensions are optional feature namespaces. The generic protocol must continue working when a backend changes vendor or host OS. Stock vendor **host** drivers are expected external system dependencies; stock vendor Windows **client** drivers are not a v1 requirement.
