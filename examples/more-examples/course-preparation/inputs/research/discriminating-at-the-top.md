# Discriminating at the top: the measurement properties that spread grades

How can you have confidence *in advance* — before grades are in — that an assessment will
spread student performance across the full range and distinguish the very best work, rather
than piling up at A? This is [open question Q2](../director-advice/grading-for-the-full-range.md)
in the director's advice. The answer is that spread is a *measurement property* you design
in, not a hope you hold afterward. This file makes the relevant psychometrics accessible to
faculty who are not measurement specialists; it complements [overview.md](overview.md),
which covers the criterion-referencing and rubric practices that decide *what* a grade
means, where this file covers *whether the instrument can register differences at all*.

The honest headline: classical test theory, ceiling-effect methodology, and item-response
theory all point to the same design lever — a test spreads scores only if it contains items
of varied, non-trivial difficulty with high discrimination, including hard items located at
the high end. For rank-ordering open-ended work and surfacing the strongest, comparative
judgement is a defensible method, but adopt it for its structure, not for its advertised
reliability numbers, which are contested.

A note on method, as in the companion files: claims marked *confirmed* survived three-vote
adversarial verification; the psychometrics below are foundational measurement theory and
verified verbatim against primary sources. The comparative-judgement reliability debate is
where the genuine uncertainty lies and is flagged as such.

---

## 1. Item difficulty and discrimination — why too-easy work compresses the top (confirmed, high)

In classical test theory, a single right/wrong item's contribution to spread is its
variance, p(1 − p), where p is the proportion of students who get it right. This is
maximized at p = 0.50 and falls to zero at the extremes:

- An item **everyone** passes (p = 1.00) or **nobody** passes (p = 0.00) makes *no*
  distinctions between students — it adds nothing to the spread.
- An item near p = 0.50 makes the most pairwise distinctions (among 100 students, an even
  split distinguishes 50 × 50 = 2,500 pairs; an 80/20 split only 1,600).

So a test built largely from items most students get right is, by construction, a test that
compresses scores near the top. (Strictly, "contributes nothing" is exact only at p = 1.00;
a p = 0.95 item contributes little but not literally zero. And many *redundant*
mid-difficulty items do not multiply differentiation — they must probe different things.)

**Discrimination** is the companion property: item discrimination (D) measures how well an
item separates strong from weak overall performers — computed by the extreme-group method
as the pass-rate of the top 27% minus that of the bottom 27% (Cureton 1957). High D means
the item tracks overall mastery; a *negative* D flags an item that weaker students do
better on than stronger ones (often a flawed or mis-keyed question), which should be revised
or cut. A test that spreads grades defensibly is one whose items are individually
discriminating, not just collectively numerous.

*Source: Kline, Classical Test Theory (SAGE), Ch. 5; corroborated by Crocker & Algina and
assess.com.*

## 2. Ceiling effects — a measurement failure, not just a fairness problem (confirmed, high)

A **ceiling effect** is what happens when an instrument lacks the range to register the top
of the population it is measuring: high performers pile up at the maximum and their real
differences vanish. Three confirmed points:

- **It has an operational definition.** Floor and ceiling effects are a recognized
  measurement property to evaluate when validating any instrument, with a common flag of
  **more than 15% of respondents scoring the maximum** (Terwee et al. 2007). That heuristic
  transfers directly to a course exam: if well over 15% of students hit full marks on a
  component, that component has a ceiling problem.
- **It is exactly the high-ability-meets-easy-test failure.** Ceiling effects "arise due to
  insufficient range of measurement … when used with gifted populations" (McBee 2010). A
  high-achieving cohort meeting an undemanding assessment is the textbook case — directly
  the Harvard situation.
- **It biases the numbers, not just the optics.** When ceiling (or floor) effects are
  present, standard analyses — and by extension simple grade means and aggregates — produce
  *biased* estimates, with bias detectable from as little as ~10% censored data (McBee 2010;
  Wang et al. 2020). A compressed top is a measurement-bias problem: the grade no longer
  estimates what it claims to.

**Practical detection rule for faculty:** before trusting a component to differentiate,
check what fraction of students hit its maximum. Past ~15% at the ceiling, the component is
not measuring the top of your class — it is hiding it.

## 3. Test information functions — put precision where you need it, including the top (confirmed, high)

Item-response theory turns "spread" into an explicit design lever. Each item carries
**information** that peaks near its own difficulty level and rises with its discrimination;
summed across items, this yields a **test information function** showing where on the
ability scale the test measures precisely and where it is noisy. The design consequences:

- A test whose items cluster near the *pass mark* is precise about who passes and nearly
  blind everywhere else — including at the top.
- To measure accurately across the full range *and* at the high end, **spread item
  difficulties across the range** (a flatter, higher information curve) and deliberately
  include **high-discrimination items located at high difficulty**. That is the
  psychometric content of the director's [Principle 2](../director-advice/grading-for-the-full-range.md):
  to distinguish mastery at the top, you must place measurement precision at the top.

*Source: Introduction to IRT for outcome measurement (PMC4520411); standard Lord (1980) /
Embretson & Reise (2000) result.*

## 4. Comparative judgement — a defensible way to rank open-ended work, with an honest caveat

