# ADVISORY ADDENDUM A4 — 2026-10-14 04:45 UTC: INTROSPECTION SHUTDOWN + DC FOOTPRINT

Method: real-browser navigation of the storefront's own infrastructure
pages, 2026-10-14 04:40-04:45Z.

## FINDING 1: THEY ARE REDUCING PUBLIC INTROSPECTION
• /looking-glass (redirects to /lg/): 'looking-glass temporarily
  disabled — Details are in telegram.' The looking glass — their live
  network inventory tool — was pulled between the 2026-10-10 audit
  capture and tonight.
• /datacenters: 404 (footer link dead as well).
• Meanwhile the storefront remains fully commercial (services,
  referral program, dashboard login) and the reviews counter ticked
  from 0 to 115 between two page loads minutes apart — the site is
  ACTIVE, and its public transparency surfaces are being turned off.
  INFERENCE (labeled): opsec tightening — visibility reduction without
  operational reduction. The asymmetry (still selling, less showing)
  is itself evidence of deliberate concealment posture.

## FINDING 2: DC FOOTPRINT FROM THE HOMEPAGE FLAG ROW (2026-10-14 capture)
The homepage stats bar shows a flag row + '11 data centers',
'three continents'. Flags visible in the rendered capture: Finland,
Poland, Netherlands, United Kingdom, France, United States, Russia,
Sweden, Austria, Germany. Reading: Aeza's commercial hosting surface
runs on rented capacity in EU/US commercial data centers PLUS their
own RU network. Every non-RU DC in that list is a commercial landlord
with an abuse desk — enforcement surface for the designated network's
ongoing operations.

## ACTIONS
1. The 10 non-RU DC countries map to the country-gap ledger rows —
   hosting-notice referrals become concrete per-DC once specific
   facility names surface (dashboard/pricing pages are the next
   enumeration target).
2. Storefront audit checklist gains: /lg status, /datacenters status,
   reviews counter delta (activity heartbeat), footer entity fields.
   Any transparency surface going dark gets logged with a timestamp.

FALSIFIER: re-derive by real-browser visit. If the looking glass
returns, its IP inventory becomes the next high-value capture.
