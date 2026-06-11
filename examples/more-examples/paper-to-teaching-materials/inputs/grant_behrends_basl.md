# What we owe to decision-subjects — digest

> **What this file is.** A detailed, section-by-section digest of the article, made to
> save future sessions from re-reading the 31-page PDF. It is a *faithful summary with
> verbatim quotes where marked*, **not** a full transcription — the source was read as
> page images. For exact wording or page-precise citation, check the PDF:
> [grant_behrends_basl.pdf](grant_behrends_basl.pdf). Quoted passages are in
> blockquotes; everything else is paraphrase.

## Citation

Grant, D. G., Behrends, J., & Basl, J. (2023/2025). "What we owe to decision-subjects:
beyond transparency and explanation in automated decision-making." *Philosophical
Studies* 182, 55–85. https://doi.org/10.1007/s11098-023-02013-6 — Open access, CC BY
4.0. Accepted 7 July 2023; published online 17 Aug 2023; in the 2025 volume.

**Authors/affiliations:** David Gray Grant (University of Florida; Jain Family
Institute, NY) · Jeff Behrends (Harvard) · John Basl (Northeastern; partly funded by
NSF Award 1928654). Corresponding author: John Basl.

## Abstract (verbatim)

> The ongoing explosion of interest in artificial intelligence is fueled in part by
> recently developed techniques in machine learning. ... But as is now widely
> discussed, the way that those systems arrive at their outputs is often opaque, even
> to the experts who design and deploy them. Is it morally problematic to make use of
> opaque automated methods when making high-stakes decisions, like whether to issue a
> loan to an applicant, or whether to approve a parole request? Many scholars answer in
> the affirmative. However, there is no widely accepted explanation for why transparent
> systems are morally preferable to opaque systems. We argue that the use of automated
> decision-making systems sometimes violates duties of consideration that are owed by
> decision-makers to decision-subjects, duties that are both epistemic and practical in
> character. Violations of that kind generate a weighty consideration against the use
> of opaque decision systems. In the course of defending our approach, we show that it
> is able to address three major challenges sometimes leveled against attempts to defend
> the moral import of transparency in automated decision-making.

**Keywords:** Artificial intelligence · Machine learning · Transparency ·
Interpretability · Opacity · Decision making · Explanation · Right to explanation.

## The thesis they defend (verbatim)

> **Explainability Thesis.** In many contexts, decision-makers are morally obligated to
> avoid basing their decisions about how to treat decision-subjects on the outputs of
> black box AI systems.

Note the hedges, which recur throughout and matter for any faithful use: "in many
contexts," and later "*pro tanto*," "prima facie," "potentially overridable,"
"often ... not always." The thesis is **not** "never use black-box AI."

## Roadmap (the paper's own §1 plan)

- §2 criticizes transparency-centric defenses.
- §3 offers the alternative: due consideration to decision-subjects.
- §4 addresses the **Definition Problem** (what "black box" means).
- §5 the **epistemic** duties (duties of *evidential* consideration).
- §6 the **Double Standard Problem**.
- §7 the **practical** duties (duties of *practical* consideration).
- §8 conclusion.

Three named challenges the approach must meet: the **Grounding Problem** (what duties
ground a duty to avoid black boxes), the **Definition Problem** (what a "black box"
is), and the **Double Standard Problem** (why hold machines to a higher bar than
humans).

---

## §1 Introduction

Institutions increasingly use AI for high-stakes calls (employment, lending, arrest/
imprisonment, life-saving medical interventions), driven by powerful ML like deep
learning. Such systems are often "black boxes" — opaque even to designers (Breiman
2001; Burrell 2016; Doshi-Velez & Kim 2017) — vs. more traditional "interpretable"
systems experts can explain. The Explainability Thesis has broad appeal and is
enshrined in many AI codes of ethics; Rudin (2019) goes further (don't use black boxes
for high-stakes decisions at all where explainable alternatives exist).

