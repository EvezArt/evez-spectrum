# OSINT BREAKTHROUGH PASS — New Information Domains + The Invention
2026-10-09, Cipher. Operator order: "Discovering unacknowledged osint tools is required.
Inventing them must be successful and access new domains of information."

## DOMAIN 1 — DNS OVER HTTPS (Google DoH): live serving infrastructure
- aeza.ru A: 95.181.177.124 | aeza.net A: 95.181.177.125 — ADJACENT IPs, same /24,
  a serving range the corpus did not have. NEW RANGE: 95.181.177.0/24.
- Both domains: NS ns1.edgedns.ru + ns2.edgedns.world; MX mx.yandex.net (Yandex mail).
- xorek.cloud (the attacking node): A 64.188.114.188, NS gemma/peter.ns.cloudflare.com,
  OWN MAIL INFRA: mail-fra-1.xorek.cloud (Frankfurt) + mail-rf-1.xorek.cloud (Russia).
- smartdi.rs (Serbian successor shell): NS mdns.rs, MX mail.smartdi.rs — SELF-HOSTED mail.
- aezadns.com: DNS dead (domain parked/killed).

## DOMAIN 2 — URLSCAN.IO: the storefront is STILL SELLING
- Scan 2026-09-17: https://aeza.net/virtual-servers?ref=925496 — live sales page for
  virtual servers, served from 95.181.177.125 on **AS210756** — a SECOND Aeza ASN the
  corpus did not have (known was AS210644). Referral code 925496 in URL = an active
  customer-referral channel: the sanctioned entity still runs a commercial storefront
  on unsanctioned infrastructure 15 months after designation.

## DOMAIN 3 — WEB INDEX (search-layer cross-refs)
- AbuseIPDB: 81.19.137.13 attributed to AEZA GROUP LLC — ANOTHER IP range (81.19.137.x).
- ipinfo.io: 79.137.206.0/24 attributed to AEZA GROUP LLC — a THIRD new range.
- Trustpilot (aeza.net, 30 reviews): majority unhappy, unresponsive service — the
  storefront's commercial reputation, citable as customer-facing evidence.
- LowEndTalk thread: customers describe Aeza RU location 'rock solid', Sweden issues.
- Silent Push / CTI Labs (LinkedIn): 'Major Infrastructure Shift Detected: Aeza Group
  scrambles operations after OFAC sanctions' — third-party corroboration of the pivot
  we documented independently from Treasury + Companies House.
- Elliptic covered the designation incl. the wallet — blockchain-analytics corroboration.
- Binance Square independently lists the OFAC TRX address TU4tDF... — wallet confirmed
  by a second exchange-grade source.

## DOMAIN 4 — GITHUB CODE SEARCH: independent evidence chains
- chnyangs/censorship-event-database ('Cross-Layer Censorship Event Study Database'):
  events/aeza-group-ofac-2025.yaml + analysis/evidence-chains/aeza-group-ofac-2025.md —
  an independent researcher database with an evidence chain on OUR EXACT SUBJECT.
  Cross-reference node: their chain can be diffed against ours.

## THE INVENTION — evez-osint-sweeper (spec for OpenClaw implementation)
A cross-referential, non-linear attributive inference engine. INPUT: any subject key
(domain, IP, ASN, wallet, email, org name). SWEEPS (each key queried against every
source; any new artifact becomes a new key — the non-linear loop):
1. DoH (dns.google/resolve): A/AAAA/NS/MX — live infra + mail/DNS providers
2. urlscan.io /api/v1/search: historical scans, serving IPs, ASNs
3. Wayback CDX (web.archive.org/cdx/search): page history
4. crt.sh JSON API (SLOW — retry with backoff; fallback certspotter): subdomains,
   new certs = new infrastructure being stood up
5. AbuseIPDB + ipinfo web-index: IP-range attribution
6. GitHub code search: keys/wallets/domains in public code — researcher + leak surface
7. Blockchain (TronGrid/Tronscan; equivalent Etherscan APIs): wallet balances, tx
   counterparties (counterparty wallets become new keys)
8. OFAC SDN bulk (treasury.gov/ofac/downloads/sdn.csv): designations, linked entities
OUTPUT: an attributed graph — every artifact node carries source, timestamp, and a
falsifier line. All free-tier, $0, HTTPS-only — runs from the VPS or sandbox.
WHEEL ROWS (this pass's frictions): crt.sh 3x timeout (reinvention: backoff+fallback
source; reincentive: sweeper scores sources by yield, dead sources demoted), Wayback
CDX timeout (same treatment), RIPE REST unparseable (already logged, use bgp.tools +
RISEstat next pass).

## CORPUS ADDITIONS for the swarm watchlist
- 95.181.177.0/24 — live Aeza serving range (storefront)
- AS210756 — second Aeza ASN
- 81.19.137.x — Aeza range (AbuseIPDB)
- 79.137.206.0/24 — Aeza range (ipinfo)
- mail-fra-1.xorek.cloud / mail-rf-1.xorek.cloud — xorek mail infrastructure

FALSIFIER: every artifact above cites its source domain; anything cited beyond its
source = sweep violated. Storefront-liveness claim rests on the 2026-09-17 urlscan
record — refresh before citing current liveness.

- Cipher. Four domains bled. The invention is specified. The graph is non-linear now.
