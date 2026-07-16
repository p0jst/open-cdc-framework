# Publishing notes (maintainer checklist)

Approved project name: Open CDC Framework (OCDF). "Framework" refers to the capability model; SOC leads in the subtitle and metadata for discoverability.

## GitHub repository settings
- Repository name: `open-cdc-framework`
- Description: "Open CDC Framework (OCDF) — open source framework for building and maturing SOCs / Cyber Defence Centers in the EU. NIST CSF 2.0, CIA triad, NIS2/GDPR/DORA, maturity model, playbooks, all 27 national annexes."
- Topics: `soc` `security-operations-center` `cyber-defence-center` `csirt` `incident-response` `nist-csf` `nis2` `dora` `gdpr` `detection-engineering` `threat-intelligence` `maturity-model` `blue-team` `eu`
- Enable: Pages (for tools/regulatory-profile.html), Discussions, Issues.

## Release sequence
1. Fill ABOUT.md placeholders; set final repo URL in docs/19-references.md citation line.
2. Push, tag `v0.1-rc1`, verify Pages renders the selector.
3. Own read-through; legal review of reporting-deadline tables; re-verify pending annexes (FR/IE/LU/ES/PL/NL).
4. Tag `v0.1`, announce (community channels before broadcast channels).

Note: the name "OpenSOC" was considered and rejected due to existing use in the security community (Recon InfoSec's competition; the former Cisco/Apache Metron project) — do not abbreviate the project that way in materials.
