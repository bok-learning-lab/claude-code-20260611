# Generated case — medical bail / ignoring available evidence

*Produced by `/teaching-case --move ignoring-evidence --domain medicine`. Validates the
skill against §5.2 in a domain distinct from C1.*

---

## Student-facing case — "DischargePredict"

A hospital uses **DischargePredict** to flag which admitted patients can be safely sent
home and which need continued inpatient care. The model scores readmission risk from
hundreds of variables in the electronic health record and the vendor reports high accuracy
on a held-out sample; clinicians see a single risk band. A patient with a long record of
prior admissions is scored **high risk** and slated to stay. But the patient's primary
physician notes that nearly all of those prior admissions stemmed from a medication
interaction that has since been identified and corrected — a fact recorded only in a free-
text note the model does not read. The hospital's position: "The model outperforms our
clinicians on average. Overriding it for anecdotes reintroduces exactly the bias we
adopted it to remove."

**Questions for discussion.** Is the hospital treating this patient as its duties require?
If the model is genuinely more accurate on average, what — if anything — is wrong with
deferring to it here? Would publishing the model's reasoning fix the problem?

## Instructor notes (not student-facing)

- **Move surfaced:** ignoring readily available evidence (§5.2). The corrected drug
  interaction is evidence a clinician would weigh and the system structurally cannot — a
  *procedural* failure of evidential consideration to this patient, independent of the
  model's average accuracy.
- **Trap to expect:** the hospital's "anecdotes vs. data" framing (this is essentially the
  S1 move in clinical dress). Press it: a procedure can be fair on average and still wrong
  *this* person by being insensitive to evidence that bears on their case (substantive vs.
  procedural).
- **Keep distinct:** the third question is a transparency probe. Publishing the model's
  reasoning would *not* fix it — the evidence never entered the model at all. Use this to
  separate transparency from due consideration.
- **Note:** this is the same structure as C1's brain-tumor example, relocated to medicine
  to show the move is domain-general.
