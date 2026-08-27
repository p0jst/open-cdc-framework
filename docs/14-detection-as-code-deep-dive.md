# 14 — Deep Dive: Detection-as-Code and ATT&CK Mapping (Advanced tier)

> Doc 15 states the principles; this document is the engineering manual. Audience: detection engineers and technical leads in S/A-tier CDCs (or teams demanding this of an MSSP). Everything below is vendor-neutral; Sigma is used as the authoring format because it is open and convertible to most platforms.

## 1. Repository layout

Treat the detection repo as a software project. A layout that has proven durable:

```
detections/
├── rules/                        # one YAML file per detection
│   ├── windows/
│   │   ├── win_priv_group_addition.yml
│   │   └── win_lolbin_certutil_download.yml
│   ├── linux/
│   ├── macos/
│   ├── identity/                 # IdP / directory detections
│   ├── cloud/                    # IaaS/SaaS control plane
│   └── network/
├── tests/
│   ├── samples/                  # sanitised log events per rule (positive & negative)
│   │   └── win_priv_group_addition/
│   │       ├── should_fire_01.json
│   │       └── should_not_fire_01.json
│   └── emulation/                # scripted attack emulation mapped to rules
├── suppressions/                 # tuning as code: owner + expiry per entry
│   └── win_priv_group_addition.yml
├── runbooks/                     # triage steps, versioned next to the rule
├── pipelines/                    # CI definitions, converters, deploy scripts
├── navigator/                    # generated ATT&CK Navigator layers (JSON)
└── docs/                         # conventions, onboarding, this workflow
```

Conventions that pay off: one rule per file · file name = rule id · everything reviewable in a diff · no logic that exists only in the SIEM console.

## 2. Anatomy of a rule (Sigma-style YAML)

Original example — detect addition to a privileged directory group:

```yaml
title: Addition To Privileged Group
id: 3f2a9c1e-7b4d-4e8a-9c21-example-uuid    # stable UUID, never reused
status: production                           # experimental | test | production | retired
description: >
  Detects a user being added to a highly privileged directory group.
  Legitimate additions should follow the PAM change process; anything
  outside it warrants investigation.
references:
  - internal: UC-0042                        # link to the use-case record
author: <team, not individual>               # bus-factor hygiene
date: 2026/07/10
modified: 2026/07/10
tags:
  - attack.persistence                       # ATT&CK tactic
  - attack.t1098.007                         # technique/sub-technique: Account
                                             # Manipulation: Additional Local or Domain Groups
  - cia.integrity                            # OCDF: primary CIA objective
  - tier.essential                           # OCDF tier tag (E/S/A)
logsource:
  product: windows
  service: security
detection:
  selection:
    EventID: 4728                            # member added to security-enabled global group
    TargetGroupName|contains:
      - 'Domain Admins'
      - 'Enterprise Admins'
      - '<your tier-0 groups>'
  filter_pam_process:
    SubjectUserName|startswith: 'svc-pam-'   # your PAM service account convention
  condition: selection and not filter_pam_process
falsepositives:
  - Emergency break-glass procedure (verify against break-glass log)
level: high
fields: [SubjectUserName, TargetUserName, TargetGroupName]
```

Metadata discipline is the point: the `tags` block is what makes coverage measurable (§4), the `id` is what makes history traceable, `status` drives pipeline behaviour, and `falsepositives` is the seed of the runbook. Extend the schema with custom fields if needed (owner, review-by date, data-source dependency) — but validate them in CI so they stay populated.

Suppressions live in their own files, never inline hacks:

```yaml
# suppressions/win_priv_group_addition.yml
- reason: "IAM migration project batch adds"
  match: { SubjectUserName: 'svc-iam-migrate' }
  owner: detection-engineering
  ticket: CDC-1234
  expires: 2026-09-30          # CI fails the build on expired suppressions
```

## 3. The pipeline (CI/CD)

Merge to main is the only road to production. Stages:

1. Lint & schema validation — YAML parses; mandatory fields present; UUID unique; tags reference valid ATT&CK IDs (validate against the ATT&CK STIX data, don't hand-maintain a list).
2. Unit tests — run each rule against its `should_fire` and `should_not_fire` samples with a Sigma-aware test harness or a scratch instance of your platform. A rule without at least one positive and one negative sample fails the build.
3. Conversion — compile Sigma to the target platform's query language (sigma-cli/pySigma backends). Conversion errors fail the build; review the compiled output for expensive constructs.
4. Staging deploy — push to a staging/QA workspace; smoke-test against recent live data for volume (an unexpectedly hot rule gets caught here, not in analysts' queues).
5. Production deploy — API-driven; the pipeline records rule id ↔ platform object id.
6. Drift detection — nightly job diffs platform state against the repo; console edits are flagged and reverted or back-ported the same week.
7. Emulation validation (scheduled, not per-commit) — periodically execute mapped attack emulations (e.g., Atomic Red Team tests matching each rule's technique tags) in a lab/canary scope and confirm the alert fires end-to-end, through the alert pipeline, not just the query.

Adoption reality: build stages 1–3 first (a week of work, immediate payoff), then 5–6, then automate 7. Do not gate initial adoption on the full pipeline.

## 4. ATT&CK mapping methodology — mapping honestly

ATT&CK mapping is easy to do badly. Rules that make it useful:

1. Map to sub-technique where one exists; technique level only when the detection genuinely spans sub-techniques. Tactic-only tags are placeholders, not mappings.
2. Map the behaviour the logic actually catches, not the scenario that inspired it. A rule catching `certutil` downloads maps to T1105 (Ingress Tool Transfer), even if you wrote it "because ransomware".
3. One detection may map to several techniques; several detections per technique is normal and good (depth beats breadth on high-value techniques).
4. Score coverage per technique on an honesty scale, not a checkbox:
   - 0 — no relevant telemetry collected
   - 1 — telemetry exists (could hunt), no detection
   - 2 — detection deployed, not validated in the last 12 months
   - 3 — detection deployed and validated (fired in test)
5. Scope the matrix before scoring: filter ATT&CK to your threat profile's techniques (doc 15 §5) and your platforms. "37% of all of ATT&CK" is meaningless; "level ≥2 on 80% of the techniques our top three threat actors use" is a management-grade statement.
6. Generate, don't hand-paint: the pipeline should emit an ATT&CK Navigator layer JSON from the rule tags + validation results, so the coverage picture is always current. Publish it to the team monthly; bring the threat-profile-scoped view to GOVERN quarterly.

Common traps: counting a noisy, permanently-suppressed rule as coverage; mapping identity attacks only under Credential Access and forgetting Initial Access; scoring on rule existence while the required log source was decommissioned last quarter (tie rule metadata to log-source dependency and check it in drift detection).

## 5. Metrics for this practice

% rules with passing unit tests · % rules validated by emulation ≤12 months · median idea→production lead time · drift incidents/month (target: zero) · expired suppressions (target: zero) · coverage level ≥2 on threat-profile techniques.

## Sources

- Sigma project & pySigma converters. https://github.com/SigmaHQ/sigma
- MITRE ATT&CK® and ATT&CK Navigator. https://attack.mitre.org · https://mitre-attack.github.io/attack-navigator/
- Red Canary, Atomic Red Team (attack emulation library). https://github.com/redcanaryco/atomic-red-team
- MITRE, *11 Strategies of a World-Class Cybersecurity Operations Center*, 2nd ed.

*Open CDC Framework (CC BY 4.0). ATT&CK® is a registered trademark of The MITRE Corporation.*
