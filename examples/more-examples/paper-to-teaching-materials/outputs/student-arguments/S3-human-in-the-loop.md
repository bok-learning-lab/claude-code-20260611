# S3 — "A human in the loop fixes the problem."

**Submitted position (student-facing):**

> Most of these worries dissolve once a human signs off. Keep the black-box system as a
> recommender, but require a judge or manager to make the final call. With a human in
> the loop, the decision is still made by a person, so agential consideration is
> satisfied and we get the accuracy of the model too.

**The flaw the paper names (instructor note):** §7.3. **Mere inclusion of a human is
not sufficient.** If the human defers to the system's recommendation without genuine
deliberation, there is "no meaningful difference between a decision structure that
includes the human and one that does not" — the juror-model wrong of
[C4](../cases/C4-juror-model.md) reappears. The empirical literature on **automation
bias** suggests this risk is significant, and is *heightened* when the system is a
black box. The paper does not say HITL always fails — a judge who genuinely examines
the defendant's circumstances can show agential consideration while consulting a
recommendation. The distinction is between **consulting** and **deferring**. A good
audit of S3 draws that line and asks what institutional design would keep the human a
real agent rather than a rubber stamp.
