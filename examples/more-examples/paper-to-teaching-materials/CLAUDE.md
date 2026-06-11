# CLAUDE.md — Decision-subject ethics (teaching project)

Project-level instructions loaded when Claude Code starts in this folder.

## What this project is

A worked example of using Claude Code to **build and run teaching material** for an ethics-of-AI session, grounded in Jeff Behrends' co-authored paper:

> Grant, D. G., Behrends, J., & Basl, J. (2025). "What we owe to decision-subjects: beyond transparency and explanation in automated decision-making." *Philosophical Studies* 182, 55–85. (Open access, CC BY 4.0.)

Built for the *Summer of Claude* faculty workshop at Harvard's Bok Center. Jeff Behrends is among the workshop participants, so the design choices throughout are aligned with **his** paper's framework and its careful hedges. See [summary.md](summary.md) for the full project overview, the framework the skills apply, the build sequence, and the alignment constraints.

This folder is meant to be opened as a standalone Claude Code project — `cd` into it, run `claude`, and everything you need is here.

## The self-referential point (read this first)

The workshop is teaching faculty to lean on an AI tool. Behrends' paper is precisely about the **limits of relying on AI for consequential decisions about people.** That tension is the lesson, not a problem to hide. So this project models the relationship the paper *prescribes*:

- Claude **augments the instructor's own reasoning** and generates teaching material.
- Claude **never makes the consequential call** — it surfaces candidates for human judgment, drafts cases, maps arguments. The human stays the moral agent.
- That is exactly the "human-in-the-loop with genuine agential consideration" the paper contrasts (§7.3) with blind deference / automation bias.

If a skill or output ever positions Claude as the *decider* about how a person should be treated, it has violated the paper it is built on.

## If you just opened this folder

Read in this order:

1. [summary.md](summary.md) — what this is, the framework, how we built it, what you can translate it to.
2. [index.md](index.md) — a map of the folder.
3. [outputs/case-study.html](outputs/case-study.html) — the published landing page for the project, suitable for sharing with a colleague who is not going to clone the folder.
4. The source paper: [inputs/grant_behrends_basl.pdf](inputs/grant_behrends_basl.pdf) or its markdown digest [inputs/grant_behrends_basl.md](inputs/grant_behrends_basl.md).

## The skills (live in `operations/skills/`)

- **`/teaching-case`** — generate a student-facing case + instructor notes, engineered to surface a specific move in the framework. See [operations/skills/teaching-case/SKILL.md](operations/skills/teaching-case/SKILL.md).
- **`/discussion-plan`** — Socratic sequence around a case, anticipating student positions and routing toward the move in the paper that answers them. See [operations/skills/discussion-plan/SKILL.md](operations/skills/discussion-plan/SKILL.md).
- **`/objection-audit`** — steelman a student argument, then diagnose against the framework with section citations. See [operations/skills/objection-audit/SKILL.md](operations/skills/objection-audit/SKILL.md).
- **`/quiz`** — short-answer comprehension check on the core argument, with student version + answer key. See [operations/skills/quiz/SKILL.md](operations/skills/quiz/SKILL.md).

## Conventions

- **Skills live in `operations/skills/<skill-name>/`** — project-scoped, so they travel.
- **`inputs/` is the read-only source paper.** Don't modify it. Generated artifacts — cases, student arguments, plans, audits, the landing page — go in `outputs/`.
- **Case and argument IDs are stable.** C1–C4 (cases) and S1–S3 (student arguments) must be preserved consistently across every skill output.
- **No emojis** in any file.
- **Markdown link syntax** for file references.
- **Cite by section** (e.g. §5.2). Page numbers only when verified against the PDF.

## Alignment with the paper (the hard constraints)

These bind everything Claude does in this project:

- **Claude is never the decision-maker about a person.** See the self-referential point above. Frame Claude as augmenting the instructor and generating material.
- **Don't collapse transparency into due consideration.** The paper's central move is that due consideration is *broader* than, and not reducible to, transparency.
- **The Explainability Thesis is not absolute.** The authors say "often," "prima facie," "potentially overridable," "context-sensitive." Never present it as "never use black boxes." Don't oversell.
- **Interpretable models are safer, not a panacea** (§6). They are *less* prone to the failures, not immune.
- **Keep the three Problems distinct** (Definition, Double Standard, Grounding) and tie claims to a section or page when you can. Defensible beats vibes.
- **Black-box ≠ "any AI."** The paper's target is high-flexibility, high-dimensional, low-rule-transparency systems (§4) — not all automation.
