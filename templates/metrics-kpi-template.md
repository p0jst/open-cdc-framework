# CDC Metrics & KPI Catalogue — Template

> Related capabilities: GV-7, DE-4, RS-*, RC-5. Pick **few metrics you will act on** over many you will only report. Every metric below lists the decision it should drive — if you wouldn't change anything based on it, don't collect it.

## Governance & coverage (GOVERN / IDENTIFY)

| Metric | Definition | Target (example) | Decision it drives |
|--------|-----------|------------------|--------------------|
| Asset inventory accuracy | % sampled assets correctly recorded | > 90% | Invest in discovery/CMDB reconciliation |
| Log source coverage | % of priority-1/2 sources onboarded (per docs/04 priority list) | 100% P1, > 90% P2 | Onboarding backlog priority |
| Maturity score trend | OCDF level per function, assessed annually | +1 level on 2 weakest functions/yr | Budget allocation |
| Training completion | % staff / % management completing role-based training | > 95% | NIS2 Art. 20 evidence; awareness focus |

## Detection (DETECT)

| Metric | Definition | Target (example) | Decision it drives |
|--------|-----------|------------------|--------------------|
| MTTD | Median time from first malicious activity to detection (measured per confirmed incident) | Trend ↓ | Detection engineering priorities |
| ATT&CK coverage | % of threat-profile techniques with ≥1 validated detection | > 70% of profile | Use-case backlog |
| Detection validation rate | % production detections tested (fired) in last 12 months | 100% | Purple-team scheduling |
| False-positive rate | FP / total alerts per use case | Per-UC threshold | Tuning / retirement |
| Triage SLA adherence | % alerts acknowledged within severity SLA | > 95% | Staffing model |

## Response (RESPOND)

| Metric | Definition | Target (example) | Decision it drives |
|--------|-----------|------------------|--------------------|
| MTTC | Median time detection → containment (P1/P2) | Trend ↓ | Containment automation, authority gaps |
| Statutory reporting timeliness | % notifications within legal deadline (NIS2 24h / GDPR 72h / DORA) | 100% | Reporting drill frequency |
| Playbook coverage | % of P1/P2 incidents handled with an existing playbook | > 80% | Playbook backlog |
| Exercise cadence | Exercises held vs. planned (incl. management participation) | 100% | Governance escalation |

## Recovery & learning (RECOVER)

| Metric | Definition | Target (example) | Decision it drives |
|--------|-----------|------------------|--------------------|
| Restore test success | % crown-jewel services with successful restore test in 12 months | 100% | Backup architecture investment |
| RTO attainment | Measured recovery time vs. agreed RTO in tests/incidents | 100% within RTO | DR investment |
| Lessons-learned closure | % post-incident actions closed within due date | > 90% | Improvement-loop health (Level 4 indicator) |

## Anti-patterns (do not use as KPIs)

- **Alert volume** ("we handled 40,000 alerts") — rewards noise.
- **Blocked attacks count** from perimeter devices — unfalsifiable vanity metric.
- **Tickets closed per analyst** — incentivises shallow triage.

## Reporting cadence

- Operational dashboard: weekly, CDC internal.
- Management report: monthly — incidents, SLA, coverage deltas.
- Executive/board report: quarterly — maturity trend, top risks, statutory compliance posture.

---
*Template from the Open CDC Framework (CC BY 4.0).*
