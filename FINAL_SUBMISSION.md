# AI Infra Summit 2026 — Final Submission Payload

## Project title

CAIOS EdgeCare Runtime

## Track

Qualcomm Model-to-device Innovation

## One-line pitch

Reliable companion-care AI for Snapdragon-class edge devices, with risk-aware fallback, provenance, and safe degradation.

## Short description

CAIOS EdgeCare Runtime is a provider-neutral edge-to-cloud inference layer for companion care. It is designed for Qualcomm Snapdragon / GenieX local inference while CAIOS applies risk-aware routing, provenance, safe degradation, and guarded execution around the model boundary.

## Long description

Pet-care AI is usually cloud-first even though many useful signals begin inside the home: camera observations, environmental sensors, owner voice notes, and routine behavior changes. Cloud-only inference creates avoidable latency, privacy, connectivity, and reliability dependencies.

CAIOS EdgeCare Runtime is a production-oriented edge-to-cloud inference layer for the CAIOS companion-animal operating system. The architecture is designed to use Qualcomm GenieX as a local inference endpoint on Snapdragon-class hardware. GenieX exposes an OpenAI-compatible local server, allowing CAIOS to reuse its provider-neutral model boundary instead of hard-coding product logic to a single model vendor.

The runtime applies three production rules. First, local execution is preferred when an approved edge provider is available. Second, low-risk tasks may use an approved cloud fallback if the local provider is unavailable, and that fallback is explicitly recorded. Third, medium/high-risk requests do not silently switch providers; if no permitted provider is available, CAIOS returns safe degradation rather than fabricating a confident answer.

Every decision preserves provider identity, fallback state, context snapshot, and prompt version. Physical-world actions remain behind CAIOS ActionGuard and owner/professional approval rules. The result is not merely an edge-model demo, but an auditable, safety-governed model-to-device architecture designed to merge into a real companion-care product.

During the hackathon we also established a real Qualcomm Device Cloud interactive session on a Snapdragon X2 Elite Compute Reference Design (QDC report/session ID 822588), confirming access to real Qualcomm-hosted hardware. Local GenieX inference on that session was not claimed as completed; the repository separates hardware-session evidence from runtime-policy proof to keep the submission verifiable.

## Qualcomm technology

- Qualcomm Snapdragon
- Qualcomm Device Cloud
- Snapdragon X2 Elite Compute Reference Design
- Qualcomm GenieX integration path
- Qualcomm AI Hub model path
- Qwen3 / Qwen3-VL family target

## Verified evidence

- Public live demo: https://www.caios.my/demo/edgecare
- Public GitHub: https://github.com/corwinlim/caios-edgecare-runtime
- Demo video: https://drive.google.com/file/d/1g6PqviNke64FR-AkmnB02IHn9KsAdnb5/view?usp=drive_link
- Qualcomm Device Cloud report/session: https://qdc.qualcomm.com/reports/job/interactive/822588
- QDC target: Snapdragon X2 Elite / Compute Reference Design / Windows 11
- Runtime-policy proof: LOCAL_OK, LOW_RISK_FALLBACK, HIGH_RISK_FAIL_CLOSED

## Technologies

Qualcomm Snapdragon, Qualcomm Device Cloud, Qualcomm GenieX, Qualcomm AI Hub, Edge AI, On-device AI, FastAPI, Python, Next.js, PostgreSQL, pgvector, Qwen, AI reliability, AI governance, companion animal care.

## Safety statement

CAIOS EdgeCare Runtime is decision support, not veterinary diagnosis. Urgent or clinically significant situations remain subject to CAIOS safety escalation and professional review pathways.

## Submission integrity

This submission does not claim that GenieX inference completed successfully on QDC session 822588. The verified claim is that a real Snapdragon X2 Elite Device Cloud session was acquired and run, while CAIOS runtime-policy behavior is independently demonstrated in the public demo and repository.

## Final submission gate

Do not mark SUBMITTED until Lablab displays a completed submission or equivalent confirmation evidence.
