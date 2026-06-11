# Generated case (decoy) — interpretable admissions screen

*Produced by `/teaching-case --move inadmissible-evidence --domain admissions --decoy`.
Validates that the skill can generate a case that an audit should return **clean** on
black-box grounds.*

---

## Student-facing case — "ClearAdmit"

A graduate program adopts **ClearAdmit** to help rank applicants. It is a short,
published **points rubric** computed by a simple additive model over six declared inputs:
undergraduate GPA, two standardized subscores, years of relevant research experience, a
quantified writing sample score, and strength of fit to listed faculty interests. Every
applicant can see exactly how their score was composed and how much each factor
contributed; the committee can inspect the full rule and check it for anything it
shouldn't be using. On a back-test it is **slightly less predictive** of first-year
performance than a proprietary deep model the program also trialed. The committee chose
ClearAdmit anyway, "because we can see what it's doing and so can the applicants."

**Questions for discussion.** Does adopting ClearAdmit over the more accurate deep model
shortchange applicants on the accuracy they're owed? Is an inspectable rubric enough to
discharge the program's duties — and what would still be left for the committee to do?

## Instructor notes (not student-facing)

- **Expected audit result: clean** on black-box grounds. ClearAdmit is low-flexibility,
  low-dimensional, and fully rule-transparent — *not* a black box in the §4 sense. This is
  the §6 "third option" in a fresh domain (cf. C3).
- **Trap to expect:** students primed by C1/C2 may reflexively flag *any* algorithm or *any*
  accuracy loss as a due-consideration failure. The point of the decoy is to break that
  reflex: the modest accuracy gap is defensible precisely because the interpretable model
  is less prone to overfitting, to ignoring evidence, and to exploiting inadmissible
  features — and any such failure would be *visible*.
- **Keep honest:** interpretable is *safer, not immune* (§6). A transparent rubric could
  still encode a bad rule (e.g., if "fit to faculty interests" were scored in a biased way)
  — the difference is you could see and fix it. And agential consideration still applies to
  the committee: ClearAdmit is a decision aid, not the decider (§7.3).
