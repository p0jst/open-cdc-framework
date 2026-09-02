# Containment Action Catalogue — Template

> The charter (§4) states *what* the CDC may do; this catalogue makes it operational: one row per concrete containment action, with its enforcement point, automation status, and whether the mandate is pre-agreed or requires per-case approval. Review at least semi-annually (tie to a control) — stale mandates are discovered at 03:00.

| ID | Action | Enforcement point | Automated? | Pre-mandated? | Requires stakeholder interaction? | Notes / limits |
|----|--------|-------------------|------------|---------------|-----------------------------------|----------------|
| CON-01 | Block domain | Proxy / DNS filtering | ☐ | ☐ | ☐ | |
| CON-02 | Block domain (sinkhole) | DNS | ☐ | ☐ | ☐ | |
| CON-03 | Block IP | Perimeter firewall | ☐ | ☐ | ☐ | |
| CON-04 | Block file hash | EDR / AV | ☐ | ☐ | ☐ | |
| CON-05 | Isolate endpoint | EDR | ☐ | ☐ | ☐ | e.g., workstations pre-mandated; servers per tier |
| CON-06 | Isolate server (tier ≥ X) | EDR / hypervisor / switch | ☐ | ☐ | ☑ typically | Crown jewels: approval per charter §4 |
| CON-07 | Disable / lock user account | Directory / IdP | ☐ | ☐ | ☐ | Pair with session/token revocation |
| CON-08 | Revoke sessions & refresh tokens | IdP / cloud | ☐ | ☐ | ☐ | |
| CON-09 | Block mail sender / recall mail | Mail gateway / mail platform | ☐ | ☐ | ☐ | |
| CON-10 | Disable service account / rotate secret | Secrets mgmt / directory | ☐ | ☐ | ☑ typically | Coordinate with service owner |
| CON-11 | Cut external connectivity — deny-all at the perimeter | Perimeter firewall | ☐ | ☐ | ☑ typically | Estate- or site-wide Availability impact; approval per charter §4. Drill it — deciding this at 03:00 without a mandate is how hours are lost |
| CON-12 | Disable remote access (client VPN, site-to-site, RDP/VDI gateways, vendor and OOB management) | VPN / gateway / firewall | ☐ | ☐ | ☑ typically | Partial isolation is not isolation — enumerate every inbound path, including supplier and management ones, before you need the list |
| CON-13 | Isolate backup infrastructure | Backup platform / storage / network | ☐ | ☐ | ☑ typically | Confirm recent restore points are readable *first*. Backup systems are a primary ransomware target and the credentials to reach them are often already held |
| CON-14 | Extend snapshot retention / export snapshots | SAN / hypervisor / storage | ☐ | ☐ | ☐ | Defaults roll off in days and take evidence and recovery points with them — a first-hour action, not a recovery-phase one |
| CON-15 | Stand up emergency log collection | Firewall, directory, hypervisor, mail, remote access | ☐ | ☐ | ☐ | For estates without central logging: pull logs somewhere the adversary cannot reach, before they rotate |
| … | | | | | | |

**Governance:** owner: [role] · review frequency: [semi-annual] · approver (outside CDC): [function] · last reviewed: [date]
**Operating-model note:** in MSSP/hybrid models, add a column "who may execute" (MSSP autonomously / MSSP on approval / internal only) — mirror the MSSP checklist's response-boundary matrix.

---
*Template from the Open CDC Framework (CC BY 4.0).*
