# 02 — IDENTIFY

## Objective

Understand what you are defending and what threatens it. Every downstream capability — detection coverage, response prioritisation, recovery ordering — depends on the quality of this function. An unknown asset cannot be monitored, patched, or restored.

## Core capabilities

| ID | Capability | Description |
|----|-----------|-------------|
| ID-1 | Asset inventory | Continuously maintained inventory of hardware, software, cloud resources, data flows, and their owners. Includes shadow-IT discovery. |
| ID-2 | Data classification | Data mapped and classified (e.g., public / internal / confidential / special-category personal data) with owners assigned. |
| ID-3 | Crown-jewel analysis | Identification of business-critical services and the assets they depend on; drives detection and recovery priority. |
| ID-4 | Vulnerability management (identification) | Regular authenticated scanning, cloud posture assessment, and external attack-surface monitoring. |
| ID-5 | Threat landscape & intelligence | A documented threat profile: which actors, sectors, and techniques (MITRE ATT&CK) are relevant to *your* organisation. Consume national CSIRT and ENISA advisories. A-tier deep dive on building a full CTI capability: [15-cti-deep-dive.md](15-cti-deep-dive.md). |
| ID-6 | Risk assessment | Periodic risk assessments combining assets, threats, and vulnerabilities; results feed GOVERN. |
| ID-7 | Improvement identification | Lessons from assessments, audits, exercises and incidents are captured as improvement actions (CSF 2.0 ID.IM). |

## CIA mapping

| Capability | C | I | A | Rationale |
|-----------|---|---|---|-----------|
| ID-1 Asset inventory | ● | ● | ● | Foundation for protecting all objectives. |
| ID-2 Data classification | ● | ○ | ○ | Primarily identifies where Confidentiality matters most (incl. GDPR special categories). |
| ID-3 Crown jewels | ○ | ● | ● | Business-critical services are usually Availability/Integrity-driven. |
| ID-4 Vulnerability mgmt | ● | ● | ● | Vulnerabilities threaten all three objectives. |
| ID-5 Threat intel | ● | ● | ● | Ransomware threatens A/I; espionage threatens C — the threat profile tells you which dominates. |

## Roles & staffing

- **Asset/configuration owner(s)** in IT operations.
- **CTI analyst** (may be part-time or shared at Level 1–2).
- **Vulnerability analyst** — often combined with detection engineering in small teams.
- **Data Protection Officer** — for data mapping and GDPR records of processing (Art. 30), which double as excellent data-classification input.

## Maturity criteria

| Level | Criteria |
|-------|----------|
| **1 — Initial** | Spreadsheet-based inventory, updated manually; annual vulnerability scan; no documented threat profile. |
| **2 — Managed** | Automated discovery for core networks; quarterly scanning; subscribed to national CSIRT advisories; crown jewels identified informally. |
| **3 — Established** | CMDB/inventory >90% accurate and reconciled automatically; risk-based vulnerability remediation SLAs; documented threat profile mapped to ATT&CK; annual risk assessment feeding budget. |
| **4 — Optimising** | Near-real-time asset and attack-surface visibility incl. cloud/SaaS; threat intel drives proactive hunting and detection engineering; risk quantification trended over time. |

## EU regulatory hooks

- **NIS2 Art. 21(2)(a), (e)** — risk analysis policies and vulnerability handling/disclosure.
- **NIS2 Art. 21(2)(d)** — supply chain security requires knowing your suppliers and dependencies (asset/dependency inventory).
- **GDPR Art. 30** — records of processing activities: reuse as data-flow inventory.
- **DORA Art. 8** — identification of ICT-supported business functions and information assets.
- **CRA (Cyber Resilience Act, Regulation (EU) 2024/2847)** — relevant when you produce or procure "products with digital elements"; feeds procurement requirements.
- **ENISA Threat Landscape (annual)** — recommended baseline input for the threat profile.

## External dependencies

| Dependency | Party | Type | Agree up front |
|-----------|-------|------|----------------|
| Crown-jewel list agreed and signed | Business service owners | [GATE] | Workshop participation; annual re-confirmation |
| Asset/CMDB data and reconciliation | IT operations | [HARD] | Data quality ownership; reconciliation cadence |
| Access to cloud tenants and SaaS admin telemetry | Platform/cloud teams | [HARD] | Read access for discovery and posture tools |
| Data classification decisions | Data owners | [HARD] | Owners named per store; classification deadline |
| Records of processing (Art. 30) as data-flow input | DPO | [SOFT] | Reuse rather than duplicate |

## Sources

- NIST CSF 2.0 (CSWP 29), IDENTIFY function. https://doi.org/10.6028/NIST.CSWP.29
- MITRE ATT&CK®. https://attack.mitre.org (© The MITRE Corporation, used under ATT&CK terms of use)
- ENISA, *ENISA Threat Landscape* report series. https://www.enisa.europa.eu/topics/cyber-threats/threat-landscape
- Directive (EU) 2022/2555 (NIS2); Regulation (EU) 2022/2554 (DORA); Regulation (EU) 2024/2847 (CRA).

*Open CDC Framework (OCDF) — CC BY 4.0. Credits: [19-references.md](19-references.md).*
