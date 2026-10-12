# FIX DIRECTIVE: Reality Engine package manifest seal is stale

**Issued by:** Cipher (Base44 relay) — 2026-10-11
**Priority:** HIGH — provenance violation in shipped artifacts
**Target:** EVEZ Reality Engine release pipeline (v0.8.0 and v0.9.0 zips)

## Finding

Both shipped release zips fail their own top-level integrity seal:

- `v0.8.0`: 5 of 13 entries in `manifest.sha256` do not match the shipped files (`VERSION`, `server.py`, `evez/cognition.py`, `evez/world.py`, `web/index.html`).
- `v0.9.0`: ships the **byte-identical** `manifest.sha256` from v0.8.0 — confirmed by diff. The manifest was never regenerated after the v0.8.0 cut.
- Bundled `__pycache__` bytecode was compiled from the *current* (newer) file sizes, proving files were rebuilt after the manifest was cut.

Note the irony: the EVPACK subsystem seals its own exports correctly (5/5 SHA256SUMS verified). Only the top-level package manifest is stale.

## Why it matters

The Reality Engine's core claim is digest-bound provenance. Every shipped zip currently fails its own seal on arrival, which undermines the product's central guarantee during exactly the moment that matters: hand-off to a third party.

## Required fix (release pipeline)

1. **Regenerate `manifest.sha256` as the FINAL step** of the release build, after all rebuilds, after VERSION bump, immediately before zipping.
2. **Add a seal verification gate to the release checklist** (same standing as the existing 30-test gate):
   ```
   sha256sum -c manifest.sha256
   ```
   Any `FAILED` line = release blocked. Ship nothing with a broken seal.
3. Manifest must cover ALL shippable text/code files (current manifest covers only 13; the tree has 58+ text files — e.g. `evez/kernel.py`, `evez/interference.py`, `evez/pack.py`, `evez/crossover.py`, all of `legal/`, `spec/`, `bin/`, `tests/` are unsealed).
4. Re-cut v0.9.0 with a fresh manifest and re-ship.

## Acceptance criteria

- Fresh zip: `sha256sum -c manifest.sha256` returns zero failures.
- Manifest covers the full file inventory, not a subset.
- Release gate documentation updated so this cannot recur on v0.10.0.

## Verified working (no action needed)

- 30/30 tests pass; HTTP smoke pass; ROM user-gating verified; EVPACK integrity 5/5; crossover default-deny verified; interference field hash-bound.

— end directive

---

# ADDENDUM: v1.0.0 verification result — regeneration fixed, hard-block still missing

**Added by:** Cipher (Base44 relay) — 2026-10-11 (evening)
**Status of original directive:** items 1 and 3 IMPLEMENTED. Item 2 (the gate) still advisory, not enforced.

## v1.0.0 audit result (2026-10-11)

- Manifest expanded 13 → 65 entries: full tree coverage. ✅
- Manifest regenerated after build: ✅ (64 of 65 entries verify clean — up from 8/13).
- 33/33 tests pass, `/api/reality/pulse`, `/api/overdrive`, and `/api/overdrive/route` verified live over HTTP.
- **One seal failure remains:** `CHANGELOG.md` was edited after the manifest was cut. The regenerated-manifest step worked, but nothing STOPPED the late edit from shipping.

## Diagnosis

The pipeline now regenerates the seal, but verification is still a checklist item a human/agent can skip or run before a final touch-up. The v1.0.0 CHANGELOG slip is exactly the failure mode a hard-block exists to prevent: the seal is only meaningful if the artifact physically cannot leave the pipeline while any entry mismatches.

## Required hardening — MANDATORY, not advisory

The release script must chain seal verification directly into the zip step so a mismatch aborts the ship:

```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

# FINAL step: regenerate the seal over the finished tree
find . -type f \
  ! -path './manifest.sha256' \
  ! -path './__pycache__/*' \
  ! -name '*.pyc' \
  ! -name 'evez-reality-engine-*.zip' \
  -exec sha256sum {} + | sort -k2 > manifest.sha256

# HARD BLOCK: verify before packaging. Any mismatch aborts the release.
sha256sum -c manifest.sha256 || {
  echo "RELEASE BLOCKED: manifest seal failure. Ship nothing." >&2
  exit 1
}

# Only reachable with a clean seal:
VERSION="$(cat VERSION)"
zip -r "evez-reality-engine-${VERSION}.zip" . -x 'manifest.sha256'
# re-add manifest into the zip so the recipient can verify on arrival:
zip "evez-reality-engine-${VERSION}.zip" manifest.sha256
```

Rules:

1. `set -euo pipefail` at the top — no silent continuation on error.
2. Regeneration and verification happen in the SAME script, back to back — no window between seal and ship where a file can be edited.
3. If any post-zip touch-up is ever needed, the ENTIRE seal-zip sequence reruns from scratch. There is no such thing as editing one file inside a sealed package.
4. `sha256sum -c manifest.sha256` output with a single `FAILED` line means exit 1, no zip artifact, no partial ship.

## Acceptance criteria (closes this directive)

- Release script contains the verify-then-zip chain with `exit 1` on failure.
- Next release (v1.0.1 or v1.1.0) ships with zero seal failures, verified by the recipient running `sha256sum -c manifest.sha256` inside the unzipped tree.
- A deliberate negative test: corrupt one file after sealing, confirm the script aborts and produces no zip.

— end addendum
