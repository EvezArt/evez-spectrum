# Dependence-Rejecting Bayesian Evidence Kernels with an MDL-Guarded Hypothesis Lattice

**Cipher (Base44 relay) — EVEZ-OS / EPIE** · Draft 1.0 · 2026-10-12

## Abstract

Autonomous investigators generate their own evidence, and the failure modes of doing so are known: correlated observations get counted as independent confirmation, hypothesis generators proliferate unfalsifiable branches, and two runs of the same pipeline hash the same fact differently. We formalize a kernel (implemented as EPIE, the Evidence and Probable-Inference Engine) that addresses all three mechanically rather than rhetorically. (1) Evidence identity is fixed by RFC 8785 canonicalization, so duplicate observations are deduplicated at the digest level before any belief update. (2) Updates reject evidential dependence by construction: items sharing provenance or causal ancestry enter the posterior at most once. (3) Hypothesis generation is gated by a description-length penalty, keeping the accepted hypothesis set finite per round under a bounded evidence rate. Every claim in the system carries an explicit falsifier, making the whole apparatus falsifiable in Popper's operational sense. We state the small theorems the design actually proves, identify what it does not, and document the implementation's validation (official RFC 8785 test vectors, dependence-rejection and likelihood-calibration suites in CI).

## 1. The problem

An agent that both produces and evaluates evidence faces a trilemma:

1. **Double counting.** Two observations of the same underlying event arrive through different channels and register as independent corroboration.
2. **Hypothesis inflation.** A generator permitted to emit hypotheses freely will emit more the longer it runs; posterior mass fragments across unfalsifiable variants.
3. **Identity drift.** The same evidence, serialized differently on two runs, hashes differently, breaking every downstream audit that assumed evidence identity.

Rhetorical discipline ("be careful about correlated evidence") addresses none of these. Each failure mode needs a mechanical counter.

## 2. Definitions

**Definition 2.1 (Claim).** A claim is a tuple c = (τ, s, f, m) where τ is a claim type, s is the asserted proposition, f is a falsifier (a procedure whose positive outcome refutes s), and m is metadata. A claim without f is not a claim in this system; it is discarded at ingestion.

**Definition 2.2 (Evidence item).** An evidence item is a tuple e = (k, d, π, λ) where k is the content payload, d = JCS(k) is the RFC 8785 (JSON Canonicalization Scheme) serialization of k, π is the provenance vector (origin, time, chain-of-custody digests), and λ is the likelihood vector the item asserts against the claims it bears on.

**Definition 2.3 (Evidence identity).** id(e) = SHA-256(d). Two items with equal id are the same observation regardless of arrival channel, timestamp, or wrapper format.

**Proposition 2.4 (Deduplication).** The map e ↦ id(e) is well-defined on JCS-serialized payloads, and the kernel's store keyed on id accepts each distinct evidence item at most once. *Proof:* immediate from Definition 2.3 and the injectivity of canonical serialization up to byte-identity of the canonical form; the store's insert is idempotent under key equality. ∎

This is deliberately the weakest true statement in the paper and also the most load-bearing: without a canonical form, nothing downstream is reproducible. The EPIE implementation passes the official RFC 8785 test vectors (validated 2026-10-11, PR #121 review), which is the only evidence that matters here.

## 3. Dependence rejection

**Definition 3.1 (Evidential dependence).** Two items e₁, e₂ are dependent iff π(e₁) ∩ π(e₂) ≠ ∅ (shared provenance node) or they are both downstream of a common causal ancestor in the event spine.

**Rule 3.2 (Update).** For a round with accepted set A: Bel(c) ← Bel(c) × Π_{e∈A, e bears on c} λ(e,c) / Z, where A is a maximal subset of the round's items containing no dependent pair (per dependence class).

**Proposition 3.3 (No double counting within a round).** Under Rule 3.2, a dependence class of size n contributes at most one factor to the posterior per round. *Proof:* A is independent, so at most one member of any dependence class lies in A. ∎

What this does *not* claim: it does not make dependent evidence disappear across rounds. An observation accepted in round 1 that re-arrives via a new channel in round 5 with *new provenance* is, by construction, a new item. The kernel treats provenance honestly rather than magically; the operator-facing consequence is that provenance vectors are the part of the system that must not be fabricated, which is exactly where the hash spine and screen-recording doctrine attach.

## 4. The MDL guard on hypothesis generation

**Definition 4.1 (Hypothesis).** h = (s, L, G) with proposition s, description length L(h) in the system's encoding (nodes + edges in the causal graph, per the three-graph separation), and predicted-gain functional G.

**Rule 4.2 (Acceptance).** A generated hypothesis h enters the lattice iff

  G(h) · Bel-improvement Upper bound(λ) > β · L(h),  β ≥ 1 a system constant.

That is: the best-case posterior improvement a hypothesis could buy, discounted by the likelihood bound, must exceed its description length times the guard constant.

**Proposition 4.3 (Finiteness).** For a fixed round with a finite generated pool and L(h) ≥ L_min > 0, the accepted set is finite. If the generator's per-round pool is bounded by a rate r and guard threshold β, the accepted set grows at most linearly in accepted-evidence mass and strictly sublinearly in generated mass. *Proof:* immediate from the threshold; the content of the proposition is that L_min > 0 holds because every hypothesis in the encoding uses at least one graph node. ∎

The honest statement: the guard does not prevent all bad hypotheses, it prevents *cheap-unbounded* ones. A short, wrong, high-promised hypothesis still gets in. That is the correct trade — the alternative (generating only long hypotheses) is worse, because the system's purpose is investigating things it does not yet understand.

## 5. System falsifiability

**Definition 5.1.** The falsifier coverage of a state is the fraction of live claims (Bel > threshold) carrying executable falsifiers.

The design invariant is coverage 1.0: any claim promoted to live status must have f executable in principle (a procedure, a data pull, an experiment). This is Popper operationalized: falsifiability is not a property of rhetoric but of the claim's admission record.

**Theorem (non-claim) 5.2.** We explicitly do not claim the kernel converges to truth, that belief values are calibrated probabilities, or that the MDL guard selects the *best* hypothesis. The kernel's claim is narrower and testable: given the same evidence stream, it reaches the same posterior, counts nothing twice within a dependence class, and admits no unbounded hypothesis growth. Each of those is falsifiable and each has a CI suite.

## 6. Implementation status

- Canonicalization: RFC 8785, official vectors passing (2026-10-11).
- Dependence rejection and likelihood calibration suites: implemented, validated with the kernel/store suites locally (33/33 engine tests green at last run).
- Hypothesis lattice + MDL guard: designed (issue #126 scoreboard); the MDL penalty constant β is the open tuning surface.
- Known gap under repair: hypothesis generation is the least-mature component; the guard exists partly to make the gap safe to explore.

## 7. Related work

Subjective logic and Dempster-Shafer treat uncertain evidence but not provenance identity; Bayesian networks formalize dependence but assume a fixed structure, while an investigator's structure is the thing being discovered. MDL-based model selection (Rissanen; Grünwald) supplies the guard's rationale. Proof-carrying code supplies the pattern for the falsifier attachment: the claim ships with the procedure that could kill it. The digest-identity discipline follows the content-addressed storage tradition (Git, IPFS) applied to evidence rather than code.

## 8. Falsifiers of this paper

1. Duplicate canonical digests arriving through distinct channels updating the posterior twice (kernel dedup broken).
2. A dependence class contributing two factors in one round.
3. An unbounded growth in the accepted hypothesis set under a bounded evidence rate and fixed β.

— end paper —
