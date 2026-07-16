# 17 — EU Regulatory Landscape for CDC/SOC Teams

> ⚠️ **This is orientation, not legal advice.** Directives are transposed into national law with variations; always verify against your member state's implementation and consult legal counsel.

## The core instruments

### NIS2 — Directive (EU) 2022/2555
The horizontal cybersecurity law for the EU. Transposition deadline was **17 October 2024** (several member states transposed late — check national status).

- **Scope (Art. 2, Annexes I–II):** *essential* and *important* entities across 18 sectors (energy, transport, health, digital infrastructure, ICT service management, public administration, manufacturing of critical products, and more), generally medium-sized and above, with exceptions.
- **Key CDC-relevant obligations:**
  - Art. 20 — management accountability and training.
  - Art. 21 — minimum risk-management measures (the list in points (a)–(j) reads like a CDC capability checklist: risk analysis, incident handling, continuity/backup/DR, supply chain, secure development/acquisition, effectiveness assessment, hygiene & training, cryptography, HR/access control, MFA).
  - Art. 23 — incident reporting: **early warning ≤ 24 h**, notification ≤ 72 h, final report ≤ 1 month, to the national CSIRT or competent authority.
- **Framework mapping:** every OCDF function document has an "EU regulatory hooks" section referencing the relevant NIS2 articles.

### GDPR — Regulation (EU) 2016/679
Applies to virtually every CDC because security operations process personal data (logs!) and security incidents often involve personal data breaches.

- Art. 32 — security of processing (the legal anchor for "appropriate measures", explicitly including the ability to ensure confidentiality, **integrity, availability and resilience** — the triad is in the law).
- Art. 33/34 — 72-hour breach notification and data-subject communication.
- Art. 30 — records of processing (reuse as data inventory input).
- **The CDC as data processor problem:** security monitoring processes employee personal data. Define legal basis, purpose limitation, retention and access for security telemetry, and involve your DPO when onboarding intrusive log sources (e.g., endpoint telemetry, email content inspection).

### DORA — Regulation (EU) 2022/2554
Digital operational resilience for the **financial sector** — applicable since **17 January 2025**. Directly applicable regulation (no transposition). ICT risk management (Art. 5–16), incident classification and reporting (Art. 17–23), resilience testing incl. threat-led penetration testing/TLPT (Art. 24–27), ICT third-party risk (Art. 28–44).

### CRA — Cyber Resilience Act, Regulation (EU) 2024/2847
Security requirements for **products with digital elements** placed on the EU market; main obligations apply from **December 2027**, with vulnerability/incident reporting obligations for manufacturers starting earlier (September 2026). CDC relevance: procurement leverage, and manufacturer reporting duties if your organisation ships digital products.

### CER — Directive (EU) 2022/2557
Resilience of critical entities (physical/all-hazards counterpart of NIS2). Relevant for critical infrastructure operators' crisis-management interface.

### Cybersecurity Act — Regulation (EU) 2019/881
ENISA's permanent mandate and the EU cybersecurity certification framework (e.g., EUCC). Relevant for procurement and assurance.

## Key institutions for a CDC to know

| Institution | Why it matters to your CDC |
|-------------|----------------------------|
| **National CSIRT(s)** | Your NIS2 reporting counterpart; advisory feeds; incident support. Build the relationship *before* the incident. |
| **ENISA** | Threat landscape reports, good-practice guides, CSIRT maturity resources. |
| **CSIRTs Network & EU-CyCLONe** | EU-level operational and crisis cooperation networks (mostly indirect relevance, via your national CSIRT). |
| **Data Protection Authority** | GDPR Art. 33 notifications; guidance on monitoring vs. privacy. |
| **Sector regulators** | e.g., national financial supervisors for DORA. |

## Practical compliance pattern for a CDC

1. **Determine applicability** (GOVERN): which regimes apply, in which member states, for which legal entities. Output: a regulatory applicability register.
2. **Map obligations to capabilities**: use the "EU regulatory hooks" sections in docs 01–06 as a starting crosswalk.
3. **Prepare reporting machinery** (RESPOND): contact lists, report templates per regime, and drilled procedures — deadlines are too short to improvise.
4. **Evidence continuously**: NIS2 Art. 21(2)(f) requires *assessing the effectiveness* of measures — your maturity assessments and metrics (see templates) are that evidence.

## Sources

- Directive (EU) 2022/2555 (NIS2): https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- Regulation (EU) 2016/679 (GDPR): https://eur-lex.europa.eu/eli/reg/2016/679/oj
- Regulation (EU) 2022/2554 (DORA): https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- Regulation (EU) 2024/2847 (CRA): https://eur-lex.europa.eu/eli/reg/2024/2847/oj
- Directive (EU) 2022/2557 (CER): https://eur-lex.europa.eu/eli/dir/2022/2557/oj
- Regulation (EU) 2019/881 (Cybersecurity Act): https://eur-lex.europa.eu/eli/reg/2019/881/oj
- ENISA: https://www.enisa.europa.eu

*Open CDC Framework (OCDF) — CC BY 4.0. Credits: [19-references.md](19-references.md).*
