# mcps-apis

Sample MCP (Model Context Protocol) servers and plain API clients built for this gallery.
Each subfolder is self-contained with its own dependencies and its own native toolchain
(Python venv, Node `node_modules`, etc.). The MCP servers are wired into the repo through
the project-scoped [`.mcp.json`](../.mcp.json) at the repo root, which Claude Code loads
automatically; the plain API clients are just scripts Claude runs directly.

| Server | Language | Entry | What it does |
|---|---|---|---|
| [academic-search](academic-search/) | Python | `academic-search/server.py` | Search Semantic Scholar: papers, details, recommendations (key optional — raises rate limits) |
| [arxiv](arxiv/) | Python | `arxiv/server.py` | Search arXiv and retrieve e-print metadata + full text |
| [gemini-vision](gemini-vision/) | Python | `gemini-vision/server.py` | Send images to Google Gemini for vision/description (needs `GEMINI_API_KEY`) |
| [replicate-image](replicate-image/) | Python | `replicate-image/server.py` | Generate images via Replicate models (needs `REPLICATE_API_TOKEN`) |
| [harvard-art-museums-mcp](harvard-art-museums-mcp/) | Node | `harvard-art-museums-mcp/dist/index.js` | Search the Harvard Art Museums collection (needs `HAM_API_KEY`) |
| [hollis-connections](hollis-connections/) | Python (API client, no MCP) | `hollis-connections/primo_search.py` | Search HOLLIS (Harvard Library catalog + article index) via the Primo API (needs `HARVARD_API_KEY` — see its [getting-an-api-key.md](hollis-connections/getting-an-api-key.md)) |

## Setup for cloners

The repo ships a placeholder [`.mcp.json`](../.mcp.json) at the root. **Workshop participants:**
replace its entire contents with the configuration from the Day 4 Google Doc (that version
carries the API keys, which are never published in this public repo), then restart your Claude
session. Everyone else can start from [`.mcp.json.example`](../.mcp.json.example), which is the
same configuration with `${ENV_VAR}` placeholders you resolve with your own keys.

One more thing won't run straight after a `git clone`:

- **Each Python server's installed dependencies** (`.venv/` — gitignored). A venv hardcodes
  absolute paths and platform-specific binaries, so it could never be shared; you rebuild it
  from the committed manifest. Easiest route, no terminal needed: in a Claude session at the
  repo root, ask Claude to run `bash mcps-apis/setup.sh`. (The Node server needs no build —
  its `dist/` ships committed.)

### 1. Build each server's environment

**Python servers (e.g. `arxiv`):**

```bash
cd mcps-apis/arxiv
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

This reproduces the environment from `pyproject.toml` and creates `mcps-apis/arxiv/.venv/`.

Servers that ship a `requirements.txt` instead of a `pyproject.toml` (e.g. `gemini-vision`,
`replicate-image`) install with `pip install -r requirements.txt` after creating the venv. The
servers needing API keys read them from the `env` block in `.mcp.json` (see step 2).

**Node servers:** `harvard-art-museums-mcp` ships its compiled `dist/` committed, so it runs
straight from a clone with only `node` installed — no build step. Rebuild only if you edit
`src/`; each Node server is self-contained — install inside its own folder (a root-level
`pnpm i` will **not** reach subfolders; this repo is not a pnpm workspace):

```bash
cd mcps-apis/<server-name>
pnpm i
pnpm build   # if it compiles TypeScript → dist/
```

### 2. Fill in `.mcp.json`

Replace the placeholder `.mcp.json` at the repo root with the workshop configuration from
the Google Doc (or build your own from [`.mcp.json.example`](../.mcp.json.example)).
The configuration points `arxiv` at the in-repo copy using paths relative to the repo root:

```json
"arxiv": {
  "command": "mcps-apis/arxiv/.venv/bin/python",
  "args": ["mcps-apis/arxiv/server.py"]
}
```

So once you've built the venv in step 1, the `arxiv` server works with no edits. If a relative
`command` does not resolve on your setup, swap in absolute paths (Claude Code expands
`${ENV_VAR}` references but **not** editor tokens like `${workspaceFolder}`).

### 3. Restart Claude Code

Claude Code reads `.mcp.json` on startup and will prompt you to approve project-scoped servers.
Run `/mcp` to confirm a server is connected.

## Windows notes

The setup above (and `setup.sh`) assumes a macOS/Linux shell. On Windows, mind these
differences:

- **`setup.sh` is a bash script** and won't run in CMD or PowerShell. Use **Git Bash** or
  **WSL**, or just run each server's install commands by hand (below).
- **Missing Node/pnpm?** Install Node ≥ 18 (`winget install OpenJS.NodeJS.LTS` or
  <https://nodejs.org/>), then enable pnpm with `corepack enable pnpm` (or `npm install -g pnpm`).
  Missing Python? `winget install Python.Python.3.12` or <https://www.python.org/downloads/>.
- **Python venvs live under `Scripts\`, not `bin/`.** Create/activate and point `.mcp.json` at
  the Windows paths:

  ```powershell
  cd mcps-apis\arxiv
  python -m venv .venv
  .venv\Scripts\activate
  pip install -e .
  ```

  Then in `.mcp.json`, the Python `command` becomes
  `mcps-apis/arxiv/.venv/Scripts/python.exe` (the committed example uses the macOS/Linux
  `.venv/bin/python` path — edit it to match your OS). Forward slashes are fine on Windows.
- **The Node server (`harvard-art-museums-mcp`) is already cross-platform.** Its `.mcp.json`
  entry uses `node` + `dist/index.js`, which runs identically on macOS and Windows once you've
  run `pnpm install && pnpm build` in its folder.
