# Qualcomm Execution Proof

This file separates **vendor-published reference performance** from **our own execution evidence**.

## CAIOS Device Cloud session — real Qualcomm hardware

A real Qualcomm Device Cloud Interactive Session has been created and connected for the CAIOS EdgeCare submission.

- Project / session name: `CAIOS EdgeCare`
- QDC interactive session / report ID: `822588`
- Report URL: `https://qdc.qualcomm.com/reports/job/interactive/822588`
- Target platform shown by QDC: `Snapdragon X2 Elite`
- Device class shown by QDC: `Compute Reference Design`
- Platform identifier shown by QDC: `SC8480X`
- Operating system shown by QDC: `Windows 11`
- QDC state captured after connection: `Running`
- QDC device streaming: connected and interactive desktop visible
- Submitted: `09/15/26 03:35:26 AM` (as displayed by QDC)
- Started: `09/15/26 03:38:05 AM` (as displayed by QDC)

This proves that CAIOS successfully acquired, started, and connected to a real Qualcomm-hosted Snapdragon X2 Elite session.

## Important provenance correction

A later PowerShell diagnostic returned:

```text
SystemType: x64-based PC
CPU: 13th Gen Intel(R) Core(TM) i5-1335U
```

Those values identify the user's local ASUS PC, not the Qualcomm Device Cloud target shown in the browser stream. Therefore the earlier local `geniex.exe` launch errors and PE-architecture diagnostics **must not be presented as execution evidence from the Snapdragon X2 Elite session**.

The repository intentionally excludes those local-machine results from the Qualcomm inference claim.

## Workload execution — still pending

To upgrade this proof from **real Qualcomm hardware-session proof** to **real on-device workload execution proof**, the next command must be run inside the streamed Qualcomm Device Cloud Windows desktop itself, not in a local PowerShell window.

Inside the QDC streamed desktop, open PowerShell from the remote Start menu and capture:

```powershell
hostname
$env:PROCESSOR_ARCHITECTURE
Get-CimInstance Win32_ComputerSystem | Select-Object SystemType
Get-CimInstance Win32_Processor | Select-Object Name,Architecture,AddressWidth
```

Only after the remote shell is verified should GenieX or another supported Qualcomm inference runtime be installed/run there.

## Vendor reference only — not our execution

Qualcomm AI Hub publishes Snapdragon support and model-card performance data for supported models. Those numbers are useful for judging model/device fit, but they are **not** presented here as CAIOS execution evidence.

## CAIOS runtime proof

The repository demo wrapper separately verifies policy behavior around the local provider boundary:

1. `LOCAL_OK` — local provider accepted.
2. `LOW_RISK_FALLBACK` — approved cloud fallback allowed and recorded.
3. `HIGH_RISK_FAIL_CLOSED` — no silent fallback; safe degradation returned.

Public demo: https://www.caios.my/demo/edgecare
