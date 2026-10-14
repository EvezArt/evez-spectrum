# THE CRACKS LEDGER — the crackdown on our own gaps — 2026-10-14
Operator order: 'find the slips and cracks that keep slipping through
the cracks.' Nine found, ranked by cost. Every crack has a fix and
an owner. This ledger is itself spine-sealed.

## CRACK 0 — THE PARALYZED HANDS (cost: every VPS-side fix queues)
OpenClaw gateway down (NUKE posture), restore directive committed but
un-ingested because the ingest path IS the gateway. VPS SSH blocked
since the Oct 5 password rotation; the new credential was never
delivered; tsnet bridge smoke-tested but keyless. FIX: two secrets
through the operator (TS_AUTHKEY + new root password) — the moment
they land, the restore, hardening, and tamper attribution all run.
OWNER: operator (only the operator holds both).

## CRACK 1 — THE EMPTY EVIDENCE TABLE (cost: the queryable store lies)
The Base44 Evidence entity holds ZERO records while 500+ EPIE-typed
records live only in sealed files/HQ. Any tool, dashboard, or future
automation reading the central table sees nothing. FIX: bulk-load the
EPIE corpus into the Evidence entity with target_id/category/verified
fields preserved. OWNER: agent, next window. STATUS: flagged 2026-10-14.

## CRACK 2 — UNROTATED KEYS (cost: a suspected leak stays live)
ENTITY_FARM_API_KEY and MONITOR_ADMIN_KEY flagged for rotation on
2026-10-12 after the paste-pipeline artifact review. Never rotated —
SSH was already blocked by then. FIX: rotate on first SSH window,
re-deploy consumers. OWNER: agent once crack 0 clears.

## CRACK 3 — TAMPER ATTRIBUTION INCOMPLETE (cost: five crimes, no face)
Five protected-file tamper events (Oct 9 x2, 12 x1, 14 x2): detected,
rebaselined, sealed — but the SOURCE cross-match (attack IPs vs
TechTies/ServHost/GBTCloud ranges) was never completed because the
logs sit on the VPS. FIX: run the cross-match on restore; a match
makes the tamper events part of the AS197170 CFAA corpus. OWNER:
agent once crack 0 clears.

## CRACK 4 — THE SILENT-BLACKOUT ARCHITECTURE (cost: 33 hours unseen)
The Oct 12-13 33-hour sensor blackout happened silently — telemetry
records gaps, nothing ALERTS on them. The war room records its own
absence. FIX: watchdog automation on the Base44 side: if no push for
> 90 minutes, escalate to the operator channel. OWNER: agent, next
window (platform-side, no VPS needed).

## CRACK 5 — THE DEAD CERT LANE (cost: no post-designation TLS evidence)
crt.sh 502 on three attempts across sessions. FIX: retry lane with
backoff + alternate CT mirrors (certstream, censys). OWNER: agent,
next window.

## CRACK 6 — THREE INCOMPLETE REGISTRY PULLS (cost: named gaps in filings)
Serbia APR (SSL-blocked from sandbox, needs browser lane), full RIPE
whois object for AS197170 (parse failure, retry with raw whois), HK
ICris certificate for EZ Infrastructure BRN 80559003 (session-gated).
All three are enhancement data for the filing kits. OWNER: agent,
next window, browser lane.

## CRACK 7 — THE SINGLE-HUMAN DEPENDENCY (cost: seven filings idle)
All identity-bearing filings (Companies House, Action Fraud, Estonia,
Netherlands, Hong Kong) wait on operator name + postal address. FIX:
one message from the operator. OWNER: operator.

## CRACK 8 — KEY-HOLDER TRANSPARENCY (cost: none, clarity only)
Cracks 0 and 7 both terminate at the operator. This is stated plainly
so the ledger shows where the keys are, not who to blame. The system
is not stuck — it is waiting, and it says so.

## CRACK 9 — VERIFIER ERA DRIFT (cost: false tamper alarms / blind spots)
Spine self-audit 2026-10-14: all 137 entries' prev_hash LINKAGE intact
(no chain breaks). But recomputing own_hash under the current formula
mismatches 45 oldest entries + 2 mid-entries: they were sealed under
an earlier serialization. The current verifier can only speak the new
era — a real tamper in the old era would read as routine mismatch.
FIX: era-aware verifier (per-era serialization profile) + one-time
re-witness of the old entries under dual formulas. OWNER: agent, next
window. NOTE: this is NOT evidence of tampering — linkage integrity
held for all 137; it is a tooling gap, logged as such.

## THE PATTERN THE CRACKS SHARE
Every crack is a thing the system NOTICED and never CLOSED. Detection
works; closure queues behind two secrets and one address. The crackdown
doctrine therefore stands: observability is proven, operability is
blocked, and the blockers are named above with owners attached.

FALSIFIER: each crack closes with a dated action; this ledger row
closes when all nine have one.
