#!/usr/bin/env python3
"""Harvard Ex Libris Primo API client — searches HOLLIS (catalog + articles).

Stdlib only. Key comes from HARVARD_API_KEY (env or project .env).

CLI:
    python3 primo_search.py "machine learning folklore"
    python3 primo_search.py --field title --contains "pop music" --limit 5
    python3 primo_search.py --raw "title,contains,home;sub,contains,korean"
    python3 primo_search.py "vagus nerve" --articles --fulltext-only

Module:
    from primo_search import search
    results = search("q=any,contains,vagus nerve stimulation")
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE_URL = "https://go.stage.apis.huit.harvard.edu/lts-exlibris-primo"
SEARCH_PATH = "/primo/v1/search"

# Harvard's real view/tab/scope values — HOLLIS web UI uses vid=HVD2.
# UNVERIFIED until first live test; portal docs only show Ex Libris
# placeholders (Auto1/default_tab/default_scope).
DEFAULT_VID = "HVD2"
DEFAULT_TAB = "everything"
DEFAULT_SCOPE = "everything"

ENV_KEY = "HARVARD_API_KEY"


def _load_env_key() -> str:
    if os.environ.get(ENV_KEY):
        return os.environ[ENV_KEY]
    # Walk up from this file looking for a .env with the key
    for parent in [Path(__file__).resolve().parent, *Path(__file__).resolve().parents]:
        env_file = parent / ".env"
        if env_file.is_file():
            for line in env_file.read_text().splitlines():
                line = line.strip()
                if line.startswith(f"{ENV_KEY}="):
                    return line.split("=", 1)[1].strip().strip("'\"")
    sys.exit(f"No API key found: set {ENV_KEY} in the environment or in the project .env")


def search(
    q: str,
    *,
    vid: str = DEFAULT_VID,
    tab: str = DEFAULT_TAB,
    scope: str = DEFAULT_SCOPE,
    limit: int = 10,
    offset: int = 0,
    sort: str = "rank",
    pc_availability: bool = True,
    q_include: str = "",
    q_exclude: str = "",
    multi_facets: str = "",
    lang: str = "eng",
    inst: str = "",
    api_key: str = "",
) -> dict:
    """Run a Primo brief search. `q` uses Primo syntax: field,precision,value
    e.g. "any,contains,glass lenses medieval" or
         "title,contains,pop music,AND;sub,contains,korean"
    """
    params = {
        "vid": vid,
        "tab": tab,
        "scope": scope,
        "q": q,
        "lang": lang,
        "offset": str(offset),
        "limit": str(limit),
        "sort": sort,
        "pcAvailability": "true" if pc_availability else "false",
        "getMore": "0",
        "conVoc": "true",
    }
    if q_include:
        params["qInclude"] = q_include
    if q_exclude:
        params["qExclude"] = q_exclude
    if multi_facets:
        params["multiFacets"] = multi_facets
    if inst:
        params["inst"] = inst

    url = f"{BASE_URL}{SEARCH_PATH}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"X-Api-Key": api_key or _load_env_key()})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        raise RuntimeError(f"HTTP {e.code} from Primo API: {body[:2000]}") from e


def summarize(doc: dict) -> dict:
    """Flatten one Primo doc into the fields that matter for finding articles."""
    pnx = doc.get("pnx", {})
    display = pnx.get("display", {})
    addata = pnx.get("addata", {})
    control = pnx.get("control", {})

    def first(d, key):
        v = d.get(key)
        return v[0] if isinstance(v, list) and v else v

    return {
        "title": first(display, "title"),
        "creator": display.get("creator") or display.get("contributor"),
        "type": first(display, "type"),
        "date": first(display, "creationdate"),
        "journal": first(addata, "jtitle"),
        "doi": first(addata, "doi"),
        "issn": first(addata, "issn"),
        "is_part_of": first(display, "ispartof"),
        "record_id": first(control, "recordid"),
        "availability": first(display, "availpnx") or first(display, "availlibrary"),
    }


def main():
    p = argparse.ArgumentParser(description="Search HOLLIS via the Harvard Primo API")
    p.add_argument("query", nargs="?", help="search terms (searched in any field)")
    p.add_argument("--field", default="any", help="any|title|creator|sub|usertag")
    p.add_argument("--contains", help="value for --field (alternative to positional query)")
    p.add_argument("--raw", help="full raw Primo q string, e.g. 'title,contains,home;sub,contains,korean'")
    p.add_argument("--limit", type=int, default=10)
    p.add_argument("--offset", type=int, default=0)
    p.add_argument("--sort", default="rank", choices=["rank", "title", "author", "date"])
    p.add_argument("--articles", action="store_true", help="restrict to articles (facet_rtype)")
    p.add_argument("--books", action="store_true", help="restrict to books (facet_rtype)")
    p.add_argument("--fulltext-only", action="store_true", help="only records with full text (pcAvailability=false)")
    p.add_argument("--vid", default=DEFAULT_VID)
    p.add_argument("--tab", default=DEFAULT_TAB)
    p.add_argument("--scope", default=DEFAULT_SCOPE)
    p.add_argument("--json", action="store_true", help="print full raw JSON response")
    args = p.parse_args()

    if args.raw:
        q = args.raw
    elif args.contains:
        q = f"{args.field},contains,{args.contains}"
    elif args.query:
        q = f"{args.field},contains,{args.query}"
    else:
        p.error("provide a query, --contains, or --raw")

    q_include = ""
    if args.articles:
        q_include = "facet_rtype,exact,articles"
    elif args.books:
        q_include = "facet_rtype,exact,books"

    data = search(
        q,
        vid=args.vid,
        tab=args.tab,
        scope=args.scope,
        limit=args.limit,
        offset=args.offset,
        sort=args.sort,
        pc_availability=not args.fulltext_only,
        q_include=q_include,
    )

    if args.json:
        json.dump(data, sys.stdout, indent=2)
        print()
        return

    info = data.get("info", {})
    total = info.get("total", "?")
    docs = data.get("docs", [])
    print(f"Total results: {total}  (showing {len(docs)}, offset {args.offset})\n")
    for i, doc in enumerate(docs, 1 + args.offset):
        s = summarize(doc)
        creators = s["creator"]
        if isinstance(creators, list):
            creators = "; ".join(creators[:3])
        print(f"{i}. [{s['type']}] {s['title']}")
        if creators:
            print(f"   {creators}")
        if s["is_part_of"]:
            print(f"   In: {s['is_part_of']}")
        for label, key in [("DOI", "doi"), ("Date", "date"), ("Record", "record_id")]:
            if s[key]:
                print(f"   {label}: {s[key]}")
        print()


if __name__ == "__main__":
    main()
