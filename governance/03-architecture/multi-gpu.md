# Local / Remote Multi-GPU
SpanGPU is an additional adapter. Local GPU remains active. Normal Windows/application adapter preference is the first selection mechanism. The architecture does not promise transparent live migration of a running graphics device to the local GPU after failure; controlled device loss + application restart is an acceptable v1 fallback if documented.

Future multiple remote GPUs use negotiated GPU offers and stable backend identities; the protocol must not assume exactly one physical GPU forever.
