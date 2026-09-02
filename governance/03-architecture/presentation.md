# Presentation
STATUS: PROOF_REQUIRED  
DECISION_OWNER: TD-012  
BLOCKING_GATE: GATE-006

A successful remote render is not sufficient. SpanGPU must present through a legitimate Windows graphics/display path usable by unmodified applications. Candidate mechanisms may include a render-only adapter plus supported cross-adapter/composition path or another WDDM-supported virtual-display mechanism proven during the prototype. A separate streaming window can be a debug tool but **cannot satisfy GATE-006**.

Metrics include remote render completion, export/copy/encode time, network frame-return time, decode/copy/composition time and final present timing where available.
