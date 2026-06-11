# Course preparation

The **before-class** counterpart to [class-processor](../class-processor/). `class-processor` handles what happens *during* a course — the transcripts, board work, and audio a live session throws off — and turns it into artifacts. `course-preparation` is the work that comes *first*: designing and sharpening the course itself before you ever walk in. Syllabi, assignments, assessment and grading policy, whole-concentration curricula — drafted and improved against real guidance and evidence instead of generic best-practice boilerplate.

It folds in the former `recentering-academics` example as its first fully worked path: turn four layers of source material — the Bok Center's published guidance, Harvard's own institutional case for change, external empirical research on grading, and the director's settled practitioner guidance — into **concrete, source-grounded curricular recommendations** for a department or an individual instructor, built around the Bok Center's *Recentering Academics* initiative (engaged classroom sessions + rigorous, AI-resilient assessment). The canonical before-class move is **running a draft syllabus through the `/syllabus-redesign` skill to improve it.**

A second prep operation, contributed from the CS 1200 project, turns blackboard **lecture recordings** into clean **lecture-notes** documents you can hand students or reuse next term — board content (read from video frames with vision) merged with the spoken narration (the transcript) into a three-layer document. This is the classic course-handoff move: take last year's recordings (even from a different instructor) and turn them into notes you adapt for your own version. See [operations/lecture-notes/](operations/lecture-notes/).

---

## What it is

Two Recentering operations, four reference layers, and a target you're improving — worked on Linguistics (concentration) and CS 20 (syllabus).

### The two Recentering operations

| Operation | Driver | Input | Output |
|---|---|---|---|
| Concentration-level recommendations | [operations/01-concentration-recommendations-prompt.md](operations/01-concentration-recommendations-prompt.md) (prompt) | One Fields-of-Concentration profile | `outputs/<slug>-concentration-recommendations.md` |
| Syllabus-level redesign | [`/syllabus-redesign`](.claude/skills/syllabus-redesign/SKILL.md) (skill) | One course syllabus | `outputs/<course>-syllabus-redesign.md` |

The two are **independent** — they share the reference layers but answer different questions and can be run separately. The syllabus operation is an invocable skill: run `/syllabus-redesign <course>`.

### The inputs (in `inputs/`)

Four **reference layers** that ground every recommendation, plus the **target** you're improving:

- [bok-advice/](inputs/bok-advice/) — the Recentering Academics framework (overview + course policies, assignment design, class sessions, non-traditional assignments, capstones, rubrics). The normative basis: what good practice looks like.
- [harvard-context/](inputs/harvard-context/) — Harvard's institutional case for change: the October 2025 grade report (A's rose from 24% in 2005 to 60.2% in 2025) and the February 2026 grading proposal, plus supporting coverage. The why-now.
- [research/](inputs/research/) — the external evidence base on grading across the full range: `overview.md`, three topic syntheses (full-range task design, discriminating at the top, rubrics differentiation), and the underlying papers. The what-works.
- [director-advice/](inputs/director-advice/) — the Bok Center executive director's settled practitioner guidance (grading for the full range, AI policies, actionable highlights). Stated plainly in the output, not cited.
- [fields-of-concentration/](inputs/fields-of-concentration/) — Harvard College Fields of Concentration (AY 2026–2027), one file per concentration. *(Used by the concentration operation.)*
- [syllabus/](inputs/syllabus/) — the target syllabus (the demo is `cs20-syllabus.md`, CS 20). **Drop your own draft here** to improve it before the term.

### The outputs (in `outputs/`)

- [linguistics-concentration-recommendations.md](outputs/linguistics-concentration-recommendations.md) — the concentration-level worked example.
- [cs20-syllabus-redesign.md](outputs/cs20-syllabus-redesign.md) — the syllabus-level worked example, produced by the skill.
- [gened1074-syllabus-redesign.md](outputs/gened1074-syllabus-redesign.md) — the canonical example the skill is calibrated to match (structure, table, altitude, voice). The skill reads it; keep it.
- [french40-syllabus-redesign.pdf](outputs/french40-syllabus-redesign.pdf) and [bioe53-syllabus-redesign.pdf](outputs/bioe53-syllabus-redesign.pdf) — real participant courses (FREN 40, BioE 53), run through the skill and shared with their instructors' permission.
- [lecture-notes/](outputs/lecture-notes/) — the CS 1200 worked lecture: `slides.md`/`.pdf` (transcribed board) and `notes.md`/`.pdf` (the three-layer deliverable).

