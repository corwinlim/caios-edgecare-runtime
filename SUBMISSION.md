# AI Infra Summit 2026 Submission

## Project

**CAIOS EdgeCare Runtime**

## Track

**Qualcomm Model-to-device Innovation**

## Summary

Reliable on-device companion-care AI on Qualcomm Snapdragon, with risk-aware cloud fallback, provenance, and safe degradation.

## Description

Pet-care AI is usually cloud-first, even though many useful signals originate inside the home: camera observations, environmental sensors, owner voice notes, and routine behavior changes. That architecture creates avoidable latency, privacy, connectivity, and reliability dependencies.

CAIOS EdgeCare Runtime is a production-oriented edge-to-cloud inference layer for the CAIOS companion-animal operating system. The Summit build uses Qualcomm GenieX as an on-device inference endpoint on Snapdragon-class hardware and targets Qwen3-VL-4B-Instruct. GenieX exposes an OpenAI-compatible local server, allowing CAIOS to reuse its provider-neutral model boundary instead of adding a Qualcomm-specific application stack.

The runtime demonstrates three real production behaviors. First, appropriate inference runs locally on the Snapdragon device. Second, low-risk tasks may fall back to an approved cloud provider when the local endpoint is unavailable. Third, higher-risk tasks do not silently switch providers: when policy does not allow another provider, CAIOS returns safe degradation instead of fabricating an answer.

Every result preserves provider identity, fallback state, context snapshot and prompt version. Physical-world actions remain behind CAIOS ActionGuard and owner or professional approval rules.

The demo follows Pika, a Pomeranian who is home alone. A camera observation reports repeated pacing near the water bowl. The local edge path performs the first inference hop, CAIOS creates a bounded observation, and the Reliable AI Runtime decides whether to accept the local result, use an allowed fallback, or safely degrade.

Most model-to-device demos stop at “the model runs locally.” CAIOS EdgeCare Runtime adds the production layer around that capability: provider independence, risk-aware fallback, provenance, safe degradation, and guarded execution.

## Public links

- Live demo: https://www.caios.my/demo/edgecare
- GitHub: https://github.com/corwinlim/caios-edgecare-runtime

## Safety

CAIOS EdgeCare Runtime is decision support, not veterinary diagnosis. Urgent or clinically significant situations remain subject to CAIOS safety escalation and professional review pathways.
