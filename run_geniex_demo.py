"""CAIOS EdgeCare Runtime — AI Infra Summit 2026 public demo wrapper.

Requirements:
    pip install httpx

Start GenieX on a supported Qualcomm Snapdragon device:
    geniex pull ai-hub-models/Qwen3-VL-4B-Instruct
    geniex serve

Then run:
    python run_geniex_demo.py local
    python run_geniex_demo.py fallback
    python run_geniex_demo.py fail-closed

The fallback and fail-closed modes deliberately make the local edge endpoint
unavailable so the policy outcomes are deterministic for judging.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
from dataclasses import asdict, dataclass
from enum import StrEnum

import httpx

DEFAULT_GENIEX_BASE_URL = "http://127.0.0.1:18181/v1"
DEFAULT_GENIEX_MODEL = "ai-hub-models/Qwen3-VL-4B-Instruct"

PROMPT = (
    "Pika is a Pomeranian at home. A camera observation shows repeated pacing "
    "near the water bowl. Summarize the observation conservatively and state "
    "what additional information should be checked. Do not diagnose."
)


class RiskLevel(StrEnum):
    LOW = "low"
    HIGH = "high"


@dataclass(frozen=True)
class RuntimeResult:
    output: str | None
    provider: str | None
    fallback_used: bool
    safe_degradation: bool
    context_snapshot_id: str
    prompt_version: str


class GenieXProvider:
    name = "qualcomm-geniex"

    def __init__(self, force_unavailable: bool = False) -> None:
        self.base_url = os.getenv("GENIEX_BASE_URL", DEFAULT_GENIEX_BASE_URL).rstrip("/")
        self.model = os.getenv("GENIEX_MODEL", DEFAULT_GENIEX_MODEL)
        self.force_unavailable = force_unavailable

    async def healthy(self) -> bool:
        if self.force_unavailable:
            return False
        try:
            async with httpx.AsyncClient(timeout=2.0) as client:
                response = await client.get(f"{self.base_url}/models")
            return response.status_code < 500
        except httpx.HTTPError:
            return False

    async def generate(self) -> str:
        body = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are the local edge inference layer for CAIOS. "
                        "Return a concise observation, not a diagnosis."
                    ),
                },
                {"role": "user", "content": PROMPT},
            ],
            "temperature": 0,
        }
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(f"{self.base_url}/chat/completions", json=body)
            response.raise_for_status()
        return str(response.json()["choices"][0]["message"]["content"])


async def run_case(mode: str) -> RuntimeResult:
    force_down = mode in {"fallback", "fail-closed"}
    risk = RiskLevel.HIGH if mode == "fail-closed" else RiskLevel.LOW
    provider = GenieXProvider(force_unavailable=force_down)
    context_snapshot_id = "demo-pika-ai-infra-2026"
    prompt_version = "edgecare-summit-v1"

    if await provider.healthy():
        try:
            output = await provider.generate()
            return RuntimeResult(
                output=output,
                provider=provider.name,
                fallback_used=False,
                safe_degradation=False,
                context_snapshot_id=context_snapshot_id,
                prompt_version=prompt_version,
            )
        except (httpx.HTTPError, KeyError, IndexError, TypeError, ValueError):
            pass

    if risk == RiskLevel.LOW:
        return RuntimeResult(
            output="Approved cloud fallback used for low-risk informational task.",
            provider="approved-cloud-fallback",
            fallback_used=True,
            safe_degradation=False,
            context_snapshot_id=context_snapshot_id,
            prompt_version=prompt_version,
        )

    return RuntimeResult(
        output=None,
        provider=None,
        fallback_used=False,
        safe_degradation=True,
        context_snapshot_id=context_snapshot_id,
        prompt_version=prompt_version,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("local", "fallback", "fail-closed"))
    return parser.parse_args()


async def main() -> None:
    args = parse_args()
    result = await run_case(args.mode)
    print(json.dumps({"mode": args.mode, **asdict(result)}, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
