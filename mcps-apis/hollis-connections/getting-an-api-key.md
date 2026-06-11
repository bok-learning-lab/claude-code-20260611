# Getting a Harvard API key

The library APIs are gated behind the **Harvard API Portal** (HAPI), run by HUIT.
One portal application gives you one key + secret pair, and that single pair can be
granted access to multiple APIs — Primo (this folder), and the other library APIs
(Alma, ArchivesSpace) if you later want them.

**The authoritative walkthrough is the portal's own infographic:**
<https://portal.stage.apis.huit.harvard.edu/hapi-infographic#top>

## The shape of the process

1. **Sign in to the portal** at <https://portal.stage.apis.huit.harvard.edu/> with
   your HarvardKey.
2. **Register an application.** An "app" is just a named credential holder — call it
   something like `<your-name>-library-search`.
3. **Request access to the API product** you need. For HOLLIS search, that's the
   **Ex Libris APIs** (the Primo product, `lts-exlibris-primo`).
4. **Wait for approval.** Library API requests are reviewed by the Library
   Operations team; approval is not instant.
5. **Collect your credentials** from the app page: an API key and a client secret.
   - The key is sent on every request as the header `X-Api-Key: <key>`.
   - The secret is not needed for Primo (key-in-header only) but keep it — other
     APIs on the same app may use it.
6. **Put the key in `.env`**: copy [`.env.example`](.env.example) to `.env` in this
   folder and paste the values in. `.env` is gitignored — it never leaves your
   machine.

## Two gateways: stage and production

Everything in this folder points at the **stage** gateway
(`go.stage.apis.huit.harvard.edu`), which is where the portal documentation lives
today. A production gateway (`go.apis.huit.harvard.edu`, no `.stage`) may exist with
separate registration — if stage proves flaky, confirm with the Library Operations
team listed on the portal page.

## Terms worth knowing before you ask for a key

- All Harvard data-usage policies apply (Information Security Policy, Policy on
  Access to Electronic Information).
- Infrastructure receiving the data must conform to the Level 3 data security
  policy.
- **Redistribution of the data is prohibited without written consent** — this is a
  research and teaching tool, not a feed you can republish.
