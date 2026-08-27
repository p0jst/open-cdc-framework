# 06 — RECOVER

## Objective

Restore affected services in a trustworthy state, communicate honestly during restoration, and convert every incident into institutional learning.

## Core capabilities

| ID | Capability | Description |
|----|-----------|-------------|
| RC-1 | Recovery planning | Documented recovery plans for crown-jewel services with RTO/RPO targets agreed with the business; restoration ordering based on dependencies (from IDENTIFY). |
| RC-2 | Trusted restoration | Verify integrity of backups and systems *before* reconnecting (assume ransomware persistence); rebuild-from-known-good procedures; credential rotation as standard recovery step. |
| RC-3 | Recovery execution & verification | Ability to execute restores at scale; post-restore validation that services function and are clean. |
| RC-4 | Recovery communication | Status communication to internal stakeholders, customers, authorities (final NIS2/DORA reports), and the public where relevant (CSF 2.0 RC.CO). |
| RC-5 | Lessons learned & improvement loop | Blameless post-incident reviews with tracked actions; findings feed the improvement backlog (CSF 2.0 ID.IM) and update playbooks, detections and controls. |
| RC-6 | Business continuity integration | CDC recovery plans aligned with enterprise BCM/DR; joint exercises. |

## CIA mapping

| Capability | C | I | A | Rationale |
|-----------|---|---|---|-----------|
| RC-1 Recovery planning | ○ | ○ | ● | RTO/RPO are Availability commitments. |
| RC-2 Trusted restoration | ○ | ● | ● | Restoring a backdoored system restores the breach: **Integrity verification before Availability restoration** is the core principle of this function. |
| RC-4 Communication | ● | ○ | ○ | Recovery comms must not leak sensitive investigation details (Confidentiality of incident data). |

## Roles & staffing

- **Service/platform owners** execute restoration; the CDC verifies cleanliness.
- **Incident manager** remains accountable until closure criteria are met.
- **BCM coordinator** — interface to continuity management.

## Maturity criteria

| Level | Criteria |
|-------|----------|
| **1 — Initial** | Restoration improvised; backups untested; no post-incident reviews. |
| **2 — Managed** | Recovery plans and RTO/RPO for critical services; annual restore test; post-incident reviews held for major incidents. |
| **3 — Established** | Rebuild-from-known-good procedures; integrity verification gates before reconnection; lessons-learned actions tracked to closure; joint BCM/CDC exercise annually. |
| **4 — Optimising** | Recovery time capabilities measured against RTO in realistic exercises (incl. ransomware-scale scenarios); improvement loop metrics show incidents driving control changes; supplier recovery dependencies tested. |

## EU regulatory hooks

- **NIS2 Art. 21(2)(c)** — business continuity, backup management, disaster recovery, and crisis management are explicitly required measures.
- **NIS2 Art. 23** — the **final report** (≤ 1 month) must include root cause, mitigation, and cross-border impact where applicable.
- **DORA Art. 11–12** — response and recovery plans, backup policies and restoration procedures for financial entities, with testing obligations.
- **GDPR Art. 32(1)(c)** — "the ability to restore the availability and access to personal data in a timely manner" is a named legal requirement.

## External dependencies

| Dependency | Party | Type | Agree up front |
|-----------|-------|------|----------------|
| RTO/RPO targets accepted | Business service owners | [GATE] | Signed per crown jewel; revisited after exercises |
| Restoration execution | Service/platform owners | [HARD] | Rebuild procedures rehearsed jointly |
| Reconnection of restored systems | CDC integrity verification | [GATE] | Cleanliness criteria checklist; CDC sign-off before reconnect |
| Business continuity alignment and joint exercises | BCM function | [HARD] | Shared scenario set; annual joint exercise |
| Supplier recovery dependencies | Vendors / procurement | [SOFT] | Recovery commitments in contracts where feasible |

## Sources

- NIST CSF 2.0 (CSWP 29), RECOVER function. https://doi.org/10.6028/NIST.CSWP.29
- NIST SP 800-34 Rev. 1, *Contingency Planning Guide for Federal Information Systems*.
- Directive (EU) 2022/2555 (NIS2) Art. 21(2)(c), 23; Regulation (EU) 2022/2554 (DORA) Art. 11–12; GDPR Art. 32.

*Open CDC Framework (OCDF) — CC BY 4.0. Credits: [19-references.md](19-references.md).*
