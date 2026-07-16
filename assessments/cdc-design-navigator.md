# CDC Design Navigator — Guiding Questions

> **How to use this:** work through each function's questions in a workshop (2–4 hours per function with the right people in the room). Every question lists *why it matters* and *where the framework helps*. If you can answer a question crisply and evidence it, move on. If the room goes quiet — you've found a design gap; log it as a backlog item. Answering all questions honestly gets a new CDC ~90% of the way to a sound design; the last 10% is your organisation's specifics.

**Legend:** ➜ = where to go in the framework · ⚠ = common failure this question prevents

---

## GOVERN — "Who owns this, and with what authority?"

| # | Question | Why it matters |
|---|----------|----------------|
| G1 | Who at executive level personally owns cyber risk — and do they know it? | NIS2 Art. 20 makes management accountable; an unnamed owner means no budget defence. ➜ 01-govern.md, GV-1 ⚠ "IT owns security" by default |
| G2 | What exactly is in scope: which legal entities, countries, networks, cloud tenants, OT? What is explicitly out — and who covers that? | Undefined scope becomes disputed scope during an incident. ➜ charter template §2 |
| G3 | May the CDC isolate a production system at 03:00 without waking anyone? Up to which tier? | Containment speed is decided here, years before the incident. ➜ charter §4 ⚠ response stalls awaiting permission |
| G4 | What is our risk appetite, stated per CIA objective and per crown-jewel service? | Without it, every trade-off is improvised. ➜ 07-cia-triad.md §1 |
| G5 | Which laws apply to which entity in which country — and who maintains that register? | Multi-country entities face different deadlines/channels per state. ➜ 17-eu-regulatory-landscape.md, docs/annexes/, regulatory selector |
| G6 | MSSP-operated, in-house tiered, or capability-based — decided on scored criteria or on hope? | This choice shapes every DETECT/RESPOND design decision after it. ➜ **11-operating-models.md** (decision criteria + what can never be outsourced), MSSP checklist template |
| G7 | How do we require, verify and enforce supplier security — contracts, monitoring, exit? | NIS2 Art. 21(2)(d); your suppliers are your attack surface. ➜ GV-6 |
| G8 | When did the board last train on cyber and join an exercise? | NIS2 Art. 20 training duty; also the fastest way to secure budget. ➜ RS-7 |
| G9 | What does the CDC report upward, how often, and does anyone act on it? | Reporting nobody acts on is theatre. ➜ metrics template |
| G10 | Who may accept a cyber risk, and where is that acceptance recorded? | Unrecorded acceptances resurface as "nobody told me". ➜ GV-2 |
| G11 | How many security tools do we run, how many consoles does one case take, and when did we last retire one? | Tool sprawl taxes every case and buries data in silos. ➜ 13-cdc-operations §5 |

## IDENTIFY — "What are we defending, against whom?"

| # | Question | Why it matters |
|---|----------|----------------|
| I1 | If ransomware hit tonight, which 5–10 services must survive or recover first — and does the business agree in writing? | Crown-jewel consensus drives everything downstream. ➜ ID-3 ⚠ IT's list ≠ business's list |
| I2 | What % of our assets do we actually know about — and how do we know that number? | You cannot defend the unknown; measure inventory accuracy, don't assert it. ➜ ID-1 |
| I3 | Where does personal and special-category data live, and who owns each store? | Drives GDPR breach scoping in minutes vs days. ➜ ID-2, GDPR Art. 30 records |
| I4 | Which threat actors and ATT&CK techniques realistically target *our* sector and footprint? | A written threat profile stops "defend against everything" paralysis. ➜ ID-5, ENISA Threat Landscape |
| I5 | What does our attack surface look like from the internet, right now? | Attackers enumerate it weekly; do it before they do. ➜ ID-4 |
| I6 | Which third parties could take our crown jewels down — and would we even be told? | Supplier dependency map + contractual notification duties. ➜ GV-6/ID-1 |
| I7 | How fast do we learn of a critical vulnerability in something we run — and who owns the clock? | Exploitation windows are now hours-to-days. ➜ ID-4, PR-5 |
| I8 | When we find a weakness (audit, pentest, incident), where does it go — and does it ever come back out as a fix? | An improvement backlog nobody drains is a risk register in denial. ➜ ID-7 |

## PROTECT — "What reduces the blast radius before anything happens?"

| # | Question | Why it matters |
|---|----------|----------------|
| P1 | Can a phished password alone still compromise us anywhere — VPN, email, admin panels, legacy apps? | Single-factor anywhere = front door open. ➜ PR-1 ⚠ "MFA everywhere except…" |
| P2 | How many people hold standing admin rights, and could that number shock the board? | Privilege sprawl converts any compromise into total compromise. ➜ PR-1 (PAM) |
| P3 | If ransomware encrypted everything tonight, do we hold a backup copy the attacker *provably couldn't reach* — and when did we last restore from it? | Untested/online-only backups fail exactly when needed. ➜ PR-7 ⚠ backups joined to the domain |
| P4 | Can a compromised laptop reach a domain controller, backup server, or OT network directly? | Segmentation is the cheapest blast-radius control. ➜ PR-6 |
| P5 | What is our patch SLA for actively exploited critical vulnerabilities — and did we hit it last quarter? | An SLA without measurement is a wish. ➜ PR-5 |
| P6 | Do new systems arrive hardened by default, or does security chase them afterwards? | Baseline-at-birth costs 1×; retrofit costs 10×. ➜ PR-4, PR-8 |
| P7 | Would our staff report the phish they clicked, or hide it? | Reporting culture beats click-rate metrics. ➜ PR-2 |
| P8 | Which protection controls does the CDC merely *assume* work — and which have we tested fire-for-effect? | Assumed controls are the ones attackers find disabled. ➜ Level 4 criteria, DE-6 |
| P9 | Can an unapproved binary or script execute on our critical servers today? | Application control is the cheapest ransomware circuit-breaker; servers first, audit mode first. ➜ PR-4 app control section |

