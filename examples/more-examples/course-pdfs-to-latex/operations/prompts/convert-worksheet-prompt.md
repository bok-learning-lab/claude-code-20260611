# Prompt — convert a worked-notes PDF into a template worksheet

Use this when the source is a *lecture-notes* PDF (worked examples, "Ex. Solve
...") that should become an in-class worksheet: each example becomes a problem
with working space plus a worked solution.

This is an idealized prompt, not a transcript. Fill in the bracketed parts.

---

You are converting a Differential Equations lecture-note PDF into a
template-styled LaTeX worksheet.

**Style packages (two of them):**

- [operations/handout.sty](../handout.sty) (referenced as `../handout`) is the
  *provided* environment package. It defines `problem`, `solution`, `note`,
  `grading`, `problemonly` and the option switches `sols`, `plan`, `grading`,
  `nospace`. Note its conventions: the `problem` environment takes an optional
  trailing work-space argument that is a **bare length** like `[4cm]` (or
  `[\vfill]` / `[\vfill \newpage]`) -- not `[\vspace{...}]`. The `note`
  environment is **teacher-only**: it is hidden unless the `plan` (or `notes`)
  option is passed.
- [operations/coursestyle.sty](../coursestyle.sty) (referenced as
  `../coursestyle`) is the *visual layer*: it provides `\handouttitle`,
  `\calloutbox`, `\numbox` (the trapezoid list label), the blue `\section`
  banners, the `color1`/`color2` palette, and the PDF accessibility metadata.

**Read the approved example first:**
[outputs/Worksheets/03-First-Order-Linear-Differential-Equations.tex](../../outputs/Worksheets/03-First-Order-Linear-Differential-Equations.tex).
Match its structure exactly.

**Process for the PDF `<FILE>.pdf`:**

1. Extract text: `pdftotext -layout "<FILE>.pdf" -`.
2. Build the worksheet with this skeleton:
   - `\documentclass[10pt]{article}`
   - `\usepackage{../coursestyle}`
   - `\usepackage[sols,plan]{../handout}` -- the key version (shows solutions and
     teacher notes). Use `[]` for the blank student handout (problems +
     work-space), or `[sols]` for solutions without the teacher notes.
   - `\hypersetup{pdftitle={<Topic> -- Worksheet <N>}}`
   - `\handouttitle{<Topic>}{Worksheet <N>}{}` where `<N>` is the leading number
     in the filename.
   - `\calloutbox{Today's Goals}{...}` with 3-5 itemized goals inferred from the
     content.
   - Short expository intro text as needed; teacher-only asides go in
     `\begin{note}...\end{note}`.
   - Each worked "Ex." becomes:
     ```latex
     \item
       \begin{problem}[<N>cm]
         <problem statement>
       \end{problem}
       \begin{solution}
         <worked solution>
       \end{solution}
     ```
     inside `\begin{enumerate}[leftmargin=*, label=\numbox{\arabic*}]`. Group
     related problems under `\section{...}` banners. Size the bracket (4-6cm) to the problem.
3. **Reconstruct the math carefully.** `pdftotext` scatters exponents,
   fractions, integrals, and subscripts into loose fragments and Unicode (e.g.
   `dy/dx`). Reassemble into correct LaTeX (`\dfrac`, `^{...}`, `_{...}`,
   `\int`, `\sqrt`, `\ln`, `\sin`) and verify each derivation actually follows
   step to step. Fix obvious source typos silently.
4. Write to `outputs/Worksheets/<NN>-<Topic-Words>.tex` (zero-padded number,
   hyphenated title).
5. **Compile to verify:** from the output directory run
   `tectonic "<file>.tex"`. Fix errors and recompile until it builds cleanly.

For any graph/figure you cannot reproduce, insert
`% FIGURE OMITTED: <description>` where it belongs and continue.

Report: output filename, compiled page count, and any figures omitted or math
you were unsure about.
