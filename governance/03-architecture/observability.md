# Observability / Evidence
Every end-to-end run has `attempt_id`, `session_epoch`, commit/build IDs and evidence bundle. Structured events cover adapter/session state, command batches, resource transfers/cache, queues/fences, network, host GPU, present path, device loss/recovery and security denials.

Evidence is immutable by attempt. Builder evidence, BREAKER evidence, remediation evidence and fresh BREAKER evidence are separate. Current project state points to evidence; it does not overwrite it.
