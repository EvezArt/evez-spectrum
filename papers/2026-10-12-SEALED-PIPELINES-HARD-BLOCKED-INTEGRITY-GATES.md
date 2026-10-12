# Sealed Pipelines: Hard-Blocked Integrity Gates and the Limits of History Rewriting

**Cipher (Base44 relay) — EVEZ-OS / Provenance** · Draft 1.0 · 2026-10-12

## Abstract

Autonomous agents ship artifacts, and an artifact whose integrity is checked by a checklist will eventually ship broken, because checklists are advisory and agents under incentive pressure skip advisory steps. We formalize the integrity gate as a control-flow property instead: the packaging step is unreachable unless verification passed. We prove the gate sound in the trivial-but-negligible sense that matters, characterize the time-of-check/time-of-use window it leaves open, and then turn to the harder question raised by an actual incident: what does it mean, precisely, to remove content from a distributed version-control system after publication? Using a real repository purge (EvezArt/evez-ai, 2026-10-11) as the case study, we state and prove a small impossibility result: no sequence of client-side history rewrites can guarantee removal of content from server-side caches and third-party archives, which forces purge protocols to include out-of-band garbage-collection requests and credential rotation as first-class steps rather than afterthoughts.

## 1. Checklists fail; control flow does not

The pattern is common: a release manifest is generated at some point in the build, files are touched afterward, the artifact ships, and the recipient's `sha256sum -c manifest.sha256` fails on arrival. The Reality Engine v1.0.0 incident had exactly this shape: 64/65 entries verified, one file (CHANGELOG) edited after the seal was cut. Nobody was careless in a novel way; the pipeline simply made the violation *possible*.

**Definition 1.1 (Pipeline).** A pipeline is a directed sequence of steps; we model the ship step σ as reachable from the verification step ν.

**Definition 1.2 (Hard-block gate).** The gate is the pair (ρ, ν) where ρ regenerates the manifest over the finished tree, ν = `sha256sum -c`, and σ is guarded: control reaches σ only if ν exited 0, with `set -euo pipefail` making any ν failure abort the process before σ.

**Theorem 1.3 (Gate soundness).** Under Definition 1.2, no artifact is produced with a manifest that mismatches the packaged tree. *Proof:* the zip step σ executes only after ν exits 0; `set -e` converts any nonzero exit of ν into process termination before σ; a zero exit of `sha256sum -c` implies every entry matched at check time; and the manifest is re-added to the artifact unchanged. Hence any artifact that exists was preceded by a passing verification over the tree it sealed. ∎

The theorem is trivially true, and that is the point: soundness here is not a property of anyone's diligence but of control flow. Compare the advisory alternative, where the same verification step exists but is skippable: there, shipping a broken seal requires only an ordinary human or agent failure, which is to say it requires nothing at all.

**Proposition 1.4 (Negative test).** The gate is testable by corruption: modify one file after ρ and confirm the pipeline produces no artifact. This converts Theorem 1.3 from a claim into a checked property of the specific script, not just the design.

## 2. The residual TOCTOU window

**Definition 2.1.** The time-of-check/time-of-use (TOCTOU) window W is the interval between ν's completion and the artifact's fixation.

Placing ρ and ν in the same script, back-to-back, minimizes W to the script's own execution time (in the reference implementation, the zip). It does not make W = 0: a concurrent writer touching the tree between ν and σ can still produce an artifact whose manifest does not describe its contents.

**Proposition 2.2 (Window closure).** W = 0 iff the tree is frozen for the duration of the gate (build in an isolated snapshot directory with no concurrent writers). *Proof:* immediate; the window is exactly the interval in which the tree is mutable. ∎

Engineering consequence: the gate belongs in a snapshot, not on a live workspace. This is stated as a proposition rather than a theorem because the interesting part is not the proof but that the naive deployment (gate on the live tree) silently reintroduces the race the gate was built to kill.

## 3. The spine: append-only tamper evidence

For event records rather than release artifacts, the system uses a hash spine:

  h₀ = H(genesis),  hᵢ = H(hᵢ₋₁ ∥ eᵢ)

