# Detection Use Case — Template

> Related capability: DE-2. One file per use case; keep under version control (detection-as-code).

## Metadata

| Field | Value |
|-------|-------|
| ID | UC-XXXX |
| Name | e.g., "Suspicious addition to privileged group" |
| Status | idea / development / testing / production / retired |
| Author / owner | |
| Created / last reviewed | |
| Severity (default) | P1–P4 |

## Threat context

- **Threat description:** what adversary behaviour does this detect?
- **MITRE ATT&CK mapping:** Tactic(s): … | Technique(s): T…
- **Threat profile link:** which actor/scenario from the organisational threat profile (ID-5) motivates this?
- **CIA objective(s) defended:** ☐ Confidentiality ☐ Integrity ☐ Availability
- **Priority assets in scope:** (crown-jewel link, ID-3)

## Technical definition

- **Required log sources:** (and current onboarding status)
- **Detection logic:** (query/rule in your platform's language — pseudocode acceptable at design stage)
- **Known blind spots / evasion:** …
- **Dependencies:** enrichment sources, allowlists, asset tags

## Operational handling

- **Triage steps:** 1) … 2) … 3) …
- **Escalation criteria:** …
- **Containment options:** (link to playbook)
- **False-positive scenarios & tuning notes:** …

## Validation & metrics

- **Test method:** unit test / attack simulation / purple team — evidence: [link]
- **Last validated (rule fired on test):** date
- **Volume:** alerts/week: … | True-positive rate: …
- **Review cadence:** every [6] months or on relevant threat-intel change

---
*Template from the Open CDC Framework (CC BY 4.0). ATT&CK® is a registered trademark of The MITRE Corporation.*
