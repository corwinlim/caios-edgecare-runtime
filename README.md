# CAIOS EdgeCare Runtime

**Reliable On-Device AI for Companion Care**

AI Infra Summit Hackathon 2026 — **Qualcomm Model-to-device Innovation** track.

## Live demo

https://www.caios.my/demo/edgecare

## One-line pitch

Reliable on-device companion-care AI on Qualcomm Snapdragon, with risk-aware cloud fallback, provenance, and safe degradation.

## Problem

Pet-care AI is usually cloud-first even though many useful signals originate inside the home: cameras, phones, sensors, and smart-home gateways. That creates latency, privacy, connectivity, and reliability dependencies.

CAIOS EdgeCare Runtime moves the first inference hop onto Snapdragon-class hardware and treats cloud inference as a governed fallback rather than an assumption.

## Architecture

```text
Camera / sensor / owner input
        ↓
Qualcomm Snapdragon device
        ↓
GenieX local inference
(Qualcomm AI Hub model)
        ↓
CAIOS canonical observation
        ↓
Reliable AI Runtime
  ├─ local result accepted
  ├─ approved cloud fallback for low-risk tasks
  └─ safe degradation when fallback is not permitted
        ↓
ActionGuard / recommendation / care event
        ↓
Auditable outcome + longitudinal memory
```

## Qualcomm technology

The Summit build uses Qualcomm GenieX as the local inference runtime and targets **Qwen3-VL-4B-Instruct** on Snapdragon-class devices. GenieX exposes an OpenAI-compatible local server, so CAIOS can reuse its provider-neutral runtime instead of coupling the product to a vendor-specific application API.

Suggested local setup:

```bash
geniex pull ai-hub-models/Qwen3-VL-4B-Instruct
geniex serve
```

Default endpoint:

```text
http://127.0.0.1:18181/v1
```

## Demo scenario

**Pika is home alone.** A camera observation reports repeated pacing near the water bowl.

CAIOS treats this as an observation, not a diagnosis.

The demo shows three governed runtime outcomes:

### 1. Local success

```text
provider=qualcomm-geniex
fallback_used=false
safe_degradation=false
```

### 2. Low-risk approved fallback

```text
provider=approved-cloud-fallback
fallback_used=true
safe_degradation=false
```

### 3. High-risk fail-closed

```text
provider=null
fallback_used=false
safe_degradation=true
```

## Why this is different

Most model-to-device demos stop at “the model runs locally.” CAIOS EdgeCare Runtime adds the production layer around local inference:

- provider independence
- risk-aware fallback
- context and prompt provenance
- safe degradation
- guarded physical-world execution

## Safety boundary

This project is decision support, not veterinary diagnosis. On-device inference can create bounded observations and low-risk recommendations, but urgent or clinically significant decisions remain subject to CAIOS safety escalation and professional review pathways.

Even when inference succeeds, the model does not directly control the physical world. CARLI actions remain behind CAIOS ActionGuard and owner/professional approval rules.

## Production relationship

The full CAIOS production repository remains private. This public hackathon repository contains only the judge-facing EdgeCare integration assets and demo wrapper required to evaluate the AI Infra Summit submission.

## Project links

- Live demo: https://www.caios.my/demo/edgecare
- Product: https://www.caios.my
- Track: Qualcomm Model-to-device Innovation

## Closing

**Local when possible. Safe when not.**
