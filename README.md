# Open CDC Framework (OCDF)

**An open source framework for building and maturing Security Operations Centers (SOC) and Cyber Defence Centers (CDC) across the European Union.**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Status](https://img.shields.io/badge/status-v0.1--rc1-blue)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen)

---

> **Scope:** this framework targets **enterprise IT environments** (endpoints, servers, identity, cloud/SaaS). It is **not** designed for OT/ICS, telco core networks, or classified environments — see [ABOUT.md](ABOUT.md) for the reasoning and the roadmap for a future OT profile.

## Why this framework exists

European organisations face a unique combination of pressures: a rapidly evolving threat landscape, a dense regulatory environment (NIS2, DORA, GDPR, CRA), and a persistent shortage of skilled security personnel. Many teams are asked to "build a SOC" with little guidance on where to start, or to "mature" an existing capability without a shared yardstick for what maturity means.

The Open CDC Framework provides a **free, vendor-neutral, community-maintained blueprint** for:

1. **Building** a Cyber Defence Center from the ground up.
2. **Maturing** an existing SOC/CDC against a structured maturity model.
3. **Aligning** operations with the NIST Cybersecurity Framework (CSF) 2.0 and EU regulatory obligations.
4. **Anchoring** every capability in the CIA triad — Confidentiality, Integrity, and Availability.

## Framework structure

The framework is organised around the **six functions of NIST CSF 2.0**, each mapped to the CIA triad and to EU regulatory requirements:

| # | Function | Question it answers | Doc |
|---|----------|--------------------|-----|
| 0 | Introduction & Design Principles | How do I use this framework? | [docs/00-introduction.md](docs/00-introduction.md) |
| 1 | **GOVERN** | Who owns cyber risk, and how are decisions made? | [docs/01-govern.md](docs/01-govern.md) |
| 2 | **IDENTIFY** | What are we defending, and what threatens it? | [docs/02-identify.md](docs/02-identify.md) |
| 3 | **PROTECT** | How do we reduce the likelihood and impact of incidents? | [docs/03-protect.md](docs/03-protect.md) |
| 4 | **DETECT** | How do we find adversary activity quickly? | [docs/04-detect.md](docs/04-detect.md) |
| 5 | **RESPOND** | How do we contain and eradicate threats? | [docs/05-respond.md](docs/05-respond.md) |
| 6 | **RECOVER** | How do we restore services and learn? | [docs/06-recover.md](docs/06-recover.md) |

Cross-cutting documents, in reading order:

| # | Document | What it gives you |
|---|----------|-------------------|
| 07 | [CIA Triad as a Design Lens](docs/07-cia-triad.md) | How Confidentiality, Integrity and Availability drive every CDC decision |
| 08 | [Maturity Model](docs/08-maturity-model.md) | Four maturity levels with concrete criteria per function |
| 09 | [Start Here: Prioritisation](docs/09-start-here.md) | The first 90 days and first year, in order, with exit criteria and anti-priorities |
| 10 | [Implementation Tiers](docs/10-tiers.md) | Essential / Standard / Advanced overlay: which capabilities apply at your size |
| 11 | [Operating Models](docs/11-operating-models.md) | MSSP vs tiered vs capability-based (and shared/community CDCs): trade-offs and what can never be outsourced |
| 12 | [Roles & Competences](docs/12-roles-and-competences.md) | CDC roles, skills matrix, career paths and hiring, built on the ENISA ECSF |
| 13 | [Running the CDC](docs/13-cdc-operations.md) | The loops that keep a live CDC improving: tuning, detection-as-code, team development, automation guardrails, tool discipline |
| 14 | [Deep Dive: Detection-as-Code](docs/14-detection-as-code-deep-dive.md) | Repo layout, rule YAML anatomy, CI/CD pipeline, honest ATT&CK coverage scoring (Advanced tier) |
| 15 | [Deep Dive: CTI Capability](docs/15-cti-deep-dive.md) | Strategic/operational/tactical intelligence and the interfaces that feed the CDC (Advanced tier) |
| 16 | [CSIRT Community Layer](docs/16-csirt-community.md) | RFC 2350, TF-CSIRT/FIRST, SIM3 crosswalk for certification, living documentation |
| 17 | [EU Regulatory Landscape](docs/17-eu-regulatory-landscape.md) | NIS2, GDPR, DORA, CRA, CER and ENISA mapped to CDC capabilities |
| 18 | [CIS Controls Crosswalk](docs/18-cis-controls-crosswalk.md) | All 18 CIS Controls with concrete actions per control |
| 19 | [References & Credits](docs/19-references.md) | Every source used by this framework |

Practical assets:

- [`templates/`](templates/) — charter, IR plan, detection use case, KPI catalogue, job description (ECSF), MSSP requirements checklist, containment action catalogue, controls register, annual operating calendar.
- [`playbooks/`](playbooks/) — IR + digital forensics playbooks for Windows 11 laptops, macOS laptops, and Linux (RHEL-class) servers, plus Microsoft/CISA baseline references.
- [`assessments/`](assessments/) — the Design Navigator (guiding questions per function) and the maturity self-assessment.
- [`tools/regulatory-profile.html`](tools/regulatory-profile.html) — interactive law selector: tick the laws that apply (EU instruments + all 27 member states) and the references show/hide to match. Host via GitHub Pages or open locally.
- [`docs/annexes/`](docs/annexes/) — national annexes for all 27 EU member states (status verified July 2026).

## Who is this for?

- **CISOs and CDC/SOC directors** planning a new capability or a maturity programme.
- **SOC managers and team leads** looking for structure, templates, and metrics.
- **Public sector and critical infrastructure teams** in scope of NIS2 or DORA.
- **SMEs** that need a pragmatic, low-cost starting point.

## How to use it

1. **Read** [docs/00-introduction.md](docs/00-introduction.md), then [docs/09-start-here.md](docs/09-start-here.md) for the order of work, and pick your tier in [docs/10-tiers.md](docs/10-tiers.md).
2. **Navigate** the design questions in [assessments/cdc-design-navigator.md](assessments/cdc-design-navigator.md) — six workshops that surface your gaps.
3. **Assess** your current state with [assessments/maturity-self-assessment.md](assessments/maturity-self-assessment.md).
4. **Plan** using the per-function documents: each contains capabilities, CIA mapping, maturity criteria, and EU regulatory hooks.
5. **Operationalise** with the templates and playbooks; pick your country annex and set your legal profile in the selector tool.
6. **Reassess** every 6–12 months and track progress with the KPI template.

## About the author & project

Written by a practitioner who spent a decade in the field — the last four years building and running a 24/7/365 CDC — and fell into most of the holes this framework now warns about. The full story, and what is deliberately out of scope: [ABOUT.md](ABOUT.md).

## Contributing

This is a community project — contributions, translations, and national-regulation mappings are very welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Documentation is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).

This framework builds on publicly available works by NIST, ENISA, MITRE, FIRST and others. It is **not** endorsed by or affiliated with any of these organisations. All sources are credited in [docs/19-references.md](docs/19-references.md).
