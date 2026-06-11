# CLAUDE.md — Recentering Academics Project

This project helps faculty bring a course or a whole concentration into alignment with
the Bok Center's **Recentering Academics** initiative: centering students' academic
experience through (1) meaningful, engaged classroom sessions and (2) rigorous
assessment and feedback that grades the full range of student achievement and is
resilient to generative AI. It turns three layers of source material — Harvard's
published guidance, Harvard's own institutional case for change, and the external
research evidence on grading — plus a concentration's Fields-of-Concentration profile
(or a single course syllabus) into concrete, source-grounded curricular recommendations.

The source materials live in `inputs/`. The prompts that drive each operation live in
`operations/`. Generated recommendations go in `outputs/`.

## Inputs

The evidence is organized into three layers that play distinct roles. Read all three
before generating anything, in the order below — the Bok guidance is the normative
standard, the Harvard context supplies the urgency and the grade data, and the research
supplies the validated practices.

- [inputs/bok-advice/](inputs/bok-advice/) — the Bok Center's
  Recentering Academics framework (each page as both `.md` and `.html`): the overview
  (`recentering-academics`) and its three guidance pages — `course-policies`,
  `designing-assignments`, `facilitating-class-sessions`. This is the **normative basis**
  for every recommendation: what good practice looks like.
- [inputs/harvard-context/](inputs/harvard-context/) — Harvard's own
  institutional case for change. The anchor documents are Dean Claybaugh's October 2025
  report [harvard-grade-report.md](inputs/harvard-context/harvard-grade-report.md)
  (the data on grade compression — A's rose from 24% of grades in 2005 to 60.2% in 2025 —
  and the argument that grading has stopped performing its core functions of motivation,
  information, and distinction) and the February 2026 Subcommittee on Grading proposal
  [proposal-grading-policies.md](inputs/harvard-context/proposal-grading-policies.md)
  (the 20%+4 cap on A grades and the average-percentile-rank internal metric). The
  Crimson, Gazette, and Inside Higher Ed pieces are supporting coverage. This layer is
  the **why now** — the stakes specific to Harvard.
- [inputs/research/](inputs/research/) — the external empirical evidence
  base on grading across the full range and curbing inflation, synthesized in
  [overview.md](inputs/research/overview.md) and backed by four collected papers
  (Sadler 2005 on criterion- vs norm-referenced grading; Jonsson & Svingby 2007 on
  analytic rubrics, exemplars, and rater training; Butcher et al. 2014 on the Wellesley
  mean cap; Bar et al. 2009 on the Cornell median-posting experiment). This layer is the
  **what works** — the validated practices a recommendation should rest on.
- [inputs/fields-of-concentration/](inputs/fields-of-concentration/) — Harvard College
  Fields of Concentration (AY 2026–2027), one Markdown file per concentration under
  `primary/` and `secondary/`. Each carries the discipline's self-description, learning
  objectives, course/tutorial requirements, and enrollment statistics.
- [inputs/syllabus/sample-syllabus.docx](inputs/syllabus/sample-syllabus.docx) — a
  representative course syllabus (LING 5312, Language & Politics) used as the worked
  example for the syllabus-level operation.

## The two operations

This project runs two **separate** operations with **separate** outputs. They share the
three source layers (Bok advice, Harvard context, research) but answer different
questions and can be run independently.

| Operation | Prompt | Input | Output |
|---|---|---|---|
| Concentration-level recommendations | [operations/01-concentration-recommendations-prompt.md](operations/01-concentration-recommendations-prompt.md) | One Fields-of-Concentration profile | `outputs/<slug>-concentration-recommendations.md` |
| Syllabus-level redesign | [operations/02-syllabus-redesign-prompt.md](operations/02-syllabus-redesign-prompt.md) | One course syllabus | `outputs/<course>-syllabus-redesign.md` |

The worked example for both is **Linguistics**: the concentration operation runs on
[inputs/fields-of-concentration/primary/linguistics.md](inputs/fields-of-concentration/primary/linguistics.md),
and the syllabus operation runs on the LING 5312 syllabus.

## How to work in this project

You are acting as a curricular consultant for the Director of Harvard's Bok Center
Learning Lab, advising a department or instructor. The job is to translate the Bok
Recentering Academics principles — backed by Harvard's institutional case and the
external research evidence — into recommendations that are **specific to this discipline
or this course**, grounded in its actual requirements, intellectual character, and
assessment structure, not generic best-practice boilerplate.

Two passes, in order, so the framing does not distort the diagnosis:
1. **Read and diagnose first.** Read all three source layers (Bok advice, Harvard
   context, research) and the target (concentration profile or syllabus) fully. Note
   where the target already centers academics and where it has gaps — be honest about
   both.
2. **Recommend second.** Organize recommendations around the two Recentering pillars
   (engaged classroom experience; rigorous assessment & feedback), and tie each to the
   specific feature of the discipline/course it addresses.

Every recommendation must trace back to something concrete — a source principle and a
specific feature of the target. Cite both. For assessment and grading recommendations,
prefer the research-validated practice (criterion-referenced standards, analytic rubrics
with exemplars, rater calibration) over generic advice, and invoke the Harvard grade
data where it sharpens the stakes. A precise "this requirement already does X, extend it
to Y" is worth more than a generic "add an AI policy."

## Constraints

- **Discipline-specific over generic.** Anchor recommendations in the concentration's
  actual structure (tutorials, tracks, thesis, method courses) or the syllabus's actual
  assignments and policies. If a recommendation would read identically for any field,
  it is too generic — sharpen it or cut it.
- **Faithful to the source.** Quote the Bok guidance, the Harvard reports, the research,
  and the target accurately. Do not invent requirements, courses, policies, or findings
  that aren't in the inputs. When citing the research, respect its cautions (e.g. mean
  caps work but are costly; publishing grade data to students can backfire).
- **Honest diagnosis.** Name what the target already does well, not only its gaps.
  Don't manufacture problems to justify recommendations.
- **Two operations, two outputs.** Keep concentration-level and syllabus-level work in
  separate output files. Don't merge them.
- **Markdown output**, written to `outputs/`. Regenerating overwrites the existing file
  rather than creating a parallel copy.
- **No emojis** in any file (workshop-wide convention).
- **Markdown link syntax** for file references.
