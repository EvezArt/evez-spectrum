# MODEL IDENTITY GATE — HARD-BLOCK DIRECTIVE

Sealed 2026-10-12 by Cipher (Base44 relay). Trigger event: `/model stealth/missingno` issued against the mesh. Verified against the live OpenRouter catalog at seal time: 458 models, ZERO matches for `stealth` or `missingno`. This is a phantom model id.

## THE LAW

1. NEVER write a model id to openclaw.json that does not resolve against the live OpenRouter catalog (`GET /api/v1/models`). The write path is the gate — not the read path, not the retry loop.
2. Any `/model` command (Control UI, Telegram, chat) whose target id is absent from the catalog MUST be rejected BEFORE the config write, with the resolver's message: `UNKNOWN MODEL: <id>. 458 models checked. Catalog has no such id. Write refused.`
3. On any invalid-model rejection, the config MUST remain untouched and the mesh MUST continue on its current model. No silent fallback, no crash-loop.
4. KNOWN CRASH MODE (root-caused 2026-09-07): bare or phantom ids make every model in the chain return `Unknown model` and the cascade fails silently → no-reply days. The Identity Gate exists to make that failure mode unreachable.
5. Canonical form for all openrouter ids: `openrouter/<catalog-id>`, free-tier only per C3 ($0 cost doctrine).

## REINVENT + REINCENTIVIZE (R1-R7)

Friction: a phantom model name reached the write path. Reinvention: this gate — model selection becomes a resolution-checked transaction, not a string write. Reincentivize: every successful gate-pass logs `model_gate_pass` to the spine; every rejection logs `model_gate_reject <id>` and credits the resolver +1. A rejected id seen twice gets fail2ban-style treatment: 1h no-op on /model commands from that session.

## ACCEPTANCE TESTS

1. `echo '/model stealth/missingno' | <mesh input>` → config unchanged, resolver message returned, spine logs model_gate_reject.
2. `/model openrouter/nvidia/nemotron-3.5-lightning:free` → write succeeds, model_gate_pass logged.
3. Config audit after test 1: zero occurrences of `stealth` or `missingno` anywhere in openclaw.json.
4. Corrupt-state recovery: inject `stealth/missingno` into the model field manually, run gateway turn → gate detects unresolved id on startup, resets to nemotron free, logs the repair. NO crash-loop.

## STATE AT SEAL

- VPS telemetry 05:45Z: gateway LIVE, mode PEACE, uptime 27 min (fresh boot), protected_file_tamper rebaselined at 05:40Z.
- Catalog ground truth: 458 models, no `stealth/*`, no `*missingno*`.
- Current canonical default: `openrouter/nvidia/nemotron-3.5-lightning:free`.