For open-ended work (essays, projects, proofs, design) where rubric scoring tends to
saturate at the top, **comparative judgement** (CJ) offers a different mechanism: instead of
scoring each piece against a scale, judges make repeated *pairwise* "which is better"
decisions, and a model (Thurstone scaling) converts the comparisons into a single quality
scale.

- **The structural advantage (confirmed, high).** With comparative scaling, the precision of
  a script's quality estimate depends on the number of *comparisons made after the exam*,
  not on test length. Precision can therefore be increased adaptively — sending extra
  targeted comparisons for scripts whose rank is still uncertain — which conventional exams,
  whose precision is fixed by the number of questions, cannot do (Pollitt, "Let's stop
  marking exams"; Cambridge Assessment / Bramley). This is the real reason CJ suits
  rank-ordering open work and surfacing the strongest pieces.
- **The honest caveat (medium confidence).** The headline claim that *adaptive* CJ (ACJ)
  achieves reliability higher than conventional marking is **contested**. The adaptive
  pair-selection itself inflates the Scale Separation Reliability statistic, so reported ACJ
  reliabilities likely overstate how well it actually separates work; in at least one
  real-data study a non-adaptive comparison scale was no less *valid* against external
  criteria despite a lower reliability coefficient. (Many of the specific claims in this
  debate failed to clear independent re-verification in this pass — they are
  under-verified, not refuted.) **The defensible position:** adopt CJ for the structural
  benefit of comparison and its fit to top-end discrimination, not because of advertised
  reliability coefficients, and weigh the real examiner-workload cost of many pairwise
  comparisons.

---

## What this means for assessment and grading design

- **Audit components for ceiling effects.** For each graded component, ask what fraction of
  students reach the maximum. Past ~15%, the component cannot differentiate the top — it is
  a completion check wearing the clothes of an assessment.
- **Reserve marks for genuinely hard, discriminating items.** A portion of every major
  assessment should sit at high difficulty and high discrimination, so the instrument has
  precision where extraordinary distinction would show up. Spreading item difficulty is how
  you buy spread in the grades.
- **Match the method to the work.** For convergent work, vary item difficulty and check
  discrimination. For open-ended work that saturates rubrics, consider comparative judgement
  to rank-order quality — chosen for structure, not reliability marketing.
- **Treat a crowded top as a measurement red flag.** Compression is not only a fairness or
  rigor concern; it means the grade is a biased estimate of achievement. That reframing
  gives an instructor an advance, technical check rather than an after-the-fact lament.

## Cautions and gaps

- **Transfer from other measurement fields.** Several primary sources come from
  health-status measurement and gifted education, not course grading. The psychometric
  *principles* transfer cleanly, but this synthesis applies general measurement theory to
  course design rather than citing grading-specific trials.
- **Gap — real-course distributional evidence.** The mechanism (hard, discriminating items
  spread grades) is well established; direct before/after evidence that reserving marks for
  hard items changes *actual course grade distributions* was not surfaced and is worth
  finding.
- **Gap — practical cut-points.** Beyond Terwee's >15%-at-maximum flag, target ranges for
  item difficulty and discrimination that faculty could use as a pre-administration check
  were not pinned down here.
- **Open link to the rubric question.** Whether a rubric's *top band* can be written to
  behave like a high-difficulty, high-discrimination item — admitting genuine distinction
  rather than saturating — connects directly to
  [rubrics-differentiation.md](rubrics-differentiation.md).

## Sources

- **Kline, T. J. B.** *Classical Test Theory* (Ch. 5), SAGE.
  <https://us.sagepub.com/sites/default/files/upm-binaries/4869_Kline_Chapter_5_Classical_Test_Theory.pdf>
- **Cureton, E. E. (1957).** "The upper and lower twenty-seven per cent rule." *Psychometrika.*
- **Terwee, C. B., et al. (2007).** "Quality criteria were proposed for measurement
  properties of health status questionnaires." *Journal of Clinical Epidemiology*, 60(1),
  34–42. <https://www.sciencedirect.com/science/article/abs/pii/S0895435606001740>
- **McBee, M. (2010).** "Modeling outcomes with floor or ceiling effects." *Gifted Child
  Quarterly*, 54(4), 314–320. <https://journals.sagepub.com/doi/abs/10.1177/0016986210379095>
- **Wang, L., et al. (2020).** Bias under floor/ceiling effects. *Behavior Research Methods.*
  <https://doi.org/10.3758/s13428-020-01407-2>
- **Introduction to Item Response Theory for outcome measurement (PMC4520411).**
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC4520411/>
- **Pollitt, A.** "Let's stop marking exams" (and the Cambridge Assessment / Bramley reports
  on ACJ reliability). <https://www.academia.edu/10028321/Lets_stop_marking_exams> ·
  <https://www.cambridgeassessment.org.uk/Images/232694-investigating-the-reliability-of-adaptive-comparative-judgment.pdf>
- **Bramley, T., & Vitello, S. (2017/2018); Verhavert et al. (2018).** On ACJ reliability
  and the SSR-inflation debate. <https://www.tandfonline.com/doi/full/10.1080/0969594X.2017.1418734>
