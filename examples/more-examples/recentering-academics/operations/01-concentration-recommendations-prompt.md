# Prompt: Generate Concentration-Level Recentering Recommendations

Use this prompt to turn one concentration's Fields-of-Concentration profile into a set
of curricular recommendations aligned with the Bok Center's Recentering Academics
initiative. Output is a single Markdown file in `outputs/`.

---

## How to share inputs

Point Claude at four things — the three evidence layers and the target profile:

1. **The Bok framework** in `inputs/bok-advice/` — the normative basis (each page is
   available as `.md` and `.html`):
   - `recentering-academics` — the overview that frames the two Recentering pillars.
   - `course-policies` — attendance, devices, generative-AI policy.
   - `designing-assignments` — rigorous, AI-resilient, cumulative assessment.
   - `facilitating-class-sessions` — engaged, attendance-dependent sessions.
2. **The Harvard context** in `inputs/harvard-context/` — why this matters now:
   - `harvard-grade-report.md` — Dean Claybaugh's October 2025 report: grade
     compression (A's rose from 24% of grades in 2005 to 60.2% in 2025), the failure of
     grading to perform its motivation/information/distinction functions, and the
     concrete steps it asks faculty to take (review grade distributions, weigh effort
     vs. mastery, articulate grading standards, calibrate across sections, consider
     seated exams).
   - `proposal-grading-policies.md` — the February 2026 Subcommittee on Grading proposal
     (20%+4 cap on A grades; average-percentile-rank internal metric; the FAS rubric's
     definition of A as "extraordinary distinction").
3. **The research evidence** in `inputs/research/` — what actually works. Read
   `overview.md` first (it synthesizes the four papers): criterion- vs norm-referenced
   grading (Sadler 2005), analytic topic-specific rubrics with exemplars and rater
   training (Jonsson & Svingby 2007), the Wellesley mean cap (Butcher et al. 2014), and
   the Cornell median-posting experiment that backfired (Bar et al. 2009).
4. **One concentration profile** in `inputs/fields-of-concentration/primary/` (or
   `secondary/`), e.g. `linguistics.md`. Each profile contains the discipline's
   self-description, learning objectives, course/tutorial requirements, tracks, thesis
   rules, and enrollment statistics.

Read the three evidence layers in full before reading the concentration, so the
framework, the stakes, and the validated practices are all in view. Then read the
concentration profile in full.

---

## Prompt

```
I'm advising the [CONCENTRATION] department on aligning its curriculum with the Bok
Center's Recentering Academics initiative. The Bok framework is in inputs/bok-advice/,
Harvard's institutional case is in inputs/harvard-context/, and the external research
evidence on grading is in inputs/research/. The concentration's profile is at
inputs/fields-of-concentration/primary/[slug].md.

First, read the three evidence layers (Bok advice, Harvard context, research) and the
concentration profile in full. Do not write recommendations yet.

Then produce a single Markdown file in outputs/ named
[slug]-concentration-recommendations.md with these sections:

1. Header — concentration name, the source profile path, the date, and a one-paragraph
   summary of what is and isn't at stake for THIS discipline. Cover both pressures: where
   generative AI genuinely threatens the field's core skills (and where the field is
   already resilient), and where the field is exposed to grade compression — does its
   assessment structure currently distinguish satisfactory, good, and excellent work?

2. What this concentration already does well — an honest read of the requirements that
   already center academics: tutorials, methods sequences, in-person argumentation,
   thesis work, oral exams, lab/fieldwork. Name the specific requirement each time. Note
   where the field's assessments already produce gradeable differences across the full
   range (the research's point that analysis/synthesis/transfer tasks spread performance
   out, while completion-style work compresses it).

3. Recommendations, organized under the two Recentering pillars:
   - Meaningful and engaged classroom experience — tie each recommendation to a specific
     course type or requirement in the profile (e.g. small-group tutorials, intro
     lecture courses, method courses) and to the relevant Bok guidance on class
     sessions and course policies.
   - Rigorous assessment and feedback — address both halves of the pillar: (a)
     AI-resilient assignment design and cumulative assessment, and (b) grading the full
     range to counter compression. For (b), draw on the research evidence base, not
     generic advice: criterion-referenced standards over norm-referenced curves (Sadler
     2005); analytic, topic-specific rubrics paired with annotated A/B/C exemplars
     (Jonsson & Svingby 2007); rater calibration across the concentration's tutorials and
     multi-section courses; and assessments designed to elicit a real range. Connect this
     to Harvard's own ask (articulate grading standards, weigh effort vs. mastery,
     calibrate across sections) and to the FAS rubric reserving A for "extraordinary
     distinction." Address a discipline-calibrated generative-AI policy here as well. Tie
     each recommendation to a specific requirement and to the Bok guidance on designing
     assignments.
   For every recommendation, state: the specific feature of the concentration it
   targets, the principle it implements (Bok, Harvard report, or research finding), and
   what the change concretely looks like.

4. A discipline-specific generative-AI stance — given what this field actually does
   (e.g. for Linguistics: formal analysis, data work, language data, computational
   methods), where should AI be embraced as a tool, where should it be fenced off to
   protect the skill being assessed, and where is it simply irrelevant? Be specific and
   honest; "ban it everywhere" and "embrace it everywhere" are both wrong answers.

5. Three things to do now — the highest-leverage, lowest-friction changes the
   department could make for the next term. At least one should address grading the full
   range (e.g. a shared rubric with exemplars, a calibration practice, or articulated
   grade standards), since that is where both Harvard's report and the research locate the
   highest leverage.

Keep every recommendation anchored to a concrete feature of this concentration. If a
recommendation would read identically for any field, sharpen it or cut it. Cite the
source you're drawing on (Bok guidance, the Harvard reports, or a specific study), and
respect the research's cautions — e.g. department mean caps work but are costly (Butcher
et al. 2014), and publishing grade data to students can backfire (Bar et al. 2009). Be
honest about what's already strong.
```

---

## Output

Write to `outputs/<slug>-concentration-recommendations.md` (one per concentration,
overwriting any existing copy).
