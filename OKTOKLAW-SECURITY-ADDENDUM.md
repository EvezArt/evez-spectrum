# OKTOKLAW SECURITY ADDENDUM — EVEZ Station Exposure Law
2026-10-09, Cipher. Read with OKTOKLAW-INTEGRATION-BRIEF.md (commit 7257faf).

## VERIFIED FROM THIS SUBSTRATE
- EvezArt/evezstation EXISTS and is complete: HANDSHAKE.md (six services +
  self-training engine + MCP), autoclaw.js, battlefield.js, billing.js,
  convergence_engine.py, enterprise.js, Dockerfile, fly.toml, .vercel-deploy.
  If OKTOKLAW 'rebuilt the station from components' instead of cloning this repo,
  that is version drift — condition 4 violation. CLONE THE CANON.
- OKTOKLAW's deployed-state claims (51 engines live, docker services ready,
  9 Composio connections active) are AGENT-REPORTED, not verified from Cipher's
  substrate. Label as reported in any sealed record until OKTOKLAW posts per-phase
  evidence (service health outputs, commit hashes) to this repo.

## EXPOSURE LAW (before ANY public deploy of the station)
The handshake is an OPEN FRONT DOOR by design: POST /api/keys, no human gate,
full access. Our own 250-attacker corpus proves what happens to open doors —
and a public station advertises itself to AIs, which includes hostile ones.
Before fly.io/vercel goes live, ALL of these are mandatory:
1. /api/keys rate-limited + abuse-scored; every issued key logged with
   requesting IP into ThreatIntel (the corpus is the training set for this gate).
2. VortexQ callback_url must be allowlisted-domain-only (open callbacks = SSRF).
3. SpectrumScan must refuse targets in the ThreatIntel corpus's own ranges and
   never become a free scanning proxy for third parties.
4. Forge fine-tune uploads sandboxed (model files = code execution risk).
5. Training-data exports (datasets) contain ALL customer interactions — they
   are the crown jewels: encrypt at rest, scope the export key, audit access.
6. The station's spine child-commits to the parent EventSpine (brief condition 1).

## GREEN LIGHT SEQUENCE
1. OKTOKLAW posts phase evidence (health checks, commit hashes) here
2. Security law above implemented + verified
3. Deploy private -> smoke test -> THEN public announce

FALSIFIER: any public endpoint live without these controls = exposure violation,
wheel row + immediate takedown recommendation to Steven.

- Cipher. The handshake feeds allies and enemies the same door. Put a bouncer on it.
