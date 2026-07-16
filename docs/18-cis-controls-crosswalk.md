# 18 — CIS Controls Crosswalk: Concrete Actions per Control

> All 18 CIS Critical Security Controls (v8/v8.1) mapped to this framework, each with the concrete actions a CDC should drive or verify. Use it three ways: as a gap check ("which controls have no owner?"), as the business-facing prioritisation narrative (doc 09), and as an implementation checklist per tier — CIS Implementation Groups align with OCDF tiers (IG1≈Essential, IG2≈Standard, IG3≈Advanced). The CDC rarely *operates* all of these; it must *require, verify and consume* them.

| # | CIS Control | OCDF ref | Concrete actions |
|---|-------------|----------|------------------|
| 1 | Enterprise asset inventory | ID-1 | Automated discovery on all networks and cloud tenants · weekly reconciliation against directory/DHCP/EDR/MDM · unknown-device process (detect → identify or block) · measure accuracy by sampling, publish the % |
| 2 | Software asset inventory | ID-1, PR-4 | Software inventory from endpoint agent/package managers · unauthorized-software review cadence · allowlisting path: script control + block execution from user-writable paths (E) → server allowlisting, audit-mode first (S) → workstation allowlisting (A) — see doc 03 |
| 3 | Data protection | ID-2, PR-3 | Classification scheme with owners · map where classified data lives (reuse GDPR Art. 30 records) · encrypt at rest/in transit per class · retention + secure disposal defined · egress/DLP proportionate to class · access logs on sensitive stores into the SIEM |
| 4 | Secure configuration | PR-4 | Adopt hardening baselines (CIS Benchmarks) per platform · golden images/IaC so systems arrive hardened · configuration-drift monitoring into DETECT · secure defaults verified at procurement · session lock, firewall-on, default-deny on servers |
| 5 | Account management | PR-1 | Full account inventory incl. service accounts with owners · joiner/mover/leaver with same-day disable · **quarterly dormant-account review** (disable >45 days unused) · unique accounts, no shared admin · separate admin accounts from daily-driver identities |
| 6 | Access control management | PR-1 | MFA everywhere externally + for all admin access (phishing-resistant for privileged) · role-based access with documented grant/revoke · **annual access recertification on crown jewels** · PAM for tier-0 · centralise authorisation through the IdP |
| 7 | Continuous vulnerability management | ID-4, PR-5 | Authenticated scans at least monthly (E: quarterly) + external scans · risk-based remediation SLAs (actively exploited/KEV: days) · emergency-patch process drilled · track SLA attainment as a KPI, report to GOVERN |
| 8 | Audit log management | DE-1 | Central collection per the priority list (doc 04) · time sync verified · retention meets legal/IR needs (typically ≥12 months hot or reachable) · log-integrity protection · **coverage check: every crown jewel emits telemetry** · review DNS/URL/command-line audit enrichment at S/A |
| 9 | Email & web protections | PR-9 (doc 03) | **DMARC (enforcing), SPF, DKIM** on all sending domains · mail gateway with attachment sandboxing/file-type blocking · protective DNS filtering for all endpoints incl. remote · browsers on supported versions with extension control · block/flag lookalike-domain and external-sender markers |
| 10 | Malware defenses | PR-4 | EDR on every supported endpoint and server, coverage measured (≥98%) · anti-malware signatures auto-update · **disable autorun/autoplay** on removable media · EDR telemetry into DETECT as source 2 · EDR tamper-protection on |
| 11 | Data recovery | PR-7, RC | Automated backups for all in-scope data · one **offline/immutable copy** · encryption of backups · quarterly restore tests, annual full-service recovery exercise (A: ransomware-scale) · backup infrastructure isolated from production identity (no domain-joined backup servers) |
| 12 | Network infrastructure management | PR-6 | Network device inventory + supported versions only · **management plane on a dedicated network/VLAN with MFA** · configs in version control with diff alerts · default-deny between zones documented · decommission process removes stale rules |
| 13 | Network monitoring & defense | DE-1, DE-7 | Netflow/DNS/proxy logs central · IDS/NDR where unmanaged devices or flat segments exist (doc 04) · alert on new device in critical segments · egress filtering + detection of denied-egress attempts · remote-access anomaly detection via IdP |
| 14 | Security awareness & skills training | PR-2, doc 12 | Role-based annual training + onboarding module · phishing simulation with reporting culture as the metric (not click-rate shaming) · developer/admin-specific tracks · management training (NIS2 Art. 20) · CDC team skills matrix (ECSF) reviewed twice yearly |
| 15 | Service provider management | GV-6, MSSP checklist | Provider inventory with data/access classification · security requirements + incident-notification clauses in contracts · annual provider review against the checklist · offboarding revokes access same-day · monitor provider incidents (they are your incidents) |
| 16 | Application software security | PR-8 | Secure SDLC requirements for in-house code · dependency/SCA scanning in CI · secrets out of code (vault + scanning) · pre-production security testing · vulnerability disclosure channel (also a NIS2 Art. 21(2)(e) expectation) |
| 17 | Incident response management | RESPOND, playbooks | Named IR roles with deputies · IR plan + top-scenario playbooks approved · statutory reporting machinery drilled against the 24 h clock · annual exercise incl. management · post-incident reviews with tracked actions |
| 18 | Penetration testing | DE-6, doc 09 | **Only after Controls 1–11 have substance** — a pentest against no inventory/MFA/backups documents known gaps expensively · scope against crown jewels and the threat profile · rules of engagement signed before any test · findings enter the same backlog as ID-7 · A-tier: purple teaming/TLPT (DORA Art. 26 where applicable) |

## How to work with this crosswalk

1. Assign an owner per control row (many sit outside the CDC — that's the point of writing them down). Classify each external row with the dependency markers from doc 00: [GATE], [HARD] or [SOFT].
2. Walk it in the annual calendar: one quarter per 4–5 controls keeps the review load sane.
3. Tie evidence to the controls register (doc 16 §4) — CIS safeguard evidence and NIS2 Art. 21 evidence overlap heavily; collect once, use twice.
4. Tier honestly: IG1/Essential rows first, in the doc 09 order. The bolded actions above are the ones most often missing in otherwise mature environments.

## Sources

- CIS, *CIS Critical Security Controls v8.1* and Implementation Groups. https://www.cisecurity.org/controls — © Center for Internet Security; control names referenced with attribution, safeguard texts paraphrased.
- Cross-references: NIS2 Art. 21(2); DORA Art. 26 (TLPT); NIST CSF 2.0.

*Open CDC Framework (CC BY 4.0).*
