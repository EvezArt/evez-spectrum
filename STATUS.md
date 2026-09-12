# SPECTRUM STATUS — 2026-09-12T23:05Z

Sealed against live GitHub + Stripe APIs.

## Identity

- Owner: EvezArt (Steven Crawford-Maggard)
- Public repos: 186
- HQ: `EvezArt/evez-spectrum`

## Now boxes

| Box | State | Evidence |
| --- | --- | --- |
| Mint Stripe $1 lifetime paylink | **TEST MODE DONE** | Product `prod_VFUy37dkMkNWUN` · Price `price_1UEzz7DBhYAyYlOhmFWkHRPF` ($1 USD one-time) · Payment link on EVEZ666 Syndicate **test** account. **Live paylink still required for real money.** |
| Publish evez-skills to ClawdHub (32) | OPEN | Not verified this session |
| Fix X poster cookie-route | OPEN | Not in spectrum tree |

## CI progress

| PR | What | State |
| --- | --- | --- |
| [#64](https://github.com/EvezArt/openclaw-fork/pull/64) | autonomous.yml → ubuntu-latest | OPEN (partial) |
| [#68](https://github.com/EvezArt/openclaw-fork/pull/68) | install-smoke / no-tabs / labeler → ubuntu-latest | **OPEN — full remaining RUNNER_LABEL kill** |
| [#65](https://github.com/EvezArt/openclaw-fork/pull/65) | control plane | wait for green CI |
| [#67](https://github.com/EvezArt/openclaw-fork/pull/67) | federation | wait for green CI |

**Merge order:** #68 (and/or #64) → #65 → #67

## Still blocked (human)

1. **Vercel account blocked** — cannot fix from GitHub API
2. **Stripe live mode** — promote product/price/paylink to livemode when ready to take real $1s
3. **ClawdHub + X cookie-route** — outside this API surface

## Product bar

Test money loop object exists. Live money loop does not. CI path is being repaired, not yet green.
