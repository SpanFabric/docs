# Caching
Immutable payloads use content-addressed identities. Session-local cache is acceptable in early phases; the schema remains persistent-cache capable. Mutable resource generations are not replaced by content-cache state.

Cache lookup validates format/layout/capability/protocol/backend compatibility. Corruption yields miss/reupload and evidence. Shader/pipeline caches are permitted only where their native API/driver semantics support safe serialization/reuse.
