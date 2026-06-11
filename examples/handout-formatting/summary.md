# Handout formatting

A faculty member has rough course materials — a Word doc with mismatched fonts,
a vocabulary list pasted with five different delimiters, a conjugation table
whose columns don't line up, a worksheet whose math is baked-in Unicode glyphs.
They want all of it re-issued as clean, consistent, print-ready handouts that
look the same across the course, with a student version and an answer key coming
from one file, and with accessibility built in.

This example packages that work as a reusable **skill**,
[handout-formatting](.claude/skills/handout-formatting/SKILL.md), and proves it
on two very different subjects: an intermediate-Spanish reading-and-vocab sheet
and a differential-equations course.

## The move worth noticing

The earlier recipe this generalizes (a math-only converter built in a previous
workshop) had a math-specific style package. The transferable idea is to
**split the house style into two layers** so one machine serves every subject
and audience:

- **[housestyle.sty](.claude/skills/handout-formatting/styles/housestyle.sty)** —
  the *look*: a plain black-and-white, standard problem-set aesthetic. Fonts
  (Unicode-first, so accents and non-Latin scripts compile directly), a centered
  title block, plain bold section headings, a thin-ruled callout box, a clean
  vocabulary table, dialogue/gloss helpers, and the PDF accessibility metadata.
  It knows nothing about math, vocab, or exercises.
- **[handout.sty](.claude/skills/handout-formatting/styles/handout.sty)** — the
  *behaviour*: the content environments (`exercise`, `solution`, `note`,
  `passage`, `problemonly`, `\fitb`) and the **audience switch**.
  `\usepackage[]{handout}` is the student handout; `[key]` shows answers;
  `[teacher]` adds teacher notes. The body is written once; the audience is a
  compile option.

Because the layers are separate, a department can drop in its own visual layer
without touching the exercise logic — and the same `handout.sty` that toggles a
math worksheet's solutions also toggles a Spanish drill's fill-in-the-blanks.

## What it is

- **Skill** (the engine):
  [.claude/skills/handout-formatting/](.claude/skills/handout-formatting/) —
  [SKILL.md](.claude/skills/handout-formatting/SKILL.md) (workflow + triggers),
  the two style packages in
  [styles/](.claude/skills/handout-formatting/styles/), three reference docs in
  [reference/](.claude/skills/handout-formatting/reference/)
  ([ingestion](.claude/skills/handout-formatting/reference/ingestion.md),
  [content-types](.claude/skills/handout-formatting/reference/content-types.md),
  [accessibility](.claude/skills/handout-formatting/reference/accessibility.md)),
  and [scripts/build.sh](.claude/skills/handout-formatting/scripts/build.sh).
- **Inputs** (read-only source):
  - [inputs/spanish/](inputs/spanish/) — a deliberately messy Word handout (the
    "before": inconsistent fonts, mixed vocab delimiters, a misaligned
    conjugation table, answers baked into the exercises).
  - [inputs/math/](inputs/math/) — the original DE worksheet and homework PDFs,
    carried over to confirm the generalized skill still handles math.
- **Outputs** (rebuildable):
  - [outputs/spanish/](outputs/spanish/) — the cleaned worksheet as one source
    (`rutina-diaria.tex`) plus a `-key` wrapper, each compiled to PDF.
    **These are the real artifact.**
  - [outputs/math/](outputs/math/) — the four DE documents re-issued through the
    generalized house style, compiled to PDF.
  - [outputs/ACCESSIBILITY.md](outputs/ACCESSIBILITY.md) — the WCAG 2.1 AA audit
    and the honest gap.

## How we built it

- **Generalized the style.** Took the math recipe's two ideas (a provided
  behaviour package + a companion visual layer; one source, multiple audiences
  via options) and rewrote both packages to be subject-agnostic: Unicode-first
  fonts, general environments (`passage`, `vocabtable`, `\dialogue`, `\gloss`,
  `\fitb`) alongside the kept `exercise`/`solution`/`note`, and a clean
  `key`/`teacher` audience switch.
- **Wrote the skill around the workflow** — ingest (per source format), convert
  (per content type), compile-and-look, accessibility pass — with the details
  pushed into reference docs so the skill body stays short.
- **Built a messy Spanish source** as a real `.docx` and cleaned it: the
  five-delimiter vocab list became a tidy `vocabtable`; the misaligned
  conjugation table became a `booktabs` table; the answers baked into the
  exercises moved into `solution`/`\fitb` so the student and key versions come
  from one file. The reading passage's accents compile directly (no escapes).
- **Regression-tested on math.** Took the four differential-equations documents
  from the earlier recipe and rebuilt them in the generalized house style. They
  needed only a preamble swap (point them at `housestyle` + `handout` and adjust
  the audience option) and one new general environment (`problemonly`, a
  student-only block); the equations render correctly in the new packages. That
  is the evidence the broadening did not break the original case.
- **Compile-verify loop.** Every file is compiled with `tectonic` and rendered to
  an image; nothing is "done" until it builds and looks right.
- **Accessibility, baked in.** Monochrome by default (maximal contrast, nothing
  on color alone), text labels on every box, real sectioning, and per-document
  PDF language + title. The one gap
  the `tectonic` engine cannot close (fully tagged PDF / equation alt text) is
  documented with its `lualatex` + `tagpdf` fallback.

## What you could translate this to

The shape is: **a pile of format- and look-inconsistent source documents becomes
a uniform set of rebuildable, accessible handouts, with student/key/teacher
versions from one source — and the house style is two swappable layers, so it
serves any subject.** That pattern recurs widely:

- **Any course standardizing its materials** — readings, labs, syllabi, exams,
  study guides — across instructors who each arrive in their own format.
- **Language programs** specifically: readings, vocab sets, conjugation drills,
  dialogues, and (with a Unicode font) non-Latin scripts, all in one look.
- **Worksheet/quiz banks** where every item needs a blank student copy and a
  matching key without maintaining two files.
- **Accessibility remediation programs** that treat the shared template as the
  unit of fixing, so every document inherits compliance.

## The hard ones (invariants worth keeping)

- One source, every audience via package options — never fork the body to make a
  key.
- Inputs stay untouched; a cleaned or converted version is always an output.
- Look and behaviour stay in separate packages, so either can be swapped alone.
- A document is not done until it compiles cleanly and you have looked at the
  rendered page — extraction is a draft, not the answer.
