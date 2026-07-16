# 15 — Deep Dive: Building a CTI Capability That Feeds the CDC (Advanced tier)

> Threat intelligence fails in one of two ways: it becomes a feed of indicators nobody contextualises, or a stream of elegant reports nobody operationalises. This document describes a CTI function whose explicit job is to make the rest of the CDC better — detection engineering, hunting, vulnerability management, incident response and governance. Audience: S/A-tier teams standing up or professionalising CTI (E-tier: consume your national CSIRT and sector ISAC, and skip to §6).

## 1. The three levels — and who each one serves

Definitions vary across the industry; fix yours in writing. This framework uses:

| Level | Time horizon | Core question | Primary consumers | Typical products |
|-------|--------------|---------------|-------------------|------------------|
| Strategic | Quarters–years | Which threats matter to us, and is that changing? | Executive management, CISO, GOVERN | Threat profile, annual/quarterly threat assessment, risk-register input |
| Operational | Weeks–months | Which actors and campaigns are active against our sector, and how do they operate? | CDC leadership, detection engineering, hunting, vulnerability mgmt | Actor cards, campaign analyses, TTP change reports, hunt hypotheses |
| Tactical | Hours–days | What observable artefacts should we detect/block right now? | Analysts, platforms (SIEM/EDR/mail/proxy), IR | Enriched indicators with context and expiry, detection opportunities, active-exploitation alerts |

The levels form a loop: strategic sets priorities, operational translates them into adversary behaviour, tactical grounds them in observables — and what tactical/operational work uncovers flows back up to revise the strategic picture.

## 2. Requirements first: PIRs

CTI without requirements is a newsfeed. Start every cycle from Priority Intelligence Requirements — questions leadership and the CDC actually need answered, e.g.: "Which ransomware groups currently target mid-size EU [sector] organisations, and what initial access do they use?" · "Are our top suppliers being targeted?" · "Which of our internet-facing technologies are being actively exploited?" Keep 5–10 PIRs, owned by named stakeholders, reviewed quarterly in GOVERN. Every product the CTI function ships must trace to a PIR — if it doesn't, either the product or the PIR list is wrong.

## 3. Collection plan (mapped to PIRs)

| Source class | Examples | Feeds level |
|--------------|----------|-------------|
| National & EU | National CSIRT advisories, ENISA Threat Landscape, CERT-EU | All |
| Sector | Sector CSIRT / ISAC sharing (often the highest-value source; see doc 16) | Operational/Tactical |
| Open source | Vendor research blogs, ATT&CK group/software entries, exploitation trackers (e.g., CISA KEV) | Operational/Tactical |
| Sharing platforms | MISP-class platforms with community feeds, TLP-governed | Tactical |
| Internal (underrated) | Your own incidents, hunt findings, honeypot/canary hits, phishing reports | All — the only intel guaranteed relevant |
| Commercial (optional) | Finished intel/actor tracking subscriptions | Strategic/Operational |

Rate each source annually: did it contribute to a PIR answer, a detection, or a decision? Cut what didn't.

## 4. Production and dissemination discipline

- Separate facts from assessment; use estimative language ("we assess with moderate confidence…") and state what would change your mind.
- Every product ends with "so what": recommended actions per consumer (detect X, hunt Y, patch Z, brief board on W).
- Right-size the format: an actor card is one page; a tactical alert is five lines with indicators attached; the strategic assessment is the only long document you ship.
- TLP 2.0 on everything shared; sharing back to the community is part of the job (doc 16 §2).
- Track RFIs (requests for information) as tickets with deadlines — the RFI queue is how the rest of the CDC pulls intel, and its response time is a CTI KPI.

## 5. The threat profile and actor cards (the strategic backbone)

The threat profile (capability ID-5) is CTI's anchor product. Structure:

1. Organisational exposure: sector(s), geography, crown jewels, technologies, suppliers, public profile.
2. Relevant threat categories with reasoning: e.g., financially-motivated ransomware (high — sector-wide), sector espionage (moderate — reasoned), hacktivism (situational), insider (baseline).
3. Named actors/groups per category — each with an actor card: motivation · targeting logic · initial access TTPs · post-compromise TTPs · relevant ATT&CK technique list · known tooling · recent activity · what we can/cannot detect today (honest, from the coverage layer in doc 14 §4).
4. Top-N technique list: the union of the actor cards' techniques, ranked by frequency × your exposure — this list IS the scope for ATT&CK coverage scoring and the detection backlog's priority order.
5. Review: quarterly light refresh, annual full revision; changes are communicated as a delta briefing ("what changed and what we're doing about it"), not a re-read.

## 6. The interfaces: how CTI feeds the rest of the CDC

This is where most CTI programmes fail — build these as standing, ticketed workflows, not hallway conversations:

| Interface | Mechanism | Cadence |
|-----------|-----------|---------|
| → Detection engineering | "Detection opportunity" tickets: technique, adversary procedure, log source, suggested logic sketch; engineering triages into the use-case backlog (doc 14). CTI reviews the coverage layer and flags profile techniques stuck at level 0–1. | Weekly |
| → Threat hunting | Hunt hypotheses ("threat hints"): actor X uses procedure Y; we have telemetry Z; hypothesis and suggested data window. Hunting returns findings, which become detections and intel. | Per hunt cycle |
| → Vulnerability management | Exploitation-aware prioritisation: profile actors' exploited CVEs + known-exploited catalogues override raw CVSS ordering; emergency-patch trigger on active exploitation of internet-facing tech. | Continuous |
| → Incident response | Enrichment on demand (RFI), actor context during incidents, and post-incident: every closed P1/P2 gets a CTI debrief — what did we learn about the adversary, and what does it change? | Per incident |
| → Triage (tactical) | Curated indicators pushed to platforms with context, confidence and expiry; stale indicators are pruned automatically (indicator sets that only grow become noise generators). | Daily/automated |
| → GOVERN | Quarterly threat briefing tied to the risk register and the coverage-vs-profile view; annual input to budget with "top risks vs. current capability" framing. | Quarterly |

Feedback loop (mandatory): every consumer reports back what was used and what was noise. CTI that never hears "that indicator set was garbage" cannot improve.

## 7. Staffing reality

One person can run PIR-driven operational/tactical CTI part-time at S-tier if §6's interfaces are ticketed and the sector ISAC does heavy lifting; a dedicated analyst (ECSF: Cyber Threat Intelligence Specialist, doc 12) is the A-tier baseline; strategic products can be quarterly even when tactical work is daily. Do not hire a CTI team before the detection and hunting consumers exist — intelligence without consumers is journalism.

## 8. KPIs

% products traceable to a PIR · detection opportunities shipped → deployed rate · hunt hypotheses issued → findings rate · RFI median response time · indicator precision (alerts from CTI indicators: TP rate) · coverage delta on profile techniques quarter-over-quarter · consumer feedback score.

## Sources

- ENISA Threat Landscape (annual). https://www.enisa.europa.eu
- MITRE ATT&CK® Groups/Software knowledge base. https://attack.mitre.org
- FIRST, *Traffic Light Protocol 2.0*; CISA Known Exploited Vulnerabilities catalog. https://www.first.org/tlp/ · https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- MISP Project (open source threat sharing platform). https://www.misp-project.org

*Open CDC Framework (CC BY 4.0).*
