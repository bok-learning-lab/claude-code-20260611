# Ex Libris Primo API — Harvard API Portal overview (as pasted, 2026-06-11)

Source: Harvard API Portal (stage), "Ex Libris APIs" page.
OpenAPI spec: `lts-exlibris-primo.yaml` (same folder).

## Key facts from the portal page

- **Purpose:** "obtaining catalog and other information from Harvard Library
  resources." This is Primo — the discovery engine behind HOLLIS.
- **Base URL (stage):** `https://go.stage.apis.huit.harvard.edu/lts-exlibris-primo`
- **Auth:** API key in header `X-Api-Key` (header ONLY — keys in query string
  are blocked by the gateway).
- **Rate limit:** 10 requests per minute.
- **One endpoint:** `GET /primo/v1/search` (Primo "Brief Search").
- Upstream vendor docs: https://developers.exlibrisgroup.com/primo/apis/
  (note: the Ex Libris key-acquisition process does NOT apply — Harvard keys
  come from the HUIT API portal).
- SLA: 24/7, dependent on Ex Libris vendor availability.
- Support: Library Operations team.

## Portal sample request

```bash
curl --location --request GET \
  'https://go.stage.apis.huit.harvard.edu/lts-exlibris-primo/primo/v1/search?vid=Auto1&tab=default_tab&scope=default_scope&q=title,contains,home&lang=eng&offset=0&limit=10&sort=rank&pcAvailability=true&getMore=0&conVoc=true' \
  --header 'x-api-key: YOUR_KEY'
```

Note: `vid=Auto1`, `tab=default_tab`, `scope=default_scope` are Ex Libris
placeholder values from the generic vendor docs — Harvard's real view/tab/scope
values need to be determined by testing (HOLLIS web UI uses `vid=HVD2`).

## Terms of use (summary)

- All Harvard data-usage policies apply (Information Security Policy, Policy on
  Access to Electronic Information, etc.).
- Infrastructure receiving data must conform to Level 3 data security policy.
- **Redistribution of data is strictly prohibited without written consent.**
