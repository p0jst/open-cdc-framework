# Incident Response Plan — Template

> Related capability: RS-1. Structure informed by NIST SP 800-61r3 and FIRST good practice. Keep this document short (10–15 pages max) — detail belongs in playbooks.

**Owner:** | **Approved by:** | **Version / date:** | **Exercised on:**

## 1. Definitions & severity classification

| Severity | Definition | Examples | Response target |
|----------|-----------|----------|-----------------|
| P1 — Critical | Confirmed compromise of crown-jewel service, or active widespread attack; major C/I/A impact | Ransomware executing; confirmed exfiltration of special-category data | Immediate, 24/7, crisis interface assessed |
| P2 — High | Confirmed compromise, contained scope | Single compromised admin account | ≤ 1 h engagement |
| P3 — Medium | Probable incident, limited impact | Malware detected and blocked, persistence suspected | Same business day |
| P4 — Low | Policy violation / no material impact | Isolated phishing click, no execution | Routine |

> Classify severity against **CIA impact per affected asset class** (see docs/07-cia-triad.md) — not against alert volume.

## 2. Roles

| Role | Person / rotation | Responsibility |
|------|-------------------|----------------|
| Incident Manager | | Coordination, decisions, log of record |
| Technical Lead | | Investigation & containment direction |
| Legal / DPO | | Breach assessment, notification decisions |
| Communications | | Internal & external messaging |
| Executive sponsor | | Crisis escalation, major trade-off approval |

## 3. Process (lifecycle)

1. **Detection & reporting** — sources: monitoring, users ([report channel]), third parties, national CSIRT.
2. **Triage & classification** — severity per §1; open incident record; start timeline log.
3. **Containment** — per playbook; authority per CDC charter §4. Record every action with timestamp (evidential integrity).
4. **Eradication & investigation** — root cause; preserve evidence (hashing, chain of custody form: [link]).
5. **Recovery** — integrity verification before reconnection; credential rotation; see recovery plans.
6. **Post-incident** — blameless review within [10] working days for P1/P2; actions tracked in [system].

## 4. Statutory notification decision tree

> Prepare per-jurisdiction contact sheet and report templates as annexes. Deadlines below are EU-level; verify national transposition.

- **Personal data breach?** → DPO assesses risk → if notifiable: DPA within **72 h of awareness** (GDPR Art. 33); data subjects if high risk (Art. 34). Document all breaches, including non-notified.
- **NIS2 significant incident?** → early warning to national CSIRT **≤ 24 h**, notification ≤ 72 h, final report ≤ 1 month (Art. 23).
- **DORA major incident?** (financial entities) → per Art. 19 timelines.
- **Law enforcement?** → decision by [role]; national cybercrime unit contact: […].

## 5. Communications

- Out-of-band channel (assume email/chat compromised): […]
- Holding statement templates: [annex]
- Spokesperson: only [role]; TLP 2.0 governs technical information sharing.

## 6. Playbook index

| Scenario | Playbook | Last exercised |
|----------|----------|----------------|
| Ransomware | PB-01 | |
| Business email compromise / phishing | PB-02 | |
| Credential / identity compromise | PB-03 | |
| Personal data breach | PB-04 | |
| DDoS | PB-05 | |
| Supplier / third-party compromise | PB-06 | |

## 7. Exercise & review schedule

- Tabletop incl. management: at least annually (NIS2 Art. 20 training obligation supports this).
- Technical exercise / reporting drill: [cadence].
- Plan review: annually and after each P1/P2 incident.

---
*Template from the Open CDC Framework (CC BY 4.0). Informed by NIST SP 800-61r3, GDPR, NIS2, DORA — verify legal specifics with counsel.*
