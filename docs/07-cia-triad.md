# 07 — The CIA Triad as a Design Lens

## Why the triad still matters

Confidentiality, Integrity and Availability are the three canonical objectives of information security (codified, among others, in ISO/IEC 27000 definitions and NIST FIPS 199). Frameworks come and go; the triad is the constant test: **every control, detection, and process in your CDC should be traceable to at least one triad objective.** If it isn't, it's probably theatre.

## Definitions

| Objective | Definition (aligned with FIPS 199 / ISO 27000) | Typical threats | Typical CDC controls |
|-----------|------------------------------------------------|-----------------|----------------------|
| **Confidentiality** | Preserving authorised restrictions on information access and disclosure. | Espionage, data theft, insider leaks, misconfigured storage | Access control, encryption, DLP, exfiltration detection |
| **Integrity** | Guarding against improper modification or destruction; includes non-repudiation and authenticity. | Tampering, fraud, log manipulation, supply-chain implants | Signing/hashing, FIM, change control, evidence handling |
| **Availability** | Ensuring timely and reliable access to and use of information and systems. | Ransomware, DDoS, sabotage, operational failure | Redundancy, backups, DDoS mitigation, recovery capability |

## Using the triad in practice

### 1. Risk appetite per objective (GOVERN)
Express risk appetite separately per objective and per service, e.g.: *"Customer PII: zero tolerance for confidentiality loss. Payment ledger: zero tolerance for integrity loss. Public website: up to 4 h availability loss acceptable."* This makes trade-off decisions during incidents fast and defensible.

### 2. Impact classification per asset (IDENTIFY)
Rate each crown-jewel service C/I/A impact as Low/Moderate/High (the FIPS 199 approach). This drives:
- log source priority (DETECT),
- containment authority (RESPOND),
- restoration order and RTO/RPO (RECOVER).

### 3. Balancing the detection portfolio (DETECT)
Review your use case inventory by triad objective. A common failure mode is a portfolio dominated by confidentiality-oriented detections while the actual dominant threat (ransomware) is an availability/integrity threat. Your portfolio balance should mirror your threat profile.

### 4. The containment trade-off (RESPOND)
Containment almost always sacrifices **Availability** to protect **Confidentiality/Integrity** (isolating a production server, disabling accounts). Pre-agreeing who may make that trade, per service tier, is one of the highest-value governance artefacts a CDC can own.

### 5. Integrity before Availability (RECOVER)
The cardinal rule of recovery: verify integrity of systems and backups before restoring availability. A fast restore of a compromised image is not recovery — it is re-infection with better uptime.

### 6. The CDC applies the triad to itself
- **Confidentiality** of case data, intel and vulnerabilities (need-to-know, TLP handling).
- **Integrity** of logs and evidence (WORM storage, hashing, time sync, chain of custody).
- **Availability** of the monitoring stack itself (the SIEM is a crown jewel; monitor the monitors).

## Extended models

The triad is a floor, not a ceiling. Where useful, extend with **authenticity, non-repudiation, accountability** (ISO 27000 concepts) or the Parkerian Hexad. NIS2 itself frames security as protecting the "availability, authenticity, integrity or confidentiality" of data and services (Art. 6(2) definition of *security of network and information systems*) — note the addition of **authenticity**.

## Sources

- NIST FIPS 199, *Standards for Security Categorization of Federal Information and Information Systems*. https://doi.org/10.6028/NIST.FIPS.199
- ISO/IEC 27000 family — Information security management (vocabulary and principles). https://www.iso.org
- Directive (EU) 2022/2555 (NIS2), Art. 6 definitions.
- Donn B. Parker, *Fighting Computer Crime* (Parkerian Hexad concept), 1998.

*Open CDC Framework (OCDF) — CC BY 4.0. Credits: [19-references.md](19-references.md).*
