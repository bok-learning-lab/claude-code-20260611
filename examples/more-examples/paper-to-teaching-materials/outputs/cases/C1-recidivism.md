# C1 — Pretrial recidivism scorer

**Type:** automated-decision-system dossier
**Engineered to surface:** the limits of the argument from accuracy (§5.1); ignoring
readily available evidence (§5.2).

## The system

A county court is considering **RiskPredict**, a proprietary tool that estimates a
defendant's risk of failing to appear or reoffending before trial, used to inform
pretrial detention decisions. It is a gradient-boosted ensemble trained on ~140
features drawn from arrest records, prior charges, age, employment history, and ZIP
code. The vendor reports strong AUC on a held-out sample and will not disclose the
model's internals (trade secret). Judges receive a single risk tier: low / medium /
high.

## The institution's argument for adopting it

"Detaining the genuinely dangerous and releasing the safe is what fairness requires.
RiskPredict predicts risk more accurately than our judges do unaided. Using the most
accurate available method is how we take defendants' claims seriously."

## What the dossier deliberately includes

- The tool is **more accurate on the vendor's test set** than the court's current
  practice. (Sets up the argument from accuracy.)
- In one flagged case, a defendant with an extensive record scores **high**, but a
  neurologist has testified that the past behavior was caused by a **brain tumor since
  successfully removed** — evidence RiskPredict was never designed to ingest. (The
  §5.2 "ignoring available evidence" hook.)
- Validation was on historical county data; **no field re-validation** after
  deployment. (Overfitting / field-degradation hook, §5.1.)

## Notes for the instructor (not student-facing)

The seductive move here is S1's: accuracy settles it. The paper grants that relative
accuracy bears on due consideration (§5.1) but then shows two ways it is not
sufficient — the system can degrade in the field, and it can be **insensitive to
readily available evidence a human would not overlook** (§5.2, the brain-tumor case is
modeled directly on the paper's). Good discussion keeps the substantive vs. procedural
distinction in view: even a fair procedure on average can wrong *this* defendant.
