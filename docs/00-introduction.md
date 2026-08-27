# 00 — Introduction & Design Principles

## Purpose

This framework describes **what a Cyber Defence Center (CDC) must be able to do**, **how to build those capabilities from zero**, and **how to measure maturity over time**. It deliberately avoids naming commercial products: every capability can be met with open source, commercial, or hybrid tooling.

## Terminology

- **CDC (Cyber Defence Center)** — an organisational capability that governs, prevents, detects, responds to and recovers from cyber threats. We use CDC and SOC (Security Operations Center) interchangeably; "CDC" emphasises that the capability is broader than monitoring alone.
- **NIST CSF 2.0** — the NIST Cybersecurity Framework version 2.0 (February 2024), organised into six functions: Govern, Identify, Protect, Detect, Respond, Recover.
- **CIA triad** — Confidentiality, Integrity, Availability: the three classic security objectives that every control ultimately serves.
- **Essential / important entities** — the two categories of organisations in scope of the EU NIS2 Directive.

## Scope boundary: IT, not OT/telco

This framework is written for **enterprise IT** security operations. OT/ICS environments (where availability and physical safety dominate, and active scanning or host isolation can be hazardous) and telco core networks (separately regulated in most member states) require different technical approaches — do not apply the PROTECT/DETECT/RESPOND content or the platform playbooks to those domains unadapted. The governance and maturity concepts transfer; the technical guidance does not. See ABOUT.md and the roadmap's OT extension profile.

## Design principles

1. **Standards-first.** The backbone is NIST CSF 2.0. Detection engineering references MITRE ATT&CK. Incident handling references NIST SP 800-61 and FIRST/ENISA good practice. This maximises interoperability with auditors, regulators, and peer organisations.
2. **CIA as the design lens.** Every capability in this framework states which leg(s) of the CIA triad it primarily protects. If you cannot articulate what a control does for Confidentiality, Integrity or Availability, question whether you need it.
3. **EU-regulation aware.** Each function document contains an "EU regulatory hooks" section mapping capabilities to NIS2, DORA, GDPR and related obligations. The framework helps demonstrate compliance; it is not legal advice.
4. **People > Process > Technology, in that order.** Most SOC failures are organisational, not technical. Governance and staffing come before tooling in every build sequence.
5. **Maturity is incremental.** The framework defines four maturity levels (see [08-maturity-model.md](08-maturity-model.md)). Level 1 is achievable by a small team in months, not years.
6. **Vendor-neutral and open.** No product names in normative text. Community contributions of tooling examples belong in non-normative appendices.

## The build sequence (greenfield)

If you are building a CDC from the ground up, the recommended order is:

| Phase | Duration (indicative) | Focus | Framework docs |
|-------|----------------------|-------|----------------|
| 1. Mandate | 1–2 months | Charter, sponsorship, scope, budget, risk appetite | Govern |
| 2. Visibility | 2–4 months | Asset inventory, log sources, network visibility | Identify |
| 3. Foundation controls | 2–6 months | Identity, hardening, backup, segmentation | Protect |
| 4. Detection | 3–6 months | SIEM/log pipeline, first use cases, triage process | Detect |
| 5. Response | 2–4 months | IR plan, playbooks, exercises, reporting duties | Respond |
| 6. Resilience | 2–4 months | Recovery plans, lessons-learned loop, continuous improvement | Recover |

Phases overlap in practice; the ordering reflects dependencies (you cannot detect what you cannot see, and you cannot respond to what you cannot detect).

## Dependency markers: [GATE] / [HARD] / [SOFT]

A CDC delivers very little alone — and most stalled CDC programmes stall on another department, not on security work. To make that visible, every function document ends with an "External dependencies" table, and dependencies are classified consistently:

| Marker | Meaning | Handling rule |
|--------|---------|---------------|
| [GATE] | Gatekeeper — an external party holds formal decision authority (sign-off, approval, risk acceptance). The checkpoint is by design and cannot be worked around. | Pre-agree the decision criteria and a deputy, so the gate is fast at 03:00 — a gate without pre-agreed criteria becomes a hard block at the worst moment. |
| [HARD] | Hard block — the capability cannot be delivered without another team's action or delivery (access, implementation, data, operation). | Name the owning team in the charter interfaces, agree an SLA, and define the escalation path through GOVERN when the SLA slips. |
| [SOFT] | Soft block — external input improves quality or speed, but the CDC can proceed with a degraded result and retrofit. | Proceed, log the debt as an ID-7 improvement item, and revisit. |

Two rules of use: first, every [HARD] on the critical path of the 90-day plan (doc 09) needs a named counterpart and an executive sponsor aware of it before week 1 — chasing access rights is the most common silent killer of new CDC timelines. Second, [GATE] entries belong in the charter (authority §4 and interfaces §8) so the gatekeepers themselves have signed up to being gates.

## How each function document is structured

Every function document (01–06) follows the same layout:

1. **Objective** — what the function achieves.
2. **Core capabilities** — the concrete things your CDC must be able to do.
3. **CIA mapping** — which triad objectives each capability serves.
4. **Roles & staffing** — who does the work.
5. **Maturity criteria** — what Levels 1–4 look like for this function.
6. **EU regulatory hooks** — relevant NIS2/DORA/GDPR articles and ENISA guidance.
7. **External dependencies** — who outside the CDC this function depends on, marked [GATE]/[HARD]/[SOFT].
8. **Sources** — credited references for that document.

## Attribution note

This framework references and builds on the NIST Cybersecurity Framework 2.0, NIST Special Publications, ENISA publications, MITRE ATT&CK®, and FIRST resources. Full credits: [19-references.md](19-references.md).

*Open CDC Framework (OCDF) — CC BY 4.0. Credits: [19-references.md](19-references.md).*
