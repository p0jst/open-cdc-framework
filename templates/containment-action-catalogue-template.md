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
| … | | | | | | |

**Governance:** owner: [role] · review frequency: [semi-annual] · approver (outside CDC): [function] · last reviewed: [date]
**Operating-model note:** in MSSP/hybrid models, add a column "who may execute" (MSSP autonomously / MSSP on approval / internal only) — mirror the MSSP checklist's response-boundary matrix.

---
*Template from the Open CDC Framework (CC BY 4.0).*
