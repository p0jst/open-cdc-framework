# 04 — DETECT

## Objective

Find adversary and anomalous activity fast enough to limit damage. Detection is the operational heart of a CDC: log collection, detection engineering, triage, and threat hunting.

## Core capabilities

| ID | Capability | Description |
|----|-----------|-------------|
| DE-1 | Log collection & management | Prioritised onboarding of log sources (identity, endpoint, network, cloud, email, critical applications) into a central platform; retention policy; time synchronisation; log integrity protection. |
| DE-2 | Detection engineering | A managed lifecycle for detection use cases: idea → develop → test → deploy → tune → retire. Each use case mapped to MITRE ATT&CK techniques and to the threat profile from IDENTIFY. |
| DE-3 | Alert triage & analysis | Documented triage process, severity matrix, enrichment (asset criticality, identity context, threat intel), and escalation criteria. |
| DE-4 | Coverage assessment | Periodic measurement of detection coverage against ATT&CK and against crown-jewel assets; gap-driven engineering backlog. |
| DE-5 | Threat hunting | Hypothesis-driven hunts based on threat intel; findings convert into new detections. |
| DE-6 | Detection validation | Testing that detections actually fire: unit tests, purple teaming, adversary emulation. |
| DE-7 | Anomaly & integrity monitoring | File/configuration integrity monitoring, identity anomaly detection, and monitoring of the CDC's own infrastructure. |

## Log source onboarding priority (greenfield guidance)

1. **Identity** (directory/IdP authentication, privileged actions) — highest detection value per gigabyte.
2. **Endpoint** (EDR telemetry) — process, persistence and lateral-movement visibility.
3. **Email & web gateway** — dominant initial access vectors.
4. **Cloud control plane** (IaaS/SaaS audit logs) — often forgotten, increasingly critical.
5. **Network** (firewall, DNS, VPN, netflow — and NDR where deployed) — breadth and containment context. Network Detection and Response earns its place precisely where EDR cannot go: unmanaged and unmanageable devices (IoT, printers, medical/lab equipment, legacy appliances, BYOD), east-west visibility for lateral movement between segments, and as an integrity check on endpoint coverage (a host talking on the network with no EDR heartbeat is itself a finding). Its limits belong in the same sentence: pervasive encryption reduces payload inspection to metadata/behavioural analysis, it sees flows rather than process context, and it is a complement to endpoint + identity telemetry — not a substitute. Decision guide: the more unmanaged devices and flat legacy segments you have, the earlier NDR climbs this priority list; in a fully managed, well-segmented, cloud-heavy estate it stays at 5.
6. **Critical applications & databases** — crown-jewel specific.

**Remote and hybrid work note:** architectures retrofitted from on-prem assumptions go blind the moment a laptop leaves the VPN. Prioritise location-independent telemetry — EDR and identity-provider logs follow the user everywhere — and verify that endpoint telemetry reaches you off-network before declaring source 1–2 coverage complete. The same applies per cloud/SaaS tenant: coverage is per environment, not per organisation.

## Owning the SIEM platform (in-house or cloud)

A SIEM that nobody clearly owns decays into an unpatched, undersized liability — and it is itself a crown jewel (it holds your most sensitive telemetry and your detection logic). Before go-live, settle ownership in writing:

| Layer | Typical owner (on-prem/self-hosted) | Covers |
|-------|--------------------------------------|--------|
| Hardware & capacity | Infrastructure team | Physical/virtual hosts, storage, network, capacity planning against ingest growth |
| Operating system | Infrastructure team | OS patching, hardening baseline, backup of the platform itself, monitoring of host health |
| SIEM application | CDC | Application upgrades and patching, configuration, data onboarding/parsers, detection content, retention settings, health of the ingest pipeline |
| Access & platform security | CDC (verified independently) | Admin access (PAM), audit logging of the SIEM itself, integrity of stored logs |

The traditional split — infrastructure maintains the server and OS, the CDC maintains the SIEM platform itself — works well, but only if the interface is explicit: agree patching SLAs for the underlying stack (an unpatched SIEM host is a high-value target), capacity review cadence, and who is paged when ingest stops at 02:00. Record the split in the charter's interfaces section and give the platform its own recovery plan (RC-1): losing the SIEM during an incident means going blind at the worst moment.

