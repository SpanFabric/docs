# Unresolved Research / Proof Required
## Presentation
STATUS: PROOF_REQUIRED  
DECISION_OWNER: TD-012  
BLOCKING_GATE: GATE-006  
OPTIONS: render-only cross-adapter path; legitimate virtual-display/presentation path; another WDDM-supported mechanism discovered during prototype.  
EVIDENCE_REQUIRED: normal Windows presentation with unmodified third-party application, no external streaming-window substitution.

## D3D12
STATUS: PROOF_REQUIRED  
DECISION_OWNER: TD-022  
BLOCKING_GATE: GATE-024  
OPTIONS: extend common WDDM/session core with a D3D12 UMD path; revise common client core if evidence proves incompatibility.  
EVIDENCE_REQUIRED: bounded D3D12 sample demonstrating allocation, queue, sync, resource and present requirements against the existing core.

## Remote VRAM/GPUVA
STATUS: PROOF_REQUIRED  
DECISION_OWNER: TD-007  
BLOCKING_GATE: GATE-007  
OPTIONS: explicit staging/shadow state with remote authority; narrower mapping model; revised allocation model consistent with WDDM.  
EVIDENCE_REQUIRED: randomized resource lifetime/mapping/eviction/readback tests on hardware.

## Protocol serialization
STATUS: PROOF_REQUIRED  
DECISION_OWNER: TD-006  
BLOCKING_GATE: GATE-003  
OPTIONS: generated binary schema; compact custom fixed-format envelopes; hybrid generated envelopes plus API-specific streams.  
EVIDENCE_REQUIRED: deterministic compatibility tests plus command-rate/decode/bandwidth benchmark before freezing the wire format.

## Project license
STATUS: PROOF_REQUIRED  
DECISION_OWNER: TD-026  
BLOCKING_GATE: GATE-000  
OPTIONS: permissive project license compatible with selected integrations; split licensing if unavoidable and justified.  
EVIDENCE_REQUIRED: pinned file-level provenance/license matrix for copied/adapted/linked components.
