# MSSP Requirements Checklist — Template

> Use before signing (or renewing) a managed detection/monitoring contract (Model A or hybrid — see docs/11-operating-models.md). Every unchecked box is a negotiation point or an accepted risk to record in GOVERN.

## Data, privacy & residency
- [ ] GDPR processor agreement (Art. 28) in place; sub-processors listed and change-notified
- [ ] Telemetry storage location(s) named; EU residency where required; transfer mechanism documented
- [ ] **We own the raw logs** — continuous copy or guaranteed full export in an open format
- [ ] Retention periods match our policy and legal duties; deletion on exit certified

## Detection quality & transparency
- [ ] Visibility into deployed detection logic (or at minimum: use-case list mapped to MITRE ATT&CK)
- [ ] Our threat profile drives custom use cases; who writes them, who owns them at exit?
- [ ] Detection validation evidence (how do they prove rules fire?) shared at least quarterly
- [ ] Coverage reporting: ATT&CK techniques and our log-source scope, not just alert counts

## Service levels that matter
- [ ] MTTA/MTTN commitments per severity (e.g., P1 notified ≤ 15 min, human-verified)
- [ ] Notification ≤ [X] hours guaranteed — leaves us margin inside the NIS2 24 h early-warning clock
- [ ] Escalation path: named channel, 24/7, tested quarterly; out-of-band option exists
- [ ] False-positive rate and tuning cadence reported; we can request suppression reviews
- [ ] Right to audit / request evidence; annual service review with improvement actions

## Response boundaries
- [ ] Written matrix: what MSSP may do autonomously (block IOC?) vs recommend-only (isolate host? never on crown jewels without our approval — mirror charter §4)
- [ ] Their actions logged to us in near-real-time; joint playbooks for top 5 scenarios; annual joint exercise
- [ ] DFIR: included or retainer? Response time to on-site/remote forensics stated

## Regulatory fit
- [ ] Contract acknowledges OUR statutory reporting duties and commits to timely incident data supporting NIS2/GDPR/DORA notifications
- [ ] MSSP is itself in NIS2 scope as a managed (security) service provider — ask for their compliance posture and incident history
- [ ] DORA entities: contract meets Art. 28+ ICT third-party requirements (exit strategy, audit rights, register of information)

## Exit & portability
- [ ] Transition-out clause: duration, cooperation duties, knowledge transfer, tuning/runbook handover
- [ ] Custom detections and enrichment logic are OUR IP or licensed for continued use
- [ ] Trial exit test (data export) executed within first year

## Scoring the relationship (feed the KPI catalogue)
Track quarterly: notification SLA adherence · validated-detection coverage vs our profile · FP rate trend · escalation drill results · improvement actions closed.

---
*Template from the Open CDC Framework (CC BY 4.0).*
