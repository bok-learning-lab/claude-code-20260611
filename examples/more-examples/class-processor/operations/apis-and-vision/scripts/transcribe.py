#!/usr/bin/env python3
"""
transcribe.py — send an image to a VISION API and get the text back.

Two providers, the same idea: you POST an image + a prompt to a URL, and a model
reads the picture and returns text. Unlike the open Luhmann API, these need a
KEY — so they read it from the example's own .env file (see ../../.env.example).

The point is the *transference*: the same move that transcribes a Luhmann slip
also transcribes a photo of your blackboard, or a scan of a student's in-class
exercise. Point it at any image:

    python3 transcribe.py --image ../../inputs/board-work/lecture3.jpg --provider both
    python3 transcribe.py --image my-zettel.jpg --provider gemini

Both calls are plain HTTPS requests — that is all an "API" is. We use `requests`
rather than a provider SDK on purpose, so the raw shape of each call is visible.

Setup:  cp ../../.env.example ../../.env   (then fill in GEMINI_API_KEY / ANTHROPIC_API_KEY)
        pip install -r ../requirements.txt
"""
import argparse
import base64
import mimetypes
import os
import sys
from pathlib import Path

import requests

# The .env lives at the class-processor root (this file is at
# class-processor/operations/apis-and-vision/scripts/transcribe.py → parents[3]).
EXAMPLE_ROOT = Path(__file__).resolve().parents[3]

DEFAULT_PROMPT = (
    "Transcribe the text in this image exactly as written. It may be handwritten "
    "(a German index card, a blackboard, a student's exercise). Preserve the "
    "layout and any equations. Output only the transcription, nothing else."
)


def load_env() -> None:
    """Tiny .env loader — reads KEY=value lines from class-processor/.env.
    (No dependency on python-dotenv, so the mechanism is fully visible.)"""
    env = EXAMPLE_ROOT / ".env"
    if not env.exists():
        return
    for line in env.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        os.environ.setdefault(key.strip(), val.strip())


def image_to_base64(path: str) -> tuple[str, str]:
    media_type = mimetypes.guess_type(path)[0] or "image/jpeg"
    data = base64.standard_b64encode(Path(path).read_bytes()).decode("utf-8")
    return data, media_type


def transcribe_with_gemini(b64: str, media_type: str, prompt: str) -> str:
    """Google Gemini — POST the image inline to generateContent?key=..."""
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        return "[skipped: set GEMINI_API_KEY in .env]"
    model = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    body = {
        "contents": [{
            "parts": [
                {"inline_data": {"mime_type": media_type, "data": b64}},
                {"text": prompt},
            ]
        }]
    }
    r = requests.post(url, params={"key": key}, json=body, timeout=120)
    r.raise_for_status()
    return r.json()["candidates"][0]["content"]["parts"][0]["text"].strip()


def transcribe_with_claude(b64: str, media_type: str, prompt: str) -> str:
    """Anthropic Claude — POST the image as a content block to /v1/messages."""
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        return "[skipped: set ANTHROPIC_API_KEY in .env]"
    model = os.environ.get("ANTHROPIC_MODEL", "claude-opus-4-8")
    body = {
        "model": model,
        "max_tokens": 2048,
        "messages": [{
            "role": "user",
            "content": [
                {"type": "image", "source": {"type": "base64", "media_type": media_type, "data": b64}},
                {"type": "text", "text": prompt},
            ],
        }],
    }
    headers = {
        "x-api-key": key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    r = requests.post("https://api.anthropic.com/v1/messages", headers=headers, json=body, timeout=120)
    r.raise_for_status()
    return "".join(b["text"] for b in r.json()["content"] if b["type"] == "text").strip()


def main() -> int:
    ap = argparse.ArgumentParser(description="Transcribe an image with a vision API (Gemini and/or Claude).")
    ap.add_argument("--image", required=True, help="path to an image file")
    ap.add_argument("--provider", choices=["gemini", "claude", "both"], default="both")
    ap.add_argument("--prompt", default=DEFAULT_PROMPT)
    args = ap.parse_args()

    load_env()
    b64, media_type = image_to_base64(args.image)

    if args.provider in ("gemini", "both"):
        print("\n=== Gemini ===")
        print(transcribe_with_gemini(b64, media_type, args.prompt))
    if args.provider in ("claude", "both"):
        print("\n=== Claude ===")
        print(transcribe_with_claude(b64, media_type, args.prompt))
    return 0


if __name__ == "__main__":
    sys.exit(main())
