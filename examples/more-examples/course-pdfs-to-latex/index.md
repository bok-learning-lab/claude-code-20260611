# Index — Course PDFs to a LaTeX template

A folder map. Start with [summary.md](summary.md) for the story;
[CLAUDE.md](CLAUDE.md) holds the session instructions.

## Top level

- [README.md](README.md) — overview of the recipe and the workflow.
- [CLAUDE.md](CLAUDE.md) — session-start instructions for working in this folder.
- [summary.md](summary.md) — the one document to read first.
- [index.md](index.md) — this map.
- [index.html](index.html) — browser-friendly version of this map.

## inputs/ (read-only source)

- [inputs/handoff.md](inputs/handoff.md) — the original anonymized request.
- [inputs/template-to-follow/worksheet-template.tex](inputs/template-to-follow/worksheet-template.tex) — the worksheet style to match.
- [inputs/template-to-follow/problem-set-template.tex](inputs/template-to-follow/problem-set-template.tex) — the problem-set style to match.
- [inputs/source-materials/Worksheets/03-First-Order-Linear-Differential-Equations.pdf](inputs/source-materials/Worksheets/03-First-Order-Linear-Differential-Equations.pdf) — a representative worksheet source (worked notes).
- [inputs/source-materials/Homework/03-First-Order-Linear-Differential-Equations.pdf](inputs/source-materials/Homework/03-First-Order-Linear-Differential-Equations.pdf) — a representative homework source (problem list).

## operations/ (the process)

- [operations/handout.sty](operations/handout.sty) — the provided environment package (used as-is).
- [operations/coursestyle.sty](operations/coursestyle.sty) — the companion visual + accessibility layer.
- [operations/prompts/convert-worksheet-prompt.md](operations/prompts/convert-worksheet-prompt.md) — worked notes to a worksheet.
- [operations/prompts/convert-homework-prompt.md](operations/prompts/convert-homework-prompt.md) — problem list to a problem set.
- [operations/prompts/accessibility-audit-prompt.md](operations/prompts/accessibility-audit-prompt.md) — audit and adapt for WCAG 2.1 AA.
- [operations/scripts/build.sh](operations/scripts/build.sh) — rebuild every example.

## outputs/ (rebuildable)

- [outputs/Worksheets/](outputs/Worksheets/) — converted worksheets (`.tex` + `.pdf`).
- [outputs/Homework/](outputs/Homework/) — converted problem sets (`.tex` + `.pdf`).
- [outputs/ACCESSIBILITY.md](outputs/ACCESSIBILITY.md) — the accessibility audit and gap.
- `outputs/handout.sty`, `outputs/coursestyle.sty` — build-time copies of the style packages (sources of truth are in `operations/`).

## To run end-to-end

Install `tectonic` (and `pdftotext`/poppler for extraction). Extract a source
PDF's text with `pdftotext -layout`, follow the matching prompt in
`operations/prompts/` to write a `.tex` into `outputs/`, then compile it with
`tectonic`. To rebuild all committed examples at once, run
[operations/scripts/build.sh](operations/scripts/build.sh).
