# CLAUDE.md — Course PDFs to a LaTeX template

These are the instructions loaded when Claude starts a session inside this
folder. Read them before doing anything else.

## What this project is

This recipe converts a course's worksheets and homework — handed over as
Word-exported PDFs (math encoded as Unicode, no LaTeX) — into clean `.tex`
files that follow a specific worksheet/problem-set **template**, and makes the
template accessible along the way.

The reusable move worth noticing: **reconstruct a missing dependency from how it
is used so you stay unblocked, then keep the provided package untouched and own
your additions in a companion file.** The template here depended on a custom
style package that was not shipped, so nothing compiled; it was reconstructed
from usage, and when the author's real `handout.sty` arrived it dropped straight
in. The visual layer and accessibility fixes live separately in
`coursestyle.sty`, so `handout.sty` stays exactly as provided. See
[summary.md](summary.md).

## If you just opened this folder

Read in this order:

1. [summary.md](summary.md) — the whole story, top to bottom.
2. [inputs/handoff.md](inputs/handoff.md) — the original (anonymized) request.
3. [operations/handout.sty](operations/handout.sty) — the provided environment
   package, and [operations/coursestyle.sty](operations/coursestyle.sty) — the
   companion visual + accessibility layer. Together they drive everything.
4. One worked example, source and result side by side:
   [inputs/source-materials/Worksheets/03-First-Order-Linear-Differential-Equations.pdf](inputs/source-materials/Worksheets/03-First-Order-Linear-Differential-Equations.pdf)
   then
   [outputs/Worksheets/03-First-Order-Linear-Differential-Equations.tex](outputs/Worksheets/03-First-Order-Linear-Differential-Equations.tex).

## The pipeline

| Step | What | Output |
| --- | --- | --- |
| 1. Set up style | Use the provided `handout.sty` as-is; put the visual layer + accessibility in the companion `coursestyle.sty`. (Reconstruct `handout.sty` from usage if it is ever missing.) | [handout.sty](operations/handout.sty), [coursestyle.sty](operations/coursestyle.sty) |
| 2. Extract | `pdftotext -layout` each source PDF to get its text + Unicode math. | (scratch) |
| 3. Convert (worksheet) | Worked notes -> problems with work-space + worked solutions. | `outputs/Worksheets/<NN>-<Topic>.tex` |
| 3. Convert (homework) | Numbered problem list -> spaced problem set. | `outputs/Homework/<NN>-<Topic>.tex` |
| 4. Compile | `tectonic <file>.tex` from the output dir; fix until it builds. | the `.pdf` beside each `.tex` |
| 5. Audit | Check the template against WCAG 2.1 AA; record gaps. | [outputs/ACCESSIBILITY.md](outputs/ACCESSIBILITY.md) |

The conversion prompts are in [operations/prompts/](operations/prompts/). To
rebuild every committed example, run [operations/scripts/build.sh](operations/scripts/build.sh).

## Conventions

- **`inputs/` is read-only.** The source PDFs and the template-to-follow are
  never edited in place. A converted file is an *output*.
- **Generated artifacts go in `outputs/`.** `outputs/handout.sty` and
  `outputs/coursestyle.sty` are build-time copies; the sources of truth are in
  `operations/`.
- **No emojis** in any file.
- **Reference files with markdown links**, never bare paths —
  `[handout.sty](operations/handout.sty)`.
- **Relative paths only.** The folder must work when copied out on its own.

## Hard rules / output contract

- **One source, three audiences.** Every document compiles to a student handout,
  a solutions key, or a teacher version by toggling `handout.sty` options (`[]`,
  `[sols]`, `[sols,plan]`) — never by editing the body. `handout.sty` is the
  provided package and stays untouched; all styling/accessibility lives in
  `coursestyle.sty`. The `problem` work-space argument is a bare length (`[4cm]`)
  or `[\vfill]`; `note` is teacher-only (shows under `plan`). Keep this true.
- **Math is reconstructed, not transcribed.** `pdftotext` scatters exponents and
  fractions; every expression must be reassembled into valid LaTeX and checked
  step to step. A converted file must compile cleanly under `tectonic` before it
  is considered done.
- **Filenames:** `<NN>-<Hyphenated-Topic>.tex`, zero-padded number matching the
  source's leading number.
- **Dependencies:** `tectonic` (compile) and `pdftotext`/poppler (extract) are
  external tools. State that plainly; do not assume a full TeX Live install.
