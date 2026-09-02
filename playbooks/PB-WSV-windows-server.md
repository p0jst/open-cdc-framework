# PB-WSV — Incident Response & Digital Forensics: Windows Server (incl. Domain Controllers)

> **Scope:** Suspected compromise of a Windows Server — file/application servers, IIS web tiers, Hyper-V hosts, and **Active Directory domain controllers**. Covers webshells, credential theft, ransomware staging, lateral movement and domain privilege escalation. Related capabilities: RS-2, RS-3, DE-3.
> **Servers ≠ laptops:** containment has direct **Availability** impact on business services — the pre-agreed authority matrix in the CDC charter §4 governs who may isolate what. <!-- law:nis2 -->
>
> **Tier 0 changes everything:** a domain controller, ADCS/PKI server, ADFS server or a host holding Domain Admin credentials *is* the identity fabric. If one is confirmed compromised, treat the **whole domain as compromised** until proven otherwise, and go to §5 before improvising. Isolating a DC also removes authentication for everything that depends on it — decide with the service owner, not alone.

## 0. Prerequisites (build these BEFORE the incident)

- [ ] EDR on servers, not just endpoints, with remote isolation and live response
- [ ] Windows Event Forwarding or agent-based forwarding to central logging — a compromised host's own event log is the first thing an adversary clears (Event ID 1102)
- [ ] Tiered admin model documented: which accounts are Tier 0, which hosts they may log on to
- [ ] **AD system-state backups from at least two DCs, held offline**, plus a written and rehearsed forest-recovery plan — this is the single control that decides how a DC compromise ends
- [ ] DSRM passwords documented and escrowed; LAPS (or equivalent) for local administrator accounts
- [ ] Out-of-band access (iLO/iDRAC/BMC or hypervisor console) documented per server
- [ ] For VMs: rights and procedure to **snapshot with memory** at the hypervisor
- [ ] BitLocker recovery keys escrowed for encrypted volumes; known-good tooling on read-only media

## 1. Triage (remote/central first)

1. Work from **central** logs first — the host copy may already be manipulated. Anchor on authentication (4624/4625 with logon type, 4672 special privileges, 4768/4769/4776 Kerberos and NTLM), service installation (7045, 4697), scheduled tasks (4698), share access (5140/5145) and log clearing (1102).
2. Establish the host's **tier and blast radius**: what does it hold, which privileged accounts have logged on to it, what trusts it, and is it Tier 0? Recent interactive logons by privileged accounts turn a single-server incident into an identity incident.
3. Identify the service impact tier (crown-jewel link) — this decides the containment authority path.
4. Fork: evidence-priority vs availability-priority (e.g. ransomware actively encrypting a file share → isolate immediately).

## 2. Containment

- **VM:** hypervisor-level **snapshot including memory first**, then network-isolate at the virtual switch/security group — the cleanest evidence-plus-containment combination available.
- **Physical:** isolate at switch port/firewall; keep power on. Use the BMC console if RDP/WinRM is untrusted.
- Do **not** reboot, run antivirus cleanup, or kill suspicious processes before volatile collection — credential material and memory-only implants are lost, and it tips off the adversary.
- Freeze credentials: disable implicated accounts, revoke Kerberos tickets and cloud sessions, and rotate every secret the host could read (service accounts, gMSA, application connection strings, API keys, certificates). Reset from a clean administrative host only — never by logging on to the suspect server.
- **If a domain controller is involved:** do not isolate it in a vacuum. Confirm remaining DCs are healthy and authoritative, plan for replication divergence, and expect that any account that authenticated through the compromised DC may need resetting.

## 3. Evidence acquisition — order of volatility (RFC 3227)

> Run collection with known-good binaries, write output to remote or external storage (never to the evidence volume), hash everything (SHA-256), and log every command with timestamp and operator.

| # | Evidence | How | Windows Server notes |
|---|----------|-----|----------------------|
| 1 | **Memory** | VM: hypervisor snapshot including memory. Physical: memory acquisition tool from external media or EDR live response | Capture **before** any reboot. Credential material (LSASS) and in-memory webshells live here. Memory integrity/VBS and Credential Guard can interfere with some tools — test yours on your standard server image in advance. |
| 2 | Volatile state | Live response: processes and parents, network connections, logged-on sessions, loaded drivers, open handles, scheduled tasks, services, WMI subscriptions, local group membership | Prefer EDR live response over interactive RDP — an interactive logon writes new artefacts and can expose fresh credentials to a resident adversary. |
| 3 | Event logs & config | Export the full `winevt\Logs` directory, not just Security; plus IIS logs, application logs, PowerShell transcripts, and the WMI repository | Compare host copies against central copies — gaps and deltas are themselves findings (Integrity). |
| 4 | Disk | Volume Shadow Copy or hypervisor snapshot, then image the snapshot to minimise downtime; full image where the case may reach court | Record BitLocker status; image while unlocked or with the recovery key in hand. Existing VSS copies may pre-date the intrusion — preserve them before they roll off. |
| 5 | Directory & platform | AD: `ntds.dit` plus the SYSTEM hive, SYSVOL, and replication metadata; hypervisor/cloud audit logs; backup catalogues; configuration-management history | `ntds.dit` contains every domain credential hash — handle it as Tier 0 evidence, encrypted, with a named custodian. Replication metadata shows *which DC* an object change originated from. |