### The lecture-notes operation (CS 1200)

A self-contained second operation, contributed by a collaborator, for instructors who teach on a blackboard with no slides. It reconstructs lecture notes from two sources — **what was written** (recovered from video frames) and **what was said** (the transcript) — and merges them into a three-layer document that visually distinguishes captured board content (blue boxes) from spoken narration (structured bullets) from best-effort reconstructions of boards the camera missed (red "GENERATED" boxes). Scripted steps (`operations/lecture-notes/scripts/`) fetch the video and transcript, extract frames, and perceptual-hash-dedupe them to a handful of distinct board states; two agent steps then transcribe the board (`outputs/lecture-notes/slides.md`) and merge it with the narration (`outputs/lecture-notes/notes.md`). Full recipe in [operations/lecture-notes/WORKFLOW_PROMPT.md](operations/lecture-notes/WORKFLOW_PROMPT.md); overview in its [README](operations/lecture-notes/README.md). The discipline that makes it trustworthy: **the board is ground truth, and every reconstruction is visually flagged** so a reader never mistakes a guess for what was actually written.

### The move worth noticing

Every recommendation must trace back to **a specific source principle and a specific feature of the target** — generic best-practice boilerplate is the failure mode the prompts are built to prevent. A precise "this requirement already does X, extend it to Y" is worth more than a generic "add an AI policy." The provenance is in the recommendation itself: the reader can see which Bok principle, which Harvard datum, and which research finding each suggestion rests on, and which feature of *their* course it touches.

The bigger move is the **before/during pairing**: course-preparation sharpens the course before it runs; class-processor captures and distills it while it runs. Same `inputs/ → operations/ → outputs/` shape on both sides of the classroom door.

---

## How we built it

The build is a reference base plus two operations — a prompt (concentration) and a skill (syllabus) — applied to a target.

1. Assemble the four reference layers in `inputs/` (Bok advice, Harvard context, research, director advice) once — they're shared across both operations.
2. Drop the target in `inputs/` — a concentration profile (`fields-of-concentration/`) or a course syllabus (`syllabus/`).
3. Run the matching driver — `/syllabus-redesign <course>` for a syllabus, or the concentration prompt for a profile — which reads the layers and the target, diagnoses honestly, then recommends against the two Recentering pillars. The syllabus skill also studies the canonical GenEd 1074 example to match its shape and voice.
4. Claude writes the recommendations to `outputs/`, one file per operation, each suggestion citing its source principle and the target feature it addresses.

### The discipline the operations enforce

- **Diagnose before recommending.** Read everything; name strengths and gaps honestly before proposing anything.
- **Discipline-specific over generic.** Anchor in the actual tutorials, tracks, thesis, assignments, or policies. If it would read identically for any field, sharpen or cut it.
- **Faithful to the source.** Quote accurately; don't invent requirements or findings; respect the research's cautions.
- **Two operations, two outputs.** Keep concentration- and syllabus-level work separate.

---

## What you can translate this to

The pattern is **a grounded reference base + a draft to improve + a prompt that forces source-specific, honest recommendations**. It applies to most before-class design work:

- **Syllabus review** against a department's or center's teaching principles.
- **Assignment and rubric design** grounded in assessment research.
- **AI-policy drafting** that's specific to a course's actual assignments rather than boilerplate.
- **Whole-program / concentration review** against institutional priorities.
- **Accreditation or learning-outcomes alignment**, where each recommendation must cite the standard and the program feature it touches.

The constant: a real reference base, a real target, and recommendations that are auditable back to both.

---

## Alignment constraints (the hard ones)

- **Source-grounded, not generic.** Every recommendation cites a source principle and a target feature.
- **Honest diagnosis.** Strengths named alongside gaps; no manufactured problems.
- **Faithful to the inputs.** No invented requirements, courses, policies, or findings; research cautions respected.
- **Two operations, two outputs.** Concentration and syllabus work stay separate.
- **Markdown output to `outputs/`**, regenerating in place. No emojis.
