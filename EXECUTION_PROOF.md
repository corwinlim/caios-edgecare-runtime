# Qualcomm Execution Proof

This file separates **vendor-published reference performance** from **our own execution evidence**.

## CAIOS Device Cloud session — real Qualcomm hardware

A real Qualcomm Device Cloud Interactive Session has been created for the CAIOS EdgeCare submission.

- Project / session name: `CAIOS EdgeCare`
- QDC interactive session / report ID: `822588`
- Report URL: `https://qdc.qualcomm.com/reports/job/interactive/822588`
- Target platform: `Snapdragon X2 Elite`
- Device class: `Compute Reference Design`
- Platform identifier shown by QDC: `SC8480X`
- Operating system: `Windows 11`
- QDC state captured: `Setup`
- QDC UI confirmation captured: `Successfully started device streaming`
- Submitted: `09/15/26 03:35:26 AM` (as displayed by QDC)

This proves that CAIOS successfully acquired and started a real Qualcomm-hosted Snapdragon X2 Elite device session. It is **hardware-session proof**, not yet a claim that the EdgeCare inference workload completed successfully.

## Workload execution — next verification gate

Inside the connected Snapdragon X2 Elite Windows ARM64 session, run GenieX and capture the result.

Official GenieX supports Windows ARM64 on Snapdragon X-series devices. Recommended path:

```powershell
geniex --help
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
- Screenshot showing the Qualcomm Device Cloud session and the successful workload

## Vendor reference only — not our execution

Qualcomm AI Hub publishes Snapdragon support and model-card performance data for supported models. Those numbers are useful for judging model/device fit, but they are **not** presented here as CAIOS execution evidence.

## CAIOS runtime proof

The repository demo wrapper separately verifies policy behavior around the local provider boundary:

1. `LOCAL_OK` — local provider accepted.
2. `LOW_RISK_FALLBACK` — approved cloud fallback allowed and recorded.
3. `HIGH_RISK_FAIL_CLOSED` — no silent fallback; safe degradation returned.

Public demo: https://www.caios.my/demo/edgecare