**The challenge for the thesis:** it can't be a *sui generis* duty; it must be grounded
in other duties. One strategy grounds it in **duties of transparency** (disclose how
the decision process works — Selbst & Barocas 2018; Vredenburgh 2022). The paper argues
that strategy only works in special cases — the **Grounding Problem**. Their
alternative: ground it in the duty to show **due consideration** to decision-subjects.

## §2 The transparency defense

**Transparency Defense:** using black boxes is problematic because decision-makers have
*duties of transparency* — to disclose details about how decisions are made to
decision-subjects (or advocates / watchdogs). To succeed it must show (1) an applicable
duty of transparency exists, and (2) it requires disclosing info unavailable if a black
box were used.

Both conditions hold in *some* cases (e.g. US law requires lenders to give adverse-
action explanations; black-box DNNs would make that hard, so lenders use interpretable
models — Selbst & Barocas 2018). But **outside special cases the defense falters**:
many high-stakes decisions aren't governed by duties of transparency (employers
generally needn't explain hiring to applicants — though see Vredenburgh 2022), and
there are cases where duties of transparency apply yet a black box is consistent with
satisfying them (London 2019: doctors often can't explain how diagnostic methods work
but still meet their transparency duties, having no obligation to disclose that sort of
info).

**The deeper point:** transparency duties aren't the only duties owed. There are
constraints on *how decisions are made in the first place*. The judge who decides bail
by flipping a coin wrongs the defendant **even if she fully discloses** how she
decided — she fails to show *due consideration*. This motivates §3.

## §3 Due consideration

> [A] decision-maker D shows due consideration to a decision-subject S just in case D
> adopts decision procedures that are appropriately responsive to S's moral claims on
> the decision process — claims that S has that place restrictions on how D ought to
> make decisions about how to treat S.

Due consideration decomposes into **duties of consideration**. Two cross-cutting
distinctions:

- **Substantive vs. procedural.** *Substantive* claims: to be treated per the features
  the subject *in fact* has (an innocent defendant's claim to be found innocent). These
  are often not directly perceptible and must be inferred, so there's risk of error;
  procedural fairness requires managing that risk with safeguards (e.g. competent legal
  representation — Rawls 1999 "imperfect procedural justice"; Di Bello & O'Neil 2020
  "due concern"). *Procedural* claims constrain permissible procedures but aren't
  grounded in the subject's substantive claims (e.g. the bar on using illegal-wiretap
  evidence even against a guilty defendant).
- **Evidential vs. practical** (cross-cuts the above). Treating others requires two
  tasks: (a) **fact-finding** — gathering/evaluating evidence to form beliefs about
  subjects (epistemic/zetetic); and (b) **decision-making** — deciding how to treat
  them given those beliefs (practical reasoning). **Duties of evidential
  consideration** constrain fact-finding; **duties of practical consideration**
  constrain decision-making. (Terminology thanks to Stephanie Sheintul; the duty to
  show due consideration unifies part of what Enoch 2018 calls "evidence law for
  morality.")

## §4 The definition problem

"Black box" is usually defined against "explainable"/"interpretable," but those terms
lack agreed definitions (Lipton 2018; Krishnan 2019 finds it "worrying" how much
importance is attached to interpretation without a grasp of what it means for
algorithms). The authors define "black box" via **three concepts**:

1. **Flexibility** — capable of modeling a much broader range of input/output
   relationships than e.g. linear models (James et al. 2021).
2. **Dimensionality** — computes over very many input features (Selbst & Barocas 2018).
   High flexibility + dimensionality drive both power and resistance to explanation.
3. **Rule transparency** — a species of Creel's (2020) "functional transparency."
   Defined via two kinds of higher-level rules:
   - **Inference rules** — rules used to answer *descriptive* questions about subjects.
   - **Decision rules** — rules used to decide *how to treat* subjects given their
     properties. Together these are the system's **"decision logic."**
   - A system is **rule transparent** to an agent to the extent the agent is in a
     position to know the inference and decision rules it implements.
   - **Global** rules give unified explanations across a broad range of situations;
     **local** rules explain behavior on particular occasions. (Maps to CS's global vs.
     local explainability — Doshi-Velez & Kim 2017; Speith 2022.) Knowing only global
     rules is insufficient (the "Aloysius" example: a local rule that almost never
     fires but is morally objectionable).

**Working definition:** "black box system" = AI with (1) high flexibility, (2) high
dimensionality, (3) limited rule transparency — roughly the systems AI researchers mean
(DNNs, random forests), contrasted with "interpretable" systems (less flexible/
dimensional, more rule transparent — Rudin 2019; Bell et al. 2022). Two clarifications:
the boundary isn't sharp (judgment required for any particular system; the claim is
decision-makers *often*, not *always*, must avoid black boxes); and whether a system is
a black box can change as XAI efforts increase rule transparency (they concede a
sufficiently rule-transparent system would neutralize their concerns, but existing XAI
tools have important limitations — Zerilli 2022; Creel 2020; Fleischer 2022).

