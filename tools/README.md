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

## regulatory-profile.html — interactive law selector (Tool 01)

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
National implementations use `<iso2>-nat` (e.g. `de-nat`, `fr-nat`) — one tag per member state.
Denmark is tagged per act (`dk-nis2`, `dk-energi`, `dk-tele`, `dk-cer`, `dk-fin`) as the
reference example; contributors adding the same granularity for another country should
follow that pattern (`<iso2>-<shortname>`).

## maturity-assessment.html — interactive maturity self-assessment (Tool 03)

A single-file, dependency-free page that turns
[`assessments/maturity-self-assessment.md`](../assessments/maturity-self-assessment.md)
into something you actually fill out, instead of a markdown checklist whose
`- [ ]` boxes render as inert text on the website. All 60 criteria across the
six CSF functions are real checkboxes with an optional evidence field each.

- **Staged auto-scoring**, exactly as the maturity model defines it: a function
  reaches Level *N* only when every criterion at *N* and every level below it is
  checked — no averaging up.
- **Target profiles** from [`docs/08-maturity-model.md`](../docs/08-maturity-model.md)'s
  target-setting table (SME, NIS2 important/essential, critical infrastructure)
  pre-fill a target per function, individually adjustable.
- **Score chart** — current level vs. target, per function — plus a Result table
  listing exactly which unchecked criteria are blocking the next level.
- **Resume link** — the full assessment (answers, evidence notes, targets and
  the header fields) is encoded into the page's URL fragment, so the address bar
  always holds a unique link that restores exactly the current state. Copy it,
  mail it to yourself or paste it into a ticket, and continue later on any
  device or browser — no account, no cookie, no server. The fragment is never
  sent in an HTTP request, so the data stays with whoever holds the link.
- **Snapshot export/import** (JSON) so you can date and keep assessments in
  version control to track the trend, per the reassessment cadence in the
  maturity model doc. Prefer this over the link for long-term archiving, and
  for assessments with long evidence notes (links past ~2 000 characters are
  mangled by some mail clients — the tool warns when that happens).

All data stays in the browser (localStorage plus the resume link) — nothing is
sent anywhere.

### Hosting
- Works locally: just open the file in a browser (no internet needed).
- For teams: enable **GitHub Pages** — the tool is then available at
  `https://<org>.github.io/<repo>/tools/maturity-assessment.html`.

### File format (for contributors)

Criteria are embedded as one JSON blob at the top of the page's script, in the
same order as `assessments/maturity-self-assessment.md`. If you edit the
criteria text in that document, mirror the change in the tool's embedded data
(and vice versa) — the two are meant to read identically; there is currently no
build step that generates one from the other.