**Cloud-hosted SIEM:** hosting in the cloud buys convenience, elasticity and no hardware ownership — but be clear-eyed that you are shipping your telemetry into a cloud you do not own. Security logs are among the most sensitive data an organisation produces: they contain personal data (GDPR — processor agreement, residency and transfer mechanism required), authentication patterns, internal hostnames and, in aggregate, a map of your defences. So decide deliberately which data may leave: classify log sources before onboarding, consider filtering or pseudonymising high-sensitivity fields, check sector/national residency constraints (see your national annex), and confirm export/exit terms so the data remains yours in practice, not just in contract (the data-and-exit sections of the MSSP checklist apply almost unchanged to SIEM SaaS). Hybrid patterns — sensitive sources retained in a local tier, the rest in cloud — are legitimate and common.

## CIA mapping

| Capability | C | I | A | Rationale |
|-----------|---|---|---|-----------|
| DE-1 Log management | ○ | ● | ○ | Log **integrity** is itself a control objective — tampered logs destroy investigations (and evidential value). |
| DE-2/DE-4 Use cases & coverage | ● | ● | ● | Exfiltration detections serve C; tampering/ransomware detections serve I/A. Balance the portfolio against your threat profile. |
| DE-3 Triage | ● | ● | ● | Severity matrix should explicitly weigh CIA impact per asset class. |
| DE-7 Integrity monitoring | ○ | ● | ○ | Direct Integrity control. |

## Roles & staffing

- **Tier 1/2 analysts** (or a tierless model at higher maturity) — triage and investigation.
- **Detection engineer(s)** — use case lifecycle; in small teams combined with analyst role.
- **Threat hunter** — Level 3+ capability.
- Minimum viable team for business-hours monitoring: **3–4 FTE**; sustained 24/7 in-house monitoring realistically requires **8–12 FTE** — below that, consider hybrid/MSSP models (a governance decision, see GOVERN GV-5).

## Maturity criteria

| Level | Criteria |
|-------|----------|
| **1 — Initial** | Perimeter and AV alerts reviewed reactively; no central log platform or minimal sources; no documented use cases. |
| **2 — Managed** | Central log platform with priority sources 1–3 onboarded; ~20+ documented use cases mapped to ATT&CK; triage runbook; business-hours coverage with on-call. |
| **3 — Established** | Detection engineering lifecycle with version control and testing; coverage measured against ATT&CK and crown jewels; enrichment automated; regular hunting; 24/7 coverage (in-house or hybrid); MTTD tracked. |
| **4 — Optimising** | Continuous detection validation (purple team/emulation); detection-as-code with CI/CD; hunting output systematically converted to detections; coverage and false-positive rates trended and drive backlog. |

## EU regulatory hooks

- **NIS2 Art. 21(2)(b)** — incident handling implies detection capability; **Art. 23** reporting deadlines (early warning within 24h) are only achievable with functioning detection.
- **GDPR Art. 33** — 72-hour breach notification to the supervisory authority starts at *awareness*; detection speed directly determines compliance feasibility.
- **DORA Art. 10** — financial entities must have mechanisms to promptly detect anomalous activities.
- **GDPR & employee monitoring** — security monitoring of user activity must respect data protection: define purpose limitation, retention, and access controls for security logs; involve the DPO. (Log data about employees is personal data.)

## External dependencies

| Dependency | Party | Type | Agree up front |
|-----------|-------|------|----------------|
| Log source enablement and forwarding | System/application owners | [HARD] | Onboarding SLA per source; the priority list above as the queue |
| SIEM hardware/OS layer (self-hosted) | Infrastructure team | [HARD] | Ownership split per the SIEM section above; paging path when ingest stops |
| Network taps/span or NDR sensor placement | Network team | [HARD] | Placement plan tied to segments and blind spots |
| Approval of privacy-intrusive sources (endpoint content, mail inspection) | DPO | [GATE] | Assessment criteria and turnaround pre-agreed |
| Business context for tuning (what is normal here?) | Application owners | [SOFT] | Named contact per crown jewel |

## Sources

- NIST CSF 2.0 (CSWP 29), DETECT function. https://doi.org/10.6028/NIST.CSWP.29
- MITRE ATT&CK®. https://attack.mitre.org
- MITRE, *11 Strategies of a World-Class Cybersecurity Operations Center* (Zimmerman et al., 2nd ed.). https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center
- NIST SP 800-92, *Guide to Computer Security Log Management*.
- Directive (EU) 2022/2555 (NIS2) Art. 21, 23; GDPR Art. 33; DORA Art. 10.

*Open CDC Framework (OCDF) — CC BY 4.0. Credits: [19-references.md](19-references.md).*
