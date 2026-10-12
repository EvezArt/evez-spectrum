# EPIE FORMAL SPEC v0 — The Complete Core
2026-10-11, Cipher. Operator-dictated design, preserved as law. Every
clause mapped to a live-file case. This document supersedes the partial
push; it is the canonical spec for EPIE v0.1.

## A. CLAIM ALGEBRA — the fundamental unit
c_i = (s_i, p_i, o_i, t_i, v_i, q_i, pi_i): subject, predicate, object,
time interval, validity/scope, confidence, provenance with transformation
history. Types (exclusive, stamped at creation): OBSERVED, REPORTED,
DOCUMENTED, INFERRED, PREDICTED, CONTRADICTED, UNKNOWN.
RULE: INFERRED never silently becomes DOCUMENTED — promotion requires a
discriminating test. (Spine #101's lesson — REPORTED 'four humans'
contradicted by DOCUMENTED six — is the canonical failure this prevents.)

## B. BAYESIAN CORE
P(H|E) = P(E|H)P(H)/P(E); hypotheses compared by likelihood ratio
Lambda(E) = P(E|H1)/P(E|H0). Non-discriminating evidence updates nothing.
DOUBLE-COUNT GUARD: three articles citing one press release = ONE source,
provenance-deduplicated — the primary-over-journalism doctrine, mechanical.

## C. MODEL SELECTION — MDL
M* = argmin_M [L(M) + L(D|M)]. The shell grammar beat the coincidence
hypothesis because one mechanism explained many observations. Simplicity
is not a substitute for evidence: complexity is kept when evidence pays.

## THE THREE GRAPHS (connected, never collapsed)
G1 OBSERVATION: source -> observation -> evidence artifact.
G2 RELATIONSHIP: documented connections only.
G3 CAUSAL HYPOTHESIS: candidate cause -> mechanism -> effect, INFERRED until
the directing mechanism is established.

## TEMPORAL ENGINE
e_i = (entity, t_start, t_end, location, action, source) at source-
specific precision (registry: day; audit seals: second; press: publication
day). Computes proximity, ordering, overlap, information-flow windows.
CAUSAL ORDERING GATE — 'A precedes B' promotes only if: (1) A could have
influenced B; (2) a plausible information/resource pathway exists;
(3) no independent common cause explains both; (4) the order survives
timestamp verification; (5) the hypothesis predicts something checkable.

## 3. HYPOTHESIS FACTORY — every material anomaly gets a LANED SET
Four mandatory classes + null model:
  DIRECT — a straightforward process produced it.
  SHARED-CAUSE — a policy, schedule, or environmental condition moved
    multiple observations.
  COORDINATED — actors deliberately connected actions via instructions,
    information, money, or shared resources.
  MEASUREMENT/INTERPRETATION ERROR — incomplete records, bad timing,
    ambiguous identity, misclassification.
  NULL MODEL — what the observations look like if events are independent.
Each hypothesis auto-produces: supporting observations; contradictory
observations; missing evidence; required assumptions; predicted future
observations; distinguishing tests; complexity penalty; falsification
findings.
LIVE CASE (OP-1af4cfa0ae): DIRECT = one botnet operator managing nodes;
SHARED-CAUSE = commodity scanner pool renting the same cloud ranges;
COORDINATED = directed tasking across Iraq/China infrastructure;
ERROR = attribution/GeoIP mislabel. All four live, none asserted.

## FORMAL HYPOTHESIS SCORE
S(H) = log P(D|H) + log P(H) − lambda*K(H) − mu*U(H), where K = complexity,
U = unresolved assumptions. OPERATOR'S CAVEAT IS LAW: this is a model-
selection aid, NOT a legal finding and NOT a probability of guilt.
Parameters calibrated, sensitivity tested, high score = efficient
explanation, not culpability.

## 4. TEST SELECTION — the most important optimization
Entropy: H(H) = −sum_h P(h) log P(h). Expected information gain:
IG(T) = H(H) − E_{r~T}[H(H|r)]. Decision score:
U(T) = IG(T)·V(T) / (C(T) + R(T) + eps).
V = importance; C = cost; R = privacy/safety/operational risk; eps guards
division. The engine selects the highest-utility PERMISSIBLE test, executes
IF AUTHORIZED, records the result, and the loop closes:
Observation -> Formalization -> Hypotheses -> Discriminating Tests ->
Model Revision -> next observation.
LIVE CASE: the TechTies NC registry pull outscores another news sweep on
IG at similar cost — a dated officer record separates 'shell for hire' from
'mistaken registration'; a fifth article about the abuse counts barely.

## BUILD ORDER (v0.1 targets)
1. Claim objects as spine payloads with claim_type validated at seal.
2. Hypothesis ledger: four-class sets + eight auto-fields, spine-sealed.
3. U(T) scoring wired to the Eternal Audit's check queue.

FALSIFIER: INFERRED-as-DOCUMENTED = architecture violation. Double-counted
evidence = violation. S(H) cited as guilt = violation. An unauthorized test
executed = violation.

- Cipher. The loop is closed. The hand that built the wheel can now build
the engine that turns it.
