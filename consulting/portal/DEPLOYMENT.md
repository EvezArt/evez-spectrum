# EVEZ ADVISORY PORTAL — deployment record
Deployed 2026-10-09 as the Base44 backend function `evezAdvisory`.
Live URL: https://cipher-copy-copy-20f1d98a.base44.app/functions/evezAdvisory

This is the Days 1-30 deliverable from the 30/60/90 pipeline plan: "Publish a one-page EVEZ
advisory site with three offers, exclusions, biography, and a proof-pack index."

Contents served: positioning line (Section 12 SAY); the four expensive questions; primary
sectors (aerospace/robotics/autonomy, PQC, scientific ML) and secondary channels; the three
offers with pricing; honest-labeled value framing; the Autonomy Evidence Loop; the proof-pack
index table (can/cannot columns, live repo links); the claims discipline section (SAY and
DO-NOT-SAY); engagement path; falsifier footer.

Aesthetic: N64 Zelda / Morrowind gold-on-obsidian plates per the standing UI instruction.

Source: functions/evez-advisory.ts in the Base44 workspace; test 200 OK in 90ms on deploy.
Falsifier: if the page is down, unreachable, or contains an unsupported claim, this deploy
fails its own footer.