## DETECT — "Would we notice, and how fast?"

| # | Question | Why it matters |
|---|----------|----------------|
| D1 | If an attacker logged in with a stolen password right now, which log would show it — and is that log actually flowing to us? | Identity telemetry is the highest-value source; verify flow, not intent. ➜ DE-1 priority list |
| D2 | Which of our crown jewels currently generate *zero* security telemetry? | Coverage gaps cluster exactly where impact is highest. ➜ DE-4 ⚠ cloud/SaaS blind spots |
| D3 | For each detection in production: when did it last fire in a test? | Silently-broken rules are worse than no rules — they buy false confidence. ➜ DE-6 |
| D4 | Does our use-case portfolio match our threat profile — or are we detecting yesterday's threats? | Balance C/I/A coverage against ID-5's profile. ➜ DE-2, 07-cia-triad §3 |
| D5 | What happens to an alert at 02:00 on a Sunday — concretely, minute by minute? | Walk the path; every undefined step is response time lost. ➜ DE-3, staffing model |
| D6 | Can our analysts see asset criticality and identity context *inside* the alert, or must they hunt for it? | Enrichment is triage speed. ➜ DE-3 |
| D7 | Could an attacker with admin rights delete or alter the logs we'd need? | Log integrity is an Integrity objective in itself. ➜ DE-1, DE-7 |
| D8 | When did we last go *looking* for an intruder rather than waiting for an alert? | Hunting finds what detections miss and seeds new detections. ➜ DE-5 |
| D9 | What is our measured MTTD on real incidents — and is it trending the right way? | You cannot improve what you don't measure. ➜ metrics template |
| D10 | Who owns the SIEM's hardware, OS and application respectively — and if it's cloud-hosted, who decided which data may be shipped there? | An unowned platform decays; unclassified telemetry export is an uncontrolled data transfer. ➜ 04-detect.md "Owning the SIEM platform" |

## RESPOND — "When it happens, does the machine run?"

| # | Question | Why it matters |
|---|----------|----------------|
| R1 | Who is the incident manager for a P1 tonight, and does that person know it? | Named humans beat documented roles. ➜ IR plan template §2 |
| R2 | Can we technically isolate any endpoint or server within 15 minutes — and legally/organisationally within the same 15? | Both halves must be true; test each. ➜ RS-4, charter §4 |
| R3 | For our top 5 likely incidents, could a competent analyst execute the playbook alone at 03:00? | Playbooks are written for the worst night, not the best day. ➜ RS-2, playbooks/ |
| R4 | Who decides — and how fast — whether an incident is NIS2-reportable, GDPR-notifiable, or both? Have we drilled the 24 h clock? | The early-warning clock is shorter than most escalation chains. ➜ RS-5, IR plan §4, national annex ⚠ deadline discovered during the incident |
| R5 | If email and chat are compromised, how does the response team talk? | Adversaries read your incident channel if it's in the environment they own. ➜ IR plan §5 |
| R6 | Can we preserve evidence to a standard that survives court or regulator scrutiny — hashing, chain of custody, imaging? | Sloppy first hours forecloses legal options forever. ➜ RS-3, platform playbooks |
| R7 | At what point does a security incident become an organisational crisis, and who pulls that lever? | The threshold must pre-exist the incident. ➜ RS-6 |
| R8 | When did management last sit in an exercise and make a real (simulated) trade-off decision? | Executives who've practised decide in minutes, not hours. ➜ RS-7 |

## RECOVER — "Can we come back clean, and do we learn?"

| # | Question | Why it matters |
|---|----------|----------------|
| C1 | For each crown jewel: what are the agreed RTO/RPO — and have we ever *measured* recovery against them? | Unmeasured RTOs are fiction with a signature. ➜ RC-1 |
| C2 | Before reconnecting a restored system, how do we prove it's clean — who signs, against what checklist? | Restoring a backdoored image is re-infection with better uptime. ➜ RC-2 ⚠ Integrity before Availability |
| C3 | Is credential/secret rotation a standard, scripted recovery step — or an afterthought? | Attackers keep the keys unless you change the locks. ➜ RC-2 |
| C4 | Could we rebuild our most critical service from code/config + data backups alone, with the original servers a total loss? | Ransomware-scale recovery is a rebuild problem, not a restore problem. ➜ RC-1/RC-3 |
| C5 | Who owns honest status communication during a multi-day outage — internally, to customers, to authorities (the 1-month final report)? | Recovery comms failures cost more trust than the incident. ➜ RC-4 |
| C6 | Name three concrete controls or detections that exist because of a past incident. | If you can't, the lessons-learned loop is decorative. ➜ RC-5 ⚠ Level 4 litmus test |
| C7 | Do our recovery plans and the enterprise BCM plan describe the same reality — and when did they last exercise together? | Two uncoordinated plans equal zero plans. ➜ RC-6 |

---

## Turning answers into a design

1. Run all six workshops; log every weak answer as a backlog item tagged with its capability ID (e.g., `DE-4`).
2. Score yourself with [maturity-self-assessment.md](maturity-self-assessment.md) — the navigator answers *are* much of your evidence.
3. Prioritise: fix GOVERN gaps first (they block everything), then the cheapest blast-radius items (P1, P3, P4), then coverage (D1, D2).
4. Set level targets per function (see [../docs/08-maturity-model.md](../docs/08-maturity-model.md)) and reassess in 6–12 months.

*Open CDC Framework (CC BY 4.0).*
