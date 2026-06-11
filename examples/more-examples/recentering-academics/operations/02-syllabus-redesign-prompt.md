# Prompt: Generate a Syllabus-Level Recentering Redesign

Use this prompt to audit one course syllabus against the Bok Center's Recentering
Academics initiative and propose concrete, line-level revisions. Output is a single
Markdown file in `outputs/`.

This operation is **separate** from the concentration-level operation
([01-concentration-recommendations-prompt.md](01-concentration-recommendations-prompt.md)).
Run it on its own. Optionally, if a concentration-recommendations file already exists in
`outputs/` for the same field, pass it in as background so the syllabus advice inherits
the discipline-level stance — but the syllabus redesign stands alone.

---

## How to share inputs

Point Claude at the three evidence layers and the syllabus:

1. **The Bok framework** in `inputs/bok-advice/` (overview + the three guidance pages, each
   as `.md` and `.html`). Read these first; they are the standard the syllabus is
   measured against.
2. **The Harvard context** in `inputs/harvard-context/` — especially
   `harvard-grade-report.md` (the grade-compression data and the functions grading has
   stopped performing) and `proposal-grading-policies.md` (the A definition as
   "extraordinary distinction" and the 20%+4 cap). This is what gives the grading-rigor
   audit its teeth.
3. **The research evidence** in `inputs/research/overview.md` — the validated practices
   for grading the full range (criterion-referenced standards, analytic rubrics with
   exemplars, rater calibration) that the recommended revisions should rest on.
4. **One course syllabus** — e.g. `inputs/syllabus/sample-syllabus.docx`. Claude can read
   the `.docx` directly. The syllabus carries the course's description, learning
   objectives, class format, graded components and weights, grading scheme, and course
   policies (attendance, late work, devices, AI, integrity).

---

## Prompt

```
I'm helping the instructor of [COURSE] revise their syllabus to align with the Bok
Center's Recentering Academics initiative. The Bok framework is in inputs/bok-advice/,
Harvard's institutional case is in inputs/harvard-context/, and the external research
evidence on grading is in inputs/research/. The syllabus is at inputs/syllabus/[file].

First, read the three evidence layers (Bok advice, Harvard context, research) and the
syllabus in full. Do not write recommendations yet.

Then produce a single Markdown file in outputs/ named [course]-syllabus-redesign.md
with these sections:

1. Header — course title and number, the source syllabus path, the date, and a
   two-to-three-sentence overall assessment: how well does this syllabus already center
   academics, and what is the single biggest gap?

2. Audit table — a table with one row per Recentering touchpoint (attendance &
   participation, in-class device use, generative-AI policy, assignment design /
   AI-resilience, cumulative assessment, grading rigor & range, feedback & consistency).
   Columns: Touchpoint | What the syllabus currently says (quote or "not addressed") |
   Expectation (Bok guidance, and the Harvard report / research where relevant) | Gap.

3. Recommended revisions, organized under the two Recentering pillars:
   - Meaningful and engaged classroom experience — concrete edits to attendance,
     participation, device, and in-class-activity language, each tied to specific
     existing syllabus text and the relevant Bok guidance.
   - Rigorous assessment and feedback — concrete edits to the graded components,
     weights, grading scheme, and assignment design so the work is reliable evidence of
     the student's own thinking, cumulative, and graded across a meaningful range. For
     the grading-range edits, draw on the research evidence: attach an analytic,
     topic-specific rubric with A/B/C exemplars (Jonsson & Svingby 2007), grade against
     explicit criterion-referenced standards rather than a curve (Sadler 2005), and
     articulate what A-level vs. B-level work looks like (Harvard's ask that faculty make
     grade standards explicit, and the FAS rubric reserving A for "extraordinary
     distinction"). Tie each to specific existing syllabus text and the Bok guidance on
     designing assignments.
   For each revision, show "Currently: ..." (quote the syllabus) and "Revise to: ..."
   (proposed replacement language the instructor could paste in).

4. A drafted generative-AI policy — actual syllabus-ready paragraph(s) calibrated to
   this course's assignments and learning objectives, following the Bok guidance on
   clear AI policies. If the syllabus already has one, strengthen it; if not, write one.

5. What to keep — name the syllabus elements that already center academics well, so the
   instructor doesn't revise away something that's working (e.g. a grading scale that
   already uses the full range, or assessments that already elicit gradeable differences).

Quote the syllabus accurately and cite the source you draw on (Bok guidance, the Harvard
reports, or a specific study). Every revision must attach to specific syllabus text, not
generic advice. Be honest about what's already strong.
```

---

## Output

Write to `outputs/<course>-syllabus-redesign.md` (overwriting any existing copy).
