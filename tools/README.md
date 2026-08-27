# Tools

## regulatory-profile.html — interactive law selector

A single-file, dependency-free page where users **tick the laws that apply to
them** (NIS2, GDPR, DORA, CRA, CER, and national acts such as Denmark's
NIS 2-loven and Lov om styrket beredskab i energisektoren). All regulatory
references in the page show/hide to match the selected profile, and
"Print / save PDF" exports a tailored document.

### Hosting
- Works locally: just open the file in a browser.
- For teams: enable **GitHub Pages** on this repo — the tool is then available
  at `https://<org>.github.io/<repo>/tools/regulatory-profile.html`.

### Law tagging convention (for contributors)

Two layers keep the framework filterable:

1. **HTML tool:** any element carries `data-law="nis2 gdpr dk-energi"` —
   it is visible if ANY of its tagged laws is selected.
2. **Markdown docs:** law-specific sentences carry an HTML comment tag, e.g.
   `<!-- law:nis2 -->` or `<!-- law:dk-nis2 -->`. These are invisible on GitHub
   but machine-readable, so future tooling (roadmap v0.2: a build script that
   generates per-profile Markdown/PDF) can filter the plain docs the same way.

### Law IDs
`nis2` `gdpr` `dora` `cra` `cer` — EU-wide ·
`dk-nis2` `dk-energi` `dk-tele` `dk-cer` `dk-fin` — Denmark ·
National contributions: use `<iso2>-<shortname>` (e.g. `de-bsig`, `fr-lpm`).
