# 11 — Choosing Your Operating Model

> **This is a decision document.** Before designing anything in DETECT or RESPOND, the organisation must choose how 24/7/365 monitoring and alerting will be operated. There are three archetypes — each with real trade-offs. Related: GOVERN GV-5, navigator question G6, charter template §3/§6.

## The three archetypes

### Model A — MSSP-operated ("telemetry out, alerts in")
Your telemetry (identity, endpoint, network, cloud) is forwarded to a Managed Security Service Provider who runs 24/7/365 eyes-on-glass triage and alerts you on qualified incidents. You retain a small internal function (often 1–3 FTE) for governance, escalation reception, and response coordination.

| Pros | Cons |
|------|------|
| 24/7 from day one, without hiring 8–12 FTE | Analysts lack your business context — expect generic triage on your crown jewels |
| Predictable OPEX; scales up/down contractually | Multi-tenant attention: your P3 competes with another client's P1 |
| Access to scarce skills (DFIR, hunting) you can't retain solo | Telemetry leaves the organisation — data residency, GDPR processor terms and log ownership must be contractually nailed down |
| Mature process, tooling and threat intel included | Detection logic is often opaque — you can't measure ATT&CK coverage you can't see |
| Fastest route to NIS2 24 h reporting readiness | **Accountability never transfers:** NIS2 Art. 20 liability, risk acceptance and statutory reporting remain yours regardless of contract |
| | Exit is hard: proprietary formats and lost tuning history create lock-in |

**Fits:** SMEs and important entities without security hiring power; organisations needing 24/7 *now*.

### Model B — In-house tiered SOC (Tier 1 → 2 → 3)
The classical pyramid: Tier 1 does front-line triage on shift, escalates to Tier 2 investigators, with Tier 3 (hunt/DFIR/engineering) behind them. Sustained 24/7 in-house realistically requires **8–12 FTE minimum** for the shift line alone.

| Pros | Cons |
|------|------|
| Full business context in every triage decision | High fixed cost; hard business case below large-enterprise scale |
| Full control of detection logic, coverage measurement, and data | Tier 1 burnout/attrition is the classic failure mode — repetitive work, night shifts, EU talent shortage |
| Clear entry-level career ladder (helps recruitment) | Tiers create hand-off friction and "ticket tennis"; knowledge concentrates at the top |
| Telemetry never leaves the organisation | Slow to build: 12–24 months to a functioning 24/7 line |
| Institutional knowledge compounds internally | Quality depends on runbooks — weak runbooks turn Tier 1 into an expensive routing layer |

**Fits:** large/essential entities, high-confidentiality sectors, organisations at Level 3+ ambitions with hiring power.

### Model C — In-house capability-based ("tierless")
No tiers: analysts own alerts end-to-end (detect → investigate → contain), organised by *capability* (detection engineering, hunting, response) rather than seniority layers. Heavy investment in automation/SOAR replaces the Tier 1 filter. Often run 8×5 + on-call, or follow-the-sun in multinationals.

| Pros | Cons |
|------|------|
| Richer work → better retention than a Tier 1 line | Requires all-senior hiring — expensive and scarce; no junior entry ramp unless you deliberately build one |
| No hand-off losses; ownership drives quality | 24/7 coverage is the hard problem: on-call fatigue or follow-the-sun complexity |
| Automation-first mindset compounds efficiency | Demands mature engineering culture (detection-as-code, SOAR) from day one |
| Detection engineering and response cross-pollinate naturally | Small teams are fragile: two resignations can break coverage |

**Fits:** engineering-strong organisations, cloud-native environments, teams of ~5–8 senior FTE that accept on-call rather than shift coverage.

## Hybrid patterns (most common EU reality)

- **A+C:** MSSP runs the 24/7 night/weekend watch; the internal capability-based team owns detection engineering, business-context triage in daytime, and all response decisions. Often the best cost/quality point.
- **A+B:** MSSP as Tier 1, internal Tier 2/3. Works only if the escalation interface is drilled and the MSSP's output quality is measured.
- **Follow-the-sun (C):** for multinationals with 3+ regions — coverage without night shifts, at coordination cost.
- **Existing 24/7 operations as first line:** if the organisation already runs a 24/7 NOC/operations desk, train it to receive security alerts out of hours and wake the CDC's on-duty officer against defined criteria. Cheap night coverage without a security night shift — but invest in crisp escalation criteria and drill them, or the desk becomes a bottleneck.
- **Shared / community CDC (Model D):** one CDC serving several constituent organisations (shared service centres, sector cooperatives, municipal partnerships — a common European pattern). Combines Model B/C internally with an MSSP-like *external* interface per constituent: it therefore needs both the in-house discipline of B/C **and** the contractual clarity of Model A — per-constituent containment mandates (see the containment action catalogue template), per-constituent reporting/SLAs, strict data separation between constituents, and an RFC 2350-style public service description. Statutory reporting duties remain with each constituent entity.

## What can NEVER be outsourced (any model)

1. **Risk acceptance and management accountability** — NIS2 Art. 20 liability sits with your management, full stop.
2. **Containment authority over crown jewels** — the MSSP may recommend; who may isolate your production is a charter §4 decision.
3. **Statutory reporting** — the 24 h early warning is filed by *you*; an MSSP SLA of "notify within 4 h" already spent a sixth of your clock.
4. **The regulatory applicability register and this framework's GOVERN function.**

## Decision criteria — score each 1–5 and discuss

| Criterion | Pushes toward |
|-----------|---------------|
| Can we realistically hire and retain 8+ security FTE in our market? | No → A or C-hybrid |
| Is our data too sensitive to leave the organisation (or hard under GDPR/data residency)? | Yes → B or C |
| Do we need 24/7 within 6 months? | Yes → A (possibly as transitional) |
| Is deep business context critical to triage (bespoke apps, OT-adjacent IT, fraud)? | Yes → B or C |
| Do we have engineering culture (IaC, CI/CD) to build on? | Yes → C |
| Budget model: OPEX-predictable vs headcount? | OPEX → A |
| Exit strategy: could we insource in 3 years if we start with A? | Contract for it now (log ownership, rule portability, transition clause) |

**Record the decision** in the CDC charter (§3 services, §6 resourcing) with rationale and a review date — operating models are 3-year decisions, not permanent ones. If choosing Model A, use the [MSSP requirements checklist](../templates/mssp-requirements-checklist.md) before signing anything.

## Maturity note

The maturity model applies to **outcomes, not employment contracts**: with an MSSP you still score DETECT on *measured* coverage, validation and MTTD — which means your contract must give you visibility into detection logic and metrics. If it doesn't, your maturity ceiling is Level 2 by construction.

## Sources
- MITRE, *11 Strategies of a World-Class Cybersecurity Operations Center*, 2nd ed. (sourcing and tiering discussion).
- NIST CSF 2.0 (GV.SC — cybersecurity supply chain risk management).
- Directive (EU) 2022/2555 (NIS2) Art. 20–21, 23.

*Open CDC Framework (CC BY 4.0).*
