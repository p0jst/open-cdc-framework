# National Annex — Denmark (DK)

> Status: community-maintained; verified July 2026. Verify against retsinformation.dk and samsik.dk before relying on it. Not legal advice.

## The Danish implementation landscape

Denmark implemented NIS2 and CER through a **family of laws** in force since 2025, rather than a single act:

| Law | Covers | In force | Selector tag |
|-----|--------|----------|--------------|
| **NIS 2-loven** — Lov nr. 434 af 6. maj 2025, *Lov om foranstaltninger til sikring af et højt cybersikkerhedsniveau* | Horizontal NIS2 implementation for most sectors | 1 July 2025 | `dk-nis2` |
| **Lov om styrket beredskab i energisektoren** | Energy sector — combines NIS2 (cyber) and CER (physical) into one regime, with requirements beyond the EU minimum (e.g., 24/7 monitoring of critical installations, network segmentation, rules on location of operations centres) | 7 March 2025 | `dk-energi` |
| **Lov om sikkerhed og beredskab i telesektoren** (L142) | Telecom sector NIS2 implementation | 1 July 2025 | `dk-tele` |
| **CER-loven** (*lov om kritiske enheders modstandsdygtighed*) | Physical resilience of critical entities across ~11 sectors | 1 July 2025 | `dk-cer` |
| **Lov om finansiel virksomhed § 333 et seq.** | Financial sector (aligned with DORA) | — | `dk-fin` |

> Note on naming: "Lov om styrket beredskab" in Danish practice usually refers to the **energy-sector** act above; the NIS 2-loven and CER-loven are separate acts. If your organisation spans sectors, several regimes can apply simultaneously — the NIS 2-loven explicitly yields to the energy, tele and financial acts for entities they cover (§ 1, stk. 2).

## Key Danish specifics for your CDC

1. **Registration duty:** entities covered by the NIS 2-loven must register on **virk.dk** (initial deadline was 1 October 2025; new entities register when they come into scope).
2. **Incident reporting channel:** significant incidents are reported via **virk.dk**; the national CSIRT function is performed by **Forsvarets Efterretningstjeneste / Center for Cybersikkerhed (CFCS)**. Timelines follow the NIS2 pattern: early warning ≤ 24 h, notification ≤ 72 h, final report ≤ 1 month.
3. **Authorities to know:**
   - **Styrelsen for Samfundssikkerhed (SAMSIK)** — overall coordination and cross-sector guidance (samsik.dk/nis2)
   - **Sector-responsible authorities** supervise their own sectors (e.g., Digitaliseringsstyrelsen for digital sectors, Energistyrelsen for energy, Finanstilsynet for finance, Trafikstyrelsen for transport)
   - **CFCS** — technical advisory and incident reception
4. **Guidance materials:** SAMSIK/CFCS publish cross-cutting NIS2 vejledninger structuring measures as *skal* (must), *bør* (should, justify deviations) and *kan* (may) — a useful evidence structure for your maturity assessments (map OCDF capability evidence to skal/bør items).
5. **Energy-sector extras** (Lov om styrket beredskab i energisektoren): expect requirements beyond this framework's Level 3 baseline — real-time 24/7 monitoring of critical installations, mandated segmentation, physical security integration, and geographic constraints on control centres. Plan DETECT and GOVERN targets at Level 3–4 accordingly.

## CDC checklist for Denmark

- [ ] Applicability determined per legal entity and sector (NIS 2-loven vs sector acts) — recorded in the regulatory applicability register (GOVERN)
- [ ] Registered on virk.dk where required
- [ ] Reporting procedure drilled against the virk.dk flow, with the 24 h early-warning clock
- [ ] Sector authority contact list maintained; relationship established with CFCS before an incident
- [ ] Datatilsynet contact and GDPR Art. 33 flow prepared (runs in parallel with NIS2 reporting)
- [ ] SAMSIK/CFCS vejledninger mapped to your control evidence (skal/bør/kan)

## Sources

- Lov nr. 434 af 6. maj 2025 (NIS 2-loven): https://www.retsinformation.dk/eli/lta/2025/434
- Styrelsen for Samfundssikkerhed — NIS2: https://samsik.dk/nis2
- Digitaliseringsstyrelsen NIS2 news (1 July 2025 entry into force): https://digst.dk
- NIS2-tjek self-assessment: https://nis2tjek.sikkerdigital.dk

*Open CDC Framework (CC BY 4.0). Contributions correcting or extending this annex are welcome.*
