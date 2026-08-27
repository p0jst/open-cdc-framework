# 03 — PROTECT

## Objective

Reduce the likelihood and blast radius of incidents through preventive controls. The CDC does not usually *operate* all preventive controls (IT and platform teams often do), but it must *influence, verify and monitor* them — protection failures become detection and response workload.

## Core capabilities

| ID | Capability | Description |
|----|-----------|-------------|
| PR-1 | Identity & access management | Centralised identity, MFA (phishing-resistant for admins), least privilege, joiner/mover/leaver process, quarterly dormant-account review, service-account inventory with owners, privileged access management. |
| PR-2 | Awareness & training | Role-based security training; phishing simulations; specific training for developers and admins; management training (NIS2 Art. 20 obligation). |
| PR-3 | Data security | Encryption at rest and in transit, key management, data loss prevention proportionate to classification. |
| PR-4 | Platform hardening & secure configuration | Hardening baselines (e.g., CIS Benchmarks), configuration monitoring, EDR/endpoint protection deployment, and **application control** (see below). |
| PR-5 | Vulnerability remediation & patching | Risk-based patching SLAs; emergency patch process for actively exploited vulnerabilities. |
| PR-6 | Network security & segmentation | Zoning/segmentation, restricted admin paths, secure remote access, egress control. |
| PR-7 | Resilient technology infrastructure | Backups (tested, offline/immutable copy), redundancy for critical services, capacity management (CSF 2.0 PR.IR). |
| PR-8 | Secure development & change | Secure SDLC requirements, change management, and pre-production security testing where software is developed in-house. |
| PR-9 | Email & web protections | DMARC (enforcing) with SPF/DKIM on all sending domains, mail gateway with attachment controls, protective DNS filtering for all endpoints including remote, and managed browser baseline. The dominant initial-access vector deserves its own preventive row, not just a detection log source. |

### Application control / allowlisting (part of PR-4)

Software inventory (ID-1 / CIS Control 1–2) has an enforcement half that is often skipped: only authorized software, libraries and scripts may execute (the logic of CIS safeguards 2.5–2.7). Application control is among the highest-impact preventive controls available — most commodity malware and many ransomware chains simply fail on a host that refuses to run unapproved binaries and scripts. A pragmatic adoption path:

1. Start where it's easiest and matters most: servers. Server workloads change rarely; allowlisting a domain controller, a backup server or a payment application host is far more tractable than a developer laptop — and those are the hosts where execution control buys the most.
2. Audit mode first: run the platform's application control mechanism in audit/log-only mode, build the ruleset from observed reality, then enforce. Weeks in audit, not months.
3. Script control counts: constraining script interpreters and unsigned scripts blocks a large share of initial-access tradecraft even where full binary allowlisting is out of reach.
4. Workstations pragmatically: publisher/path-based rules plus blocking execution from user-writable locations gives much of the benefit at a fraction of the maintenance; full allowlisting on standard-build workstations is an A-tier ambition.
5. Feed DETECT: application-control audit and block events are a first-class log source — every block is prevention, and every audit-mode "would have blocked" is a free detection.

Ownership follows the SIEM pattern (doc 04): platform teams operate the mechanism; the CDC sets the policy intent, monitors the events and owns exceptions (each exception gets an owner and an expiry — same discipline as detection suppressions).

## CIA mapping

| Capability | C | I | A | Rationale |
|-----------|---|---|---|-----------|
| PR-1 IAM | ● | ● | ○ | Access control is the primary confidentiality/integrity control. |
| PR-3 Data security | ● | ● | ○ | Encryption serves C; signing/hashing serves I. |
| PR-4 Hardening & app control | ○ | ● | ● | Configuration/execution integrity reduces exploitability; app control directly caps ransomware blast radius (A). |
| PR-6 Segmentation | ● | ○ | ● | Contains lateral movement (C) and limits outage blast radius (A). |
| PR-9 Email/web protections | ● | ● | ○ | Cuts phishing/BEC (C) and malware delivery (I) at the front door; DMARC also protects your domain's authenticity toward others. |
| PR-7 Backups/redundancy | ○ | ● | ● | The core Availability control; immutable backups also protect Integrity against ransomware encryption/tampering. |

## Roles & staffing

- **IT/platform teams** operate most controls; the CDC defines requirements and verifies via posture monitoring.
- **Security engineer(s)** in the CDC own EDR, hardening verification, and control telemetry.
- **Awareness lead** — often shared with HR/communications.

## Maturity criteria

| Level | Criteria |
|-------|----------|
| **1 — Initial** | MFA for remote access only; annual generic awareness training; backups exist but restore untested; patching best-effort. |
| **2 — Managed** | MFA broadly enforced; hardening baselines defined for main platforms; patching SLAs for critical vulnerabilities; backup restores tested annually. |
| **3 — Established** | Phishing-resistant MFA for privileged access; PAM in place; segmentation of critical zones; immutable/offline backup copy; control coverage measured (e.g., % endpoints with EDR); application control enforced on critical servers, script control broadly. |
| **4 — Optimising** | Continuous control validation (e.g., attack simulation); zero-trust roadmap; protection telemetry feeds detection engineering; secure-by-design embedded in procurement and development; application allowlisting extended to standard workstation builds. |

## EU regulatory hooks

- **NIS2 Art. 21(2)** — explicitly requires, among others: (f) policies for cryptography and encryption; (g) HR security and access control; (h) MFA/continuous authentication where appropriate; (j) basic cyber hygiene and training.
- **Commission Implementing Regulation (EU) 2024/2690** — technical requirements detailing NIS2 Art. 21 measures for digital infrastructure entities; useful as a control checklist even outside its formal scope.
- **GDPR Art. 32** — encryption and pseudonymisation named as example measures.
- **DORA Art. 9** — protection and prevention measures for financial entities.
- **CIS Benchmarks / ENISA guidance** — recommended hardening baselines.

## External dependencies

| Dependency | Party | Type | Agree up front |
|-----------|-------|------|----------------|
| Operation of most preventive controls (patching, hardening, backups) | IT/platform teams | [HARD] | Control requirements set by CDC; SLAs and coverage telemetry back to CDC |
| MFA and identity control rollout | Identity/IAM team | [HARD] | Rollout order (admins first); exception governance |
| Segmentation and network changes | Network team | [HARD] | Zone model ownership; change lead times |
| Emergency change approval for critical patches | Change advisory board | [GATE] | Pre-approved emergency path with post-hoc review |
| Application-control exceptions | Platform teams + CDC | [GATE] | Exception owner + expiry, CDC veto on tier-0 |
| Awareness programme delivery | HR / communications | [SOFT] | CDC provides content priorities from incident data |

## Sources

- NIST CSF 2.0 (CSWP 29), PROTECT function. https://doi.org/10.6028/NIST.CSWP.29
- NIST SP 800-53 Rev. 5, *Security and Privacy Controls*. https://doi.org/10.6028/NIST.SP.800-53r5
- CIS, *CIS Critical Security Controls* (esp. Controls 1–2 incl. software allowlisting safeguards 2.5–2.7) and *CIS Benchmarks*. https://www.cisecurity.org
- Directive (EU) 2022/2555 (NIS2), Art. 21; Implementing Regulation (EU) 2024/2690; GDPR Art. 32; DORA Art. 9.

*Open CDC Framework (OCDF) — CC BY 4.0. Credits: [19-references.md](19-references.md).*
