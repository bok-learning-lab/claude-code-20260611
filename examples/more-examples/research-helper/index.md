# research-helper — folder index

A small project that turns source research papers into HTML summaries — each with a neutral summary plus an explicit "implications for teaching, learning & research with LLM harnesses" pass. Start with [summary.md](summary.md); everything else is here for browsing.

## Top-level

- [summary.md](summary.md) — what this project is, how we built it, what you can translate it to
- [CLAUDE.md](CLAUDE.md) — project-level instructions loaded by Claude Code on session start
- [index.md](index.md) / [index.html](index.html) — this file

## inputs/

The source corpus. Currently four papers on long-context attention in LLMs. Numeric filename prefixes are preserved into the outputs.

- [01_context-rot_hong-troynikov-huber_2025.md](inputs/01_context-rot_hong-troynikov-huber_2025.md)
- [02_lost-in-the-middle_liu_2024.pdf](inputs/02_lost-in-the-middle_liu_2024.pdf)
- [03_context-length-alone-hurts_du_2025.pdf](inputs/03_context-length-alone-hurts_du_2025.pdf)
- [14_fully-utilize-context_an_2024.pdf](inputs/14_fully-utilize-context_an_2024.pdf)

## operations/

- [operations/01-generate-research-summary-prompt.md](operations/01-generate-research-summary-prompt.md) — the prompt: read each paper fully, write a faithful neutral summary, then a separate "twist" pass relating the findings to the research agenda

## outputs/

One self-contained HTML per source paper, plus a hub index. Each file is portable (inline CSS, no external assets); the hub states the agenda up top and links every summary.

- [outputs/index.html](outputs/index.html) — the hub
- [outputs/01_context-rot_hong-troynikov-huber_2025.html](outputs/01_context-rot_hong-troynikov-huber_2025.html)
- [outputs/02_lost-in-the-middle_liu_2024.html](outputs/02_lost-in-the-middle_liu_2024.html)
- [outputs/03_context-length-alone-hurts_du_2025.html](outputs/03_context-length-alone-hurts_du_2025.html)
- [outputs/14_fully-utilize-context_an_2024.html](outputs/14_fully-utilize-context_an_2024.html)
- outputs/assets/ — figures/diagrams referenced by the per-paper HTML

---

*To regenerate: drop new papers into `inputs/` (preserve numeric prefixes), then run the prompt at [operations/01-generate-research-summary-prompt.md](operations/01-generate-research-summary-prompt.md). Existing summaries are overwritten in place; the hub is regenerated to include the new entries.*
