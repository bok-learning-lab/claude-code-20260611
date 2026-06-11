# HOLLIS Connections — searching Harvard Library from Claude

**HOLLIS** (hollis.harvard.edu) is the front door to Harvard Library. Behind it sits
**Ex Libris Primo**, the discovery engine that searches the catalog *and* the Primo
Central article index. The Harvard API Portal exposes that engine as an API — which
means a Claude session, given a key, can search HOLLIS for you: real records, real
DOIs, real availability, not citations the model might invent.

## What a professor can do with this

- **Live literature search from a Claude session.** "Find recent articles on X that
  Harvard has full-text access to" becomes one command, with results carrying DOIs
  and record IDs that trace back to the catalog.
- **Restrict to what you can actually read** — articles only, full-text-only — and
  page through at catalog scale.
- **Build teaching materials on real holdings**: reading lists, bibliographies,
  course reserves candidates, all grounded in records rather than memory.
- **Route a hit to the document**: take the DOI to `https://doi.org/<doi>` through
  Harvard's proxy, or the record ID to its HOLLIS permalink.

## What's in this folder

| File | What it is |
|---|---|
| [`primo_search.py`](primo_search.py) | Stdlib-only Python client for the Primo search API. Works as a CLI or an importable module. |
| [`getting-an-api-key.md`](getting-an-api-key.md) | How to get a key from the Harvard API Portal. |
| [`.env.example`](.env.example) | Key names without values — copy to `.env` and fill in. |
| [`docs/exlibris-primo-guide.md`](docs/exlibris-primo-guide.md) | The working guide: query syntax, the parameters that matter, facets, gotchas, response shape. |
| [`docs/raw/`](docs/raw/) | The portal documentation as received — the page overview and the OpenAPI spec. |

## Quickstart

```bash
cp .env.example .env        # then paste in your key (see getting-an-api-key.md)

python3 primo_search.py "medieval glass lenses"
python3 primo_search.py "vagus nerve stimulation" --articles --fulltext-only
python3 primo_search.py --field title --contains "invisible cities" --books
```

Or from a Claude session in this folder: ask in plain language ("search HOLLIS for
recent articles on structural folklore, full-text only") and let Claude drive the
client.

## Status and limits

- **Untested until the first key arrives.** The client and guide were built from the
  portal documentation; items marked [unverified] in the guide are educated guesses (Harvard's
  real `vid`/`tab`/`scope` values among them) that the first live calls will confirm.
- **Rate limit: 10 requests/minute.** Prefer `--limit 25` over paging.
- **The key goes in the header** (`X-Api-Key`) — the gateway blocks keys in the URL.
- **Terms of use:** Harvard data-usage policies apply, and redistribution of the data
  is prohibited without written consent. Search for yourself; don't republish feeds.
