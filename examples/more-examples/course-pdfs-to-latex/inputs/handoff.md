# Handoff brief — convert course materials to a LaTeX template

*This is the anonymized brief that kicked off the recipe. It is source material:
the request as the instructor framed it, lightly cleaned. Do not edit it to match
what was actually built — the gap between this brief and the outputs is part of
the lesson.*

## Who and what

An instructor receives course materials for a class that arrive as typed
documents in `.docx` or `.pdf` form, and occasionally as scanned handwriting.
They want those materials re-issued as
clean, consistent `.tex` files that follow a specific worksheet/problem-set
**template** they already use in another course.

## The two groups of inputs

1. **Class materials to convert** — mostly typed documents (`.docx` / `.pdf`),
   possibly a few scans. Split into `Worksheets/` and `Homework/`.
2. **A template to follow** — an example worksheet and an example problem set,
   in `.tex`, from a course the instructor already taught. The new materials
   should match this template's look and structure.

## The ask

> Look through the class materials, split into Worksheets and Homework, and
> convert each one to a `.tex` file that follows the provided template. Save the
> new files in a parallel folder structure. In the template's worksheets,
> problems are spaced out as proper in-class "work" sheets, whereas the incoming
> documents are usually just a numbered list of problems.

## The additional challenge

> Double-check whether the provided template is considered accessible, then make
> adaptations where needed. Look up the relevant college / state regulations for
> material accessibility. (The incoming materials in their current state are not
> accessible, so improving them is a plus.)

## Notes that shaped the build

- The "Worksheet" source files turned out to be *worked lecture notes*
  ("Ex. Solve ..."), not blank problem lists. Decision: render each worked
  example as a `problem` (with student work-space) plus a worked `solution`, so
  one source produces both a student handout and a solutions key.
- The "Homework" source files *are* bare numbered problem lists. They map onto
  the problem-set template directly, with vertical work-space added.
- The provided template depended on a custom style package that was **not
  included** with it, so the template could not compile as handed over.
  Reconstructing that package is the first real step of the process.
