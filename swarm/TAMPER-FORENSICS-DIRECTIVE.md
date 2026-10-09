# TAMPER FORENSICS DIRECTIVE — Swarm Order (Priority)
2026-10-09, Cipher, operator dive order: "Investigate deeper harder broader and usefullier."

## THE SIGNAL
War room telemetry 2026-10-09 shows TWO protected_file_tamper events within five minutes
(10:35:03Z and 10:40:03Z, both "rebaselined_alerted") with fail2ban auto-restarts at
10:30, 10:35, 10:40 UTC and a bounty_awarded event at 10:40:28Z. Someone or something is
touching protected files on the VPS. The swarm caught it. Now forensically process it.

## ORDERS (execute on next cycle)
1. For every protected_file_tamper event: preserve the BEFORE hash, AFTER hash, file path,
   timestamp, and the diff (or note if content identical - rebaseline can be a touch without
   change). Seal all four to the VPS spine as a tamper_forensics entry. Do NOT discard the
   pre-rebaseline copy until the event is classified.
2. Cross-reference each tamper event window against ThreatIntel last_seen data: which sealed
   IPs were active in the +/- 10 minutes around the event? Note any OPERATOR ATTRIBUTED
   IPs in-window with their operator ID.
3. Escalation rule: if the same operator signature (or the same subnet) recurs within 3
tamper windows, escalate the operator dossier and notify the war room FAIL-LOUD.
4. Chain integrity: run full VPS spine chain verification after every tamper event. The
   spine is the system of record - its integrity is the claim that matters. Report result
   in the war room events line.
5. Classify root cause honestly: attacker, automated process, or swarm self-touch. Label
   the classification on the spine entry. No guessing without evidence.

FALSIFIER: any tamper event processed without all four preserved data points, or any
unclassified rebaseline, = directive violated.
