## Why this framework exists

I have worked numerous years with critical infrastructure in cyber security. I started where many readers of this framework are now: as one of few analysts in a large organisation, spending most of the time on reactive firefighting with little room to address root causes. After spending two years as the lead for DFIR I took over as manager.  and over the following eighteen months the team developed from that starting point into a process-driven Cyber Defence Center with 24/7/365 in-house monitoring, organised as a capability-based (tierless) SOC rather than a tiered one — analysts own their cases end-to-end. The trade-offs behind that choice are the ones described in [docs/11-operating-models.md](docs/11-operating-models.md), Model C.

I have also served as both main and secondary sponsor in SIM3 assessments for national and international CSIRT teams pursuing TF-CSIRT certifications. Working on the sponsor side of maturity assessments across different teams shaped this framework's emphasis on living documentation, independent verification, and evidence over assertion (see [docs/16-csirt-community.md](docs/16-csirt-community.md)).

Along the way I encountered most of the problems this framework now addresses. Among them:

- as three analysts we treated firefighting as the normal state; the underlying problem was not workload but that no one had the mandate to pause triage long enough to fix root causes
- we acquired technology before we had the mandate, and spent a year establishing authority we should have had in writing from the start
- we onboarded log sources by what was easy rather than by detection value, and paid for volume that taught us very little
- and many others..

Each of these was avoidable with the kind of structured, practitioner-written guide I was looking for at the time and could not find. This project is an attempt to write it, and to make it freely available so other teams in mainly Europe do not have to learn the same lessons the painful way.

## Who I am

- Frederik B. Krogsgaard
- Senior Manager, Norlys Cyber Defence Center
- Certifications: SANS LDR553 Cyber Incident Management, LDR551 Building and Leading Security Operations Centers, FOR500 Windows Forensics, MITRE Application of the MITRE ATT&CK Framework, Investigation Theory, Effective Information Security Writing, Kusto Query Language (KQL) for Security Analyst and many, many more...
- https://www.linkedin.com/in/frederikbogeskov/

This is a personal, community-driven project. It is not affiliated with, endorsed by, or the position of my employer, nor of NIST, ENISA, MITRE, or any authority referenced in it.

## What this project is — and is not

In scope: building and maturing a CDC/SOC for enterprise IT environments — endpoints, servers, identity, cloud/SaaS, enterprise networks — for organisations mainly across the EU. This is not limited to EU, but my experience and knowledge of building SOC/CDC outside of the EU is limited.

Explicitly out of scope (for now):

- OT/ICS environments (industrial control systems, SCADA, building automation). OT monitoring, safety-first response and the Purdue-model realities differ fundamentally from IT — applying IT playbooks to OT can be dangerous. An OT extension profile is on the [roadmap](ROADMAP.md).
- Telco core networks (signalling, RAN, lawful intercept environments) — regulated separately in most member states and operationally distinct.
- Defence/classified environments and other regimes with their own mandatory frameworks.

If you work in those domains, the GOVERN and maturity-model thinking still transfers — but treat the technical content (PROTECT/DETECT/RESPOND playbooks) as IT-specific.

## How you can help

Corrections, national annex updates, translations, and above all your own pitfalls — see [CONTRIBUTING.md](CONTRIBUTING.md). If this framework spares your team one of the mistakes above, it has done its job.

Frederik B. Krogsgaard, 2026
