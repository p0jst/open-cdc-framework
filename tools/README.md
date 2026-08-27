# Tools

## skill-matrix.html — team skill matrix (Tool 02)

A single-file, dependency-free page for **mapping the skills of a CDC/SOC team**.
Team members each fill in the self-assessment sheet
([`templates/skill-self-assessment.xlsx`](../templates/skill-self-assessment.xlsx)
or the [CSV version](../templates/skill-self-assessment.csv)) and send it back;
the manager drops the returned files onto the page and gets:

- a **team heatmap** (people × 47 skills in 8 domains) with per-skill coverage,
  *bus factor 1* and *nobody proficient* flags, and mentor markers;
- a **gap analysis** against editable per-role target levels (defaults derived
  from [`docs/12-roles-and-competences.md`](../docs/12-roles-and-competences.md));
- an **actions view**: whom to train (gap + motivation first), which in-house
  mentor pairings close gaps for free, and which skills to hire or buy;
- **snapshot export/import** (JSON) to archive review rounds.

Uploads are cumulative and keyed by the person's name: re-uploading a sheet for
the same person **overwrites their previous answers**, so the picture always
reflects the latest round. All data stays in the manager's browser
(localStorage) — nothing leaves the page. Skill data is personal data under
GDPR: collect it transparently, use it for development only, keep access limited.

### File format (for contributors)

The tool reads `.xlsx` natively (zip + XML via the browser's built-in
`DecompressionStream` — no libraries) and `.csv`. Parsing is positional-free:
it locates the header row containing `Skill ID`, then matches rows by skill ID
(`GV-01` … `PF-05`), takes the first digit 0–3 found in the level column, and
reads `Name` / `Role` / `Date` from labelled rows above the table. Keep the
skill IDs and the `Skill ID` header intact when translating or re-styling the
sheet; everything else (column order, extra columns, formatting) is free.
The catalogue and default role targets live in one JSON blob at the top of the
page's script — edit there to localise or extend (bump the version marker in
both the sheet and the tool if you change skill IDs).

### Hosting
- Works locally: just open the file in a browser (no internet needed).
- For teams: enable **GitHub Pages** — the tool is then available at
  `https://<org>.github.io/<repo>/tools/skill-matrix.html`, and the download
  links to the templates resolve automatically.

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
