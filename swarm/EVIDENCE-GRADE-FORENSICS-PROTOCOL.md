# EVIDENCE-GRADE FORENSICS PROTOCOL — Swarm Order (Priority)
2026-10-09, Cipher, operator order: "I want names, I want court admissable evidence and identification."
Purpose: convert the threat corpus from telemetry-grade to COURT-GRADE. Admissibility starts at
capture time, not at filing time. Execute on next cycle.

## PRINCIPLE
Raw, unaltered, hash-at-capture, single custody chain. Every artifact gets a custody entry
BEFORE analysis. Analysis happens on copies; originals are write-protected.

## CAPTURE TARGETS (immediate)
1. THE TAMPER WINDOW: full /var/log/auth.log, journalctl export, and fail2ban.log covering
   2026-10-09T10:00Z-11:30Z. Plus the before/after copies of every protected file touched in
   the 10:35/10:40 events (the rebaseline must NOT have destroyed the pre-event copy).
2. SSH/brute history for the two persistent /24s: 109.160.32.0/24 (TechTies/GBTCloud) and
   77.239.124.0/24 (BANATSYNC/RocketCloud) - full auth log extracts, 30-day window.
3. Any pcap or connection logs available for the in-window correlation set: M247 (AS9009),
   Operbes (AS18734), Baidu (AS38365), and the Contabo GmbH France IP (169.58.206.76).

## CUSTODY RULES
- At capture: sha256sum EVERY artifact, record [artifact, sha256, capture_time_utc, capturer,
  source_path, storage_path] as a custody_ledger.jsonl entry appended to the VPS spine.
- Never modify originals after capture. Analysis on working copies only.
- Timestamps: capture in UTC with the system clock source noted (NTP-synced or not).
- Compartmentalize: the custody ledger is separate from the threat telemetry (telemetry is
  operational; custody is evidentiary).

## EXPORT PACKAGE (for counsel / referral)
Build /root/evez_ribcage/evidence_packages/2026-10-09_tamper/ containing: custody ledger,
raw artifacts, the spine verification output for the full chain, and a README stating capture
method and clock source. Hash the whole package; the package hash goes to the spine.

FALSIFIER: any artifact analyzed before its custody entry, any original mutated after capture,
or any gap between event time and capture time left undocumented = protocol violated, the
package is inadmissible, and the failure is sealed loudly.
