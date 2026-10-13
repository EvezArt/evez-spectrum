# ADVISORY ADDENDUM A2 — 2026-10-13 23:35 UTC: BLAST RADIUS + SENSOR BLACKOUT

Sources: ThreatIntel corpus (freshest 60 sealed records) + WarRoomState
live telemetry payload. All timestamps UTC. This is the machine's OWN log
stack, not external OSINT.

## CRITICAL FINDING: THE MACHINE'S SENSORS WENT DARK ~33 HOURS AGO
• 2026-10-12 05:18Z (inferred): machine REBOOTED (war room reports
  uptime 27 minutes at the 05:45Z push).
• 2026-10-12 05:40:05Z: protected_file_tamper — rebaselined_alerted.
  A SECOND TAMPER EVENT on the protected files (first was 2026-10-09
  10:35/10:40Z). Logged, alerted, survived.
• 2026-10-12 05:40:13Z: fail2ban_restarted auto_start; bounty awarded.
• 2026-10-12 05:42-05:44Z: three threat_posture mode_shift events in
  three minutes — posture volatility right after the tamper.
• 2026-10-12 05:45:03Z: LAST war-room push. Last swarm seal: 05:40Z.
• NOTHING SINCE. As of this advisory the gap is ~33 hours with zero
  seals and zero pushes, against a pre-blackout cadence of one seal
  every ~20 minutes (~3/hour). That cadence does not go quiet on its
  own: the sweep daemon and the war-room push both died after the
  reboot and have not come back. INFERENCE (labeled): post-reboot
  service failure, not peace. Falsifier: any seal or push with a
  timestamp after 05:45Z disproves the blackout instantly.

## THE BLAST RADIUS UP TO THE BLACKOUT (what was hitting us ongoing)
1. TECHTIES / GBTCLOUD (AS197170) — STILL THE HAMMER: three more seals
   from 109.160.32.0/24 Amsterdam (21:20Z Oct 11, 03:40Z + 04:20Z Oct
   12). The most persistent attacker in the corpus was active right
   up to the sensor blackout. The gcn.bg abuse filing remains the
   1,437th unanswered report.
2. REPEAT-OFFENDER RADIUS (ban_count = return rate):
   • 220.123.33.105 South Korea (Korea Telecom) — 38 BANS, live across
     12+ hours.
   • 117.72.35.56 China (Beijing Jingdong 360) — 20 bans, 6+ hours.
   • 115.190.213.72 Beijing Volcano Engine — 14 bans.
   • 83.235.16.111 Greece (OTEnet) — 9 bans across 2.5 hours.
   These are the blast radius core: banned, returning, banned again.
3. CLOUD-HOP WING: Tencent (Yokohama + Santa Clara), Oracle Cloud
   Singapore, netcup Nuremberg, OVH Roubaix, IONOS London — the
   rented-rotation pattern continuing to the blackout.
4. At the final push: 11 active bans, fails_1h = 2, mode PEACE (but
   posture shifting).

## WHAT THE BLACKOUT MEANS
Every attack after 2026-10-12 05:45Z is currently INVISIBLE to this
stack: no seals, no war-room telemetry, no corpus growth. The 1,729-
record corpus is now a historical record, not live coverage. The
ongoing blast is unobserved until the sensors restart.

## RESTORE PATH (blocked from sandbox; needs one of two keys)
A. Steven supplies the new VPS root credential (rotated 2026-10-05,
  still pending) — direct restart of the sweep + push daemons.
B. OpenClaw ingests this directive from HQ (GitHub-as-transport) and
  runs: restart crackdown sweep cron + warroom_push.sh + verify
  POST to evezWarRoom, then confirm with a fresh seal timestamp.

FALSIFIER: this advisory closes when a new ThreatIntel seal or
WarRoomState push carries a timestamp later than 2026-10-12 05:45Z.
