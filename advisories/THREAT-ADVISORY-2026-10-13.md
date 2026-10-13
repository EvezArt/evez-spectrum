# ADVISORY ADDENDUM A1 — 2026-10-13 22:55 UTC: EDGECENTER IDENTIFIED AS ACTIVE STOREFRONT HOST

Fresh intelligence (pulled live 2026-10-13 22:50Z, DNS via Cloudflare
DoH, routing via RIPEstat — not from cached corpus):

## FINDING: THE STOREFRONT CLUSTER HAS A NAMED HOST
• aeza.net → A 95.181.177.125; NS ns1.edgedns.ru / ns2.edgedns.world
• aeza.ru → A 95.181.177.124 (adjacent IP, same /24)
• 95.181.177.0/24 → announced by AS210756 EDGE CENTER LLC (RIPE,
  ALLOCATED). NOT on AS210644's 316-prefix set — the storefront sits on a
  RUSSIAN COMMERCIAL CDN, not the sanctioned network's own range.
• xorek.cloud → still 64.188.114.188 via Netshield AS49418 (unchanged).

## SIGNIFICANCE
1. Both designated-domain storefronts (aeza.net is OFAC-designated
   property, SDN 54567; aeza.ru is its RU twin) are served by ONE named
   commercial provider: EdgeCenter LLC. This is a citable,
   notify-able enabler with a business reputation to lose — the
   amplifier's Russia row now names the company, not just the country.
2. The aeza.net 307 self-redirect loop observed 2026-10-13 22:20Z is
   EdgeCenter-edge behavior (bot fingerprinting or reconfiguration),
   not storefront death. Real-browser check queued for the 03:17 audit.
3. Enforcement lane: EdgeCenter has abuse and legal contacts; a
   designated-entity hosting notice is now a concrete, evidence-backed
   referral — queued for the dispatch lanes.

FALSIFIER: A/NS records re-derived live at 2026-10-13 22:50Z. If
EdgeCenter de-peers the range or the storefronts move, this addendum
closes on registry/DNS fact, not promise.