**Key Windows Server artefacts:**

- **Authentication & privilege**: Security log (4624/4625 with logon type, 4672, 4720/4732 account and group changes, 4768/4769/4776), NTLM and Kerberos anomalies, `LSASS` access attempts (Sysmon 10)
- **Persistence**: services (7045, 4697), scheduled tasks (4698), **WMI event subscriptions**, Run keys, startup folders, GPO and logon scripts in SYSVOL, DLL side-loading in application directories, IIS modules and handlers
- **Active Directory**: `ntds.dit` + SYSTEM hive, SYSVOL contents, GPO changes (5136), AdminSDHolder and ACL changes on privileged objects, DSRM account use, `krbtgt` password age, replication metadata (`repadmin /showobjmeta`), DCSync-shaped directory access (4662 on replication GUIDs)
- **Execution evidence**: Amcache.hve, ShimCache (SYSTEM hive), SRUM (`SRUDB.dat`), PowerShell Operational and transcript logs, `ConsoleHost_history.txt` per admin profile — note that **Prefetch is disabled by default on server SKUs**, so do not expect it
- **Remote access**: RDP (TerminalServices-RemoteConnectionManager 1149, LocalSessionManager 21/25), WinRM and PowerShell Remoting logs, SMB share access (5140/5145), bitsadmin and BITS transfer logs
- **File activity**: `$MFT`, USN Journal (`$J`), Volume Shadow Copies, Recycle Bin, and — on file servers — the share ACL and access history that scopes a ransomware or exfiltration case
- **Web tier (IIS)**: webroot diff against the deployment source (webshells), IIS logs around first touch, application pool identities and their privileges, `web.config` handler additions
- **Certificate services (ADCS)**: issued-certificate database, template permission changes, and certificates issued to unexpected subjects — a common and durable domain-persistence path

## 4. Analysis pointers

- Build a super-timeline (filesystem metadata + event logs + EDR + central auth logs) and pivot on the first anomalous authentication or exploit signature.
- Work the **identity blast radius** deliberately: every privileged account that logged on to the host during the suspected window must be treated as exposed, along with the systems those accounts could reach.
- Look for domain-persistence techniques explicitly — DCSync, golden and silver tickets, `krbtgt` misuse, rogue certificate templates, AdminSDHolder and ACL backdoors, skeleton key. These survive a rebuild of the affected server and are the reason "we reimaged it" is not an answer for Tier 0.
- Map findings to MITRE ATT&CK; feed new indicators to DETECT via the use case template.
- Determine data impact: what the server held or processed, and whether there is evidence of staging or exfiltration (archives in temp paths, large outbound transfers, unusual cloud-storage or DNS volume). This feeds breach notification decisions. <!-- law:gdpr -->

## 5. Eradication & recovery

- **Rebuild from known-good** — reimage or redeploy from configuration management. Never trust a "cleaned" server that had SYSTEM or Domain Admin level compromise.
- Restore data from backups **after integrity verification** (Recover principle: Integrity before Availability), and check the backup system itself: modern ransomware operators target backup infrastructure first.
- Rotate every secret the host could read; re-issue host keys and certificates; review trust relationships (service accounts, delegation, SPNs, federation trusts).
- **If Tier 0 was compromised:** reset the `krbtgt` account password **twice**, allowing full replication between the two resets, and reset all privileged accounts, service accounts and computer accounts for Tier 0 systems. Revoke and re-issue certificates issued during the intrusion window; audit ADCS templates. If the extent cannot be established with confidence, execute the **forest recovery plan** rather than hoping — a partial cleanup of a compromised directory usually ends in a second incident.
- Fleet hunt: run the same indicator and persistence checks across all similar servers before closing.
- Closure criteria: no residual indicators fleet-wide for [7] days; privileged credential rotation complete and evidenced; lessons-learned filed.

## 6. Reporting hooks

- Service disruption or data impact on essential/important services → NIS2 Art. 23 clock (early warning ≤ 24 h). <!-- law:nis2 -->
- Personal data in scope (file shares, databases, mailboxes, logs) → GDPR Art. 33/34 via the DPO. <!-- law:gdpr -->
- Financial entities → DORA classification and Art. 19 timelines. <!-- law:dora -->
- A confirmed domain compromise is almost always significant at organisational level — start the notification assessment early rather than waiting for the investigation to finish.

## Non-normative tooling examples (open source)

Memory: WinPmem/DumpIt-class tools, Volatility 3 · Collection: Velociraptor, KAPE-style targeted collection, Eric Zimmerman's tools · Event logs: Hayabusa, Chainsaw, DeepBlueCLI · Timeline: Plaso/log2timeline · AD posture review (before and after): PingCastle.

## Sources
- NIST SP 800-86; RFC 3227; NIST SP 800-61r3.
- Microsoft public documentation on Active Directory forest recovery, the tiered administrative model, and Windows event logging — https://learn.microsoft.com

*Open CDC Framework (CC BY 4.0).*
