# Finding Lifecycle
`OPEN → ACCEPTED → FIXED_PENDING_REVIEW → VERIFIED`, or `OPEN → REJECTED_WITH_EVIDENCE`. History is append-only. BLOCKER/HIGH requires concrete mechanism, violated ID, impact/severity, remediation and regression expectation. A remediation creates a new builder attempt and a new fresh BREAKER attempt before VERIFIED.
