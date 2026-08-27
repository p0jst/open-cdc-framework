# 08 — Maturity Model

## Design

The OCDF maturity model defines **four levels**, applied to each of the six CSF functions. The level names and philosophy are informed by the NIST CSF 2.0 **Tiers** (Partial, Risk Informed, Repeatable, Adaptive) and by the general structure of capability maturity models (CMMI); teams already using **SOC-CMM** (van Os) will find the levels easy to cross-map.

We deliberately use four levels rather than five: in practice the difference between "defined" and "quantitatively managed" is where most models lose their audience.

## The levels

| Level | Name | One-line test |
|-------|------|---------------|
| **1** | Initial | "It happens when someone remembers." — Activities are reactive, undocumented, person-dependent. |
| **2** | Managed | "It's written down and someone owns it." — Core processes documented, approved, and executed; coverage partial. |
| **3** | Established | "It's measured and consistent." — Processes are integrated, coverage is broad, metrics exist, and output of one function feeds another. |
| **4** | Optimising | "It improves itself." — Data-driven, validated, trended; lessons systematically change the system. |

Per-function criteria live in each function document (sections "Maturity criteria" in docs 01–06).

## Relationship to tiers

Tier ([10-tiers.md](10-tiers.md)) selects *which* capabilities apply; maturity measures *how well* you run the selected set. Score only capabilities at or below your tier; mark the rest "above tier".

## Scoring method

1. For each function, review the maturity criteria table and the self-assessment checklist ([../assessments/maturity-self-assessment.md](../assessments/maturity-self-assessment.md)).
2. A level is achieved only when **all** criteria of that level and the levels below are met ("staged" scoring — no averaging up).
3. Record evidence for each criterion (documents, screenshots, metric exports). Evidence-free self-assessment inflates scores by roughly one level.
4. Plot the six function scores as a radar/spider profile. **A balanced Level 2 beats a spiky profile with Level 4 detection and Level 1 governance** — attackers exploit the weakest function.

## Target-setting guidance

| Organisation type | Suggested target profile |
|-------------------|--------------------------|
| SME, low regulatory exposure | Level 2 across all functions |
| NIS2 *important* entity | Level 2–3, with RESPOND at 3 (reporting deadlines) |
| NIS2 *essential* entity / DORA financial entity | Level 3 across all functions |
| Critical infrastructure, high-threat sectors | Level 3–4, prioritising DETECT/RESPOND at 4 |

Targets are risk decisions — set them in GOVERN, with executive sign-off.

## Reassessment cadence

- Full assessment: **annually**, or after major organisational change.
- Progress review on open improvement actions: **quarterly**.
- Track the score trend, not just the snapshot — the improvement *rate* is itself a Level 4 indicator.

## Relationship to other models

| Model | Relationship |
|-------|--------------|
| **NIST CSF 2.0 Tiers** | OCDF levels are function-scoped rather than organisation-scoped, but philosophically aligned (Tier 1↔L1 … Tier 4↔L4). |
| **SOC-CMM** | Much finer-grained (5 domains, ~25 aspects, continuous scoring). Recommended as a deep-dive follow-up once OCDF assessment identifies weak functions. SOC-CMM © Rob van Os, available free at soc-cmm.com. |
| **CMMI** | Conceptual ancestor of all staged maturity models; not security-specific. |
| **ENISA CSIRT Maturity Framework** | Focused on national/sectoral CSIRTs; relevant if your CDC provides CSIRT services externally. Based on SIM3 (Open CSIRT Foundation). |

## Sources

- NIST CSF 2.0 (CSWP 29) — Tiers concept. https://doi.org/10.6028/NIST.CSWP.29
- R. van Os, *SOC-CMM — Capability Maturity Model for Security Operations Centers*. https://www.soc-cmm.com
- ENISA, *CSIRT Maturity Framework*. https://www.enisa.europa.eu
- Open CSIRT Foundation, *SIM3 — Security Incident Management Maturity Model*. https://opencsirt.org
- CMMI Institute, *Capability Maturity Model Integration*.

*Open CDC Framework (OCDF) — CC BY 4.0. Credits: [19-references.md](19-references.md).*