Two kinds of interference to come: (1) some duties enjoin decision-makers to implement
inference/decision rules satisfying constraints, and black boxes interfere with
ensuring those constraints are met; (2) some duties require decision-making be done by
full-blown moral agents.

## §5 Duties of evidential consideration

Decision-makers often have duties of evidential consideration **not to base
fact-finding on black-box outputs.** Surprising at first because black boxes are often
*more accurate* (e.g. McKinney et al. 2020, breast-cancer screening from mammograms
outperforming radiologists; large literature on actuarial > clinical judgment). Call
the pro-black-box argument **the argument from accuracy**. Three rebuttals follow.

### §5.1 Accuracy

Worked example: **pretrial detention on estimated recidivism risk.** Detention is
*substantively* fair when the defendant poses sufficient danger; *procedurally* fair
when the evidence supports that and courts can evaluate it. Sensitivity to substantive
claims is partly a matter of predictive accuracy, so accuracy bears on due
consideration.

**The TEALEAVES / COMPAS thought experiment (Sacco & Vanzetti):** suppose the only ways
to estimate recidivism risk are COMPAS (known highly accurate) and TEALEAVES (random
scores, no information). Courts know this but use TEALEAVES anyway. Sacco and Vanzetti
are both wrongly accused and pose no danger. Sacco gets a high TEALEAVES score and is
detained; Vanzetti a low score and is released. Sacco has a **noncomparative** claim
(detained though insufficiently dangerous) *and* a **comparative** claim (treated worse
than Vanzetti for no reason) — both violated (Feinberg 1974 on comparative vs.
noncomparative). So relative accuracy *does* bear on due consideration.

**But** the argument from accuracy faces two objections:

1. **Field degradation.** Black boxes aren't *always* more accurate in deployment than
   in the lab, for three reasons they share: they need more input data (→ transcription/
   data-quality errors — Rudin 2019); their flexibility makes them prone to
   **overfitting** (the **"Jared" résumé-screener**: a tool "learned" that applicants
   named Jared were stronger because the training data happened to contain a star
   employee named Jared — Shellenbarger 2019); and their lack of rule transparency
   makes overfitting harder to detect (Caruana 2015; Rudin 2019; Creel 2020). If an
   interpretable model is available, there's a duty-of-evidential-consideration reason
   to prefer it even at some accuracy cost in testing. (Bell et al. 2022; Rudin 2019
   suggest the accuracy–explainability tradeoff may be insignificant in many contexts.)
2. The substantive/procedural distinction: even the most accurate method may violate
   weighty **procedural** claims. Two such procedural constraints follow (§5.2, §5.3).

