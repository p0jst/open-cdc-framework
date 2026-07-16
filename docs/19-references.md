# 19 — References & Credits

This framework synthesises and builds upon the following publicly available works. **OCDF is an independent community project and is not endorsed by, affiliated with, or approved by any of the organisations below.**

## Primary framework backbone

- **NIST**, *The NIST Cybersecurity Framework (CSF) 2.0*, NIST CSWP 29, February 2024. https://doi.org/10.6028/NIST.CSWP.29 — NIST publications are U.S. Government works, not subject to copyright in the United States.

## NIST Special Publications & standards

- NIST SP 800-61 Rev. 3, *Incident Response Recommendations and Considerations for Cybersecurity Risk Management*, 2025. https://doi.org/10.6028/NIST.SP.800-61r3
- NIST SP 800-53 Rev. 5, *Security and Privacy Controls for Information Systems and Organizations*. https://doi.org/10.6028/NIST.SP.800-53r5
- NIST SP 800-92, *Guide to Computer Security Log Management*.
- NIST SP 800-34 Rev. 1, *Contingency Planning Guide for Federal Information Systems*.
- NIST FIPS 199, *Standards for Security Categorization of Federal Information and Information Systems*. https://doi.org/10.6028/NIST.FIPS.199

## MITRE

- **MITRE ATT&CK®**. https://attack.mitre.org — © The MITRE Corporation. ATT&CK is used under MITRE's Terms of Use permitting use with attribution. ATT&CK® is a registered trademark of The MITRE Corporation.
- C. Zimmerman et al., *11 Strategies of a World-Class Cybersecurity Operations Center*, 2nd edition, MITRE. https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center

## EU legislation (EUR-Lex; © European Union, reuse permitted under Commission Decision 2011/833/EU)

- Directive (EU) 2022/2555 (**NIS2**). https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- Regulation (EU) 2016/679 (**GDPR**). https://eur-lex.europa.eu/eli/reg/2016/679/oj
- Regulation (EU) 2022/2554 (**DORA**). https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- Regulation (EU) 2024/2847 (**Cyber Resilience Act**). https://eur-lex.europa.eu/eli/reg/2024/2847/oj
- Directive (EU) 2022/2557 (**CER**). https://eur-lex.europa.eu/eli/dir/2022/2557/oj
- Regulation (EU) 2019/881 (**Cybersecurity Act**). https://eur-lex.europa.eu/eli/reg/2019/881/oj
- Commission Implementing Regulation (EU) 2024/2690 (NIS2 technical requirements for certain digital entities).

## ENISA

- ENISA, *European Cybersecurity Skills Framework (ECSF) — Role Profiles* and *User Manual*, September 2022 (revision in progress). https://www.enisa.europa.eu/topics/skills-and-competences/skills-development/european-cybersecurity-skills-framework-ecsf

- ENISA, *ENISA Threat Landscape* (annual report series). https://www.enisa.europa.eu/topics/cyber-threats/threat-landscape
- ENISA, *CSIRT Maturity Framework* and CSIRT capability materials. https://www.enisa.europa.eu

## Maturity models & incident response communities

- Rob van Os, **SOC-CMM** — *Capability Maturity Model for Security Operations Centers*. https://www.soc-cmm.com — free to use; referenced here as a complementary deep-dive model.
- Open CSIRT Foundation, **SIM3** — *Security Incident Management Maturity Model*. https://opencsirt.org
- **FIRST**, *CSIRT Services Framework* v2.1. https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1
- **FIRST**, *Traffic Light Protocol (TLP) 2.0*. https://www.first.org/tlp/
- TF-CSIRT / **Trusted Introducer** — European CSIRT listing, accreditation and certification. https://www.trusted-introducer.org
- IETF **RFC 2350**, *Expectations for Computer Security Incident Response*; **RFC 2142**, *Mailbox Names for Common Services, Roles and Functions*.
- **VERIS** — *Vocabulary for Event Recording and Incident Sharing*. http://veriscommunity.net
- CMMI Institute, *Capability Maturity Model Integration* (conceptual basis for staged maturity levels).

## Incident response playbook baselines

- Microsoft, *Incident response playbooks* (learn.microsoft.com) — scenario runbooks to be adapted per environment. https://learn.microsoft.com/security/operations/incident-response-playbooks
- CISA, *Federal Government Cybersecurity Incident and Vulnerability Response Playbooks*, 2021. https://www.cisa.gov

## Digital forensics

- NIST SP 800-86, *Guide to Integrating Forensic Techniques into Incident Response*. https://doi.org/10.6028/NIST.SP.800-86
- IETF RFC 3227, *Guidelines for Evidence Collection and Archiving*. https://www.rfc-editor.org/rfc/rfc3227
- Apple, *Apple Platform Security Guide*. https://support.apple.com/guide/security/
- Microsoft public documentation (BitLocker, Windows artefact behaviour). https://learn.microsoft.com
- Red Hat public documentation (auditd, LVM, systemd). https://docs.redhat.com

## Danish legislation & authorities (retsinformation.dk; samsik.dk)

- Lov nr. 434 af 6. maj 2025, *Lov om foranstaltninger til sikring af et højt cybersikkerhedsniveau* (NIS 2-loven). https://www.retsinformation.dk/eli/lta/2025/434
- *Lov om styrket beredskab i energisektoren* (2025) — energy-sector NIS2+CER regime.
- *Lov om sikkerhed og beredskab i telesektoren* (2025) — telecom NIS2 implementation.
- *CER-loven* — kritiske enheders modstandsdygtighed (2025).
- Styrelsen for Samfundssikkerhed (SAMSIK), NIS2 guidance. https://samsik.dk/nis2

## Other

- CIS, *CIS Critical Security Controls* and *CIS Benchmarks* (the Implementation Groups pattern inspired OCDF's tier overlay). https://www.cisecurity.org
- Sigma — generic signature format for SIEM detections; pySigma converters. https://github.com/SigmaHQ/sigma
- MITRE ATT&CK Navigator (coverage layers). https://mitre-attack.github.io/attack-navigator/
- Red Canary, Atomic Red Team (attack emulation library). https://github.com/redcanaryco/atomic-red-team
- CISA, Known Exploited Vulnerabilities catalog. https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- MISP Project. https://www.misp-project.org
- ISO/IEC 27000-series, *Information security management systems* (vocabulary, ISMS requirements, controls). https://www.iso.org — ISO standards are paywalled; this framework references concepts only.
- Donn B. Parker, *Fighting Computer Crime: A New Framework for Protecting Information*, Wiley, 1998 (Parkerian Hexad).

## How to cite this framework

> Open CDC Framework (OCDF), version 0.1, 2026. Licensed CC BY 4.0. Available at: [repository URL].

## Corrections

Found a missing or incorrect attribution? Please open an issue — proper credit is a core value of this project.
