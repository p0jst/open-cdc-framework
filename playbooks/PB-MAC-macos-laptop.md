# PB-MAC — Incident Response & Digital Forensics: macOS Laptop

> **Scope:** Suspected compromise of a corporate macOS laptop (Apple Silicon or Intel). Related capabilities: RS-2, RS-3, DE-3.
> **Legal note:** Employee personal data considerations apply as on Windows — legal basis, DPO involvement, chain of custody. <!-- law:gdpr -->

## 0. Prerequisites

- [ ] MDM enrolment (required for many response actions on modern macOS) with remote lock/isolate
- [ ] EDR with macOS live-response support
- [ ] **FileVault recovery keys escrowed in MDM** — same rule as BitLocker: no key, no dead-box analysis
- [ ] A dedicated analysis Mac (target disk / share mode acquisition requires Apple hardware)
- [ ] Volume-owner/admin credentials strategy documented (Apple Silicon requires volume owner auth for some operations)

## 1. Platform realities to internalise before responding

- **Apple Silicon changes forensics.** Traditional full memory acquisition is effectively unavailable on Apple Silicon without specialised solutions; prioritise **live collection via EDR** and treat the unified logs + cloud telemetry as your primary record.
- **SIP (System Integrity Protection)** limits what even root can touch — good for evidence integrity, limiting for some tools.
- **TCC** (privacy consent database) governs what your collection tooling may access — pre-approve your forensic/EDR tools via MDM PPPC profiles *in advance* or collection will silently fail.
- **Sealed system volume:** the OS volume is cryptographically sealed; malware lives in the Data volume, LaunchAgents/Daemons, and user context — scope collection accordingly.

## 2. Triage (remote first)

1. Pull EDR telemetry, IdP sign-ins, MDM device record, and unified log excerpts remotely.
2. Check XProtect/Gatekeeper/quarantine events for the suspicious file's provenance.
3. Classify severity; choose evidence-priority vs containment-priority fork.

## 3. Containment

- EDR network isolation preferred; otherwise MDM-based network restriction or physical disconnect.
- **Do not power off** if live collection is still possible (volatile data, decrypted FileVault state).
- Revoke the user's cloud sessions/tokens; rotate credentials from a clean device.
- If the device may be remotely wiped by the adversary (stolen Apple ID / MDM compromise scenario), isolate from network *and* record MDM/Apple ID state immediately.

## 4. Evidence acquisition — order of volatility

| # | Evidence | How | macOS notes |
|---|----------|-----|-------------|
| 1 | Volatile state | EDR live response: processes, connections, launchd jobs, kexts/system extensions, logged-in users | Prefer scripted collection to interactive use. |
| 2 | **Unified logs** | `log collect` (creates a `.logarchive`) | The single richest macOS source; collect early — it rolls over. |
| 3 | Targeted triage collection | Collect key artefact paths (list below) with hashing | Faster and often sufficient vs full image. |
| 4 | Disk image | Image the **Data volume** while unlocked, or full APFS acquisition on an analysis Mac (target/share mode) | FileVault: unlocked-state acquisition or escrowed key required. APFS snapshots can preserve pre-incident state — check `tmutil listlocalsnapshots /`. |
| 5 | Cloud artefacts | IdP logs, MDM record, iCloud/Drive/SaaS audit as applicable | Survives device wipe. |

**Key macOS artefacts:**
- Persistence: `/Library/LaunchDaemons`, `/Library/LaunchAgents`, `~/Library/LaunchAgents`, login items (`BackgroundItems-v*.btm`), configuration profiles, cron/periodic
- Execution & provenance: quarantine database (`com.apple.LaunchServices.QuarantineEventsV2`), Gatekeeper/XProtect logs, `ExecPolicy`/CoreAnalytics
- User activity: `KnowledgeC.db`, Spotlight shortcuts, shell history (`~/.zsh_history`), Recent items, browser data
- Filesystem: FSEvents (`/System/Volumes/Data/.fseventsd`), APFS snapshots
- Security state: TCC.db (what had which permissions), sudo log entries in unified log

## 5. Analysis pointers

- Reconstruct provenance: quarantine db → what was downloaded from where; unified log → what executed with what parent.
- Verify persistence exhaustively — macOS malware overwhelmingly lives in launchd items and profiles.
- Map to ATT&CK (macOS matrix); feed indicators to DETECT.

## 6. Eradication & recovery

- Confirmed compromise → **erase and reprovision** (Erase All Content and Settings / MDM re-enrol); don't hand-clean.
- Rotate credentials, tokens, and certificates present on the device; review the user's OAuth grants.
- Verify restored device: clean EDR baseline, expected profiles only, TCC grants reviewed.

## 7. Reporting hooks

- GDPR Art. 33/34 assessment via DPO where personal data affected. <!-- law:gdpr -->
- NIS2 Art. 23 timelines if organisationally significant. <!-- law:nis2 -->
- DORA Art. 19 for financial entities. <!-- law:dora -->

## Non-normative tooling examples (open source)

Triage/collection: Velociraptor, osquery, Aftermath-class collectors, `log collect` (built-in) · Analysis: mac_apt, APOLLO (pattern-of-life from KnowledgeC), Sleuth Kit/Autopsy for APFS.

## Sources
- NIST SP 800-86; RFC 3227; NIST SP 800-61r3.
- Apple Platform Security Guide (platform behaviour: FileVault, SIP, sealed volume, Gatekeeper). https://support.apple.com/guide/security/

*Open CDC Framework (CC BY 4.0).*
