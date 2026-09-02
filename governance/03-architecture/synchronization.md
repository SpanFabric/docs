# Synchronization
SpanGPU preserves API/WDDM ordering while aggressively avoiding WAN waits.

- queue order is authoritative per queue;
- cross-queue dependencies are explicit edges;
- local shadow fence state advances only from authoritative completion;
- completion messages are asynchronous and prioritized;
- duplicate completion is idempotent; stale epoch completion is rejected;
- CPU readback/semantic waits may block and must be measured;
- no ordinary draw/submit requires an acknowledgement before independent future work is prepared.

GATE-009 is the central correctness/performance proof. Randomized dependency graphs and disconnects must attack the implementation; a benchmark that merely renders frames is insufficient.
