# AI Infra Summit 2026 — Final Submission Payload

## Project title

CAIOS EdgeCare Runtime

## Track

Qualcomm Model-to-device Innovation

## One-line pitch

Reliable on-device companion-care AI on Qualcomm Snapdragon, with risk-aware cloud fallback, provenance, and safe degradation.

## Short description

CAIOS EdgeCare Runtime moves the first inference hop for companion-care observations onto Snapdragon-class devices using Qualcomm GenieX, while CAIOS applies provider-neutral, risk-aware routing, safe degradation, provenance, and guarded execution.

## Long description

Pet-care AI is usually cloud-first even though many useful signals begin inside the home: camera observations, environmental sensors, owner voice notes, and routine behavior changes. Cloud-only inference creates avoidable latency, privacy, connectivity, and reliability dependencies.

CAIOS EdgeCare Runtime is a production-oriented edge-to-cloud inference layer for the CAIOS companion-animal operating system. The Summit build uses Qualcomm GenieX as the local primary inference runtime on Snapdragon-class hardware. GenieX exposes an OpenAI-compatible local server, so CAIOS can reuse its provider-neutral model boundary instead of adding a Qualcomm-specific application stack.

The runtime applies three production rules. First, appropriate inference runs locally. Second, low-risk tasks may use an approved cloud fallback if the local provider is unavailable, and that fallback is recorded. Third, medium/high-risk requests do not silently switch providers; if no permitted provider is available, CAIOS returns safe degradation rather than fabricating an answer.

Every decision preserves provider identity, fallback state, context snapshot and prompt version. Physical-world actions remain behind CAIOS ActionGuard and owner/professional approval rules. The result is not just a model running on-device, but an auditable and safety-governed model-to-device architecture designed to merge back into a real product.

## Qualcomm technology

- Qualcomm GenieX
- Qualcomm AI Hub
- Snapdragon X-class target
- Qwen3-VL-4B-Instruct
- Qualcomm AI Workbench / hosted-device execution proof

## Public URLs

- Live demo: https://www.caios.my/demo/edgecare
- Public GitHub: https://github.com/corwinlim/caios-edgecare-runtime
- Demo video: PENDING_PUBLIC_VIDEO_URL
- Qualcomm execution proof: PENDING_REAL_JOB_URL_OR_ID

## Technologies

Qualcomm Snapdragon, Qualcomm GenieX, Qualcomm AI Hub, Edge AI, On-device AI, FastAPI, Python, Next.js, PostgreSQL, pgvector, Qwen, AI reliability, AI governance, companion animal care.

## Safety statement

CAIOS EdgeCare Runtime is decision support, not veterinary diagnosis. Urgent or clinically significant situations remain subject to CAIOS safety escalation and professional review pathways.

## Final submission gate

Do not mark SUBMITTED until Lablab displays a completed submission or equivalent confirmation evidence.
