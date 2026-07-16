# 16 — The CSIRT Community Layer: Networking, Certification, and Living Documentation

> A CDC that operates alone learns slowly. Europe has a mature CSIRT community infrastructure — trust networks, certification schemes, and maturity audits — that most new CDCs discover years too late. This document covers joining it, and the documentation discipline that community certification forces upon you (which is worth adopting even if you never certify).

## 1. Publish who you are: RFC 2350

RFC 2350 defines a standard, public description of a CSIRT: constituency, services, contact channels, hours, PGP keys, reporting expectations. Publishing one (e.g., at `https://yourdomain/rfc2350.txt`) costs an afternoon and buys instant legibility with national CSIRTs, peer teams, and researchers who want to report something to you. Pair it with RFC 2142 standard mailboxes (`security@`, `abuse@`, `cert@`) routed to the CDC — attackers' victims and vulnerability reporters will try those addresses whether you monitor them or not. Review both annually (put it in the annual calendar, §5).

## 2. Join the trust networks

| Network | What it gives you | Path |
|---------|-------------------|------|
| **National CSIRT** | Statutory reporting counterpart, advisories, incident support | Establish contact pre-incident (see national annex) |
| **TF-CSIRT / Trusted Introducer** | The European CSIRT trust directory: Listed → Accredited → **Certified** (SIM3-audited) | Listing is lightweight; certification requires a SIM3 audit — see §3 |
| **FIRST** | Global incident-response community, standards (TLP, CVSS, CSIRT Services Framework), conferences | Membership requires sponsorship by existing members and a site visit process |
| **Sector CSIRTs / ISACs** | The highest-value intel: your sector's actual incidents, shared early under TLP | E.g., financial, energy, health ISACs at national/Nordic/EU level — ask your national CSIRT which exist for your sector |

Practical rules learned the hard way across the community: send a *named, consistent* person to community meetings (trust is personal, not institutional); share something before you need something; and record community memberships in GOVERN — some regulators expect notification when you join or leave information-sharing communities.

## 3. SIM3 and certification-grade maturity

**SIM3** (Security Incident Management Maturity Model, Open CSIRT Foundation) measures 40+ parameters across four quadrants — **O**rganisation, **H**uman, **T**ools, **P**rocesses — on a 0–4 scale. It underpins TF-CSIRT certification and ENISA's CSIRT maturity work, and it audits *documentation and anchoring*, not technology: can you show the mandate, is the process written, is it reviewed, is review verified by someone independent?

OCDF and SIM3 are complementary: OCDF says *what to build*, SIM3 audits *whether it's institutionalised*. Crosswalk for teams pursuing certification (or just wanting SIM3's discipline):

| SIM3 area (examples) | OCDF equivalent |
|----------------------|-----------------|
| O-1 Mandate · O-3 Authority · O-4 Responsibility | GV-1 charter (§1, §4, mission) |
| O-2 Constituency | Charter §2 scope |
| O-5/O-7 Service & service-level description | Charter §3 services + SLA table |
| O-8 Incident classification | IR plan §1 severity + closure taxonomy (§4 below) |
| O-9 Integration in CSIRT systems · H-7 External networking | This document §2 |
| O-11 Security policy | GV-3 |
| H-1 Code of conduct | Adopt a community code of practice; record acceptance |
| H-2 Personnel resilience | 13-cdc-operations §3 (shift protection, minimum staffing) |
| H-3..H-6 Skillsets & training | 12-roles-and-competences (ECSF matrix, training plans) |
| T-1/T-2 Resource & information source lists | ID-1 inventory · ID-5 intel sources register |
| T-4 Incident tracking · T-5..T-7 resilient comms | RS-1/IR plan §5 out-of-band channel |
| T-8..T-10 Prevention/detection/resolution toolsets | PROTECT/DETECT capability evidence |
| P-1..P-3 Escalation to governance/press/legal | IR plan §2 roles + RS-6 |
| P-8 Audit/feedback | §4 below + maturity reassessment |
| P-11 Secure information handling | Charter §7 (TLP, retention, need-to-know) |
| P-13..P-15 Outreach, reporting, statistics | GV-7 + metrics catalogue |

(Parameter names paraphrased; consult the official SIM3 standard for the authoritative list and scoring.)

## 4. Living documentation: the controls pattern

The difference between documentation that passes an audit and documentation that rots is a simple mechanism: **every key document/section gets a verification control** — an owner, a review frequency, and an **approver from outside the CDC** (compliance, internal audit) who confirms the review happened. Templates: [controls register](../templates/controls-register-template.md).

Three review layers work well together:
1. **Self-assessment** — yearly, using this framework's maturity assessment and/or ENISA's CSIRT maturity (SIM3-based) self-assessment tooling; gaps feed the roadmap.
2. **Recurring controls** — quarterly/semi-annual verification of the high-churn artefacts (containment mandate, contact details, severity scheme, reporting process).
3. **Independent audit** — internal audit or external assessor, yearly, from a separate reporting line.

Closure taxonomy worth standardising (it feeds honest metrics and SIM3 O-8): every case closes as **true positive with impact** (a CIA attribute was breached → incident, report), **true positive without impact** (malicious but stopped), **indeterminate**, or **false positive** (→ tuning loop). Consider VERIS as the classification vocabulary for incident types — it makes your statistics comparable across years and, anonymised, with peers.

## 5. The annual operating calendar

Recurring obligations die in backlogs unless scheduled. Maintain an annual wheel of yearly/quarterly tasks — document reviews, exercises, restore tests, self-assessment, RFC 2350 refresh, threat-landscape updates — with each task tied to its control. Template: [annual operating calendar](../templates/annual-calendar-template.md).

## Sources

- IETF RFC 2350, *Expectations for Computer Security Incident Response*; RFC 2142, *Mailbox Names for Common Services, Roles and Functions*. https://www.rfc-editor.org
- Open CSIRT Foundation, *SIM3 — Security Incident Management Maturity Model*. https://opencsirt.org/maturity/sim3/
- TF-CSIRT / Trusted Introducer — listing, accreditation and certification. https://www.trusted-introducer.org
- FIRST — membership, *CSIRT Services Framework*, *TLP 2.0*. https://www.first.org
- ENISA — CSIRT maturity resources and self-assessment. https://www.enisa.europa.eu
- VERIS — *Vocabulary for Event Recording and Incident Sharing*. http://veriscommunity.net

*Open CDC Framework (CC BY 4.0).*
