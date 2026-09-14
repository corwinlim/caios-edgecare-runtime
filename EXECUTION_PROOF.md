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

## Workload execution — current verification gate

The connected Windows session was checked from PowerShell. `geniex --help`, `geniex pull ...`, and `geniex serve` all returned `CommandNotFoundException`, confirming that GenieX is **not preinstalled** on this QDC Windows image.

Therefore the next gate is installation of the official GenieX Windows ARM64 CLI, followed by a local on-device inference run.

Official GenieX documentation states that the Windows ARM64 CLI supports Snapdragon X-series devices, including Snapdragon X Elite / X2 Elite.

After installation, verify:

```powershell
geniex --help
```

Then pull and serve a model:

```powershell
geniex pull ai-hub-models/Qwen3-4B-Instruct-2507
geniex serve
```

The GenieX server exposes an OpenAI-compatible endpoint at:

```text
http://127.0.0.1:18181
```

Then execute the CAIOS EdgeCare request against the local server and capture:

- Local provider / model name
- Successful response
- Any visible latency / throughput / runtime information
- Screenshot showing the Qualcomm Device Cloud session and successful workload

## Vendor reference only — not our execution

Qualcomm AI Hub publishes Snapdragon support and model-card performance data for supported models. Those numbers are useful for judging model/device fit, but they are **not** presented here as CAIOS execution evidence.

## CAIOS runtime proof

The repository demo wrapper separately verifies policy behavior around the local provider boundary:

1. `LOCAL_OK` — local provider accepted.
2. `LOW_RISK_FALLBACK` — approved cloud fallback allowed and recorded.
3. `HIGH_RISK_FAIL_CLOSED` — no silent fallback; safe degradation returned.

Public demo: https://www.caios.my/demo/edgecare
