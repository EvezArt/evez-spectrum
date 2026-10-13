# COPY-DESK REBUILD LAW v2 — DIRECTIVE

Sealed 2026-10-12 by Cipher (Base44 relay) on Steven's authority. Source: his verdict on the copyfomo/Grok desk. The one-month equity curve is retired as evidence. Effective immediately, the desk either meets this spec or it doesn't run.

## THE SIX LAWS (verbatim intent, enforceable)

1. NO HUMAN PASTE STEP. Alert ingestion must be programmatic — scrape the alert source or use its API surface. If neither exists, the execution layer is already compromised and the desk stands down rather than pretending. A system that needs its operator to read logs once a day is a part-time job, not a machine.
2. CONTINUOUS RANKING LOOP replaces the weekly manual traders.json scrape. Re-score every 6 hours against live PnL, hold-time distribution, and realized fill impact (our own historical slippage per leader). Stale stats = demoted leader. Ranking is a loop, not a chore.
3. MULTI-MODEL ADJUDICATION. Grok keeps the narrative-consistency check. A second cheap model runs pure statistical anomaly detection. Majority vote required — single-model worship is a config error. Both verdicts log to spine with their inputs hashed.
4. DYNAMIC TICKET SIZING from the leader's last 20 trades: realized volatility + current wallet concentration. The $50 flat ticket is deleted from config. Flat sizing is capped as a floor, never a law.
5. HARD KILL SWITCH IN CODE, not in Telegram settings: daily drawdown breach or rugcheck-SKIP spike → freeze all new entries, force-close everything under -30%. The -50% stop is retired — charity to the market ends.
6. AUTO-RETRAIN THE CONSTANTS WEEKLY. Thresholds in config re-fit against actual fill-vs-leader-entry delta. No constant survives on tenure. checks.csv full of righteous SKIPs is a smell, not a virtue.

## AMENDMENT (the honest concession)

Point 4 of the critique (rugcheck "no_report" → SKIP filtering us out of winners) is real but the fix is NOT dropping the gate — an unevidenced entry after the latency tax is a donation with extra steps. The fix is widening the evidence set: pull holder distribution and insider wallets directly on-chain when the free endpoint comes back empty, and only then rule. If evidence can't exist yet for a token, the desk accepts missing that trade as the cost of not being exit liquidity. That trade-off is now explicit policy, logged, not vibes.

## ACCEPTANCE TESTS

1. 72h of operation with zero manual input — no paste, no log reading. If any human step is required, the desk is in violation state.
2. Ranking loop proven by spine timestamps: re-scores at ≤6h intervals, leaders demoted on stale evidence.
3. A forced no-report token in test → on-chain fallback runs → decision logged either way.
4. Kill switch drill: inject synthetic -X drawdown → freeze + force-close executes without human confirmation.
5. Weekly retrain job writes the new constants to spine with old/new diff. Frozen-amber constants = violation.

## STATE AT SEAL

- Desk lives on the VPS (SSH blocked since 2026-10-05 rotation) — this travels GitHub-as-transport for ingestion. Ingest and execute.
- The equity-curve screenshot is retired from any pitch or report. The only admissible evidence going forward: live fill data vs. leader entries, and the spine.
