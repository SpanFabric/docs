# Memory / VRAM
Remote VRAM is explicitly remote-authoritative. Local system memory and remote GPU memory are not made magically coherent over WAN.

## Resource states
`NEW_LOCAL_METADATA → REMOTE_CREATED → PAYLOAD_UPLOADING → REMOTE_VALID → GPU_RESIDENT/EVICTABLE → DESTROYED`. Mutable resources additionally carry generation/range state. Cache presence is separate from residency.

## Mapping
CPU-visible maps are classified by semantics: local staging, explicit upload, explicit readback, or unsupported capability. Persistent/coherent same-machine mappings from virtio/Venus cannot be assumed over WAN.

## IDs
Never serialize pointers as identity. Resource IDs include session epoch/type/sequence and immutable payloads may additionally use cryptographic content hashes.
