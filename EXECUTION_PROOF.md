# Qualcomm Execution Proof

This file separates **vendor-published reference performance** from **our own execution evidence**.

## CAIOS Device Cloud session — real Qualcomm hardware

A real Qualcomm Device Cloud Interactive Session has been created and connected for the CAIOS EdgeCare submission.

- Project / session name: `CAIOS EdgeCare`
- QDC interactive session / report ID: `822588`
- Report URL: `https://qdc.qualcomm.com/reports/job/interactive/822588`
- Target platform: `Snapdragon X2 Elite`
- Device class: `Compute Reference Design`
- Platform identifier shown by QDC: `SC8480X`
- Operating system: `Windows 11`
- QDC state captured after connection: `Running`
- QDC device streaming: connected and interactive desktop visible
- Submitted: `09/15/26 03:35:26 AM` (as displayed by QDC)
- Started: `09/15/26 03:38:05 AM` (as displayed by QDC)

This proves that CAIOS successfully acquired, started, and connected to a real Qualcomm-hosted Snapdragon X2 Elite device session.

## GenieX binary verification

The official GenieX CLI was installed to:

```text
C:\Users\Asus\AppData\Local\GenieX CLI\geniex.exe
```

Verification captured from PowerShell:

- File size: `33,963,008` bytes
- Windows PE header begins with `4D 5A` (`MZ`)
- PE machine type: `0xAA64` = **ARM64**

This rules out an x64/x86 binary mismatch. Despite the ARM64 PE architecture, attempting to run the binary on the current QDC Windows image returns:

```text
The specified executable is not a valid application for this OS platform.
```

At this point the remaining issue is most likely either the remote Windows OS architecture / image compatibility, or a GenieX build compatibility issue with this QDC Windows image.

## Next diagnostic gate

Run these exact commands in PowerShell:

```powershell
$env:PROCESSOR_ARCHITECTURE
[System.Runtime.InteropServices.RuntimeInformation]::OSArchitecture
```

Expected for native Windows ARM64:

```text
ARM64
Arm64
```

If the OS reports `AMD64` / `X64`, then the ARM64 GenieX binary cannot run even though the underlying Qualcomm hardware is Snapdragon X2 Elite.

If the OS reports `Arm64`, then this becomes a GenieX/QDC-image compatibility issue rather than a CPU architecture mismatch.

## Vendor reference only — not our execution

Qualcomm AI Hub publishes Snapdragon support and model-card performance data for supported models. Those numbers are useful for judging model/device fit, but they are **not** presented here as CAIOS execution evidence.

## CAIOS runtime proof

The repository demo wrapper separately verifies policy behavior around the local provider boundary:

1. `LOCAL_OK` — local provider accepted.
2. `LOW_RISK_FALLBACK` — approved cloud fallback allowed and recorded.
3. `HIGH_RISK_FAIL_CLOSED` — no silent fallback; safe degradation returned.

Public demo: https://www.caios.my/demo/edgecare
