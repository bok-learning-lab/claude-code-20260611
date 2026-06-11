---
name: discussion-plan
description: >-
  Build a Socratic discussion plan for teaching a case or a section of Grant, Behrends &
  Basl, "What we owe to decision-subjects." Produces a timed sequence — warm-up, core
  dilemma, the positions students will take, the objection to steer toward, and the move
  in the paper that addresses it — with an honest note on what the case can and can't show.
  Use when the user runs /discussion-plan, asks for a seminar plan, lesson plan, Socratic
  sequence, or discussion questions around a case or a section of the paper.
---

# /discussion-plan — build a Socratic discussion plan

Turn a case (or a section) into a sequence that walks students *from* the intuitive answer
*to* the paper's reframing — eliciting the moves rather than asserting them.

## Inputs

- **Case or section** (required): a case ID (e.g. `C1`), a path to a generated case, or a
  section of the paper (e.g. `§5.3`).
- **Length** (optional): default ~45 minutes; accept shorter/longer.

## Process

1. Read the case (or section) and identify the single move it best surfaces.
2. Anticipate the student positions — check the corpus student arguments in
   `../../../output/student-arguments/` and route each to the section that answers it.
3. Sequence from intuition to reframing; end on what the case can and cannot show.

## Output

One markdown file:

- **Warm-up** — a question that elicits the *intuitive* (usually transparency- or
  accuracy-based) answer, so the reframing has something to push against.
- **Core dilemma** — the turn that makes the intuitive answer uncomfortable.
- **Positions to expect** — the likely student moves, each linked to its corpus argument
  (S1–S3) and the section that addresses it.
- **Objection to steer toward** — the one Problem or distinction this case is built to
  teach.
- **The move that resolves it** — the relevant step in the paper.
- **Honest note** — what the case does *not* establish (so the room doesn't overshoot).

Write plans to the skill's `examples/` (for demos) or to `output/discussion-plans/`.

## Hard constraints (inherited — see ../../../prompts/CLAUDE.md)

- **Don't lecture the conclusion.** The plan should make students *do* the reasoning;
  questions over assertions.
- **Keep transparency vs. due consideration, and substantive vs. procedural, live** where
  they do work.
- **Don't present the thesis as absolute.** End on the honest note; the paper is
  context-sensitive and overridable.
- **Cite by section; never invent a page number. No emojis.**

## Worked example

- [examples/discussion-plan-C1.md](examples/discussion-plan-C1.md) — a 45-minute plan
  around the pretrial recidivism case (C1), routing through S1 to §5.2. (Also promoted to
  `output/discussion-plans/`.)
