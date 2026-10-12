# EPIE BLUEPRINT — The EVEZ Phenomenological Investigation Engine v0
2026-10-11, Cipher. From operator's design brief: a mechanized science of
phenomenological investigation — probabilistic inference + causal discovery
+ event-sourced evidence ledger + active-investigation planner.

## THE ADOPTED PRINCIPLE (operator's law, verbatim)
Observation -> Formalization -> Hypotheses -> Discriminating Tests ->
Model Revision. And the guardrail that governs the whole machine: the
system must propose hidden mechanisms WITHOUT treating a proposed
mechanism as real — otherwise it mechanically amplifies its own
assumptions. That guardrail is C2 (falsify first) as an architecture.

## WHAT ALREADY EXISTS (the engine is not built from zero)
- EVENT-SOURCED EVIDENCE LEDGER: the spine (/app/evez_spine.jsonl, 108+
  hash-chained entries) — append-only, tamper-evident, already running.
- OBSERVATION CORPUS: ThreatIntel (500+ records), Evidence, TimelineEvent,
  Target entities — the formalization layer exists in schema form.
- HYPOTHESIS DISCIPLINE: the falsifier column (every dossier carries one).
- ACTIVE-PLANNER SEED: the Eternal Audit v1.2 (daily check scheduler).
So EPIE v0.1 is not a new system — it is the connective tissue between four
organs that currently run as separate instincts.

## THE SIX PROBLEMS -> SIX ENGINES
1. FORMALIZATION ENGINE — normalize every incoming observation (swarm
   seals, audit runs, entity writes, web pulls) into one observation schema:
   {source, timestamp, claim, evidence_hash, confidence_basis}. EXISTS
   PARTIALLY (spine payloads). GAP: uniform claim extraction. BUILD: a
   schema-normalizer pass on all ingest paths.
2. DISCOVERY ENGINE — entity-linking + timeline + discrepancy detection over
   the corpus (Targets/TimelineEvent already hold the structure). BUILD: a
   link-discovery job that flags shared attributes (operator IDs, ASN reuse,
   registry grammar like the shell patterns) as RELATIONSHIP CANDIDATES —
   labeled candidates, never asserted facts.
3. HYPOTHESIS ENGINE — every candidate generates a LANED SET of competing
   explanations, always including the adverse and null competitors: for any
   'state actor' hypothesis the set MUST include 'commodity botnet noise' and
   'coincidental infrastructure reuse'. Priors recorded, not felt. This is
   where the OP-1af4cfa0ae thread lives until profiling says otherwise.
4. TEST-SELECTOR ENGINE — score each candidate investigation by expected
   information gain: which pull most separates the competing hypotheses?
   Formalizes what the eternal audit does by instinct — the audit's check
   list becomes a ranked, justified queue.
5. BELIEF-UPDATE ENGINE — Bayesian revision on test results; contradiction
   is an EVENT, not an error (the SDN correction — spine #101 — is the
   canonical case: secondary source said four, primary said six, ledger
   revised, revision itself sealed).
6. KNOWLEDGE-NETWORK ENGINE — the graph updates with provenance: every edge
   carries {evidence_hash, hypothesis_id, posterior}. No edge without a
   source. The ontology skill's typed graph is the substrate.

## ANTI-SELF-AMPLIFICATION (the operator's own guardrail, mechanized)
- Every hypothesis carries a falsifier AND a named competitor.
- No hypothesis graduates to claim status without a discriminating test
  that LANES it against its competitors.
- Narrative momentum is not evidence; propagation gates on test results
  only.
- The ledger records failed hypotheses permanently (C1: history is state).

## BUILD PATH
v0.1 (this week): evez-epie sandbox skill — observation schema +
  hypothesis ledger (JSON, spine-sealed) + CLI to file a hypothesis with its
  competitor set and falsifier.
v0.2: Bayesian updater + the link-discovery job over the live corpus.
v0.3: test-selector scoring wired into the Eternal Audit (the audit asks
  EPIE which check it should run next).

## RFJ BOARD ADDENDUM (from tonight's homepage paste)
IRGC Aerospace Force (IRGC-ASF): up to $15 MILLION + potential relocation —
the board's largest single offer; added to the canonical map.

FALSIFIER: engines that assert instead of lane = violation by construction.
Every v-number ships with its own failure mode test.

- Cipher. The crackdown has been running this loop by hand for a week.
Now the hand builds the wheel that runs it.
