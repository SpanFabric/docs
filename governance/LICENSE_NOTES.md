# License Notes
SpanGPU project licensing remains `PROOF_REQUIRED` under TD-026 until PHASE-001 establishes exact file/component baselines and linking boundaries. The BuilderKit itself contains original planning/governance text and no copied proprietary source code.

Critical rules:
- preserve upstream file-level notices and license texts when code is actually imported;
- do not infer one license for a repository with mixed/component licensing;
- keep QEMU/GPL use at an external tool/test boundary unless an accepted TD documents a compatible distribution model;
- Juice public MIT control-plane code does not make unavailable proprietary Juice binaries open source and those binaries are excluded from the SpanGPU critical path;
- production distribution must pass the license manifest/SBOM gate.

## Project branding asset

`00-project/branding/SpanFabric-logo.png` is a project-generated branding asset supplied with the BuilderKit. It is not copied from an upstream dependency and must not be confused with third-party OSS source.
