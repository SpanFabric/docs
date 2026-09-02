# Root AGENTS Template
Mission: implement only the active SpanGPU phase while preserving global architecture. Required reading: BuilderKit START HERE, invariants, active phase, linked TDs/gates, interfaces, repo contract, verification contract.

Forbidden: hidden context assumptions; future-scope implementation; fake test success; retry-until-green; changing control-plane metadata merely to make validators pass; bypassing anti-cheat; introducing unavailable proprietary critical path.

Required: explicit assumptions, Boundary Audit on changed stable interfaces, immutable attempt/evidence metadata, fresh BREAKER before acceptance.
