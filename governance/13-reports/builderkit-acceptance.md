# BuilderKit Acceptance Result

**GATE-BK-000: PASS for packaged metadata/control-plane validation**

BuilderKit v1.2.3 incorporates the two HIGH findings from the fresh v1.2.1 pre-apply BREAKER: fixed mutation-target enforcement and global materialization preflight plus apply journaling/forward recovery. Cross-platform semantic tests, metadata/traceability/upstream validators, conflict zero-write regression, and injected I/O recovery regression must pass from a clean extraction before packaging.

The Windows-specific target-rejection and PowerShell 5.1 regressions are embedded and are **mandatory Stage-A evidence on the user's Windows machine**; this release does not claim those Windows executions occurred in the packaging environment. This PASS applies only to BuilderKit package consistency, not to PHASE-000 Stage A, Stage B, GATE-000, WDDM, or GPU functionality.


v1.2.3 additionally fixes F-000-03 and requires Manual Verification Bridge v1 materialization before first push/merge. Real Windows PowerShell 5.1 proof remains a Stage-A requirement.
