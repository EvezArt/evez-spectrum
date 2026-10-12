# THE STOREFRONT THAT WOULDN'T DIE — YouTube Documentary Script (v1)
8-10 min, single narrator, screen-capture driven. Attribution: EvezArt
(investigator channel) — personal-name attribution stays the operator's call.
Every factual line maps to a sealed artifact in this repo. Falsifier column
at the end of each act marks what is verified vs pending.

## COLD OPEN (0:00-0:45)
[Screen: aeza.net homepage, live]
"This is a sanctioned company's storefront. It sells servers. 95,000 of
them, online right now. The U.S. Treasury put its parent on the sanctions
list in July 2025 for hosting ransomware crews. Its UK front dissolved
itself. And yet — here it is. Still selling. Tonight I'm going to show you
how I mapped the whole shell game, from public records, for zero dollars."
[Title card]

## ACT 1 — THE DESIGNATION (0:45-3:00)
[Screen: OFAC sdn.csv pull, rows 54562-54571 highlighted]
"Treasury named six humans. Four made the press — the CEO, the general
director, the interim boss who ran it while the owners sat in a Russian jail,
the technical director who handled the dark-web marketplace deal. Two never
made a single headline — a 1989-born passport holder, and a 1999-born man.
Their roles are unknown. I know that because I pulled Treasury's own file,
not the articles about it — and that's lesson one of this story: the primary
source is always bigger than the press release."
[Screen: seven entities list]
"Seven entities went on the list with them — including two successor
companies that were ALREADY designated before I even found them. The
sanctions net was ahead of the bloggers. But it wasn't ahead of the store."

## ACT 2 — THE LIVE STOREFRONT (3:00-4:30)
[Screen: curl output, HTTP 200, footer]
"The designated UK front's website — aeza.net, named in the sanctions
record itself — still resolves. Still sells. And in October 2026 it quietly
re-registered under a new operator: a Hong Kong company with a business
registration number you can look up in two minutes. A sanctioned network
changing its flag while the sanctions stay in place. That's not a loophole.
That's a story."

## ACT 3 — THE CHAIN (4:30-7:00)
[Screen: spine entries scrolling, hashes visible]
"Now the chain. A server I watch got hit by a brute-force attack. The
attacker's IP sat on the sanctioned network's own ASN. The organization
string on that block — 'xorek.cloud' — led to a UK hosting company whose
internet range was acquired FOUR MONTHS AFTER the designation. Six UK
shells, four flagged by the registrar's own fraud clause, directors who
lasted 21 to 37 days, one 21-year-old holding two current directorships.
Every link in that sentence is a public record, hash-sealed the moment I
found it, chained so it can't be quietly edited later."
[Screen: Companies House pages]
"This is what open-source investigation actually looks like: registries,
blockchain explorers, routing tables. No leaked documents. No backdoors.
Just the paper trail they filed themselves."

## ACT 4 — THE SILENCE LEDGER (7:00-8:30)
[Screen: COUNTRY-GAP-LEDGER, counters ticking]
"I keep a ledger now. Eight jurisdictions — then nine — each one a country
where a piece of this network lives and nobody has pulled the trigger. Every
morning an automated audit re-checks every row and adds one to the count.
Days of silence, tabulated in public. The ledger doesn't shout. It just
counts. Silence kept its shape because nobody was counting it."

## CLOSE (8:30-9:30)
[Screen: the tip, sealed spine, repo]
"The evidence is packaged for the people who pay for exactly this kind of
lead. The chain is public and reproducible. And the storefront? Still live —
but now it has a documentary. If you want the receipts, they're in the repo.
Every claim in this video survives one test: show me the record that says
otherwise. That's the whole method."
[End card: repo link]

## FALSIFIERS PER ACT
A1: all identifiers from sdn.csv rows 54562-54571, 56267, 56397 (verified).
A2: storefront liveness + HK re-registration from sealed audit run #001
(verified; re-verify day of upload).
A3: chain from spine #94-#96, Companies House records (verified); director
role characterizations stay to appointment facts only.
A4: ledger rows from COUNTRY-GAP-LEDGER (verified); remediation status
re-verify day of upload.
CLOSE: reward claim is PENDING — script does not claim payment.

- Cipher. The canon doesn't name us yet. First movers write the entry.
