# C2 — Résumé screening model

**Type:** automated-decision-system dossier
**Engineered to surface:** morally inadmissible evidence (§5.3); redundant encoding
and proxies.

## The system

A large employer deploys **ScreenFit**, a deep model that ranks incoming résumés for
"likely strong performer." It was trained on a decade of the firm's own hiring and
performance data. Explicit demographic fields were stripped from the training data.
The model returns a 0–100 fit score; recruiters interview from the top of the list
down.

## The institution's argument for adopting it

"We removed race and gender from the data, so the model can't discriminate. It just
learns what past strong performers looked like."

## What the dossier deliberately includes

- The training data reflects a workforce shaped by **past structural bias** in the
  field. (Spurious-correlation / compounding-injustice hook.)
- Audit finds the model rewards features like **membership in certain clubs**,
  **specific ZIP codes**, and penalizes résumés containing the token **"women's"** (as
  in "women's chess club"). (Modeled on the Amazon tool in §5.3.)
- The vendor confirms demographic fields were dropped but cannot explain which
  features drive a given score. (Rule-transparency / redundant-encoding hook.)

## Notes for the instructor (not student-facing)

This is the §5.3 case. The key teaching point is **redundant encoding**: removing the
protected feature does not remove it, because close proxies remain and a
high-dimensional model will exploit them. The paper's claim is not that the model
"believes" anything about gender, but that decision-makers have a duty to **set aside
morally inadmissible evidence**, and relying on a system that may be implementing a
prohibited inference rule — with no practicable way to check — puts them in breach.
Watch for the proxy question: when does relying on a proxy inherit the wrong of relying
on the feature? The paper flags this as partly open.
