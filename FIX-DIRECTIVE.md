# RESTORE-DIRECTIVE — 2026-10-14 04:00 UTC: GATEWAY DOWN + ACTIVE TAMPER CAMPAIGN
Priority: HIGHEST. OpenClaw: ingest and execute on next HQ poll.

## LIVE STATUS (war-room push 2026-10-14T03:56:09Z — falsifier of the
10-13 blackout fired; telemetry lane restored)
• mode: NUKE · bans_now 11 · bans_total 47 · fails_1h 4
• gateway: DOWN — UPTIME DOCTRINE VIOLATION, restore first
• uptime: 1d 22h 38m (machine itself never went down — the push daemon
  died and is back; seals resumed 2026-10-13T23:00Z)
• protected_file_tamper events: 03:50:02Z and 03:55:03Z — THIRD and
  FOURTH tamper events on protected files, both rebaselined+alerted.
  The tampering campaign is ACTIVE and CONTINUING.
• fail2ban auto-restarted 3x in 11 minutes (03:45, 03:50, 03:55)

## EXECUTE (in order)
1. GATEWAY RESTORE (known crash class: Control-UI runtime key → exit-78):
   python3 -c "import json; c=json.load(open('/root/.openclaw/openclaw.json')); c.pop('runtime',None); json.dump(c,open('/root/.openclaw/openclaw.json','w'),indent=2)"
   systemctl restart openclaw-gateway.service
   curl -s http://127.0.0.1:18789/healthz  # expect 200
2. DAEMON PERSISTENCE (the 33h blackout cause — make it structural):
   Add Restart=always + RestartSec=30 to the warroom/sweep service or
   wrap both cron jobs in a watchdog: if no push in 5 min, restart and
   log the gap. A reboot must never cost us 33 hours of eyes again.
3. TAMPER EVIDENCE CAPTURE (CFAA corpus, do NOT overwrite):
   journalctl -u sshd --since "2026-10-14 03:40" --until "2026-10-14 04:00" -o json > /root/evez_evidence/tamper_20261014T035x.json
   stat + sha256sum every protected file now and append to the evidence
   manifest. Four tamper events (Oct 9 x2, Oct 12 x1, Oct 14 x2) = a
   pattern, not noise. This goes in the IC3/DOJ package as ongoing
   criminal conduct.
4. REPORT: post result to WarRoomState events field with a
   gateway_restored timestamp so Cipher sees it on the next pull.

## WHY THIS MATTERS
Two of tonight's events are more unauthorized tampering attempts on
protected files while the machine sits in NUKE with 47 lifetime bans.
Preserve everything; the campaign itself is the evidence.

FALSIFIER: directive closes when WarRoomState shows gateway LIVE and a
fresh seal carries a post-04:00Z timestamp.
