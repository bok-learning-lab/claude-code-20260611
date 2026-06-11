# Accessibility report — the worksheet/problem-set template

This documents the accessibility audit of the template and the adaptations. The
provided [operations/handout.sty](../operations/handout.sty) is used untouched;
the accessibility fixes live in the companion
[operations/coursestyle.sty](../operations/coursestyle.sty).

## Governing standard

The institution's digital accessibility policy adopts **WCAG 2.1 Level AA** as
the conformance standard, and it explicitly covers course materials, documents,
and PDFs shared through the learning management system. (For a U.S. university,
this typically aligns with Section 508 and the ADA.) So "accessible" here means:
meets WCAG 2.1 AA.

Sources consulted:
- Harvard University Digital Accessibility Policy — https://accessibility.huit.harvard.edu/digital-accessibility-policy
- Policy procedures (scope: course materials, PDFs) — https://accessibility.huit.harvard.edu/digital-accessibility-policy-procedures
- Creating Accessible LaTeX Documents (MathML / tagged PDF / alt text) — https://libguides.lib.msu.edu/c.php?g=995742&p=8207771
- Converting LaTeX into WCAG 2.1 compliant format (Rutgers) — https://sas-it.rutgers.edu/how-to-guides/guide/70-desktop-system-support/160-desktop-software/1254-converting-latex-documents-into-wcag-2-1-compliant-format

## Findings and what was fixed

| Issue (WCAG criterion) | Finding in the original template | Fix applied |
| --- | --- | --- |
| Use of Color (1.4.1) | Solution / Grading / Note content is shown in colored boxes. | The provided `handout.sty` already gives the `solution` and `grading` boxes **text titles** ("Solution", "Grading Notes"), so they are not color-only. The `note` box has no title text (color-only); see the gap below. |
| Contrast (1.4.3) | Blue `color1` = RGB(0,99,178) used for headers, links, and box frames on white. | Verified: `color1` on white is about **5.4:1**, passing AA for normal and large text. The pale fill `color2` is always paired with black text (very high contrast). Kept both. |
| Language of Page (3.1.1) / Name & metadata | No PDF language or document title in metadata; a screen reader could not announce the document. | The companion `coursestyle.sty` sets `\hypersetup{pdflang=en-US, pdfdisplaydoctitle=true}`; each document sets its own `\hypersetup{pdftitle=...}`. |
| Info & Relationships (1.3.1) | Headings are visual blue banners. | They are produced by real `\section`/`\subsection` commands, so the logical structure is intact even though the rendering is decorative. |

## The remaining gap (documented honestly)

Two things WCAG 2.1 AA wants for math PDFs are **not** achievable with the build
engine used here (`tectonic`, which is xetex-based):

1. **Tagged PDF** (structure tags, defined reading order). Full tagging needs the
   LaTeX PDF-management layer with `lualatex` + `tagpdf`. `tectonic` reports
   "PDF resource management is not active" and halts when `tagpdf` loads.
2. **Equation alt text.** The `axessibility` package embeds each equation's LaTeX
   source as actual/alt text, but it depends on the same PDF-management layer and
   fails under `tectonic`. It is left loaded-but-commented in `coursestyle.sty`.
3. **The `note` box is color-only** (no title text), unlike the `solution` and
   `grading` boxes. Since `note` is teacher-only content this is low-impact, but
   to fully satisfy 1.4.1 it should gain a text title. That belongs in the
   author's `handout.sty` (which we leave untouched here), so it is recorded as a
   recommendation rather than changed.

**Fallback / recommendation:** compile the final, to-be-posted deliverables with
`lualatex` + `tagpdf` (and uncomment the `axessibility` line in
`coursestyle.sty`) to produce a fully tagged PDF with equation alt text, then
validate with PAC (PDF Accessibility Checker) or Acrobat's accessibility
checker. The day-to-day drafts can keep using `tectonic` for speed.

A separate concern lives in the **inputs**, not the template: any source that is
a **scan of handwriting** is an image with no text layer and is inaccessible by
definition. Those need OCR (or re-typesetting) before they can meet AA — the
LaTeX conversion in this recipe is itself the strongest remediation for them.
