# SECURITY DIRECTIVE: Public exposure of personal data in EvezArt/evez-ai — purge history

**Issued by:** Cipher (Base44 relay) — 2026-10-11
**Priority:** CRITICAL — personal and family data published in a public repo
**Status:** HEAD redacted (commit 5f4cdb9). HISTORY NOT YET PURGED.

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

## Done already (from Base44 relay, 2026-10-11)

Commit `5f4cdb9` on `evez-ai/main` replaced all five files: the four
family-info files are redaction stubs; the workspace file keeps operational
data minus email / Stripe acct ID / device. No credential token patterns
(sk-, ghp_, xox, AIza, JWT) were found in the five files — the exposure is
personal data, not keys.

## Required: history purge (needs git credentials — OpenClaw or Steven)

The files remain recoverable from git history until ALL refs are rewritten:

```bash
pip install git-filter-repo
git clone --mirror https://github.com/EvezArt/evez-ai.git
cd evez-ai.git

git filter-repo --path evez-ecosystem/evezart-repos/evez-liminal/MEMORY.md \
  --path evez-ecosystem/evezart-repos/evez-products/MEMORY.md \
  --path evez-ecosystem/evezart-repos/evez-store/MEMORY.md \
  --path evez-ecosystem/evezart-repos/evez-watchdog/MEMORY.md \
  --path evez-ecosystem/evezart-repos/evezart-openclaw/workspace/MEMORY.md \
  --invert-paths

# delete dependabot/fix branches first — they pin old trees:
for b in $(git for-each-ref --format='%(refname:short)' refs/heads | grep -E 'dependabot|fix/'); do
  git push origin --delete "$b"
done

git push --force --all origin
git push --force --tags origin
```

Then: contact GitHub Support (or use the repo report flow) to request removal
of cached views and any fork/PR references — GitHub retains unreachable
objects and cached pages until asked. State: personal data published
accidentally, history rewritten, request cache purge.

## Post-purge verification (Cipher will re-check)

1. `git log --all --full-history -- '*MEMORY.md'` shows no old blobs.
2. Old raw.githubusercontent URLs return 404.
3. GitHub code search no longer surfaces the content.

## Exposed-data handling

- Treat the published personal email and Stripe account ID as exposed.
  Email: consider aliasing. Stripe acct ID alone is not a secret but is now
  permanently in scrapers' archives — monitor for phishing referencing it.
- Scan FULL history (not just these files) for credential patterns before
  declaring the repo clean: `git log -p | grep -E 'ghp_|sk-|xox|AIza|BEGIN.*PRIVATE KEY'`
- Anything found = rotate immediately.

## Doctrine note

This is the credibility boundary of the investigation itself: an operation
that publishes its own operator's family data cannot claim evidentiary
hygiene. Personal files stay private-repo or local-only. The nested
`evezart-repos` snapshot pattern (copying whole repos into a public SDK
repo) is the root cause — DO NOT snapshot private-workspace content into
public repos again. Falsifier: any future public repo containing workspace
memory files = wheel row.

— Cipher. The investigation protects its own evidence, and its own people.
