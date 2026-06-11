# recentering-academics — folder index

A worked example of using Claude Code to turn Bok Center guidance, Harvard institutional context, and external grading research into source-grounded curricular recommendations for a department or an individual course. Start with [summary.md](summary.md); everything else is here for browsing.

## Top-level

- [summary.md](summary.md) — what this project is, how we built it, what you can translate it to
- [CLAUDE.md](CLAUDE.md) — project-level instructions loaded by Claude Code on session start
- [index.md](index.md) / [index.html](index.html) — this file

## inputs/

Three source layers (Bok normative, Harvard urgency, external research) plus two targets (concentration profiles and a sample syllabus).

- inputs/bok-advice/ — the Bok Center's *Recentering Academics* framework
  - [recentering-academics.md](inputs/bok-advice/recentering-academics.md) / [.html](inputs/bok-advice/recentering-academics.html) — overview
  - [course-policies.md](inputs/bok-advice/course-policies.md) / [.html](inputs/bok-advice/course-policies.html)
  - [designing-assignments.md](inputs/bok-advice/designing-assignments.md) / [.html](inputs/bok-advice/designing-assignments.html)
  - [facilitating-class-sessions.md](inputs/bok-advice/facilitating-class-sessions.md) / [.html](inputs/bok-advice/facilitating-class-sessions.html)
- inputs/harvard-context/ — Harvard's institutional case for change
  - [harvard-grade-report.md](inputs/harvard-context/harvard-grade-report.md) / [.pdf](inputs/harvard-context/harvard-grade-report.pdf) — Dean Claybaugh's October 2025 grade report (the data)
  - [proposal-grading-policies.md](inputs/harvard-context/proposal-grading-policies.md) / [.pdf](inputs/harvard-context/proposal-grading-policies.pdf) — February 2026 Subcommittee proposal (20%+4 cap, ave-percentile-rank)
  - Supporting coverage: [Gazette plan-explained](inputs/harvard-context/gazette-plan-explained.md), [Gazette leading-fas](inputs/harvard-context/gazette-leading-fas.md), [Crimson on the rigor problem](inputs/harvard-context/crimson-rigor-problem.md), [Crimson 15Q with Claybaugh](inputs/harvard-context/crimson-claybaugh-15q.md), [1636 on grade-inflation](inputs/harvard-context/1636-grade-inflation-persists.md), [1636 on PhD cuts](inputs/harvard-context/1636-phd-cuts.md), [Inside Higher Ed on the cap](inputs/harvard-context/insidehighered-cap.md)
- inputs/research/ — external empirical evidence on grading
  - [overview.md](inputs/research/overview.md) — synthesis
  - [Sadler_2005](inputs/research/Sadler_2005.md) / [.pdf](inputs/research/Sadler_2005.pdf) — criterion- vs norm-referenced grading
  - [Jonsson & Svingby_2007](inputs/research/Jonsson%20%26%20Svingby_2007.md) / [.pdf](inputs/research/Jonsson%20%26%20Svingby_2007.pdf) — analytic rubrics, exemplars, rater training
  - [Butcher et al_2014](inputs/research/Butcher%20et%20al_2014.md) / [.pdf](inputs/research/Butcher%20et%20al_2014.pdf) — the Wellesley mean cap
  - [Bar et al_2009](inputs/research/Bar%20et%20al_2009.md) / [.pdf](inputs/research/Bar%20et%20al_2009.pdf) — Cornell median-posting experiment
- inputs/fields-of-concentration/ — the targets for the concentration operation
  - [fields-of-concentration.pdf](inputs/fields-of-concentration/fields-of-concentration.pdf) — official source
  - **primary/** — one markdown file per primary field
  - **secondary/** — one markdown file per secondary field
- inputs/syllabus/ — the target for the syllabus operation
  - [sample-syllabus.docx](inputs/syllabus/sample-syllabus.docx) — LING 5312 (Language & Politics)

## operations/

Two prompts, one per operation.

- [operations/01-concentration-recommendations-prompt.md](operations/01-concentration-recommendations-prompt.md) — takes one Fields-of-Concentration profile; produces concentration-level recommendations
- [operations/02-syllabus-redesign-prompt.md](operations/02-syllabus-redesign-prompt.md) — takes one course syllabus; produces a syllabus-level redesign

## outputs/

Worked examples for the Linguistics demo.

- [outputs/linguistics-concentration-recommendations.md](outputs/linguistics-concentration-recommendations.md) — recommendations for the Linguistics concentration
- [outputs/sample-syllabus-redesign.md](outputs/sample-syllabus-redesign.md) — redesign of LING 5312 (Language & Politics)

---

*To run the demo: open this folder in Claude Code, then invoke either prompt against the Linguistics target (or substitute a different concentration profile or syllabus). Existing outputs are overwritten in place rather than producing parallel copies.*
