# C3 — Interpretable alternative to C1

**Type:** automated-decision-system dossier (the stress-test / decoy)
**Engineered to surface:** the §6 "third option"; the §4 definition of "black box."
**Expected audit result:** largely **passes** on black-box grounds.

## The system

The same county from [C1](C1-recidivism.md) evaluates **ClearScore**, an alternative
pretrial tool. It is a **sparse, monotonic scoring model** built on six inputs (age at
current arrest, number of prior failures-to-appear, current charge category, and
three others). Each point's contribution is published; a defendant and their counsel
can see exactly which factors produced the score and by how much. Field accuracy is
**modestly lower** than RiskPredict's reported test accuracy.

## The institution's argument for adopting it

"It is a little less accurate on paper, but anyone can see why it scored someone the
way it did, and we can inspect whether it is using anything it shouldn't."

## What the dossier deliberately includes

- **Low flexibility, low dimensionality, full rule transparency** — the three
  features that, per §4, make something *not* a black box in the paper's sense.
- A real, **modest accuracy gap** vs. C1. (Tests whether the audit overweights
  accuracy and wrongly faults C3.)
- Global *and* local rules are inspectable, so morally inadmissible inference rules
  could be detected if present. (§5.3, §6.)

## Notes for the instructor (not student-facing)

C3 is the decoy. A naive audit that equates "algorithm" with "black box," or that
treats any accuracy loss as a failure of due consideration, will wrongly condemn it.
The paper's §6 point is exactly that the interpretable model is the **safer third
option**: less prone to overfitting, to ignoring evidence, and to exploiting
inadmissible features, *and* checkable. But note the hedge — interpretable is *less*
prone, not immune (a transparent model can still implement a bad rule; the difference
is you can see it). A correct audit returns C3 mostly clean and says why, while still
flagging that ClearScore is a decision aid, not a decision-maker (agential
consideration still applies to the human using it, §7.3).
