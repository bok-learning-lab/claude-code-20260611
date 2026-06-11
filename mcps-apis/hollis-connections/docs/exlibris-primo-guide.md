# Ex Libris Primo API (HOLLIS search)

> **Status: UNTESTED** — client built, awaiting API key for live verification.
> Items marked [unverified] are educated guesses that the first test calls will confirm
> or correct.

## What this API is for

This is the discovery engine behind **HOLLIS** (hollis.harvard.edu). One
endpoint, `GET /primo/v1/search`, searches across Harvard's catalog **and**
the Primo Central article index — which makes this the key API for the project
goal: finding articles Harvard has institutional access to that a plain web
search can't reach.

## Quick reference

| | |
|---|---|
| Base URL | `https://go.stage.apis.huit.harvard.edu/lts-exlibris-primo` |
| Endpoint | `GET /primo/v1/search` |
| Auth | header `X-Api-Key: <key>` — **header only**, gateway blocks key-in-query |
| Key env var | `HARVARD_API_KEY` (in project `.env` — one portal app key shared by all the library APIs) |
| Rate limit | **10 requests/minute** (watch `X-Exl-Api-Remaining` response header) |
| Response | JSON (PNX record format) |
| Client | [`primo_search.py`](../primo_search.py) |
| Vendor docs | https://developers.exlibrisgroup.com/primo/apis/ |

## Required parameters

Every request needs `vid`, `tab`, `scope`, and `q`. The portal docs only show
Ex Libris placeholder values (`Auto1` / `default_tab` / `default_scope`).

[unverified] Harvard's real values (inferred from the HOLLIS web UI, unconfirmed):

| Param | Likely value | Source |
|---|---|---|
| `vid` | `HVD2` | HOLLIS URLs use `vid=HVD2` |
| `tab` | `everything` | HOLLIS URLs use `tab=everything` |
| `scope` | `everything` | HOLLIS URLs use `search_scope=everything` |
| `inst` | omit | spec says required, but only "for on-premises customers"; Harvard is hosted — test both ways |

## Query syntax (`q`)

```
q=<field>,<precision>,<value>[,<operator>;<field>,<precision>,<value>...]
```

- **field:** `any`, `title`, `creator`, `sub` (subject), `usertag`
- **precision:** `contains`, `exact`, `begins_with`
- **value:** words/phrase; may contain `AND`, `OR`, `NOT`; **must not contain
  a semicolon** (semicolons delimit multiple field clauses)
- **operator** (between clauses): `AND` (default), `OR`, `NOT`

Examples:

```
q=any,contains,vagus nerve stimulation
q=title,contains,pop music,AND;sub,contains,korean
q=creator,exact,Calvino, Italo        ← careful: commas in values are risky
```

## The parameters that matter for article search

- **`pcAvailability`** — `true` returns everything Primo Central knows about;
  `false` returns **only records with full text available to Harvard**. For
  "what can I actually read?", use `false`.
- **`qInclude=facet_rtype,exact,articles`** — restrict to articles. Other
  useful `facet_rtype` values: `books`, `journals`, `dissertations`,
  `reviews`. [unverified] exact facet names need confirming from a live response (the
  response includes the full facet list).
- **`limit`/`offset`** — paging. Default limit 10.
- **`sort`** — `rank` (relevance), `title`, `author`, `date`.

Facet filtering format (multiple categories delimited by `|,|`):

```
qInclude=facet_rtype,exact,articles|,|facet_lang,exact,eng
qExclude=facet_rtype,exact,reviews
multiFacets=facet_rtype,include,articles|,|facet_lang,exclude,spa   ← OR within category
```

Valid facet categories: `facet_rtype`, `facet_topic`, `facet_creator`,
`facet_tlevel` (availability), `facet_domain` (collection), `facet_library`,
`facet_lang`, `facet_lcc`.

## Working curl

```bash
curl -s "https://go.stage.apis.huit.harvard.edu/lts-exlibris-primo/primo/v1/search?vid=HVD2&tab=everything&scope=everything&q=any,contains,glass%20lenses%20medieval&limit=5&sort=rank&pcAvailability=false" \
  -H "X-Api-Key: $HARVARD_API_KEY"
```

## Client usage

```bash
python3 primo_search.py "medieval glass lenses"
python3 primo_search.py "vagus nerve" --articles --fulltext-only
python3 primo_search.py --field title --contains "invisible cities" --books
python3 primo_search.py --raw "title,contains,optics;sub,contains,theology" --json
```

```python
from primo_search import search, summarize
data = search("any,contains,structural folklore", limit=5, pc_availability=False)
for doc in data["docs"]:
    print(summarize(doc))
```

## Response shape

[unverified] To be filled in from real responses. Expected (standard Primo brief-search):

- `info.total` — total hit count
- `docs[]` — array of PNX records; each has `pnx.display` (title, creator,
  type, ispartof...), `pnx.addata` (doi, issn, jtitle — citation data),
  `pnx.control` (recordid), `delivery` (availability/links)
- `facets[]` — facet names + counts for the whole result set (useful for
  discovering Harvard's exact facet vocabulary)

## Gotchas

- **Key in header only.** `?apikey=` in the query string is hard-blocked by
  the HUIT gateway (this differs from Ex Libris's own docs).
- **10 req/min** is tight — batch carefully, prefer `limit=25`+ over paging.
- This is the **stage** portal URL. [unverified] A production gateway
  (`go.apis.huit.harvard.edu`, no `.stage`) may exist with a separate
  key/registration — confirm with Library Operations if stage proves flaky.
- Semicolons cannot appear in search values at all.
- `200 OK` with an empty object body is listed as the documented response —
  the real schema is undocumented in the portal; our guide's response-shape
  section is the substitute.

## Getting full text from a result

The search response gives metadata (DOI, ISSN, record id) — not the PDF.
Routes from a hit to the article:
1. **DOI** → `https://doi.org/<doi>` via Harvard's proxy, or
2. **HOLLIS permalink** → `https://hollis.harvard.edu/primo-explore/fulldisplay?docid=<record_id>&vid=HVD2` [unverified] (pattern unconfirmed)
3. `delivery` section of the record may contain direct `linktorsrc` URLs.
