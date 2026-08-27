# 09 — Start Here: Prioritisation Guide

> If you read only one document after the README, read this. It answers the question the rest of the framework can't answer for you page by page: **in which order?**

## The priority logic (why this order)

The ordering below deliberately mirrors the logic of the CIS Critical Security Controls: the controls are numbered roughly in order of foundational value, beginning with Control 1 (enterprise asset inventory) and Control 2 (software inventory) — and ending with Control 18 (penetration testing). That ordering is the answer to a question every new security leader faces from the business: "shouldn't we get a pentest first?" No — a penetration test against an organisation with no asset inventory, no MFA baseline and no tested backups mostly documents what you already know is missing. Inventory first, blast-radius controls next, testing when there is something meaningful to test. Use the CIS ordering when explaining prioritisation to the business; it is independent, widely recognised, and matches this guide.

1. **Mandate before machinery** — authority and scope gaps poison everything built on top.
2. **You can't detect what you can't see** — visibility precedes detection.
3. **Blast-radius controls beat detection breadth** — MFA, offline backups and segmentation cap the damage of the incidents you *will* miss.
4. **Reporting readiness is a legal clock** — the NIS2 24 h early warning must work before your first significant incident, not after.
5. **Only then: depth** — hunting, validation, automation, Level 4 ambitions.

## First 90 days (any tier, any operating model)

| Week | Do | Framework |
|------|----|-----------|
| 1–2 | Run the GOVERN navigator workshop; draft the charter incl. containment authority (§4) | navigator G1–G10, charter template |
| 1–4 | Regulatory applicability register: which laws, which entities, which countries; register with authorities where overdue | 09 + your national annex, selector tool |
| 2–6 | **Decide the operating model** (MSSP / tiered / capability-based) with the scored criteria | 11-operating-models.md |
| 3–8 | Crown-jewel workshop with the business (I1); C/I/A impact rating per service | ID-3, 07-cia-triad |
| 4–10 | Blast-radius sprint: MFA everywhere (P1), one offline/immutable backup copy restore-tested (P3), admin-path segmentation quick wins (P4) | PROTECT |
| 6–12 | Onboard priority log sources 1–3 (identity, endpoint, email) — in-house or to the MSSP | DE-1 priority list |
| 8–12 | IR plan v1 + ransomware & breach playbooks; statutory reporting contacts and one **reporting drill against the 24 h clock** | RS templates, playbooks/, annex |
| 12 | Baseline maturity self-assessment; publish the gap backlog | assessments/ |

**Dependency warning:** most of the 90-day rows above contain a [GATE] or [HARD] dependency on another department — charter sign-off [GATE], log onboarding [HARD on system owners], MFA rollout [HARD on IAM], reporting drill [GATE on legal/DPO participation]. See each function document's "External dependencies" table and the marker convention in doc 00. Secure named counterparts for every [HARD] on this plan before week 1; it is the most common silent killer of new CDC timelines.

**Exit criteria for day 90:** signed charter · applicability register · operating model decided · crown jewels agreed in writing · MFA coverage measured · one clean restore proven · identity+endpoint telemetry flowing · reporting drill executed.

## Months 4–12

- Detection: reach ~20+ ATT&CK-mapped use cases; establish the tuning loop and triage SLAs (14-cdc-operations.md)
- Response: containment technically tested; tabletop with management; DFIR retainer if not in-house
- Recover: RTO/RPO agreed for crown jewels; rebuild-from-known-good procedure drafted
- Govern: quarterly executive reporting running; supplier security clauses in new contracts
- Reassess maturity at month 12; set year-2 targets per function (aim: balanced Level 2, RESPOND at 3 if NIS2 essential)

## Anti-priorities (deliberately NOT first-year work)

Penetration tests and red teaming before the foundations exist (CIS puts penetration testing at Control 18 for a reason) · threat hunting programme · SOAR platform selection · deception tech · Level 4 detection-as-code pipelines · custom threat intel platform. All valuable — all wasted if attempted before the 90-day foundations exist. The most expensive failure mode in new CDCs is buying Level 4 technology for a Level 1 organisation.

*Open CDC Framework (CC BY 4.0).*
