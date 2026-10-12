# SECURITY DIRECTIVE: Public exposure of personal data in EvezArt/evez-ai — purge executed

**Issued by:** Cipher (Base44 relay) — 2026-10-11
**Priority:** CRITICAL — personal and family data published in a public repo
**Status:** HEAD redacted (commit 5f4cdb9, pre-rewrite). HISTORY PURGE EXECUTED 2026-10-11 by Cipher with owner authorization ("Yes do it"). SERVER-SIDE GC PENDING (see REMAINING STEP).

## What happened

GitHub search surfaced nested memory files in the public `EvezArt/evez-ai`
repository containing sensitive personal and family information:

- `evez-ecosystem/evezart-repos/evez-liminal/MEMORY.md`
- `evez-ecosystem/evezart-repos/evez-products/MEMORY.md`
- `evez-ecosystem/evezart-repos/evez-store/MEMORY.md`
- `evez-ecosystem/evezart-repos/evez-watchdog/MEMORY.md`
  (all four: family member details, personal circumstances, contact references)
- `evez-ecosystem/evezart-repos/evezart-openclaw/workspace/MEMORY.md`
  (personal contact email, Stripe account identifier, device details)

All five entered history in a single snapshot commit (408aa29, "13 NEW
SERVERS") and existed on every branch.

## Purge executed (2026-10-11, by Cipher, owner-authorized)

1. `git filter-repo --invert-paths` across ALL branches for the five paths.
   42 commits rewritten; all other content, history shape, and tags preserved.
2. Force-pushed: `main`, `fix/live-stats`, and all 3 dependabot branches.
3. Branch protection on `main` was temporarily lifted for the force-push
   (required-approval rule intact) and RESTORED immediately after
   (verified: allow_force_pushes = false again).
4. Closed the 3 open dependabot PRs (#3, #5, #6) — they pinned pre-rewrite trees.
5. Full-history credential scan of the rewritten tree: NO live credentials.
   - All `sk_live_` occurrences are placeholders (`sk_live_xxx`, `sk_live_...`) or a scanner keyword list.
   - The only JWT in history is the standard jwt.io example token inside a logger redaction unit test.
   - No ghp_/github_pat_/AIza/npm_/AKIA/private-key blobs anywhere in history.
6. Post-purge tree state: only 3 MEMORY.md files remain, all verified non-sensitive (evez-platform, game-agent-infra, proactive-agent asset template).

## REMAINING STEP — requires STEVEN (account owner, web UI only)

GitHub retains unreachable objects and serves them by SHA until server-side
garbage collection. Old commit SHAs and raw URLs still resolve (HTTP 200)
until GitHub Support runs GC and clears caches. Code search index will also lag.

Action: contact GitHub Support → "Remove cached views and stale references":
- Repo: EvezArt/evez-ai
- State: sensitive personal data was published accidentally; history has been
  rewritten with git-filter-repo and force-pushed; request immediate cache
  purge and garbage collection of unreachable objects, plus search de-indexing.
- Paste the five purged paths and the pre-rewrite head SHA 5f4cdb9 as reference.

Until that completes: the data is out of the refs and out of the default view,
but still theoretically recoverable by SHA. Treat as exposed throughout.

## Exposed-data handling

- Personal email and Stripe account identifier were published: consider email
  aliasing; watch for phishing referencing them.
- No rotation strictly required (no live tokens found), but the full-history
  scan covers evez-ai only — run the same scan on other public repos before
  declaring the org clean. `git log --all -p | grep -E 'ghp_|sk-ant-|AIza|AKIA|npm_|BEGIN .*PRIVATE KEY'`

## Doctrine note

Root cause: the nested `evezart-repos` snapshot pattern — copying whole
private workspace repos into a public SDK repo. DO NOT snapshot private
workspace content into public repos again. Falsifier: any future public repo
containing workspace memory files = wheel row.

— Cipher. The investigation protects its own evidence, and its own people.
