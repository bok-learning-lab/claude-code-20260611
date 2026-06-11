# Index — Handout formatting

A folder map. Start with [summary.md](summary.md) for the story;
[CLAUDE.md](CLAUDE.md) holds the session instructions.

## Top level

- [CLAUDE.md](CLAUDE.md) — session-start instructions for working in this folder.
- [summary.md](summary.md) — the one document to read first.
- [index.md](index.md) — this map.

## .claude/skills/handout-formatting/ (the skill — the engine)

- [SKILL.md](.claude/skills/handout-formatting/SKILL.md) — workflow, triggers, and the two-package house style.
- [styles/housestyle.sty](.claude/skills/handout-formatting/styles/housestyle.sty) — the look (plain black-and-white p-set style: fonts, title block, headings, callout, vocab table, accessibility metadata).
- [styles/handout.sty](.claude/skills/handout-formatting/styles/handout.sty) — the behaviour (environments + the student/key/teacher switch).
- [reference/ingestion.md](.claude/skills/handout-formatting/reference/ingestion.md) — getting text out of `.docx`, PDF, and scans.
- [reference/content-types.md](.claude/skills/handout-formatting/reference/content-types.md) — mapping prose, tables, vocab, dialogue, math, and non-Latin scripts to environments.
- [reference/accessibility.md](.claude/skills/handout-formatting/reference/accessibility.md) — the WCAG 2.1 AA checklist and the engine's gap.
- [scripts/build.sh](.claude/skills/handout-formatting/scripts/build.sh) — compile a `.tex` or a whole tree.

## inputs/ (read-only source — the "before")

- [inputs/spanish/spanish-rutina-diaria-DRAFT.docx](inputs/spanish/spanish-rutina-diaria-DRAFT.docx) — a deliberately messy intermediate-Spanish handout.
- [inputs/math/Worksheets/](inputs/math/Worksheets/) and [inputs/math/Homework/](inputs/math/Homework/) — the original DE source PDFs, carried over to regression-test the generalized skill.

## outputs/ (rebuildable — the "after")

- [outputs/spanish/rutina-diaria.tex](outputs/spanish/rutina-diaria.tex) — the single source for the Spanish worksheet, plus a [rutina-diaria-key.tex](outputs/spanish/rutina-diaria-key.tex) wrapper, each compiled to `.pdf`. (The source also builds a teacher copy via `[teacher]`; the math worksheets ship that tier.)
- [outputs/math/Worksheets/](outputs/math/Worksheets/) and [outputs/math/Homework/](outputs/math/Homework/) — the four DE documents re-issued in the generalized house style, `.tex` + `.pdf`.
- [outputs/ACCESSIBILITY.md](outputs/ACCESSIBILITY.md) — the accessibility audit and the honest gap.
- `housestyle.sty`, `handout.sty` beside each `.tex` — build-time copies (sources of truth live in the skill's `styles/`).

## To run end-to-end

Install `tectonic` (compile), `pandoc` (`.docx`), and `pdftotext`/poppler (typed
PDF). Then follow [SKILL.md](.claude/skills/handout-formatting/SKILL.md): ingest
a source, convert it to a house-style `.tex` in `outputs/`, and compile with
`tectonic`. To rebuild every committed example at once, run
`bash .claude/skills/handout-formatting/scripts/build.sh outputs`.
