# Changelog — Open CDC Framework (OCDF)

## Unreleased

- **Interactive maturity self-assessment** (Tool 03): `tools/maturity-assessment.html` — the maturity checklist filled out in the browser instead of as inert markdown checkboxes. Real checkboxes with evidence fields for all 60 criteria, staged auto-scoring per the maturity model's rules, target-profile presets from `docs/08-maturity-model.md`, a score-vs-target chart, a Result table naming exactly which criteria block the next level, and JSON snapshot export/import for tracking the trend. `assessments/maturity-self-assessment.md` now links to it at the top; landing page's "Assess your maturity" button points to it directly.

- **Website**: the framework now publishes as a documentation site (MkDocs Material) via GitHub Actions — landing page, full-text search, themed to match the tools; `site/` holds the landing page, theme CSS and staging script, `mkdocs.yml` the nav, `.github/workflows/publish-site.yml` the deployment. Repo layout and all links unchanged.

- **Team skill mapping** added to the Roles & Competences layer:
  - `templates/skill-self-assessment.xlsx` (+ CSV version) — 47-skill self-assessment sheet across 8 domains (six CSF functions + Platform & Automation + Professional Skills), rated 0–3 on the framework scale with a per-skill "want to grow?" flag
  - `tools/skill-matrix.html` (Tool 02) — single-file, dependency-free team skill matrix: upload returned sheets (cumulative, per-person overwrite), team heatmap with coverage/bus-factor flags, gap analysis against editable per-role targets, train/mentor/hire action view, JSON snapshot export/import
  - New "Team skill mapping" section in `docs/12-roles-and-competences.md` (process, cadence, GDPR ground rules, hiring hook)

## v0.1-rc1 — 2026-07-15 (freeze candidate)

Project name approved: Open CDC Framework (OCDF). First feature-complete release candidate. Contents:

- Six NIST CSF 2.0 function documents with CIA mapping, four-level maturity criteria, EU regulatory hooks, and external-dependency tables ([GATE]/[HARD]/[SOFT])
- Design layer: Start Here prioritisation (CIS-ordered), E/S/A implementation tiers, operating models (MSSP / tiered / capability-based / shared CDC), ECSF-based roles and competences
- Operations layer: tuning loop, detection-as-code (+ engineering deep dive with Sigma/YAML, CI/CD, honest ATT&CK coverage scoring), CTI deep dive (strategic/operational/tactical), automation & AI-triage guardrails, tool portfolio discipline, SIEM ownership incl. cloud data considerations
- Community layer: RFC 2350, TF-CSIRT/FIRST, SIM3 crosswalk, living-documentation controls, annual calendar
- Regulatory layer: EU landscape (NIS2/GDPR/DORA/CRA/CER), 27 national annexes (status verified July 2026), interactive law selector, CIS Controls v8 crosswalk with concrete actions
- Practical assets: 9 templates, 3 platform IR/forensics playbooks (Win11/macOS/RHEL), design navigator, maturity self-assessment

Known pre-v1.0 work: fill ABOUT placeholders; legal review of reporting-deadline tables and national law references; re-verify "pending" annexes (FR/IE/LU/ES/PL/NL); set final repository URL in docs/19-references.md citation line.
