# course-preparation — folder index

The before-class counterpart to [class-processor](../class-processor/): the work you do *before* you teach — sharpening syllabi, assignments, assessment design, and curricula against real guidance and evidence. Start with [summary.md](summary.md); everything else is here for browsing.

The fully worked path folds in the former `recentering-academics` example — running a draft syllabus (or a concentration profile) through the Bok Center's Recentering Academics framework to get source-grounded recommendations back. Room remains for more prep operations (assignment design, rubric drafting, reading lists) on the same shape.

## Top-level

- [summary.md](summary.md) — what this project is, how we built it, what you can translate it to
- [CLAUDE.md](CLAUDE.md) — project instructions, the inputs, the operations, and the constraints
- [index.md](index.md) — this file
- [.claude/skills/syllabus-redesign/](.claude/skills/syllabus-redesign/SKILL.md) — the invocable `/syllabus-redesign` skill

## inputs/

Four shared **reference layers** plus the **target** you're improving.

- [inputs/bok-advice/](inputs/bok-advice/) — the Recentering Academics framework (overview + course-policies, designing-assignments, facilitating-class-sessions, assessing-non-traditional-assignments, capstone-assignments, rubrics). Normative basis
- [inputs/harvard-context/](inputs/harvard-context/) — Harvard's institutional case: the Oct 2025 grade report and Feb 2026 grading proposal, plus Crimson/Gazette/Inside Higher Ed coverage. Why-now
- [inputs/research/](inputs/research/) — the grading-research evidence base: `overview.md`, three syntheses (full-range-task-design, discriminating-at-the-top, rubrics-differentiation), and the underlying papers (Sadler 2005, Jonsson & Svingby 2007, Butcher et al. 2014, Bar et al. 2009). What-works
- [inputs/director-advice/](inputs/director-advice/) — the executive director's settled practitioner guidance (grading-for-the-full-range, ai-policies, full-range-advice-highlights). Stated plainly, not cited
- [inputs/fields-of-concentration/](inputs/fields-of-concentration/) — Harvard College Fields of Concentration (AY 2026–2027), `primary/` and `secondary/`, one file per concentration
- [inputs/syllabus/](inputs/syllabus/) — the target syllabus; the demo is `cs20-syllabus.md` (CS 20). Drop your own draft here
- [inputs/lecture-recordings/](inputs/lecture-recordings/) — *(lecture-notes operation)* one worked lecture's captured material: deduped blackboard `frames_deduped/` + `transcript.srt`

## operations/ (and the syllabus skill)

- [.claude/skills/syllabus-redesign/SKILL.md](.claude/skills/syllabus-redesign/SKILL.md) — **`/syllabus-redesign`** skill: syllabus-level redesign from one course syllabus (the "improve your draft before class" move)
- [operations/01-concentration-recommendations-prompt.md](operations/01-concentration-recommendations-prompt.md) — concentration-level recommendations from one Fields-of-Concentration profile
- [operations/lecture-notes/](operations/lecture-notes/) — *(third operation)* the CS 1200 lecture-notes pipeline: [WORKFLOW_PROMPT.md](operations/lecture-notes/WORKFLOW_PROMPT.md) (the recipe), [README.md](operations/lecture-notes/README.md) (overview), `scripts/` (fetch/extract/dedupe frames), `render-helpers/` (pandoc boxes)

## outputs/

- [outputs/linguistics-concentration-recommendations.md](outputs/linguistics-concentration-recommendations.md) — concentration worked example
- [outputs/cs20-syllabus-redesign.md](outputs/cs20-syllabus-redesign.md) — syllabus worked example (from the skill)
- [outputs/gened1074-syllabus-redesign.md](outputs/gened1074-syllabus-redesign.md) — canonical calibration example the skill matches (keep it)
- [outputs/french40-syllabus-redesign.pdf](outputs/french40-syllabus-redesign.pdf) — real participant course (FREN 40), used with permission
- [outputs/bioe53-syllabus-redesign.pdf](outputs/bioe53-syllabus-redesign.pdf) — real participant course (BioE 53), used with permission
- [outputs/lecture-notes/](outputs/lecture-notes/) — *(lecture-notes operation)* `slides.md`/`.pdf` (transcribed board) and `notes.md`/`.pdf` (three-layer deliverable)

---

*To run the syllabus path on your own course: drop your draft in `inputs/syllabus/`, then run `/syllabus-redesign <course>` — it reads the four reference layers, your syllabus, and the canonical GenEd 1074 example, and writes `outputs/<course>-syllabus-redesign.md`.*
