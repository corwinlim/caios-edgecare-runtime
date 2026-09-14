# Qualcomm Execution Proof

This file separates **vendor-published reference performance** from **our own execution evidence**.

## Required user-run proof

Run a real Qualcomm AI Workbench / GenieX inference job with:

- Model: `Qwen3-VL-4B-Instruct`
- Preferred target: Snapdragon X Elite / Snapdragon X Plus / Snapdragon X2 Elite
- Command path: `geniex infer ai-hub-models/Qwen3-VL-4B-Instruct`

Capture:

- Job/result URL or job ID
- Target device/chipset
- Runtime / precision
- Visible latency or throughput metrics
- Screenshot of the completed result page

## Vendor reference only — not our execution

Qualcomm AI Hub currently publishes support for Qwen3-VL-4B-Instruct on Snapdragon X-class devices and exposes model-card performance data. Those numbers are useful for judging model/device fit, but they are **not** presented here as CAIOS execution evidence.

## CAIOS runtime proof

The repository demo wrapper separately verifies policy behavior around the local provider boundary:

1. `LOCAL_OK` — local provider accepted.
2. `LOW_RISK_FALLBACK` — approved cloud fallback allowed and recorded.
3. `HIGH_RISK_FAIL_CLOSED` — no silent fallback; safe degradation returned.

Public demo: https://www.caios.my/demo/edgecare
