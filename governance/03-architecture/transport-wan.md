# Transport / WAN
MsQuic is the default direct dependency behind `RGPU_TRANSPORT`; RDMA/libfabric may later implement the same contract in controlled networks.

Separate logical traffic prevents resource uploads from head-of-line blocking commands/completions. Backpressure is explicit and bounded. The test baseline includes LAN and 1/5/10/20/30/40 ms RTT plus jitter, loss, bandwidth constraints, temporary and hard disconnect.

WAN correctness is invariant even where playability is not. At high RTT the acceptable result may be `SUPPORTED_WITH_LIMITATIONS`; state corruption or hidden local fallback is never acceptable.
