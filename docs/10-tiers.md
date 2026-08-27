# 10 — Implementation Tiers (Essential / Standard / Advanced)

## One framework, three ambition levels

Not every organisation needs every capability. Instead of maintaining three editions, OCDF uses a **tier overlay** (pattern borrowed from the CIS Controls' Implementation Groups): every capability is tagged with the lowest tier that should implement it. Higher tiers include everything below them.

| Tier | Who | Rough profile |
|------|-----|---------------|
| **E — Essential** | SMEs, ≤5 security FTE, NIS2 *important* entities, low-complexity IT | The defensible minimum; mostly Model A/hybrid operating models |
| **S — Standard** | Dedicated CDC, NIS2 *essential* entities, regulated mid/large orgs | Full six-function coverage with measurement |
| **A — Advanced** | Critical infrastructure, high-threat sectors, DORA TLPT-scope entities | Validation, automation and self-improvement |

**Tier ≠ maturity.** Tier answers *which capabilities*; the [maturity model](08-maturity-model.md) answers *how well you run them*. A sensible target pairing: E-tier at Level 2, S-tier at Level 3, A-tier at Level 3–4.

## Capability tier map

| Function | Essential (E) | + Standard (S) | + Advanced (A) |
|----------|---------------|----------------|----------------|
| GOVERN | GV-1 charter · GV-3 policies · GV-4 RACI · GV-7 basic reporting | GV-2 risk integration · GV-5 resourcing governance · GV-6 supply chain | Quantified risk; board exercises (L4 criteria) |
| IDENTIFY | ID-1 inventory · ID-3 crown jewels · ID-4 basic vuln mgmt | ID-2 data classification · ID-5 threat profile · ID-6 risk assessment · ID-7 improvement loop | Continuous attack-surface mgmt; intel-driven engineering |
| PROTECT | PR-1 MFA/least-priv · PR-2 awareness · PR-5 patching · PR-7 tested offline backups · PR-9 email/web basics (DMARC, DNS filtering) · script control & blocking execution from user-writable paths | PR-3 data security · PR-4 hardening baselines incl. server allowlisting · PR-6 segmentation | PR-8 secure SDLC · continuous control validation · workstation allowlisting |
| DETECT | DE-1 sources 1–3 · DE-3 triage runbook (or MSSP equivalent with transparency) | DE-2 use-case lifecycle · DE-4 coverage measurement · DE-7 integrity monitoring · network/NDR telemetry where unmanaged devices or flat segments exist | DE-5 hunting · DE-6 systematic validation · detection-as-code (doc 14) · CTI programme (doc 15) |
| RESPOND | RS-1 IR plan · RS-2 top-3 playbooks · RS-5 reporting machinery | RS-3 forensics (retainer ok) · RS-4 pre-authorised containment · RS-7 annual exercises | RS-6 crisis integration · automated containment with gates |
| RECOVER | RC-1 recovery plans+RTO/RPO · RC-5 post-incident reviews | RC-2 trusted restoration · RC-3 verified execution · RC-6 BCM integration | Ransomware-scale recovery exercises; measured RTO attainment |

## How to use tiers

1. **Pick your tier** honestly (regulatory category + threat exposure + team size). When in doubt between two, take the lower and reach maturity Level 2–3 there first — a solid E beats a hollow S.
2. **Filter the framework:** in the self-assessment and navigator, skip capabilities above your tier — mark them "above tier" rather than "missing", so the score reflects your ambition, not an enterprise ideal.
3. **Regulatory floor:** your national law may mandate S-tier items regardless of size (e.g., Denmark's energy-sector act pushes DETECT toward A). The annex + selector tool trump the tier map.
4. **Review the tier choice** at every annual reassessment — tiers are meant to be outgrown.

*Open CDC Framework (CC BY 4.0). Tier-overlay pattern inspired by CIS Critical Security Controls Implementation Groups (© Center for Internet Security), credited in 19-references.md.*