> Footnote on differential accuracy / fairness: the authors focus on overall accuracy
> but note subgroup accuracy also matters; statistical fairness criteria (e.g.
> equalized odds — Hardt et al. 2016; Grant 2023) and the "accuracy–fairness tradeoff"
> (Corbett-Davies & Goel 2018; Rodolfa et al. 2021) are flagged but not resolved here.

### §5.2 Ignoring available evidence

Predictive algorithms can be **completely insensitive to readily available evidence a
human decision-maker would not overlook.** Basing fact-finding on a black box compounds
this (you can't tell whether/how particular evidence is influencing the output).

**The brain-tumor example:** a judge deciding bail for a defendant with an extensive
record; COMPAS naturally returns high risk. But the defendant's **neurologist
testifies** that the past criminal behavior was caused by a **brain tumor since
successfully removed**, so he now poses low risk. COMPAS wasn't designed to take such
evidence into account → mislabels him high risk. Ignoring readily available evidence
that would benefit a particular subject is **procedurally unfair** to that subject.
Black boxes share this limitation and (being non-rule-transparent) make it hard to tell
which evidence is/isn't taken into account.

### §5.3 Morally inadmissible evidence

A piece of evidence E is **morally inadmissible** for an agent A making decision D when
A is obligated to "set aside" E — to reason about what the correct decision would be
*as if she did not have E*. Paradigm: **statistical discrimination** — an employer who
won't hire from a racial group because she believes (perhaps even correctly, given
structural discrimination) they're less qualified on average. Even if the statistical
relationship holds, the applicant's **race is morally inadmissible** for hiring (Eidelson
2015; Lippert-Rasmussen 2011; Bolinger 2021; Enoch & Spectre 2021 on individualized vs.
"naked" statistical evidence; Thomson 1986).

**Why black boxes raise the risk:** (1) training data encodes inadmissible features
(race/gender), often **"redundantly encoded"** — inferable from other features even
after explicit removal (Dwork et al. 2012); (2) those features are often correlated with
the target; (3) black boxes excel at finding/exploiting such correlations (flexibility +
dimensionality); (4) lack of rule transparency makes it hard to tell if inadmissible
evidence is being used. So: reason to suspect the system bases predictions on
inadmissible features, but no practicable way to confirm → a *pro tanto* duty not to base
fact-finding on it.

**The Amazon example:** Amazon scrapped a résumé tool after it learned to **downgrade
résumés containing "women's"** (e.g. "women's chess club") — Dastin 2018. Close
**proxies** for an inadmissible feature are often themselves inadmissible (shopping at
certain stores, "cultural affinity" groups, geography). When relying on a proxy inherits
the wrong of relying on the feature is **partly an open question** (Hu forthcoming).

Two anticipated objections answered: (a) the prohibition is against using epistemic
methods that *implement prohibited inference rules*, whether implemented by humans or
algorithms (the "former employee's program that adds points if the employee is a man"
example); (b) redundant encoding + distributed representation in DNNs (Buckner 2018,
2019) means a system can directly implement inference rules on a prohibited feature even
if it's not explicitly in the data.

## §6 The double standard problem

Objection: humans are also "black boxes" — psychology (Gazzaniga split-brain work;
Schwitzgebel 2019) casts doubt on reliable introspective access to our decision
processes, and humans may not report motivations truthfully. Defenders of the thesis
don't want to say relying on human expert judgment is impermissible — so aren't they
committed to an **objectionable double standard** (Zerilli et al. 2019)?

Indeed the §5 arguments seem to generalize: humans commit base-rate fallacies
(Bramwell et al. 2006) and take social group membership into account (Bertrand &
Mullainathan 2004; "algorithmic bias" often inherited from human judgments —
Corbett-Davies & Goel 2018).

**Two responses:**

