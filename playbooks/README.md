# Playbooks

Basic incident response + digital forensics playbooks, per platform.
All are vendor-neutral; open source tooling examples are non-normative.

| ID | Platform | File |
|----|----------|------|
| PB-W11 | Windows 11 laptop | PB-W11-windows11-laptop.md |
| PB-MAC | macOS laptop (Intel & Apple Silicon) | PB-MAC-macos-laptop.md |
| PB-LNX | Linux enterprise server (RHEL-class) | PB-LNX-rhel-server.md |

**Scope: enterprise IT only** — these playbooks must not be applied to OT/ICS or telco core systems unadapted (isolation and live-response actions can be unsafe there).

## External baseline playbooks

Two public playbook collections are recommended as starting points alongside the platform playbooks here — with the important caveat that they are baselines: the reader must adjust and tailor them to their own environment, tooling, authority matrix and reporting obligations before relying on them.

- Microsoft incident response playbooks — practical, scenario-based runbooks (phishing, password spray, app consent grant, token theft, compromised applications), strongest for Microsoft-centric estates. https://learn.microsoft.com/security/operations/incident-response-playbooks
- CISA, Federal Government Cybersecurity Incident and Vulnerability Response Playbooks — clear, tool-neutral incident and vulnerability response workflows that adapt well outside the US federal context. https://www.cisa.gov/resources-tools/resources/federal-government-cybersecurity-incident-and-vulnerability-response-playbooks

Adaptation checklist when importing any external playbook: replace product assumptions with your stack; align severities with your IR plan §1; insert your containment mandates (containment action catalogue); add your statutory reporting hooks (NIS2/GDPR/DORA and national annex); and exercise it once before you need it.

Shared principles: order of volatility (RFC 3227), chain of custody, hash
everything, "Integrity before Availability" on recovery, and GDPR-aware
handling of employee/personal data. See docs/05-respond.md and 06-recover.md.
