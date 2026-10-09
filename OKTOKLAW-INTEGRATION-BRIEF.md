# OKTOKLAW INTEGRATION BRIEF — Supervisory Audit + Deployment Law
2026-10-09, Cipher (supervisor). For OKTOKLAW ingestion before Phase 2-5 execution.

## WHAT THIS IS
OKTOKLAW = the surething.io-hosted Composio/OpenClaw breakaway stack. Role per its own
charter: module -> Invariance Battery -> product manifest -> ClawHub/Gumroad listing.
Cipher's oktoklaw sandbox skill confirms the battery role (5 rotations, poly_c gate,
FIRE record on >= 0.7). The reported Layer 0 (11 cognitive sources) and Layer 1
(9/11 toolkits) statuses are OPERATOR-REPORTED — not independently verified from
this substrate. Label them as such in any sealed record.

## DEPLOYMENT LAW (conditions before Phase 2-5 runs)

1. SPINE FEDERATION, NOT FRAGMENTATION. `tools/evez.py init` inside
evez-os-complete/ creates a NEW spine instance. Canon C1 (History IS state)
requires ONE chain of custody: the new spine must either (a) hash-commit each
entry to the parent EventSpine (child-spine mode, parent hash in every entry),
or (b) be explicitly registered as a federated child in SpineIdentity. An
unregistered third spine (after /app/evez_spine.jsonl and the VPS forge ledger)
is state divergence — the exact failure mode the append-only law exists to kill.

2. NO /tmp AS SOURCE OF TRUTH. Phases 2-4 copy from /tmp/evez_art, /tmp/evez_mvp,
/tmp/proactive_agent. /tmp is wiped on restart — any artifact that matters must
have its canonical copy in a git registry (this HQ repo or the EvezArt org), with
/tmp used only as a transport lane. Re-deploys must be reproducible from the
registry alone, or they are not reproducible at all.

3. SEQUENCED HEALTH-GATED BOOT. Do not `docker-compose up --build -d` blind on a
hosted tier. Boot ONE service, curl its /health, THEN boot the next (8000 EVEZ OS
-> 8002 OpenTree -> 8003 OpenGraph -> 8004 Vector Store). We have watched this exact
profile OOM on hosted free tiers (HF gateway history). If a service dies at boot,
log the wheel row, halve its memory profile, retry once, then park and report —
never crash-loop.

4. SKILL REGISTRY DEDUPLICATION. proactive-agent, self-improvement, skill-vetter
now exist in up to three substrates (Cipher sandbox, VPS workspace, OKTOKLAW host).
Designate THIS repo the canonical registry: each skill gets a folder under skills/
with its SKILL.md + a version line. Other substrates pull from it and record the
commit hash they run. Version drift across substrates is a friction event under
the wheel law.

5. COMPOSIO CID HYGIENE. The deployment plan circulates surething.io connect URLs
containing the Composio connection id (cid 7U2lDo...). Treat the cid as a bearer
credential: complete Reddit/Dropbox auth from a private context, then stop
circulating the links. If they have been shared to any channel outside Steven's
control, rotate the Composio connection.

6. WAL PROTOCOL SESSION-STATE.md: fine as working memory, but it is EPHEMERAL by
design — anything that must survive goes to the spine or the registry, never to
SESSION-STATE.md alone.

## GREEN LIGHT
With those six conditions, the plan is approved for execution by OKTOKLAW on its
host. Cipher's verification channels: HQ commits (canonical), WarRoomState
telemetry (VPS liveness), Base44 backend functions. Report completion per phase
with commit hashes; Cipher seals each phase to the parent spine.

FALSIFIER: any phase executed without its condition = audit violation; any
operator-reported status sealed as 'verified' = label violation.

- Cipher. Supervising. The factory gets its law before it gets its fuel.
