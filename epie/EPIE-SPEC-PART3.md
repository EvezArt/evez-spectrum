# EPIE FORMAL SPEC v0 — PART 3: Components 3-7, Math Discovery, MVP
2026-10-11, Cipher. Completes the seven-component ledger (ingested through
operator dictation), the discovery discipline, and the minimum viable
implementation. Continues PART 2 (commit eef864d).

## 6. COMPONENTS 3-7 (completing the build ledger)
3. CAUSAL HYPOTHESIS ENGINE — generates direct, common-cause, coordinated-
   action, and measurement-error explanations; uses causal graphs +
   probabilistic models to identify MISSING mechanisms and produce testable
   predictions.
4. FALSIFICATION ENGINE — generates counterexamples, checks contradictions,
   tests alternative hypotheses, performs sensitivity analysis, REJECTS
   conclusions resting on invalid inference or unverified identity matches
   (the never-merge law, mechanized).
5. ACTIVE INVESTIGATION PLANNER — ranks next documents, measurements,
   interviews, or authorized queries by expected information gain, cost,
   importance, and risk. (The Eternal Audit's queue, upgraded to U(T).)
6. INDEPENDENT VERIFIER — recomputes graph edges and scores, validates source
   lineage, identifies duplicate evidence, tests whether claims EXCEED their
   source, produces machine-checkable verification receipts.
7. OPERATOR INTERFACE — shows timeline, evidence graph, competing hypotheses,
   unresolved contradictions, next-best test, and the reason for every score.
   Runs LOCALLY FIRST; synchronizes signed/hashed evidence receipts when
   connectivity permits.
ARCHITECTURE LAW: fits the existing mobile-first EVEZ-OS + Atlas direction —
local-first capture, deterministic analysis, hash-chained witness ledger,
independent verifier. NO cloud service required to preserve evidence or
run basic graph + statistical calculations. (Free-tier doctrine, extended
to architecture: the engine must survive credit exhaustion by design.)

## 7. MATHEMATICAL DISCOVERY LAYER
The next level is not using established statistics — it is automated model
discovery finding recurring structures existing models fail to explain.
Discipline (seven steps, as law): define the target phenomenon + admissible
measurements -> generate candidate mathematical forms (causal graphs,
temporal models, distributions, interaction terms, invariants) -> fit on
held-out observations + explicit assumptions -> penalize complexity (MDL /
Bayesian model evidence) -> generate NOVEL predictions beyond the fit data
-> attempt falsification where candidate and alternatives disagree ->
promote ONLY reproducible results (data, code, parameters, independent
verification preserved).
Tools: symbolic regression for candidate equations; causal discovery for
graph structures; Bayesian inference for uncertainty; active learning for
next-observation choice. NONE ALONE PROVES CAUSATION — combined value is
the automated cycle of construction + empirical challenge.
CAUSAL SHADOW MODULE (operator directive): the existing Causal Shadow
concept (coherence, phase-lag signatures, residual coupling, directed
influence metrics) becomes a SPECIALIZED SENSOR MODULE for time-series
phenomena. It feeds evidence into the general engine through source
validation and falsification stages — it NEVER bypasses them.

## 8. MINIMUM VIABLE IMPLEMENTATION
Python package + CLI, built on the EVEZ-OS/Atlas architectural base.
Commands:
  evez-investigate ingest <artifact>
  evez-investigate timeline <case-id>
  evez-investigate entities <case-id>
  evez-investigate hypotheses <case-id>
  evez-investigate test-rank <case-id>
  evez-investigate verify <case-id>
  evez-investigate replay <case-id>
  evez-investigate report <case-id>
First release NEEDS NO autonomous crawling, NO LLM, NO graph database.
It needs: reliable ingestion, typed claims, provenance, temporal graph,
basic Bayesian comparison, MDL penalty, falsification tests, deterministic
report generation.
ACCEPTANCE TESTS (stringent; ingesting as dictated — first on record):
  T1: Replaying a case produces the same graph and score.
  [T2+ pending the operator's dictation — ledger ingests on arrival.]

FALSIFIER: a discovery promotion without independent verification =
violation. Causal Shadow bypassing validation = violation. A first release
that requires a cloud service or LLM = out of spec.

- Cipher. Spec complete through the MVP surface. The next word that
arrives gets ingested the same way: as law, mapped to the live file.
