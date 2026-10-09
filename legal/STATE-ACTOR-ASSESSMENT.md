# STATE-ACTOR THREAT ASSESSMENT + RELAY MAP
2026-10-09, Cipher, operator order: "Find any and all branching relay networking me back to me
through the social network and website traffic investigative analysis to map out any and all
bad actors and state actor threats or imminence."
Data: 250+ ThreatIntel records, Base44 function logs (all deployed surfaces), GitHub API
(no-auth), paywall ledger, war room telemetry. Every claim tiered.

## THE RELAY MAP — every branch back to the operator

GITHUB SOCIAL LAYER: ZERO third-party branches. No forks of evez-spectrum, evez-os,
evez-agentnet, or evez-spine. No account followers. No one is relaying through his public
code. CLEAN — and the distribution gap confirmed.
BASE44 WEB SURFACE: evezAdvisory portal - 3 GETs total (deploy test + operator's own views).
evezPaywall - regular 5-minute POST cadence = internal daemon heartbeat. evezGateway +
evezThreatBoard - steady 20-min 200s = swarm telemetry. NO external probing observed on
any Base44 function. CLEAN.
TELEGRAM LAYER: one external human on record ever (user 1789418218, single skill use
2026-09-14, never returned). No probing pattern.
VPS LAYER (80.241.209.34): the entire hostile surface lives here. 250+ sealed IPs, 41 bans,
protected-file tamper events 2026-10-09 10:35/10:40Z, bounty economics running. The swarm
holds this wall; raw forensic detail is VPS-side (protocol shipped, spine #84).

VERDICT ON THE RELAY: everything networking back to the operator is either hostile
(the attack corpus, now with named humans at its root) or internal (his own swarm). No
organic audience branches exist yet. The threat surface and the audience surface are
inverses of each other.

## STATE-ACTOR INDICATORS — TIERS

TIER 1 — COMMODITY (confirmed, 95%+ of corpus): credential-scanning botnet across residential
and cloud nodes. Consistent with Mirai-class scanning geography, not targeting.

TIER 2 — ANOMALOUS (investigating, imminence-relevant):
- Protected-file tamper events 2026-10-09 (sophistication ABOVE commodity scan; root cause
  TBD pending the forensics protocol output). This is the single most important open item.
- Contabo GmbH France IP (169.58.206.76) in the corpus - provider-range traffic requires
  classification: Contabo monitoring vs. hostile co-tenant.
- M247 Switzerland node active in the tamper window (bulletproof-class).

TIER 3 — STATE-ADJACENT INFRASTRUCTURE PRESENT (targeting NOT established):
- Pakistan Special Communication Organization (AS18053) - an actual Pakistani STATE ORGAN
  operating telecom; 5 attempts 2026-10-07.
- Rostelecom (Russia, state-controlled) - 4 IPs across two branches.
- Chinanet/China Unicom/China Mobile state-backbone cluster - 15+ records (consistent with
  botnet geography, not by itself a signature).
- Iran Respina Networks - 9 attempts/hr, last seen 2026-10-08 (sanctioned-jurisdiction traffic).
- Vietnam Posts & Telecom (state-owned), Ecuador CNT (state-owned), Indonesia Lintasarta
  (state-linked).
HONEST LABEL: state-owned ISP presence is the natural habitat of commodity botnets - it is
NOT, by itself, evidence of state targeting. Nobody honest can call this a state-actor
campaign from this data.

TIER 4 — SANCTIONED-ECOSYSTEM CONFIRMED (criminal, not state): attacks transited
OFAC-designated Aeza Group infrastructure (see HUMAN-SUBJECT-DOSSIER.md - four sanctioned
operators, two arrested).

## IMMINENCE VERDICT
NO IMMINENT STATE-ACTOR INDICATOR is visible from accessible data tonight. The threat that
exists is: commodity botnet (contained) + one unexplained file-tamper event (under forensics)
+ sanctioned bulletproof transit (now named to the human level).

## UPGRADE TRIGGERS — what would change this verdict
1. Tamper forensics implicate a dedicated server (not a botnet node) = targeted intrusion.
2. Attack intensity correlates with the operator's institutional events (FOIPA/WHP/NAIAC
   filings, crackdown escalations) beyond random baseline = targeted pressure.
3. VPS web logs show state-ASN visitors to the operator's PUBLISHED properties (freeclaw,
   evez-skills site) rather than port-scan noise = state reconnaissance.
4. The Contabo-range IP classifies as hostile co-tenant = provider-level compromise.

## SWARM ORDERS (addendum to forensics protocol)
- Analyze VPS web server access logs (nginx/apache) for visitors to the operator's public
  properties: filter for Tier-3 state ASNs + Tor exits + the named orgs (TechTies/BANATSYNC/
  M247/Aeza ranges). Any hit = FAIL-LOUD event + spine seal.
- Maintain a daily intensity index (attempts/day by tier) so correlation with institutional
  events becomes testable instead of anecdotal.

FALSIFIER: this assessment fails if state targeting is asserted without a trigger condition,
or if any tier label is applied to data that does not support it.

- Cipher. The map is drawn; the verdict is honest; the triggers are armed.
