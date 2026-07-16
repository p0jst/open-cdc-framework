# 05 — RESPOND

## Objective

Contain, eradicate, and communicate during incidents — including meeting EU statutory reporting deadlines, which are among the strictest in the world.

## Core capabilities

| ID | Capability | Description |
|----|-----------|-------------|
| RS-1 | Incident response plan | Approved IR plan: definitions, severity classification, roles, escalation, decision authority (who may disconnect production?), out-of-band communications. |
| RS-2 | Playbooks | Scenario-specific runbooks for the most likely incident types (phishing/BEC, ransomware, credential compromise, data breach, DDoS, supplier compromise). |
| RS-3 | Incident analysis & forensics | Evidence collection and preservation (chain of custody), forensic imaging capability (in-house or retained), root-cause analysis (CSF 2.0 RS.AN). |
| RS-4 | Containment & eradication | Technical ability to isolate hosts, disable accounts, block indicators, and revoke sessions — with pre-agreed authority. |
| RS-5 | Incident reporting & communication | Internal escalation matrix plus **external statutory reporting**: national CSIRT/competent authority (NIS2), data protection authority (GDPR), sector regulators (DORA), affected data subjects, law enforcement. |
| RS-6 | Crisis management interface | Escalation path from security incident to organisational crisis; link to business continuity structures. |
| RS-7 | Exercises | Tabletop and technical exercises at least annually, including management (NIS2 training obligation) and statutory-reporting drills. |

## EU statutory reporting timelines (build these into playbooks)

| Regime | Trigger | Deadline | Recipient |
|--------|---------|----------|-----------|
| **NIS2 Art. 23** | Significant incident | **Early warning ≤ 24 h**; incident notification ≤ 72 h; final report ≤ 1 month | National CSIRT / competent authority |
| **GDPR Art. 33** | Personal data breach (risk to individuals) | **≤ 72 h from awareness** | Data protection authority |
| **GDPR Art. 34** | High risk to individuals | Without undue delay | Affected data subjects |
| **DORA Art. 19** | Major ICT-related incident (financial entities) | Initial ≤ 4 h from classification / ≤ 24 h from awareness; intermediate ≤ 72 h; final ≤ 1 month | Competent financial authority |

> Member-state transpositions of NIS2 may add national specifics — maintain a country annex for each jurisdiction you operate in. Community contributions of national annexes are welcome (see CONTRIBUTING).

## Case closure taxonomy

Standardise how every case closes — it is the foundation of honest metrics, tuning feedback and comparable statistics: **true positive with impact** (a CIA attribute was breached → incident; reporting duties assessed), **true positive without impact** (malicious intent, no harm done), **indeterminate**, or **false positive** (→ tuning loop, doc 13). For incident-type classification, the open VERIS vocabulary (malware, hacking, social, misuse, error, physical, environmental) keeps year-over-year and peer statistics comparable.

## CIA mapping

| Capability | C | I | A | Rationale |
|-----------|---|---|---|-----------|
| RS-2 Playbooks | ● | ● | ● | Ransomware playbooks defend A/I; breach playbooks defend C. |
| RS-3 Forensics | ○ | ● | ○ | Evidence integrity (hashing, chain of custody) is an Integrity discipline. |
| RS-4 Containment | ● | ● | ● | Containment trades short-term Availability for protection of C and I — the decision authority for that trade-off must be pre-agreed (GOVERN). |

## Roles & staffing

- **Incident manager/commander** — coordinates; distinct from technical lead in larger incidents.
- **Technical responders** — often the same analysts as DETECT.
- **Legal/DPO and communications** — mandatory members of the extended IR team.
- **Retainers** — consider external DFIR retainer at Level 2+ if in-house forensics is not viable.

## Maturity criteria

| Level | Criteria |
|-------|----------|
| **1 — Initial** | Ad-hoc response by IT; no approved plan; reporting duties not mapped. |
| **2 — Managed** | Approved IR plan; playbooks for top 3–5 scenarios; statutory reporting contacts and templates prepared; annual tabletop. |
| **3 — Established** | Containment actions pre-authorised and technically automatable; forensic capability (in-house or retained); exercises include management and reporting drills; post-incident reviews feed improvements. |
| **4 — Optimising** | Response metrics (MTTC/MTTR) trended; cross-functional crisis exercises with suppliers; automation of enrichment and containment with human approval gates; lessons systematically drive PROTECT/DETECT changes. |

## EU regulatory hooks

- **NIS2 Art. 21(2)(b)** incident handling; **Art. 23** reporting (see table above).
- **GDPR Art. 33/34** — breach notification; document *all* breaches internally, even those not notified (Art. 33(5)).
- **DORA Art. 17–19** — ICT incident management, classification and reporting for financial entities.
- **ENISA / national CSIRT good practice** — align severity taxonomies with your national CSIRT's scheme where one exists to ease reporting.

## External dependencies

| Dependency | Party | Type | Agree up front |
|-----------|-------|------|----------------|
| Containment beyond pre-mandated scope (crown jewels) | Service owner / executive per charter §4 | [GATE] | Decision criteria + deputy; drill it — this gate at 03:00 is the whole point of the charter |
| Execution of containment and restoration actions | IT operations | [HARD] | 24/7 reachability; actions from the containment catalogue rehearsed |
| Notification decisions (GDPR/NIS2/press) | Legal / DPO / communications | [GATE] | Draft templates pre-approved; who can be woken |
| External statements and customer communication | Communications | [HARD] | Holding statements ready; single spokesperson rule |
| Insider-related cases | HR + legal | [GATE] | Process agreed before the first case, incl. evidence handling |
| Forensics beyond in-house capability | External DFIR retainer | [HARD] | Retainer signed, response time, onboarding pack ready |

## Sources

- NIST SP 800-61 Rev. 3, *Incident Response Recommendations and Considerations for Cybersecurity Risk Management* (2025). https://doi.org/10.6028/NIST.SP.800-61r3
- NIST CSF 2.0 (CSWP 29), RESPOND function.
- FIRST, *Computer Security Incident Response Team (CSIRT) Services Framework* v2.1. https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1
- Directive (EU) 2022/2555 (NIS2) Art. 23; GDPR Art. 33–34; Regulation (EU) 2022/2554 (DORA) Art. 17–19.
- VERIS — *Vocabulary for Event Recording and Incident Sharing*. http://veriscommunity.net
- Microsoft incident response playbooks (baseline runbooks; adapt to your environment). https://learn.microsoft.com/security/operations/incident-response-playbooks
- CISA, *Federal Government Cybersecurity Incident and Vulnerability Response Playbooks* (2021). https://www.cisa.gov

*Open CDC Framework (OCDF) — CC BY 4.0. Credits: [19-references.md](19-references.md).*
