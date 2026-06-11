---
name: quiz
description: >-
  Generate a short-answer quiz that checks whether students grasped the CORE ARGUMENT of
  Grant, Behrends & Basl, "What we owe to decision-subjects" — not example recall. Produces
  a student version (questions only) and a separate instructor answer key with section
  references, common errors, and a scoring band. Use when the user runs /quiz, asks for a
  quiz, exit ticket, end-of-class assessment, comprehension check, or short-answer questions
  on the paper.
---

# /quiz — end-of-class comprehension check

Generate a paper-based short-answer quiz that assesses understanding of the paper's
**core argument**. The default is a closed-book, ~10–15 minute, six-item quiz suitable for
the last block of class.

## What this skill is for

Checking whether students internalized the *structure* of the argument — the
transparency → due-consideration move, the evidential/practical split, and the duties that
fall out of it — rather than whether they can name the examples. Questions should be
answerable in one or two sentences and gradable for the *idea*, not the wording.

## Inputs (all optional)

- **Length / time:** default 6 items / 10–15 min. Accept "exit ticket" (2–3 items, 5 min)
  or "longer" (8–10 items, 20–25 min).
- **Focus:** default covers the whole argument. Accept a narrower target (e.g. "just §5
  evidential consideration," "agential consideration only").
- **Open- vs. closed-book:** default closed-book; adjust phrasing if open-book.
- **Format:** default short answer. Can mix in one applied mini-case drawn from
  `output/cases/` if asked.

## What every quiz must cover (the core-argument checklist)

Unless the user narrows the focus, hit these load-bearing points across the items:

1. **The thesis with a hedge** — the Explainability Thesis is context-sensitive
   ("in many contexts," "often," "prima facie"), not "never use black boxes."
2. **Transparency vs. due consideration** — the paper's central move; due consideration is
   *broader* and constrains how the decision is made, not just what can be disclosed (§2–3).
3. **Evidential vs. practical** consideration — what each constrains (fact-finding vs.
   decision-making) (§3).
4. **At least one evidential failure** — accuracy isn't sufficient; ignoring available
   evidence (§5.2) or relying on inadmissible evidence (§5.3).
5. **Agential consideration** — some decisions need a responsible moral agent; isolate it
   with a case (like the juror models) where accuracy/transparency/rule-content are all
   stipulated away (§7.2–7.3).
6. **The Double Standard reply** — the authors *concede* humans are partly opaque and route
   around it via interpretable models + agential capacity, rather than denying the premise
   (§6).

## Output format

Produce one markdown file with three parts:

1. A short header: topic, format, time, item count, and suggested point weighting.
2. **Student version** — questions only, with a name line and brief instructions. No
   answers, no section references.
3. **Answer key (instructor)** — per item: what a good answer contains, the section
   reference (for the instructor, not required of students), and the **common error** to
   watch for. Close with an optional scoring band tied to whether they got the
   transparency → due-consideration move.

Write generated quizzes to `output/`, not into `inputs/` (which holds the source paper).

## Hard constraints (inherited from the project — see ../../../prompts/CLAUDE.md)

- **Claude writes the quiz; the instructor owns grading and final marks.** Do not assign
  scores to real student work or render a verdict on a person — produce the instrument and
  the key, and leave judgment to the human.
- **Test the argument, not "AI is bad."** A correct answer to Q1 must include the hedge; an
  answer that reads the thesis as absolute is a *wrong* answer, and the key must say so.
- **Keep transparency and due consideration distinct** in both questions and key.
- **Cite by section; add a page number only if verified against the PDF.** Never invent one.
- **No emojis.** Grade-for-the-idea phrasing in the key.

## Worked example

See [examples/end-of-class-quiz.md](examples/end-of-class-quiz.md) — the default
six-item, 10–15 minute quiz with student version and full instructor key. Use it as the
template for tone, structure, and the level of the answer-key guidance.
