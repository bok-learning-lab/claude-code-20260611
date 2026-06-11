# Course PDFs to a LaTeX template

Turn a course's worksheets and homework — handed over as Word-exported PDFs, with
the math baked in as Unicode glyphs — into clean `.tex` files that follow a house
worksheet/problem-set **template**, with student handouts, solution keys, and
teacher notes all produced from one source, and accessibility built into the
template itself.

This folder is a self-contained **recipe**: a worked example plus the writing
that makes it legible. It works when copied out on its own.

## The move worth noticing

Two transferable ideas. First, when a template depends on a piece you were not
given (here a custom style package that was missing, so nothing compiled),
**reconstruct it from how it is used** so you stay unblocked — and when the real
one arrives, it drops straight in. Second, **keep the provided package untouched
and own your additions in a companion file**: the visual layer it expects inline
and the accessibility fixes live in `coursestyle.sty`, so one source of truth
governs each concern and the author's package can be updated without losing your
work.

## The workflow

| Step | What happens | Where |
| --- | --- | --- |
| 1. Set up the style | Use the provided [handout.sty](operations/handout.sty) as-is for environments; put the visual layer + accessibility in a companion [coursestyle.sty](operations/coursestyle.sty). (If the package is missing, reconstruct it from usage to stay unblocked.) | the two `.sty` files |
| 2. Extract | `pdftotext -layout` each source PDF to recover its text + Unicode math. | (scratch) |
| 3. Convert | Worked notes become problems with work-space + worked solutions; bare problem lists become spaced problem sets. | [operations/prompts/](operations/prompts/) |
| 4. Compile | `tectonic <file>.tex`; reconstruct any scattered math and fix until it builds. | [outputs/](outputs/) |
| 5. Audit | Check the template against WCAG 2.1 AA; apply fixes; record the gap. | [outputs/ACCESSIBILITY.md](outputs/ACCESSIBILITY.md) |

One style package, three audiences: each document compiles to a student handout,
a solutions key, or a teacher version by toggling a package option (`[]`,
`[sols]`, `[sols,plan]`) — never by editing the body.

## Folder layout

- **[inputs/](inputs/)** (read-only source) — the [anonymized request](inputs/handoff.md),
  the [template to follow](inputs/template-to-follow/), and representative
  [source PDFs](inputs/source-materials/) (the "before").
- **[operations/](operations/)** (the process) — the provided
  [handout.sty](operations/handout.sty), the companion
  [coursestyle.sty](operations/coursestyle.sty), the conversion/audit
  [prompts](operations/prompts/), and [build.sh](operations/scripts/build.sh).
- **[outputs/](outputs/)** (rebuildable) — converted worksheets and homework as
  `.tex` plus compiled `.pdf` (the "after"), and the
  [accessibility report](outputs/ACCESSIBILITY.md). Each output topic has a
  matching source PDF in `inputs/` so you can compare before and after.

## Read next

- [summary.md](summary.md) — the full story, top to bottom (start here).
- [CLAUDE.md](CLAUDE.md) — instructions for a Claude session working in this folder.
- [index.md](index.md) — a plain map of every file.

## Running it

Install `tectonic` (compile) and `pdftotext`/poppler (extraction). Then run
[operations/scripts/build.sh](operations/scripts/build.sh) to rebuild every
committed example, or follow a prompt in [operations/prompts/](operations/prompts/)
to convert a new PDF.