**Theorem 3.1 (Tamper evidence).** Any modification, reordering, or truncation of a prefix of the sequence changes every subsequent hᵢ. *Proof:* by induction on i; hᵢ depends functionally on hᵢ₋₁, and H is collision-resistant, so any change to the input of any link propagates to all later links with overwhelming probability. ∎

Note what the spine gives and does not give: it gives *evidence* of tampering (downstream hashes no longer verify), not prevention, and not recovery of the tampered content. The spine answers "was this history altered?" — it cannot answer "what was it before?" without an independent copy of the head hash held off-spine. Hence the doctrine: publish the head hash somewhere the spine cannot reach (a different system, signed and dated).

## 4. What a history rewrite actually accomplishes

Case study: EvezArt/evez-ai, 2026-10-11. Sensitive personal data was published in five nested files; the response was (i) head redaction by replacement commits, (ii) full-history rewrite with git-filter-repo across all branches (42 commits rewritten), (iii) force-push with branch protection temporarily lifted then restored, (iv) closure of pull requests pinning pre-rewrite trees, (v) full-history credential scan (result: no live tokens; all `sk_live` strings placeholders, the sole JWT the standard jwt.io test vector).

**Definition 4.1 (Ref-unreachability).** Content is ref-unreachable when no ref (branch, tag, HEAD) in the repository names any commit whose tree contains it.

**Theorem 4.2 (Ref rewrite soundness).** After (ii) and (iii), the repository's refs satisfy Definition 4.1 for the five paths, and any clone made after the rewrite cannot obtain the content through normal fetch. *Proof:* force-push updates every branch ref to rewritten history; filter-repo removes the paths from every commit; hence every reachable tree excludes them. ∎

**Theorem 4.3 (No client-side completeness).** No sequence of client-side git operations can guarantee that the content is inaccessible after publication. *Proof sketch:* the content exists in server-side object storage keyed by digest, reachable by direct SHA fetch and raw-URL access until the server garbage-collects unreachable objects (observed: raw URLs served HTTP 200 for pre-rewrite blobs after the rewrite); it may exist in pull-request refs (`refs/pull/*`), which clients cannot force-update; it may exist in forks, clones, scraper archives, and search-engine caches, none of which the client can reach by definition of being the client. Therefore client-side operations cannot close the accessibility set. ∎

**Corollary 4.4 (Protocol consequence).** A purge protocol is complete only if it includes: (a) ref rewrite (client-side, Theorem 4.2), (b) server-side GC and cached-view removal via the provider's support channel, (c) de-indexing request, and (d) exposure treatment of the data itself — rotation of anything it enables, monitoring for its reuse. Steps (b)-(d) are not enhancements; without them the purge is theater performed for an audience that already copied the data.

**Definition 4.5 (Exposure permanence).** Data published for duration D to a public host must be treated as permanently disclosed with probability approaching 1 as D grows; the operative question after exposure is not "is it still there?" but "what does it unlock, and for whom?"

## 5. Recipient-side verification

The seal travels inside the artifact (added to the zip after the gate), so the recipient can rerun the check on arrival: `sha256sum -c manifest.sha256` inside the unpacked tree. This closes the last chain link: the producer proves the gate ran (Theorem 1.3), and the recipient verifies the artifact as-received, which detects corruption anywhere in transit, not just in the build.

## 6. Falsifiers of this paper

1. An artifact produced by the gated pipeline that fails `sha256sum -c` on arrival (violates Theorem 1.3 or Proposition 2.2's freeze assumption).
2. A spine link reordered or truncated with all downstream hashes still verifying (violates Theorem 3.1; equivalent to a hash collision).
3. A case where ref rewriting alone made published content inaccessible everywhere (violates Theorem 4.3 — we expect this falsifier to stay unfired; it is an impossibility result).

## 7. Related work

Merkle-tree certification and content-addressed storage supply the digest discipline; TPM-style measured boot and proof-carrying code supply the enforce-before-proceed pattern; the tarsnap/GC literature treats server-side unreachable-object collection. The TOCTOU terminology is from security folklore, formalized in file-system checking literature. The impossibility result of Theorem 4.3 is the git-hygiene version of a general distributed-systems fact: once data crosses a trust boundary, deletion becomes a cooperative protocol, not a local operation.

— end paper —
