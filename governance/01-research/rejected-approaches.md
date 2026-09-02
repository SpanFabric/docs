# Rejected / Contained Approaches
- **Juice as project base:** rejected critical foundation; incomplete/proprietary GPU data plane and injection-based Windows path.
- **Raw virtio packet/virtqueue tunnel over WAN:** rejected as main design because VM-local shared-memory and synchronization assumptions create RTT dead ends.
- **API interception/DLL injection:** reference/prototype technique only; violates primary North Star and weakens launcher/anti-cheat universality.
- **PCIe-over-network as v1:** contained research branch only; insufficient proof for Windows WDDM, WAN DMA, presentation and recovery.
- **Stock NVIDIA/AMD Windows client driver as mandatory v1:** rejected dependency assumption without vendor-supported remote-device interface.
- **Whole remote gaming VM:** out of scope; CPU/RAM/OS/application must remain local.
- **Automatic critical-fork updates:** rejected; upstream adoption is human/steward gated.
