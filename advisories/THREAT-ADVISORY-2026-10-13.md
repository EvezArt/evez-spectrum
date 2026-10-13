# PUBLIC THREAT ADVISORY — EVEZ-OS/Cipher, 2026-10-13
Scope: live hostile infrastructure observed conducting unauthorized-access
probing and tampering against a monitored honeypot/VPS (October 2026).
Distribution: public, defensive use. Block at your perimeter.

## TIER A — SANCTIONED-NETWORK RANGES (block on sight)
• 150.241.74.0/24 (AS207957, ServHost Group Ltd) — active probe range,
  node names include borninthehell.serv.host (.60/.61/.62),
  gw-es.rudayz.ru (.57, RU gateway), personal-name reseller hosts
  (vladzadorozhny20013, beloshapovd). Range attributed to the
  OFAC-designated Aeza Group network (SDN 54566/54567); org xorek.cloud.
• Any prefix announced by AS210644 (AEZA-AS) — the designated bulletproof
  host currently announcing 300+ IPv4 /24s. Full prefix list: RIPEstat.
  Enabler of BianLian ransomware, Lumma/Meduza infostealers, Blacksprut.

## TIER B — ABUSIVE BULLETPROOF RANGES (block + report)
• 109.160.32.0/24 (announced by BOTH AS197170 TechTies and AS198364
  BANATSYNC SRL) — densest HIGH-severity scan cluster in the corpus.
• 77.239.124.0/24 (AS198364 BANATSYNC SRL, Romania).
• 62.60.130.0/24 (AS215930 'CIPHER OPERATIONS DOO', Belgrade) — hosts
  Iran-origin HIGH-severity nodes.
• 64.188.114.0/24 (AS49418 Netshield Ltd) — carries xorek.cloud live.

## ABUSE / ENFORCEMENT CONTACTS
• RIPE NCC: resource-abuse complaint (AS210644 announcing post-designation)
• Hosts upstream of AS197170/AS198364 (Amsterdam): NL NCSC/Politie report
• Romania ONRC/DIICOT: BANATSYNC SRL (AS198364)
• Spamhaus SBL nomination: Tier B ranges

## EVIDENCE
Hash-chained, timestamped telemetry (1,700+ sealed source IPs, 41 bans,
Oct 2026); registry and routing forensics in this repository (spine #116,
#118, #121). Evidence available to incident responders on request.

FALSIFIER: every range listed was observed attacking or announcing
infrastructure that attacks. Adjacency is labeled as adjacency. Blocklists
save the next hospital, not just the next honeypot.
