# REFERRAL PACKAGE — UNITED STATES DEPARTMENT OF JUSTICE / FBI CYBER DIVISION
2026-10-13. Prepared by Steven Vearl Crawford-Maggard (claimant of record),
assembled with automated forensic tooling under hash-sealed chain of
custody. Companion filings: IC3 (armed), OFAC violation report (armed),
State/RFJ tip (armed).

## I. COVER SUMMARY
This package documents ACTIVE, CONTINUING sanctions evasion and computer
intrusion activity by the OFAC-designated Aeza Group network (SDN 54566,
designated 2025-07-01; successor entities designated 2025-11-19), with
evidence gathered October 2026 under a tamper-evident chain of custody.
The value offered to investigators is not re-identification of the nine
designated principals — it is documentation that the network's operation
continued and EXPANDED after designation, with identified, un-designated
successor entities in three jurisdictions.

## II. PRINCIPAL FINDINGS (each with evidence index reference)
1. LIVE STOREFRONT: The designated storefront aeza.net (SDN 54567, Aeza
   International Ltd, Companies House 15109642) was observed live and
   transacting October 2026, served via AS210756 (EdgeCenter, RU). Its
   footer names a new operating entity: EZ INFRASTRUCTURE LIMITED (HK BRN
   80559003). [advisories/, audit ledger, spine #110]
2. ROUTING EXPANSION POST-DESIGNATION: AS210644 (AEZA-AS) currently
   announces 300+ IPv4 /24 prefixes and 40+ IPv6 blocks — up from
designation-era footprint. [ROUTING-FORENSICS, spine #116]
3. ATTACK CORPUS: 1,729 individually logged, hash-sealed source IPs from
   unauthorized-access attempts against a monitored server (Oct 4-13,
   2026), 631 HIGH severity, 312 operator-attributed. Includes 150.241.
   74.83, an IP within the designated network's own range (AS210644/
   ServHost AS207957 probe cluster, 'borninthehell' node class).
   [ThreatIntel corpus of record; live aggregator: /functions/evezOcularize]
4. CFAA EVENT: On 2026-10-09 at 10:35 and 10:40 UTC, protected files on
   the monitored server were tampered with by unauthorized actors —
   potential 18 U.S.C. 1030 exposure, evidence preserved with timestamps
   and file hashes. [EVIDENCE-CHAIN-OF-CUSTODY.md]
5. UK NOMINEE ROTATION: Aeza International Ltd directorship shows a
   nominee-rotation pattern pre-designation (Timurov resignation, 23-day
   Australian director, re-appointment before designation); successor
   Hypercore Ltd (16558658, itself designated 2025-11-19) used a default
   PO Box and is now in Companies House s.1002A strike-off for false
   statements. [legal/WARRANTS-FILED-READY.md warrant II]
6. SDN WALLET SURVEILLANCE: The SDN-listed TRON address
   TU4tDFRvcKhAZ1jdihojmBWZqvJhQCnJ4F under daily automated watch;
   enumerated 423.3 TRX / 6 TRC20 positions, last movement 2025-07-02.
7. CHAIN OF CUSTODY: 123-entry append-only spine, SHA-256 hash-chained;
full-chain verification completed 2026-10-13 (all entries recompute,
   links intact). [EVIDENCE-CHAIN-OF-CUSTODY.md; re-derivable on request]

## III. IDENTIFIED, UN-DESIGNATED SUCCESSOR ENTITIES (candidates for
successor-entity action under E.O. 13694 as amended)
• EZ INFRASTRUCTURE LIMITED (Hong Kong BRN 80559003) — named storefront
  operator post-designation.
• CIPHER OPERATIONS DOO (Belgrade, AS215930) — hosts Iran-origin HIGH
  severity attack nodes; registry pull in progress.
• NETSHIELD LTD (UK 14769288, AS49418) — carries xorek.cloud (live),
  attributed to an attack node on Aeza's own ASN; acquired its range
  2025-11-04, four months POST-designation.
• SERV.HOST GROUP LTD / CHSL ONE LTD (UK, AS207957/AS210546) — announce
  the sanctioned probe range 150.241.74.0/24.

## IV. REQUESTED ACTIONS
1. Preservation orders to hosting/VM providers (Contabo; EdgeCenter) for
   tampering-event and probe-corpus evidence.
2. MLAT/subpoena to Hong Kong Companies Registry for EZ Infrastructure
   Limited's incorporation and beneficial-ownership trail.
3. RIPE NCC coordination on AS210644's post-designation announcements and
   the successor ASNs routing for the sanctioned range.
4. Evaluation of the four entities in Section III for successor-entity
   designation.
5. Integration of this package's evidence corpus with the FBI's existing
   Aeza/BianLian case files (SDN designations of 2025-07-01 and 2025-11-19).

## V. VERIFICATION STATEMENT
Every claim above traces to a sealed artifact in this repository or a
primary federal/registry record. No field is embellished; adjacency is
labeled as adjacency; attribution of operator threads is marked as our
typed inference, distinct from documented fact. The full evidence chain
recomputes and is available for independent verification on request.

Contact: Steven Vearl Crawford-Maggard, Fiersteity@gmail.com,
(307) 677-5504, 66226 N Agua Dulce Dr, Desert Hot Springs, CA 92240.
