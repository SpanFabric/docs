# OSS Reuse Report
Research estimate: approximately **30–35% direct OSS**, **35–40% modified/adapted/forked OSS**, **25–35% genuinely greenfield**. Risk is not proportional to lines of code: WDDM/WAN VRAM/fence/presentation/recovery boundaries dominate engineering difficulty.

Controlled forks: Triton KMD, Triton Mesa UMD, Neptune virglrenderer, DXVK Native UTM/osy branch. Direct dependencies currently include MsQuic, optional libfabric fast-path tooling and QEMU as dev/test harness (license boundary explicit). Adapted/reference components remain replaceable and are not presumed production-ready simply from README claims.
