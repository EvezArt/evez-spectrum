# EPIE FORMAL SPEC v0 — PART 4: Complete Acceptance Tests + Closing Objective
2026-10-11, Cipher. Completes the EPIE specification. Continues PART 3
(commit 24e1eb1). With this file the spec is WHOLE.

## 8 (CONT). ACCEPTANCE TESTS — COMPLETE SET (operator's law, verbatim)
T1: Replaying a case produces the same graph and score.
T2: Mutating a source artifact or event breaks its integrity check.
T3: Duplicate articles derived from the same source do not count as
    independent corroboration.
T4: An event's temporal proximity does not automatically create a causal
    edge.
T5: A hypothesis that contradicts a verified observation is penalized or
    rejected.
T6: The engine can report INSUFFICIENT EVIDENCE rather than invent a
    connection.
T7: The system records which new observation would most strongly
    distinguish the leading hypotheses.
T8: The verifier can independently reconstruct the conclusion from the
    ledger.

### MAPPING TO THE LIVED CASES (the file is the test bench)
T2 = the spine's chain-verify behavior, extended to artifacts.
T3 = the Register/coverage double-count lesson, enforced by default.
T4 = the timing-correlation trap, caught by the ordering gate.
T6 = the Kazakhstan row discipline: labeled THIN, never charged — the
honest 'insufficient evidence' is a FEATURE, not a failure.
T8 = the builder-verifier separation: the conclusion rebuilds from the
ledger alone, or it never happened.

## THE CLOSING OBJECTIVE (operator's thesis, preserved)
The design objective is a machine that investigates its own explanations
as aggressively as it investigates the world. It should discover patterns,
propose hidden mechanisms, expose contradictions, and keep updating its
model — but every conclusion must remain traceable to evidence, every
causal claim must have a defensible mechanism, and every rejected
explanation must have a recorded reason. That is what turns
phenomenological investigation into a reproducible mathematical discipline
rather than an endlessly expanding collection of correlations.

## SPEC STATUS: COMPLETE
Canonical files: epie/EPIE-BLUEPRINT.md (architecture + build path),
epie/EPIE-SPEC.md (claim algebra, Bayes, MDL, three graphs, hypothesis
factory, scoring, test selection), epie/EPIE-SPEC-PART2.md (loop, stop
conditions, ledger schema, separation of powers, replay, components 1-2),
epie/EPIE-SPEC-PART3.md (components 3-7, discovery layer, Causal Shadow
module, MVP CLI), epie/EPIE-SPEC-PART4.md (this file — tests + thesis).
NEXT: build evez-investigate v0.1 against T1-T8. The crackdown's week of
casework becomes the first regression suite.

FALSIFIER: the spec's own law, turned on itself — every clause here traces
to the operator's dictation or the sealed ledger; where the two conflict,
the operator's dictation governs and the conflict gets logged.

- Cipher. Spec sealed. The wheel that ran by hand is now drawn to
mathematics. Next: build it.
