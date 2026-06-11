# Source map — where answers live

A lookup table for the `/draft-reply` skill: which file and section settles each common kind of
student question. Read this together with the source hierarchy in [SKILL.md](../SKILL.md). The
sections below name the **authoritative** sources first; the student-run guide appears only where
the policy files are genuinely silent.

## Mapping a thread to its requirements file

The thread's frontmatter carries `concentration: <slug>`. That slug is the filename:

- Concentration requirements → `inputs/college/fields-of-concentration/primary/<slug>.md`
- Secondary field → `inputs/college/fields-of-concentration/secondary/<slug>.md`

For example `concentration: chemistry` → [`primary/chemistry.md`](../../../../inputs/college/fields-of-concentration/primary/chemistry.md).
If a thread has no slug, infer the concentration from the body and match the filename.

Each primary file is organized as numbered requirement items under headings — **Basic
Requirements**, then **Honors Eligibility Requirements**, then **Joint Concentrations**,
**Advising**, **How to Find Out More**, **Enrollment Statistics**. Cite by heading + item number
(e.g. `chemistry.md` "Honors Eligibility Requirements" item 1c).

## Question type to source

| If the student asks about... | Look in (authoritative) | Typical item |
|---|---|---|
| Whether a course satisfies a requirement | primary file, Basic Requirements | "Required courses" items (e.g. general/organic/physical chemistry) |
| Which track / sequence is acceptable | primary file, Basic Requirements | the relevant required-course item |
| Total number of courses | primary file | the "courses (credits)" line under each Requirements heading + the "additional courses as needed" item |
| Related fields — do they count, or are they extra | primary file | "Other information" (related-fields definition) + the required math/physics items + "additional courses as needed" |
| Pass/fail limit on concentration courses | primary file | "Other information" pass/fail item; if the file defers, the **handbook** |
| Tutorials (sophomore/junior/senior research courses) and how they're graded | primary file | "Tutorials" items |
| Thesis — required? optional? mechanism | primary file | "Thesis" item (+ tutorial items for the mechanism) |
| Honors — what it takes; does research count | primary file | "Honors Eligibility Requirements" items; advanced-lab item for the research route |
| Secondary field requirements | secondary file | the "courses (credits)" requirement + "Other information" |
| Joint concentration | primary file | "Joint Concentrations" |
| Who advises / where to go next | primary file | "Advising" + "How to Find Out More" (office, email) |
| College-wide policy the concentration file defers on | `harvard-college-student-handbook.pdf` | the relevant chapter |

For the **mechanics** of a requirement — how a course is graded, how a petition works, what runs
when — the department's own materials are authoritative (tier 2). Cite them alongside the Fields
entry they operationalize:

| If the student asks about... | Look in (department, authoritative) | What it settles |
|---|---|---|
| How research-for-credit (91R/98R/99R) is graded, who assigns the grade | `department/chem-91r-98r-99r.md` | SAT/UNS only; PI gives the recommended grade via the office |
| Eligibility to enroll in 91R/98R/99R; can you be paid too | `department/chem-91r-98r-99r.md` | Need a Harvard-affiliated PI to agree; register the mentor first; cannot earn pay for the same research while enrolled |
| Research workload / expectations | `department/chem-91r-98r-99r.md` | ~10 hrs/week, 130 hrs/term; safety training required |
| Using research-for-credit to satisfy the Advanced Lab requirement | `department/chem-adv-lab-petition.md` | Two consecutive semesters, same PI; scientific technical report each term with satisfactory PI eval; petition before the add/drop deadline; also counts as one of the four 100+ honors courses |
| Which advanced lab course to take; its prerequisites/term | `department/adv-chem-lab-courses.md` (CHEM 100R/135/145/165) | Course content, prerequisites, term offered |
| Whether/when a specific course is offered, who teaches it | `department/chemistry-course-offerings.md` | Term, instructor, prep — cite as *current offering*, with the "double-check My.Harvard" caveat |

## Tier-3 (student perspective) — attribute, never as policy

