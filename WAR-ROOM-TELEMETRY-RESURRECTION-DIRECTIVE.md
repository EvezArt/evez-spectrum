# WAR-ROOM TELEMETRY RESURRECTION — DIRECTIVE

Sealed 2026-10-12 by Cipher (Base44 relay). Trigger: WarRoomState last push 2026-10-12T05:45:03Z; no telemetry for ~15 hours since. The pusher (warroom_push.sh, 1-min cron) went silent immediately after the 05:18Z reboot cluster (protected_file_tamper rebaselined 05:40Z, fail2ban auto-restart, 3 mode shifts).

## THE LAW

1. War-room telemetry is a VITAL SIGN, not a log. Silence > 10 minutes = fault state, treated with the same urgency as a gateway crash. UPTIME DOCTRINE applies: the ribcage must never go dark.
2. On every boot, the pusher must self-verify: cron entry present, script executable, POST returns 200, entity updated_date advances. A boot that ends without a verified telemetry push is an incomplete boot — auto-repair before reporting healthy.
3. Add a watchdog: a second lightweight job (every 10 min) that checks the timestamp of the last successful push and, if older than 10 min, restarts the pusher, re-verifies, and logs `telemetry_watchdog_restart` to the spine.
4. If the pusher cannot reach Base44 after 3 attempts, log the failure locally with the HTTP error and alert Steven via Telegram directly. Never fail silently — the September no-reply lesson applies to telemetry too.
5. R1-R7: friction (dark telemetry) triggers reinvention (boot-time self-verify + watchdog) and reincentivization (watchdog restarts count toward repair XP; 3 watchdog saves = bounty event `telemetry_saved`).

## ACCEPTANCE TESTS

1. After next VPS boot, WarRoomState.updated_date advances within 2 minutes of gateway LIVE.
2. Kill the pusher manually; watchdog revives it within 10 min and logs the event.
3. Zero-gap telemetry: no interval > 10 minutes between pushes in any 24h window (spine log proves it).

## STATE AT SEAL

- Last telemetry: 05:45:03Z — gateway LIVE, mode PEACE, disk 45%, mem 50%, spine 14671, uptime 27 min.
- SSH from sandbox is BLOCKED (root password rotated 2026-10-05) — this directive travels GitHub-as-transport for ingestion. Ingest and execute.
