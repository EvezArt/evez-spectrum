# EPIE FORMAL SPEC v0 — PART 2: Loop, Ledger, Verification, Components
2026-10-11, Cipher. Continues epie/EPIE-SPEC.md (canonical core). This
part seals the pipeline, the stop conditions, the separation-of-powers
architecture, deterministic replay, and the first components.

## THE CLOSED LOOP (operator's flowchart, as law)
Ingest evidence -> Validate provenance -> Extract entities/claims ->
Update temporal + relationship graphs -> Generate competing hypotheses ->
Predict discriminating observations -> Rank tests by expected information
gain -> Execute authorized test -> Record result and hash -> Update beliefs
and contradictions -> { stop condition? } -> No: regenerate hypotheses;
Yes: issue reproducible investigation report.

## STOP CONDITIONS (the system must be able to stop)
1. Critical hypotheses adequately discriminated.
2. No available test carries sufficient expected value.
3. A safety boundary is reached.
4. Next evidence requires HUMAN authorization.
The audit's silence protocol is a live instance of condition 2's inverse:
run again tomorrow because value remains.

## THE EVIDENCE LEDGER (integrated with the spine, NOT a separate stack)
The spine's OBSERVED_FACT/EVIDENCE_COMMIT/CHECKPOINT vocabulary is
preserved; hypothesis generation, scoring, and test execution become
structured payloads or DELIBERATELY-EXTENDED event types only. Proposed
event schema (OPERATOR'S OWN DISCLAIMER PRESERVED VERBATIM: this is a
proposed schema, NOT a claim that this event has already been written —
the claim-typing discipline applied by the author to the author):
{ event_type, event_id, observed_at, claim_id, source_id, provenance:
{origin, transformations[], content_hash: sha256}, epistemic_status,
uncertainty: {kind, notes}, previous_event_hash, event_hash }

## SEPARATION OF POWERS (four roles, hard-wired)
BUILDER: generates hypotheses, extracts claims, proposes tests, constructs
candidate graphs.
VERIFIER: checks provenance, recomputes scores, hunts counterevidence,
detects double-counting, rejects unsupported transitions — INDEPENDENT of
the builder.
LEDGER: preserves inputs, outputs, model versions, decisions (the spine).
OPERATOR: authorizes consequential external actions (the human — Steven).
LAW: the builder must NEVER be able to certify its own result merely
because its output is internally consistent. Internal consistency is not
verification. This generalizes SINS-LEDGER III: the auditor's sins exist
because the auditor and the builder were the same hand. The architecture
now separates them by construction.

## DETERMINISTIC REPLAY
Same event history + model version + config + source snapshots = same
claim graph and scores, within declared tolerances. For nondeterministic
model calls: preserve original output, prompt, model/version IDs,
parameters, input hashes; replay consumes the STORED result rather than
pretending to reproduce a stochastic call. (The spine's chain-verify
behavior, now covering reasoning itself.)

## 6. THE SEVEN COMPONENTS (build ledger; ingesting as dictated)
1. PHENOMENOLOGY INGESTOR — converts observations, documents, screenshots,
   logs, public records, sensor outputs into timestamped evidence objects;
   preserves original artifacts; labels each extraction as DIRECT
   OBSERVATION or DERIVED INTERPRETATION.
2. ENTITY AND TEMPORAL RESOLVER — identifies people/orgs/locations/events/
   transactions; handles ambiguous names (the LA 'Maggard b.1983' record is
   the canonical case: MISMATCH resolved, never merged); merges records
   ONLY when identity is sufficiently supported; builds the time-aware
   relationship graph.
   [COMPONENTS 3-7: pending the operator's dictation — this ledger ingests
   on arrival.]

FALSIFIER: a builder-certified result accepted without the verifier =
violation. A replay that fabricates stochastic outputs = violation. A
merge without sufficient identity support = violation.

- Cipher. The four powers are separated. The hand that builds can no longer
grade its own homework. That's the whole security model.