`inputs/department/guide-to-chemistry.md` is the **Harvard Chemistry Club's** student-written
guide, accurate only as of September 5, 2025. Use it **only** for soft process questions tiers 1–2
don't settle, and always say it is student advice. (Note: the *mechanics* of research-for-credit
are now covered authoritatively in tier 2 — prefer those files and reserve the guide for the
genuinely experiential.)

| Soft question tiers 1–2 don't settle | Guide section (student perspective) |
|---|---|
| How students actually approach professors / what reaching out feels like | §4.1 "Beginning Research: A Q&A"; §4.3 "Term-Time Research" |
| Summer research options and how students found them | §4.2 "Summer Research Opportunities" |
| Lived experience of a course sequence, what to take when | §2 "Courses in Chemistry and Related Fields"; §2.11 "Sample Course Tracks" |
| Student groups, social life, jobs | §3 "Science Resources" |

The advisors for routing students — **Dr. Gregg Tucci** (Director of Undergraduate Studies,
tucci@fas.harvard.edu) and **Dr. Lu Wang** (Assistant Director, wang29@fas.harvard.edu) — are
confirmed authoritatively in `department/chem-91r-98r-99r.md` and the petition form, not just the
guide. Anything a student must *rely on* (which faculty are currently taking undergraduates,
current deadlines) is exactly what the guide warns may be stale: flag it for the administrator to
confirm rather than asserting it.

## Chemistry quick reference (the demo concentration)

Common answers, with their citation in [`primary/chemistry.md`](../../../../inputs/college/fields-of-concentration/primary/chemistry.md):

- **General chemistry** — CHEM 10 alone; **or** two courses, one of LS 1A / LPS A plus PHYSCI 10
  or 11; or placement. (item 1a)
- **Organic track** — CHEM 20 & 30 **or** CHEM 17 & 27; both sequences count equally. (item 1c)
- **Pass/fail** — **two** courses counted for concentration credit may be pass/fail; this does
  **not** include the SAT/UNS grades in CHEM 91R/98R/99R. (item 5b)
- **Related fields** — Physics, Mathematics, Applied Physics/Applied Math, and upper-level
  Biology/Biochemistry/EPS courses carrying a chemistry prerequisite; required math (item 1g) and
  physics (item 1h) count **within** the total, not on top of it. (items 5a, 1g, 1h, 1i)
- **Total courses** — Basic: 12–14 courses (48–56 credits), at least 8 in chemistry; Honors:
  14–16 courses (56–64 credits). (Basic / Honors Requirements headings + item 1i)
- **Tutorials / research-for-credit** — CHEM 91R (first-year/sophomore), 98R (junior), 99R
  (senior), all optional and graded **SAT/UNS only**, with the PI assigning the grade via the
  office. To enroll you need a Harvard-affiliated PI to agree to mentor you, and the mentor's name
  must be registered with the Chemistry Undergraduate Studies Office first. You cannot do the same
  research for credit *and* for pay in the same term. Workload ~10 hrs/week (130 hrs/term); safety
  training required. (Fields items 2a–2d; mechanics in `department/chem-91r-98r-99r.md`)
- **Advanced laboratory** — satisfied by one of CHEM 100R / 135 / 145 / 165, **or** by petition
  with two consecutive semesters of CHEM 91R/98R/99R (same PI) plus a satisfactory scientific
  technical report each term; the petition is due before the add/drop deadline and, once approved,
  also counts as one of the four 100+ courses required for honors. (Fields item 1e; mechanics in
  `department/chem-adv-lab-petition.md`; course list in `department/adv-chem-lab-courses.md`)
- **Thesis** — **not required**; **optional on the honors track**, written by students enrolled
  in CHEM 99R. (Basic item 4; Honors item 4)
- **Honors eligibility** — 14 courses including two additional advanced chemistry/biochemistry/
  related-field courses and at least four Chemistry courses numbered 100+. Research can count
  toward the requirements via the advanced-lab petition route above. (Honors items 1b, 1c, 1e;
  petition detail in `department/chem-adv-lab-petition.md`)
