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
