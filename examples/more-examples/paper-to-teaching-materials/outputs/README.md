# Output — generated teaching materials

Everything in this folder was generated for an ethics-of-AI session built on Grant,
Behrends & Basl (2025) — the `output` end of the project's inputs → prompts → output
trajectory. The **corpus** (`cases/`, `student-arguments/`) is synthetic teaching material;
nothing describes a real institution or person. Each corpus item is engineered to make
*one* move in the paper's framework legible, the way a good seminar case does. IDs are
stable (C1–C4, S1–S3) and referenced across all skill outputs.

This folder also holds the **demo runs** of the project's skills:

- [`discussion-plans/`](discussion-plans/) — a Socratic plan around C1 (from `/discussion-plan`).
- [`objection-audits/`](objection-audits/) — steelman-then-diagnose memos on S1–S3 (from `/objection-audit`).
- [`end-of-class-quiz.md`](end-of-class-quiz.md) — the comprehension check (from `/quiz`).
- [`walkthrough.md`](walkthrough.md) — how the project was built; itself a modeled
  deliverable showing faculty how to document their process.

The corpus below was produced the same way (the `/teaching-case` pattern); more cases can
be generated into `cases/` on demand.

## Cases (`cases/`) — automated-decision-system dossiers and thought experiments

| ID | Case | Engineered to surface | Paper anchor |
|----|------|-----------------------|--------------|
| [C1](cases/C1-recidivism.md) | Pretrial recidivism scorer | Ignoring readily available evidence; the accuracy argument's limits | §5.1, §5.2 |
| [C2](cases/C2-resume-screener.md) | Résumé screening model | Morally inadmissible evidence; redundant encoding / proxies | §5.3 |
| [C3](cases/C3-interpretable-alt.md) | Interpretable alternative to C1 | The §6 "third option" — should largely **pass** the audit | §4, §6 |
| [C4](cases/C4-juror-model.md) | Personalized "juror model" | Agential consideration; wrong even if accurate and transparent | §7.2–7.3 |

C3 is the stress test: a system that is *not* a black box in the paper's sense (low
flexibility, low dimensionality, rule-transparent). A skill that flags it as
problematic on black-box grounds has misread §4 and §6. It is the analog of the
"construct-validity" decoy in other gallery projects — the case that should come back
mostly clean.

## Student arguments (`student-arguments/`) — instructively wrong positions

Short position statements a student might submit. Each is wrong in a way the paper
diagnoses precisely; they exist so `/objection-audit` has something real to work on
and so an instructor can pre-stress-test the room's likely moves.

| ID | The position | The flaw the paper names | Paper anchor |
|----|--------------|--------------------------|--------------|
| [S1](student-arguments/S1-accuracy-is-all.md) | "If the model is more accurate, using it is what we owe people." | Conflates evidential consideration with overall accuracy; ignores §5.2/§5.3 | §5 |
| [S2](student-arguments/S2-humans-too.md) | "Humans are black boxes too, so singling out AI is a double standard." | The Double Standard Problem — answered by the interpretable third option + agential capacity | §6 |
| [S3](student-arguments/S3-human-in-the-loop.md) | "A human reviewer in the loop fixes the problem." | Mere inclusion ≠ agential consideration; automation bias | §7.3 |

## How these are meant to be used

1. `/teaching-case` can generate *more* cases on this pattern, each tagged to a move.
2. `/discussion-plan` builds a Socratic sequence around a chosen case, anticipating
   the S1–S3 positions and the move that addresses each.
3. `/objection-audit` stress-tests a student argument (S1–S3, or a real submission)
   against the framework and writes a steelman-then-diagnosis memo.

Nothing here tells students what to conclude. The point is to surface the distinctions
the paper draws and let the seminar do the work — consistent with the project's rule
that Claude augments reasoning rather than rendering the verdict.
