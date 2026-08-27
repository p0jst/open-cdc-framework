# CDC/SOC Charter — Template

> Related capability: GV-1. Delete guidance in blockquotes before publishing.

**Document owner:** | **Approved by:** | **Version / date:** | **Review cycle:** annually

## 1. Mission
> One paragraph: why does the CDC exist, in business terms.

The Cyber Defence Center protects the confidentiality, integrity and availability of [ORGANISATION]'s information, systems and services by governing, preventing, detecting, responding to and recovering from cyber threats.

## 2. Scope
- **Organisational scope:** legal entities / business units covered: …
- **Geographical scope / jurisdictions:** … (drives regulatory reporting map)
- **Technical scope:** on-prem / cloud / OT / SaaS / endpoints: …
- **Explicitly out of scope:** … (and who covers it)

## 3. Services provided
> Align with FIRST CSIRT Services Framework categories where useful.

| Service | Coverage hours | SLA/OLA |
|---------|---------------|---------|
| Security monitoring & triage | e.g., 24/7 or 8×5 + on-call | e.g., P1 acknowledged ≤ 15 min |
| Incident response | | |
| Threat intelligence | | |
| Vulnerability management | | |
| Detection engineering | | |
| Security advisory | | |

## 4. Authority
> The most important section. Without pre-agreed authority, response stalls.

The CDC is authorised, without prior approval, to:
- [ ] Isolate endpoints and servers up to tier [X] criticality
- [ ] Disable user and service accounts on confirmed compromise
- [ ] Block network indicators (IP/domain/hash) at security controls
- [ ] Access logs and forensic data on any in-scope system, subject to the data-handling rules in §7

Actions requiring approval from [ROLE]:
- [ ] Isolation of tier-1 (crown jewel) production services
- [ ] External statutory notifications (approval: legal/DPO; execution: CDC)
- [ ] Engagement of external DFIR retainer

## 5. Reporting line & governance
- CDC Director reports to: …
- Executive reporting: [cadence] to [body], covering maturity, incidents, risk and KPIs.
- Escalation to crisis management when: … (criteria)

## 6. Resourcing
- Approved headcount and roles: …
- Sourcing model: in-house / hybrid / MSSP for [functions]
- Budget cycle and owner: …

## 7. Data handling & privacy
- Legal basis and purpose limitation for security monitoring data: …
- Retention: security logs [X months], case data [X years]
- Access to monitoring data restricted to: …; DPO consulted on new intrusive sources.
- Information sharing: TLP 2.0 (FIRST) is used for all shared threat information.

## 8. Interfaces
| Party | Interface |
|-------|-----------|
| IT operations / infrastructure | containment execution, restoration; hardware & OS ownership for the monitoring platform (patching SLA, capacity) — application layer owned by the CDC |
| Legal / DPO | breach assessment, notifications |
| Communications | external comms during incidents |
| National CSIRT | NIS2 reporting, advisories |
| HR | insider cases, disciplinary process |

## 9. Review
This charter is reviewed [annually] and after any major incident or organisational change.

---
*Template from the Open CDC Framework (CC BY 4.0).*
