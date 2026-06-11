# Prompt — audit and adapt the template for accessibility

Use this to check the template against the governing accessibility standard and
to bake the achievable fixes into `handout.sty`.

This is an idealized prompt, not a transcript.

---

You are auditing a LaTeX worksheet template for accessibility and adapting it.

1. **Find the governing standard.** Look up the institution's digital
   accessibility policy and the standard it adopts (for a U.S. university this is
   typically WCAG 2.1 Level AA, often citing Section 508 / ADA). Note that
   course materials and PDFs are usually explicitly in scope. Record the source
   links in the report.

2. **Audit the template against that standard.** Check at least:
   - **Color as the only cue** — is any meaning carried by color alone? (e.g. a
     "solution" shown only in a colored box.) Add a text label.
   - **Contrast** — compute the contrast ratio of every text-on-fill and link
     color against its background; confirm it meets AA (4.5:1 normal text, 3:1
     large text / UI).
   - **Document metadata** — is the PDF language set, and the title in the
     metadata, so a screen reader announces the document correctly?
   - **Equations** — are equations recoverable by assistive tech (alt text /
     tagging), or are they just glyphs?
   - **Reading order / structure** — do headings use real sectioning commands so
     the document has navigable structure?

3. **Bake in the achievable fixes** in `handout.sty`:
   - Convey version/status in text, never color alone (e.g. a `Solution.` label).
   - Choose colors that pass AA contrast on the page background.
   - Set `\hypersetup{pdflang=en-US, pdfdisplaydoctitle=true}` and a
     per-document `pdftitle`.
   - Use real `\section`/`\subsection` for structure.

4. **Document the gap honestly.** Note what the build toolchain *cannot* do and
   the fallback. (Here: fully *tagged* PDF and equation alt text via
   `axessibility`/`tagpdf` require the LaTeX PDF-management layer / `lualatex`
   and fail under the xetex-based `tectonic` engine. The fallback is to compile
   the final deliverables with `lualatex` + `tagpdf`, or to validate the PDF in
   a checker such as PAC or Acrobat.)

Write the findings, the contrast numbers, the fixes applied, and the remaining
gap into an `ACCESSIBILITY.md` report next to the outputs.
