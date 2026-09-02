# Recovery / Failure Semantics
Recovery is **attempt-scoped**, never a silent continuation of stale state.

1. Detect transport/host/GPU failure and freeze new dependent work.
2. Capture evidence and classify completion certainty for in-flight mutations.
3. Move to controlled device-loss or a new recovery epoch.
4. If reconnect is permitted, authenticate again, negotiate capabilities, create a new attempt/session epoch and revalidate resources/cache before reuse.
5. Ambiguous operations resolve through idempotency/reconciliation rules; never assume completion.
6. Bound retry count/time. No infinite reconnect and no retry-until-green.

Historical evidence and current publication/project state use different identifiers/digests. A previous PASS never substitutes for a current attempt.
