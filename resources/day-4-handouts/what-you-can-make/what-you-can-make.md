# What You Can Make with Claude — A Gallery

*A gallery of faculty projects, ordered from familiar text toward unfamiliar code.*

**How to read this.** The spine runs from what you already do every day — writing — toward things you may never have built before. Each category names a *kind* of thing you can make: quick examples first, then one unpacked fully — the situation, the inputs, the operations, the outputs, and which Claude interface fits best (Chat / Cowork / Code). Start where you have expertise; climb when you're ready.

## 1. Structured Text & Documents — *most familiar*

Generating finished products in genres you already know.

**Examples:** an email to a chair proposing a new course · an NSF/NIH grant Specific Aims page from a project description · a committee report from raw meeting notes · a letter of recommendation from a CV and a prompt · a conference abstract from a draft paper · a syllabus skeleton from a reading list.

**Unpacked: meeting notes → a clean report for the dean**
- **Situation:** you left a faculty meeting with messy notes and need a structured report by tomorrow.
- **Inputs:** `meeting-notes.md` — your raw bullet points.
- **Operations:** one prompt: "Turn these notes into a report with a summary, decisions made, and action items with owners and dates."
- **Outputs:** `report.md`, or a polished `.docx` on request.
- **Best fit:** Chat or Cowork; Code if repeated monthly.

## 2. Reference Pages (Static HTML) — *intro to code*

Your first step into code: one file, opens in any browser, no setup.

**Examples:** a searchable glossary of course terms · a one-page syllabus website · a printable command/reference dashboard · an illustrated lecture handout · a course-policy FAQ page.

**Unpacked: a glossary your students can search and copy from**
- **Situation:** you want one page holding every key term in your course, searchable, that works offline.
- **Inputs:** `glossary.md` — terms and definitions.
- **Operations:** "Build a single-file HTML page with a search box and click-to-copy, styled for comfortable reading."
- **Outputs:** `glossary.html` — one file you can email or host anywhere.
- **Best fit:** Code or Cowork.

## 3. Web Apps (Next.js) — *more complex*

Multi-page, deployable sites with real interactivity.

**Examples:** a course website with interactive concept demos · a reading-response collection app · an interactive timeline of a period or movement · a "build your own X" student exercise.

**Unpacked: course site for GENED 1049 *East Asian Cinema***
- **Situation:** you want a site that pairs a cinematography glossary with interactive demos built on the films you actually teach.
- **Inputs:** syllabus, *Rashomon* stills, glossary text.
- **Operations:** scaffold a Next.js app, build parametric demo components, deploy to Vercel.
- **Outputs:** a live site (e.g. `gened-1049.vercel.app`) you share by link.
- **Best fit:** Code.

## 4. Bots & Connected Tools (MCP, Slack) — *more complex; today's topic*

Claude wired to live data and other services.

**Examples:** Claude connected to Semantic Scholar for live literature search · an art-history lecture pulling live images from Harvard Art Museums · a Slack bot that answers from your course materials · an oral-exam practice bot · Claude connected to your Google Drive.

**Unpacked: live literature search via the Semantic Scholar MCP**
- **Situation:** you want real papers with real citation counts and DOIs — not citations the model might invent.
- **Inputs:** your research question; a free API key in `.mcp.json`.
- **Operations:** "Find recent papers on X, get details, find related work, save." Claude chains `academic_search` → `academic_get_paper` → `academic_recommend`.
- **Outputs:** a markdown literature summary in `output/` with real DOIs.
- **Best fit:** Code (MCP servers run here).

## 5. Data Visualizations (d3, three.js) — *even more complex*

Turning a corpus or dataset into something you can see and manipulate.

**Examples:** a 2D semantic-embedding map of a text corpus · an interactive chart of course-evaluation trends · a 3D model of a molecule, artifact, or building · a network graph of citations or characters · an animated explainer for a hard concept.

**Unpacked: Calvino's *Six Memos*, by the numbers**
- **Situation:** you want students to see literary qualities as a measurable space — and plot their own prose against it.
- **Inputs:** the five memos as text; definitions for each measure.
- **Operations:** deterministic text analysis + a 2D embedding map + a live draft composer, charts drawn in d3.
- **Outputs:** a live page where pasted prose appears in every chart in real time.
- **Best fit:** Code.

## 6. Agentic Pipelines & Systems — *most complex*

Many tools orchestrated at scale: subagents, connected data, automation.

**Examples:** close-reading a whole corpus with parallel subagents · a reproducible coding pipeline for interview transcripts · an automated weekly research digest (scheduled) · a recommendation engine grounded in institutional data.

**Unpacked: naming every writer cited across 538 Dylan songs**
- **Situation:** you want a close reading at corpus scale — every author named in any lyric, with the line quoted — not a keyword grep.
- **Inputs:** the full corpus of songs (or transcripts, or a long text).
- **Operations:** spawn parallel close-reading subagents, each told to read like a scholar and refuse to grep; aggregate their findings.
- **Outputs:** one aggregated JSON plus a prose writeup pairing each name with its quoted line.
- **Best fit:** Code (subagents, scale).

## ?. The Gesamtkunstwerk — *beyond the map*

Every category above ends in a file. This one doesn't. Somewhere past the bottom of the axis is the **total work** — beyond text, beyond code, out into media forms and the world: an installation that listens and answers; a seminar that generates its own archive as it runs; a dataset performed as sound; an instrument, a fabrication, a room. The project where the website, the handouts, the bots, and the physical space are one continuous thing.

**Nobody has a worked example yet.** The spine runs off the edge of the page here — this row is yours to invent.
