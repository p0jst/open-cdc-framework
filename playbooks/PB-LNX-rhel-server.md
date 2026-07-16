# PB-LNX — Incident Response & Digital Forensics: Linux Enterprise Server (RHEL-class)

> **Scope:** Suspected compromise of an enterprise Linux server (RHEL, and by extension SLES/Ubuntu Server with path adjustments) — webshells, cryptominers, rootkits, lateral movement, ransomware on file/virtualisation servers. Related capabilities: RS-2, RS-3, DE-3.
> **Servers ≠ laptops:** containment decisions have direct **Availability** impact on business services — the pre-agreed authority matrix in the CDC charter §4 governs who may isolate what. <!-- law:nis2 -->

## 0. Prerequisites

- [ ] auditd (or equivalent) with a meaningful ruleset, forwarding to central logging — local logs on a rooted box are untrustworthy
- [ ] journald/syslog forwarded centrally; NTP/chrony verified (evidence timelines die without time sync)
- [ ] Out-of-band access (iLO/iDRAC/BMC or hypervisor console) documented per server
- [ ] Known-good static binaries kit (busybox-class or vendored coreutils) on read-only media — assume on-host binaries are trojaned
- [ ] For VMs: rights and procedure to **snapshot with memory** at the hypervisor
- [ ] LUKS keys/escrow documented where disk encryption is used

## 1. Triage (remote/central first)

1. Work from **central** logs first: auth events (`/var/log/secure` forwarded), auditd, netflow, EDR — the host copy may be manipulated.
2. Identify the service impact tier (crown-jewel link) — this decides the containment authority path.
3. Fork: evidence-priority vs availability-priority (e.g., active ransomware encrypting an NFS export → isolate immediately).

## 2. Containment

- **VM:** hypervisor-level **snapshot including memory first**, then network-isolate at the virtual switch/security group — this is the cleanest evidence + containment combo available anywhere.
- **Physical:** isolate at switch port/firewall; keep power on. Use BMC console for access if SSH is untrusted.
- Do **not** kill suspicious processes or reboot before volatile collection — rootkit persistence may be memory-only, and reboot destroys it (and tips off the adversary).
- Freeze credentials: disable implicated accounts, remove authorized_keys additions, rotate secrets the server held (DB creds, API keys, service accounts) — check your secrets manager audit log.

## 3. Evidence acquisition — order of volatility (RFC 3227)

> Run collection with known-good binaries, output to remote/external storage (never to the evidence disk), hash everything, log every command with timestamp.

| # | Evidence | How | RHEL notes |
|---|----------|-----|------------|
| 1 | **Memory** | VM: hypervisor snapshot (.vmem-class file). Physical: kernel-module or /proc/kcore-based acquisition (AVML/LiME-class) | Secure Boot/lockdown mode may block unsigned modules — AVML-style userspace tools avoid this. Test per RHEL major version in advance. |
| 2 | Volatile state | From known-good binaries: `ps`, `ss -tunap`, `lsof`, loaded modules (`lsmod`, `/proc/modules`), mounts, users (`w`), iptables/nftables rules, environment of suspicious PIDs (`/proc/<pid>/environ`, `/proc/<pid>/exe`, `maps`, deleted-but-running binaries) | `/proc/<pid>/exe` recovers deleted running malware — collect before killing anything. |
| 3 | Logs & audit | `journalctl` export, `/var/log/` (secure, audit/audit.log, cron, httpd/nginx, application logs), auditd raw logs | Compare host copies against central copies — deltas are themselves findings (Integrity). |
| 4 | Disk | LVM snapshot then image the snapshot (minimises downtime), or dd/ewf image via boot from external media; VM: copy virtual disks from the snapshot | Record LUKS status; image while unlocked or with key escrowed. |
| 5 | Platform/cloud | Hypervisor/cloud audit logs, config management history (what *should* the host look like), backup catalogues | Config management (Ansible/Satellite) diffs are gold for spotting unauthorised change. |

**Key Linux artefacts:**
- Accounts & access: `/etc/passwd|shadow|group`, sudoers(+.d), `~/.ssh/authorized_keys` (all users), last/btmp/wtmp/lastlog, PAM configs
- Persistence: cron (all crontabs + /etc/cron.*), **systemd units & timers** (incl. user units `~/.config/systemd/user`), rc.local, `/etc/ld.so.preload` & LD_PRELOAD, shell profiles/rc files, udev rules, malicious PAM modules, SSH forced commands
- Execution/history: shell histories (all users incl. root; note gaps/`HISTFILE` tampering), `/tmp`,`/dev/shm`,`/var/tmp` contents, auditd execve records
- Package integrity: `rpm -Va` against a trusted rpmdb (flags modified binaries — classic rootkit tell)
- Web tier: webroot diff vs deployment source (webshells), access logs around first-touch
- Containers: `podman/docker ps -a`, images, overlay diffs, container logs — a "clean host" may have a dirty container

## 4. Analysis pointers

- Timeline: filesystem metadata + auditd + central auth logs + application logs; pivot on first anomalous auth or exploit signature.
- Rootkit checks: kernel taint (`/proc/sys/kernel/tainted`), hidden PIDs (compare `/proc` walk vs `ps`), `rpm -Va`, `ld.so.preload`.
- Determine data impact: what data did the service hold/process, was there staging/exfil (large outbound transfers, archive files in tmp)? This feeds breach notification decisions. <!-- law:gdpr -->

## 5. Eradication & recovery

- **Rebuild from known-good** (image/config management) — never trust a "cleaned" server that had root-level compromise.
- Redeploy from IaC/config management; restore data from backups **after integrity verification** (Recover principle: Integrity before Availability).
- Rotate every secret the host could read; re-issue host keys/certs; review trust relationships (NFS exports, SSH trust, service mesh certs).
- Fleet hunt: run the same indicator/persistence checks across all similar servers before closing.

## 6. Reporting hooks

- Service disruption or data impact on essential/important services → NIS2 Art. 23 clock (early warning ≤ 24 h). <!-- law:nis2 -->
- Personal data in scope (databases, logs, user content) → GDPR Art. 33/34 via DPO. <!-- law:gdpr -->
- Financial entities → DORA Art. 19. <!-- law:dora -->

## Non-normative tooling examples (open source)

Memory: AVML, LiME, Volatility 3 · Collection: Velociraptor, UAC (Unix-like Artifacts Collector), osquery · Disk/timeline: Sleuth Kit, Plaso · Integrity: AIDE, `rpm -Va`.

## Sources
- NIST SP 800-86; RFC 3227; NIST SP 800-61r3.
- Red Hat public documentation (auditd, LVM snapshots, systemd) — https://docs.redhat.com

*Open CDC Framework (CC BY 4.0).*
