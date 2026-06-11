# How we built this — a walkthrough

> **This document is itself an output.** It lives in `output/` alongside the cases,
> discussion plans, audits, and quiz because it models something we want faculty to do:
> *document your own process so the next person — or the next Claude session — can follow
> it.* Read it as both a record of how this project was made and a template for the
> kind of process note you might keep for your own.

A record of the conversation steps that produced this project, the way the
interview-coding gallery project documents its own making. For Jeff and other
participants who want to see the *process* of using Claude Code to turn a piece of
scholarship into a teaching system — not just the final folder.

The shape follows the gallery's interview-coding project on purpose: a dense source
text, the author named as the human in the room, a synthetic corpus engineered for
specific moves, citation-tied skills, and a project-scoped `CLAUDE.md` (in
[`../prompts/`](../prompts/)) that makes the folder self-introducing.

---

## Step 1 — Brief Claude on the source and name the human in the room

> Read this PDF and keep it in context: the Grant, Behrends & Basl paper on what we owe
> to decision-subjects. Jeff Behrends is a participant in our workshop, so I want to
> build a teaching project grounded in *his* paper. Help me think of ways a philosopher
> could use Claude Code to teach the ethics of automated decision-making — aligned with
> his framework, not a generic AI-ethics take.

**The move worth noticing:** a single dense source plus a named human whose view must
be respected produces far more aligned output than "help me teach AI ethics." The paper
is the constraint; Jeff's authorship is the second constraint. It also surfaced the
guardrail that organizes everything else — see Step 3.

## Step 2 — Capture the thinking in a document

> Put the brainstorm in a claude-thoughts doc, with a skills catalog and a section on
> what to avoid given that this is Jeff's own paper.

**What happened:** [claude-thoughts.md](../prompts/claude-thoughts.md) — the teaching use
cases, a six-skill catalog each tied to a section, MCP candidates, and **Section E: what
to avoid in front of Jeff**, the analog of the "don't pitch theme-discovery in front of
Mary" guardrail.

## Step 3 — Find the alignment constraint that the source itself dictates

The paper is about the limits of relying on AI for consequential decisions about
people. The workshop is about relying on an AI tool. That tension *is* the lesson, so
the hard constraint wrote itself:

> **Claude is never the decision-maker about a person. It augments the teacher and
> generates material; the human stays the moral agent.**

A project built on this paper that let Claude render verdicts would refute itself. The
constraint is recorded at the top of [CLAUDE.md](../prompts/CLAUDE.md) ("The
self-referential point") and threaded through every skill spec. This is the step most
worth imitating when you build from someone's scholarship: let the source text tell you
what the tool must *not* do.

## Step 4 — Build a synthetic teaching corpus

> Generate the cases and sample student arguments we'll teach against.

**What happened:** four cases and three student arguments (here in `output/`, since they
are generated artifacts) — each engineered to surface one move, including
[C3](cases/C3-interpretable-alt.md), the decoy that should *pass* an audit (the §6
interpretable third option), and S1–S3, designed to be wrong in ways the paper diagnoses
precisely. Synthetic beats real here for the same reasons as in the interview-coding
project: right length for live reading, no FERPA/privacy issues, and you can engineer the
exact edge case you want to teach.

## Step 5 — Turn the brainstorm into a parallelizable plan

> Put the three demo skills into a PLAN.md so different Claudes can build them in
> parallel.

**What happened:** [PLAN.md](../prompts/PLAN.md) — shared context and hard constraints up
top, then three self-contained tasks (`/teaching-case`, `/discussion-plan`,
`/objection-audit`), each with behavior, what-good-looks-like, what-to-avoid, build
location, and validation against the corpus.

## Step 6 — Build the skills in parallel, then audit

We opened fresh Claude Code sessions and ran the three PLAN tasks, then audited each
return against the corpus and **verified every section citation against the paper** — the
characteristic failure mode for a project like this is a plausible but slightly-off
citation. What the three produced:

- **`/teaching-case`** — built at [`../.claude/skills/teaching-case/`](../.claude/skills/teaching-case/),
  with worked examples in its `examples/` folder: a fresh §5.2 case in a medical-bail
  setting and a decoy that correctly comes back clean.
- **`/discussion-plan`** — built at [`../.claude/skills/discussion-plan/`](../.claude/skills/discussion-plan/);
  its run on C1 was promoted to [`discussion-plans/`](discussion-plans/).
- **`/objection-audit`** — built at [`../.claude/skills/objection-audit/`](../.claude/skills/objection-audit/);
  its audits of S1–S3 were promoted to [`objection-audits/`](objection-audits/).

**The move worth noticing:** the audit step is not optional. The most common failure for
parallel-built skills is plausible-looking output with small honesty bugs — a paraphrase
passed off as a quote, a section number that's slightly wrong. A short verification pass
against the source catches those before they reach a reader. Trust, but verify.

## Step 7 — Ship one finished skill as the reference example

> Also generate a short-answer quiz students could do on paper at the end of class to
> check whether they grasped the core argument — then turn it into a reusable /quiz skill.

**What happened:** we built [`/quiz`](../.claude/skills/quiz/) end-to-end — a `SKILL.md`
plus a worked example — and promoted the quiz itself to
[`end-of-class-quiz.md`](end-of-class-quiz.md). Its hard constraint follows the project's
line: Claude writes the instrument and the key, but the instructor owns grading and final
marks. Leaving a completed exemplar (not just specifications) is a good move when handing
a project to others.

---

## Why this is a good Day-3 anchor

Day 3's ethics block is where the values conversation is meant to land, on the work
participants just did. These three skills are narrow, repeatable, and single-purpose —
and the paper they implement is *about* when a narrow automated system should and should
not be trusted with a decision. So the ethics conversation and the skills lesson become
the same conversation. And because the project visibly keeps Claude in the augmentation
role the paper prescribes, the demo *shows* the thesis instead of just citing it.

## A note on prompting

Each prompt above is short. None dictates what Claude should write. They give a goal
and one or two alignment constraints (align with Jeff's view; keep Claude out of the
verdict; make it parallelizable) and trust Claude to produce the artifact. That
delegation — and the audit pass that follows it — is the part worth practicing live.
