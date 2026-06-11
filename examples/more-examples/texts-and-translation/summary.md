# Texts and translation with Claude Code

A scaffolded demonstration of how LLM-assisted close work might look in disciplines whose primary sources are not in English — classics, comparative literature, religious studies, modern languages, and the area-studies fields that maintain serious philological traditions of their own. The project ships two demo corpora (the *Odyssey* in fourteen translations, and the first *ānana* of Jagannātha Paṇḍitarāja's seventeenth-century Sanskrit *Rasagaṅgādhara*) and four Claude Code skills (`/split-into-books`, `/show-passage`, `/identify-figures-greek`, `/identify-figures-sanskrit`) that operate on them.

The companion essays that previously sat in `overview/` — a longer summary, a piece on the philological tradition, and a piece on what LLMs do and do not change about it — are folded into the relevant sections below. The plan and the deep-research output are now in `operations/` and `outputs/` respectively.

---

## What it is

Four Claude Code skills, scoped to this project's `.claude/skills/` directory.

- **`/split-into-books`** splits the Odyssey translation files into 24 per-book files for fast passage queries. Run it once before using `/show-passage`.
- **`/show-passage`** displays a passage (by primary coordinate, e.g. *Odyssey* 1.1–10) with the original Homeric Greek at the top and chosen translations below, quoted verbatim. Shows what each translator chose to preserve or let go.
- **`/identify-figures-sanskrit`** identifies candidate *alaṃkāras* in a passage from the *Rasagaṅgādhara*, with the figure named, the relevant text quoted, and a brief account of what the figure is doing rhetorically. Frames every identification as a candidate to be verified against Jagannātha's own definitions.
- **`/identify-figures-greek`** identifies rhetorical figures in a passage of Homeric Greek, with verbatim quotation and citation by line.

Two corpora, each set up as a standalone demo target:

- **Homer's *Odyssey* in fourteen translations** at `inputs/the-odyssey/`, spanning Greek, Latin, Spanish, French, Swedish, and eight English versions (Bryant, Butcher/Lang, Butler, Cotterill, Cowper, Merry/Riddell, Monro, Pope). The Homeric original is in TEI/XML from PerseusDL (Murray edition); Polylas's nineteenth-century Modern Greek is also included. The corpus is set up for *comparative translation* — line up five or fourteen versions of the proem, of the Cyclops episode, of the Sirens, and look at where translators diverge.
- **Jagannātha Paṇḍitarāja's *Rasagaṅgādhara*** at `inputs/early-modern-sanskrit/`, in Devanāgarī from the GRETIL archive at Göttingen, edited by Timothy C. Cahill from four printed editions. Only Ānana 1 is currently downloaded. The *Rasagaṅgādhara* is one of the last great works of classical Sanskrit poetics; it is itself an *alaṃkāra-śāstra* — a treatise on figures of speech — which makes it an unusually apt target for a skill that identifies figures, since the same text that defines the categories can also audit the skill's calls.

The skill outputs (figure identifications, passage views) land in `outputs/the-odyssey/`; the deep-research report on the project's place in the tradition lives at `outputs/research-result.md`.

### The tradition this sits in

Close textual work in the modern humanities has its origins in the early-nineteenth-century philological revolution. Karl Lachmann's edition of the Greek New Testament (1831) is the conventional milestone; what Lachmann did was assemble the procedures — comparing surviving manuscript witnesses, identifying shared errors, reconstructing a hypothetical archetype via the *stemma codicum* — into a method robust enough to be taught. The critical edition with its *apparatus criticus* of variants became the form in which philological labor reached the rest of the field.

Alongside the philological tradition runs the parallel history of translation theory. Friedrich Schleiermacher's 1813 address "On the Different Methods of Translating" articulated a distinction that has organized the field ever since: the translator must either move the reader toward the author (preserving the foreignness of the source) or move the author toward the reader (naturalizing into the target idiom). Walter Benjamin's "The Task of the Translator" (1923) pushed the question into more difficult territory — translation as the *afterlife* of the original. Lawrence Venuti's *The Translator's Invisibility* (1995, rev. 2008) refigured the distinction in political terms: domestication conceals the labor of the translator and the foreignness of the source; foreignization makes both visible. A side-by-side comparison of fourteen *Odyssey* translations is not a neutral data display; it is a comparison of fourteen positions on the Schleiermacher–Venuti axis.

The Sanskrit philological tradition has its own deep history, predating European philology by more than two millennia. Pāṇini's *Aṣṭādhyāyī* (c. 5th–4th century BCE) and the commentarial tradition (*bhāṣya*, *vārttika*, *ṭīkā*) constitute a model of textual scholarship as elaborate as anything in Europe; Nāgeśa Bhaṭṭa's commentary on Pāṇini and Mathurā Nāth Śāstrī's *Gurumarmaprakāśikā* on the *Rasagaṅgādhara* are not external aids but integral to how the texts are read. European Indology in the nineteenth century built on this indigenous tradition often without acknowledging the debt and frequently subordinating the indigenous commentaries to its own racial and theological priors. Sheldon Pollock's "Future Philology? The Fate of a Soft Science in a Hard World" (2009) is one sustained recent effort to reckon with that inheritance.

### What LLMs change about it

The labor of close textual work is heterogeneous. There is work that is labor-intensive but conceptually well-defined (collation, glossary building, line-by-line alignment of translations, indexing). There is interpretively irreducible work (deciding what a contested passage means, weighing competing readings, identifying which *alaṃkāra* is operating in a verse where two or three could be defended). And there is a slippery middle — tasks that look mechanical but contain interpretive moves (transliterating an ambiguous Sanskrit *sandhi*; rendering an epithet that has no English equivalent; choosing a tense for a Greek aorist given the temporal nuance of the surrounding narrative).

The LLM helps with what is *labor-bound*. Comparative translation at scale (assemble what fourteen translators did with *Odyssey* 1.1–10, with attribution; the scholar reads and decides what the choices mean). Glossary construction (a first pass that the scholar edits). Candidate identification of figures of speech (especially apt for the *Rasagaṅgādhara*, where the same text defines the categories and supplies illustrative verses — internal consistency check). Indexing across long corpora. Non-Latin script handling (frontier LLMs handle Devanāgarī, polytonic Greek, classical Chinese, Arabic, Hebrew, Tibetan, Pali natively in their tokenizers, though competence varies dramatically by training-data substrate). The LLM does not help — and should not be allowed to be seen as helping — with what is *judgment-bound*.

Failure modes the discipline should keep in view: the politics of training data (LLMs trained on existing scholarly editions reproduce and may launder the editorial and ideological choices in those sources — colonial-era European editions of South Asian texts are deeply embedded in model priors); hallucinated citations (a *Nature* analysis in early 2026 estimated tens of thousands of 2025 publications may contain LLM-invented citations); the "good enough translation" risk (LLM translations are often good enough for casual reading and not nearly good enough for scholarly use — a student may not be in position to see what's wrong); the colonial inheritance (automating philological work without engaging its history risks reproducing the history at scale); access and corpus politics (whose digital editions get used, who pays the API costs).

The framing the project adopts is the conservative one: the LLM is a *first-pass collaborator*, never a final arbiter. The scholar reads the primary source; the LLM surfaces candidates the scholar evaluates. Source text is quoted verbatim, never paraphrased. Citations use primary coordinates (*Odyssey* 1.1, *Rasagaṅgādhara* Ān. 1 §17), not file paths. The model's confidence is treated as a hypothesis to be checked, not as expertise.

---

## How we built it

This project followed the same shape as `interview-coding` but with a smaller initial scope. Two corpora went into place first — the *Odyssey* translations and the Homeric Greek source from PerseusDL, and Ānana 1 of the *Rasagaṅgādhara* from GRETIL — because no skill could be tested without them. The corpus assembly is itself a piece of scholarly labor: deciding which translations to include (a span across centuries, languages, and translator stances), which edition of the Greek to use, which Sanskrit substrate (and the implicit editorial inheritance that comes with it).

The skills were built in a single round, not in parallel, because the two corpora suggested a natural sequence: **`/split-into-books`** first (a pure utility — the Odyssey translation files needed to be split into per-book files for fast passage queries before any skill could read them efficiently); **`/show-passage`** next (the comparative-translation skill the Odyssey corpus was assembled for, demonstrable on the proem, the Cyclops episode, the Sirens); **`/identify-figures-sanskrit`** and **`/identify-figures-greek`** as a pair (the figure-identification skills that exploit the *Rasagaṅgādhara*'s status as an *alaṃkāra-śāstra* — the same text that defines the categories audits the skill's calls). The build sequence is documented in the deep-research output at `outputs/research-result.md`.

Hard constraints applied throughout: quote source text verbatim (character-for-character including diacritics and stage marks); cite by edition and primary coordinate, not by file line number; preserve script (do not silently transliterate or romanize); frame outputs as candidates, not verdicts ("Candidate alaṃkāra: anuprāsa (alliteration of velar stops at L34, L36); verify against Jagannātha's definition at §X"); be honest about the model's limits — Sanskrit philology and Homeric Greek prosody are technical fields, and the LLM produces first-pass surfacing for a trained scholar to evaluate, not finished philological judgments.

The workshop session for this project is reflective rather than demonstrative. Attendees see the two corpora laid out, walk through what `/show-passage` does against *Odyssey* 1.1–10 (the proem — every translator's most labored opening, where Wilson's "complicated man" sits next to Lattimore's "man of many ways" and Pope's "man for wisdom's various arts renown'd"), and what `/identify-figures-sanskrit` does against an illustrative verse from the *Rasagaṅgādhara* whose *alaṃkāra* Jagannātha himself names. The session then steps back to the broader question — what *should* the discipline ask of an LLM, and what should it keep firmly with the trained scholar?

### Things this approach taught us

Faculty who do close philological work daily are, with reason, the most skeptical audience for AI tools in the university. The project is built so they can find their own answer rather than be sold one. The framing matters: a skill output that says "this passage exhibits anuprāsa" makes a verdict the scholar will (correctly) push back on; a skill output that says "candidate alaṃkāra: anuprāsa, verify against Jagannātha §X" invites the scholar to do what they were going to do anyway. The shift from verdict to candidate is the smallest thing that distinguishes a useful tool from a presumptuous one.

The two-corpus design is doing real work. The Odyssey corpus is set up for *comparative* work — many translations, one source. The Sanskrit corpus is set up for *internal-consistency* work — the same text defines and applies the categories. These are different validation regimes, and a discipline that wants to keep LLM-assisted work honest needs both kinds.

---

## What you can translate this to

The pattern in this project is portable to any domain where the substantive work is:

1. **A primary source the practitioner is responsible for reading** — and would be embarrassed to be seen substituting the LLM for. The LLM does the labor; the practitioner does the judgment.
2. **A taxonomy with public definitions** the LLM can apply as candidates. *Alaṃkāras* in the *Rasagaṅgādhara*. Schemes and tropes in classical rhetoric. Diagnostic codes in the DSM. Legal precedents in case law. Plant families in field botany.
3. **A verbatim discipline.** Source text quoted character-for-character. Citations to primary coordinates. No silent transliteration, no silent paraphrase.
4. **An honest naming of the limits.** Where the model's training data is thin, where the model's confidence has been built out of suspect priors, where the model produces fluent prose that hides the wrongness.

Domains where the same shape applies almost without modification:

- **Comparative editions of any canonical text** — Shakespeare folios and quartos, the Hebrew Bible across Masoretic / Septuagint / Vulgate / modern translations, primary statutes across jurisdictions. Same `/show-passage` skill, different corpora.
- **Glossary construction for any specialized vocabulary** — medical terminology, legal terms of art, the technical vocabulary of any sub-field. First-pass surfacing for the expert to curate.
- **Candidate-identification skills for taxonomies** with public definitions. The *Rasagaṅgādhara* pattern generalizes wherever a corpus defines and exemplifies its own categories: rhetorical handbooks, taxonomic keys, legal commentaries, codified diagnostic criteria.
- **Indexing and cross-referencing across long corpora** — letter collections, archival series, multi-volume works. Skills like `/split-into-books` are pure utilities that make later work tractable.
- **Translation workshops** that line up multiple versions of the same passage for student analysis — the comparative-translation skill is exactly what a translation seminar already does by hand, scaled.

The pattern in all of these is the same: a primary source the practitioner reads, a taxonomy the LLM applies, a verbatim discipline that keeps the practitioner in the position of judgment, and an honest naming of where the model's outputs cannot be trusted.

---

## Alignment constraints (the hard ones)

These apply throughout this project and survive translation to other domains:

- **First-pass collaborator, not final arbiter.** Skill outputs surface candidates for the scholar to evaluate. Verdicts are the scholar's.
- **Quote verbatim.** Paraphrase is the scholar's job, not the LLM's. Source text in any output must match the source file character-for-character, including diacritics.
- **Cite by primary coordinate**, not by file path. *Odyssey* 1.1, *Rasagaṅgādhara* Ān. 1 §17. The file path is secondary.
- **Preserve script.** Do not silently transliterate or romanize. If a transliteration is needed, produce a separate file and label it.
- **Frame as candidates.** "This passage exhibits X" → "Candidate X: ...; verify against Y."
- **Name the limits.** The model produces first-pass surfacing for a trained scholar; it does not produce finished philological judgments.
- **No emojis.** Markdown link syntax for file references.