1. **The argument generalizes but doesn't *over*generalize.** Where there's reason to
   suspect human fact-finders implement prohibited inference rules, there are
   corresponding reasons not to rely on them — granted, possibly even of equal strength.
   But that doesn't cancel the thesis, because there's a **third option: interpretable
   models.** Decades of research show even simple linear models often outperform human
   experts and roughly match black boxes (Bell et al. 2022; Rudin 2019). Interpretable
   models are *less* likely to implement prohibited inference rules, less prone to
   overfitting/data-quality issues, and when they do err it's easier to detect. So
   using an interpretable system is often the best way to show evidential consideration.
2. **Different standards may be appropriate** for human vs. machine systems given
   morally significant differences (capacities, relationships), and humans can evaluate
   what evidence they're responding to. Whether the reasons against black boxes and
   against humans are *equally* strong is left an open question.

## §7 Duties of practical consideration

These constrain **decision-making** (not fact-finding). Example: an employer who
promised a position to a particular employee has a duty of practical consideration to
give that promise appropriate weight. A black box can implement **decision rules** too.
There's a growing field — **machine ethics** — that builds machines simulating moral
reasoning (Anderson & Anderson 2010, who used *interpretable* ML to infer bioethicists'
decision rules for caregiving robots; black-box methods could be used instead, yielding
non-rule-transparent systems). Two ways reliance fails:

### §7.1 Decision rules and duties of practical consideration

Just as inference rules can be morally prohibited, **decision rules** can be prohibited
in virtue of subjects' claims on how decision-making should work. It's often
impracticable to anticipate in advance what moral claims particular subjects have and
how they interact in context, and decision-makers can't inspect a black box's decision
rules → often a duty of practical consideration **not to base decision-making on a black
box.** Illustrated via a **Kantian injunction against treating people as mere things**
(Strawsonian "participant stance" — Rini 2020; Schroeder 2019; Strawson 1962): we treat
subjects as mere things when decisions about them rely too heavily on features
disconnected from their agency. Since black boxes aren't rule transparent, we can't rule
out that their decision rules violate the injunction → *pro tanto* reason not to rely.

**Caveat (delegation):** sometimes decision-makers bound by a constraint may permissibly
*delegate* to proxies not so bound (Brighouse 1995: the state giving the NSF discretion
to fund basic science on non-public reasons, because the discretion yields legitimating
public goods). But this doesn't undermine the argument: even where delegation is
permissible, other constraints on the proxy's decision rules may remain; and different
decision-makers/systems may be subject to different constraints given differing
capacities and relationships — which helps dissolve the double-standard worry.

### §7.2 Beyond decision rules: duties of agential consideration

**Duties of agential consideration** place constraints on the *nature* of the system
making decisions: where they apply, decision-making **must be carried out by full-blown
moral agents** exercising moral reasoning, deliberating in good faith.

