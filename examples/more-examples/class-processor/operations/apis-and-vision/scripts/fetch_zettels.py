#!/usr/bin/env python3
"""
fetch_zettels.py — call an OPEN data API (no key needed).

An API is just a URL you can ask for data. The Niklas Luhmann Archiv (Bielefeld)
scanned the sociologist's entire Zettelkasten — his famous paper slip-box — and
serves it from an open API. Ask it for a branch of slips and it returns JSON:
each slip's metadata, the archive's own human TRANSCRIPTION of the handwriting,
and an image id for the scanned card.

This is the gentlest possible introduction to APIs: no key, no auth, just a URL.

Usage:
    python3 fetch_zettels.py --branch 9/8 --rows 5 --out ../../inputs/zettelkasten/zk-9-8.json

Then look at the JSON, or pass a slip's facsimile image to transcribe.py to see
a vision model re-derive the text — and compare it to the archive's own.

Docs: https://niklas-luhmann-archiv.de/projekt/dokumentation
"""
import argparse
import json
import sys
import urllib.parse
import urllib.request

API = "https://v0.api.niklas-luhmann-archiv.de/ZK/search"


def fetch(branch: str, rows: int) -> dict:
    # The query is a JSON object passed as the `q` URL parameter. We search by
    # "zettelnummer" (the slip number) with "starts-with", so "9/8" returns the
    # whole 9/8 branch. (Open the URL in a browser to see the raw JSON yourself.)
    query = {
        "page": 1,
        "rows": rows,
        "fulltext": "",
        "fuzzy": False,
        "FTSearchMode": "and",
        "zettelnummer": branch,
        "zettelnummerSearchMode": "starts-with",
        "areas": [],
        "ref": "",
        "zks": ["2"],  # ZK II — the second Zettelkasten
    }
    url = f"{API}?q={urllib.parse.quote(json.dumps(query))}"
    print(f"GET {url}\n")
    with urllib.request.urlopen(url, timeout=30) as resp:
        return json.load(resp)


def main() -> int:
    ap = argparse.ArgumentParser(description="Fetch Zettelkasten slips from the open Luhmann Archiv API.")
    ap.add_argument("--branch", default="9/8", help='slip-number prefix, e.g. "9/8"')
    ap.add_argument("--rows", type=int, default=5, help="how many slips to fetch")
    ap.add_argument("--out", help="write the JSON here (otherwise just prints a summary)")
    args = ap.parse_args()

    data = fetch(args.branch, args.rows)
    results = data.get("results", [])
    print(f"{data.get('numberOfResults')} slips in branch {args.branch}; showing {len(results)}:\n")
    for r in results:
        preview = " ".join((r.get("transcriptionPreview") or "").split())
        print(f"  • {r.get('shortTitle','?'):8}  image={r.get('image',{}).get('id','?')}")
        print(f"      “{preview[:90]}…”")

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"\nWrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
