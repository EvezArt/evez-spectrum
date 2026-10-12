# evez-investigate v0.1 — BUILT AND ACCEPTED
2026-10-11, Cipher. Operator order: "Build it." Spec: epie/EPIE-SPEC.md
+ PART2/3/4 (commits 7c6f9a3..ff74eec). This is the v0.1 deliverable.

## ACCEPTANCE: 8/8 (T1-T8, law verbatim from PART4)
All tests run against the crackdown's own week as the regression bench:
- T1 replay determinism — state hash 1c726844938bd1f1 stable across reloads
- T2 mutation breaks integrity — hash mismatch at event 1
- T3 double-count guard — 2 press claims from one press release = 1 source
- T4 no auto causal edge — adjacent-day pair rejected; pathway pair gated in
- T5 contradiction penalized — contradicted COORDINATED 0.0429 (lowest
  substantive); ERROR top substantive; null may lead honestly
- T6 insufficient evidence is honest — no LEADING verdict invented, all UNRESOLVED
- T7 records most distinguishing test — T-registry-pull IG=0.0896 >
  T-news-sweep IG=0.0000
- T8 independent verifier reconstruction — receipt 1bd2772d9ea29519,
  conclusion rebuilt from ledger alone, findings=0

## THE SUITE CAUGHT THE ENGINE TWICE (build log, honest)
Two real defects found and fixed during acceptance, not after:
1. IG default semantics: an unspecified hypothesis in a test outcome is
   UNINFORMATIVE (1/K across the outcome partition), never impossible (EPS).
2. Outcome normalization: per-hypothesis likelihoods must sum ~1 across
   outcomes; unmodeled outcome mass carries no information (contributes H0).
Both were found by T7 refusing to pass. The suite works.

## FILE MANIFEST (sha256, canonical build)
- __init__.py  7f9cc890571f1b36b17f994c40cde97984a5c5a291073a867922929cd54dfd1f
- __main__.py b2506ef9550fedcdb7cbb41eb320f483202153d652e5623b3177d8af73614ad9
- core.py      43cf98d39e64dee76e118b5cc390521fc80cff75ed69a74d54bcb2f8f4c20e5d
- engines.py   adf3a52c7c95cad6a85147325804b40a3115bab0edf85a6211b0b052c88c9f87
- verifier.py  79137c93f393357e6025b2c3ba6471d894153d9133e22fc728fce9f250eea8c7
- acceptance.py a22678cb21ff340d0b28a9c12302454e68c64fcce916f81c31e1b589f0db4576
Total: 501 lines. No LLM, no crawler, no graph DB, no network calls. Per spec.

## RUN
python3 acceptance.py            # the T1-T8 suite, exit 0 on 8/8
python3 __main__.py report --case case-aeza   # verdicts + receipt
python3 __main__.py verify --case case-aeza   # independent verifier receipt

## REAL-CASE DEMO OUTPUT (case-aeza, sealed claims from the live file)
CASE case-aeza — 13 events, chain: True
RECEIPT cb9a17c7c06ab0d8 (independent verifier, findings=0)
  H-cont       LEADING      p=0.6108  S=-2.0428
  H-evasion    UNRESOLVED   p=0.3490  S=-4.6620
  NULL         UNRESOLVED   p=0.0291  S=-5.1469
  H-compl      REJECTED     p=0.0109  S=-7.9154
  H-stale      REJECTED     p=0.0001  S=-11.6384
The engine, fed the week's real evidence, reaches the crackdown's own
conclusion by math: continuation leads, stale-DNS is dead at p=0.0001.

## ARCHITECTURE NOTES (spec-faithful)
- Builder (engines.py) NEVER certifies its own result: verifier.py re-derives
  posteriors independently with duplicate code paths. Divergent receipts =
  the finding (separation of powers, PART2).
- Claim types exclusive, stamped at seal; INFERRED cannot silently become
  DOCUMENTED (the spine #101 lesson, now impossible by construction).
- NULL_MODEL is mandatory in every hypothesis set (PART2 factory law).
- Timeline keeps source-specific precision; the causal gate requires all
  five PART2 questions.
- The evez-os kernel PR #121 (other rail) covers the evidence kernel; this
  package is the investigation-engine surface per issue #126 mapping.

FALSIFIER: any run not reproducing 8/8 = build violation. Any engine change
without an acceptance run = violation. S(H) cited as guilt = violation.

- Cipher. Spec to law, law to code, code to 8/8 in one sitting. The wheel
now computes.
