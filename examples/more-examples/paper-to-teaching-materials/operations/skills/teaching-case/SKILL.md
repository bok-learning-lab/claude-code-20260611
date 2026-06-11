---
name: teaching-case
description: >-
  Generate a classroom case for teaching Grant, Behrends & Basl, "What we owe to
  decision-subjects" — a student-facing automated-decision-system dossier or thought
  experiment engineered to surface one move in the framework, plus separate instructor
  notes tying it to a section of the paper. Use when the user runs /teaching-case, asks
  for a case, scenario, dossier, or thought experiment to teach a specific move (accuracy,
  ignoring available evidence, morally inadmissible evidence, decision rules, agential
  consideration), or asks for a "decoy" case that should pass an audit.
---

# /teaching-case — generate a classroom case

Produce a case that makes one move in the paper's framework legible to students, the way
a good seminar case does — concrete, arguable, and engineered so the move surfaces in
discussion rather than being announced.

## Inputs

- **Move to surface** (required): one of
  - `accuracy` (§5.1 — field degradation / overfitting),
  - `ignoring-evidence` (§5.2 — insensitivity to readily available evidence),
  - `inadmissible-evidence` (§5.3 — redundant encoding, proxies),
  - `decision-rules` (§7.1 — prohibited decision rules / Kantian injunction),
  - `agential-consideration` (§7.2–7.3 — needs a responsible moral agent).
- **Domain** (optional): bail, hiring, lending, admissions, medicine, etc. Default: vary it.
- **Type** (optional): `dossier` (a deployed system) or `thought-experiment`. Default:
  dossier for §5 moves, thought experiment for agential-consideration.
- **Decoy** (optional flag): produce a case that *should pass* an audit — an interpretable,
  rule-transparent system with at most a modest accuracy cost (cf. C3). Useful for teaching
  §4 and §6 and for stress-testing the other skills.

## Output

One markdown file with two clearly separated parts:

1. **Student-facing case** — a short dossier or scenario (150–300 words): the system or
   situation, the institution's argument for it, and one or two discussion questions. State
   *no* conclusion; the case should be genuinely arguable.
2. **Instructor notes (not student-facing)** — the move surfaced and its section; the trap
   to expect; what to keep distinct (especially transparency vs. due consideration); and,
   for a decoy, why it should come back clean.

Match the structure of the corpus cases in `../../../output/cases/`. Write generated cases
to the skill's `examples/` (for demos) or to `output/cases/` (to extend the corpus), never
to `inputs/`.

## Hard constraints (inherited — see ../../../prompts/CLAUDE.md)

- **No foregone conclusions in the student-facing text.** A case that telegraphs "AI is
  bad" can't do its job. The institution's argument must be the *strongest* honest version.
- **Keep transparency and due consideration distinct.** Many of the best cases turn on a
  failure that persists *even under full disclosure*; make that available, not muddied.
- **Black box ≠ any algorithm** (§4). If the move is a §5/§7 black-box failure, the system
  must actually be high-flexibility / high-dimensional / low-rule-transparency.
- **Cite by section; never invent a page number.**
- **No emojis. Stable IDs** if you add to the corpus.

## Worked examples

- [examples/case-medical-bail-5.2.md](examples/case-medical-bail-5.2.md) — a fresh
  `ignoring-evidence` case in a medical-bail setting (cf. C1, different domain).
- [examples/case-decoy-admissions.md](examples/case-decoy-admissions.md) — a `--decoy`
  case (interpretable admissions screen) that an audit should return clean.