**The Juror Substitution thought experiment:** computer scientists build perfectly
accurate **customized juror models** that replicate how a given juror would vote by
implementing the *same* inference and decision rules. Under the Juror Substitution
Policy, selected jurors go home and their models adjudicate. The models even disclose
their "deliberations" (satisfying any duty of transparency). **Intuition: this is
morally problematic** — yet the wrong can't be explained by the content of the rules
(same as the humans'), nor by transparency (fully disclosed), nor by accuracy (perfect).

**The diagnosis:** some decisions (e.g. criminal punishment) ought to be made by
full-blown moral agents exercising their distinctive moral capacities with appropriate
care. When a human decides by genuinely reasoning through the subject's claims, she
**takes responsibility** for the decision and thereby shows the subject respect as a
fellow member of the moral and political community — legitimating, e.g., the change in
criminal status. A juror model replaces members of the defendant's moral/political
community with systems that can't do this → a morally objectionable lack of respect for
the defendant's civic status. Connected to **responsibility gaps** in autonomous-weapons
debates (Sparrow 2007 on LAWs; Matthias 2004; Asaro 2020; Roff 2013): the wrong isn't
that *no one* is responsible for accidental deaths, but that **responsibility for
deciding to kill was inappropriately delegated** to something incapable of agential
consideration. Agential consideration is owed across many contexts (medical decisions
for an unconscious partner; political representatives; financial advisers) and what it
requires is mediated by context (law, fiduciary duties, relationships) — Sandler & Basl
2021; Palmer 2010 on differing moral status.

### §7.3 Agential consideration and the explainability thesis

Outsourcing decision-making wholesale to a black box is incompatible with showing
agential consideration **because black box systems cannot show it — only full-blown
moral agents can, and automated systems aren't full-blown moral agents.** So using a
black box is at least *prima facie* impermissible where agential consideration is owed
(e.g. jury trials).

**Important:** these reasons tell against ceding decision-making authority to **any**
automated system, not just black boxes — where agential consideration is owed, the
black-box/interpretable distinction is largely irrelevant.

**Human-in-the-loop (HITL):** mere inclusion of a human is **not sufficient.** If the
human defers to the recommendation without further thought, "there is no meaningful
difference between a decision structure that includes the human and one that does not."
At the other extreme, a judge who carefully examines the defendant's circumstances
isn't rendered incapable of agential consideration just by consulting a recommendation.
The distinction is **consulting vs. deferring**; the **automation-bias** literature
(Citron 2008) suggests the risk of inappropriate deference is significant and
*heightened* with black boxes → special reason to resist HITL structures incorporating
black boxes.

Differential transparency standards for jurors vs. juror-models are **not** an
objectionable double standard: it might be reasonable to let human jurors deliberate in
secret (to prevent misconduct / manipulation) while requiring transparency of juror
models — the justification for secrecy doesn't transfer to the models.

## §8 Conclusion

Our duties to decision-subjects — to implement permissible inference and decision rules,
and to provide agential consideration — often give significant reasons to reject
black-box-based decision systems. Sometimes because we can't verify such systems abide
by these duties; sometimes because they can't possibly do so; sometimes because
integrating them undermines our ability to do so. These duties also explain *which*
forms of transparency matter in which contexts, and why it's often appropriate to hold
human decision-makers and automated systems to **different standards** (not an
objectionable double standard). The import of design decisions about automated systems
is **highly context-sensitive**; sweeping impermissibility claims aren't supported.
Closes by flagging the value of further work on the ethics of delegating decisions to
others not bound by the same constraints.

---

## Key named cases / examples (quick index for prompting)

| Example | Section | Illustrates |
|---------|---------|-------------|
| Coin-flipping bail judge | §2 | Due consideration ≠ transparency |
| Lender adverse-action explanations | §2 | Where the transparency defense *does* work |
| London's doctors | §2 | Transparency duties met without explaining the method |
| Sacco & Vanzetti / COMPAS vs. TEALEAVES | §5.1 | Comparative + noncomparative claims; accuracy bears on due consideration |
| The "Jared" résumé screener | §5.1 | Overfitting / field degradation |
| Brain-tumor neurologist + COMPAS | §5.2 | Ignoring readily available evidence |
| Statistical discrimination in hiring | §5.3 | Morally inadmissible evidence |
| Amazon "women's" résumé tool | §5.3 | Redundant encoding; proxies |
| Juror Substitution Policy | §7.2 | Agential consideration (the central thought experiment) |
| Lethal autonomous weapons / Sparrow | §7.2 | Responsibility gaps; inappropriate delegation |
| NSF funding discretion (Brighouse) | §7.1 | Permissible delegation to an unconstrained proxy |

## The three "problems" (quick index)

- **Grounding Problem** — what duties ground a duty to avoid black boxes? *Answer:*
  duties of (evidential + practical) consideration, not duties of transparency.
- **Definition Problem** (§4) — what is a "black box"? *Answer:* high flexibility + high
  dimensionality + limited rule transparency.
- **Double Standard Problem** (§6) — why hold machines to a higher bar than humans?
  *Answer:* the argument partly generalizes to humans, but interpretable models are the
  safer third option, and humans have agential capacities machines lack.
