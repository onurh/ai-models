---
name: research-new-models
description: Research workflow for discovering and verifying new AI models before they enter the ai-models comparison board. Use when a new model release needs to be investigated — finding what shipped, confirming GA vs preview status, verifying modalities and pricing from primary sources, and producing a row proposal that satisfies the repo's SCHEMA rules.
---

# Research New Models

Single job: turn "X released a new model" into a verified row proposal for the ai-models board. Research happens here; writing to the board happens via the `update-model-board` skill.

## Workflow

1. **Identify the claim.** Exact model name, provider, announcement date. Distinguish: base model release, API availability, product (chat app) availability — these lag each other by days to weeks.

2. **Collect from primary sources first**, in this order:
   - Provider's official announcement / changelog / docs (pricing page for prices, model card for modalities)
   - Provider's API reference (confirms the actual model string and parameters)
   - Independent trackers for cross-checking: Artificial Analysis (artificialanalysis.ai), LMArena, Epoch AI, BenchLM

3. **Verify each field against the SCHEMA rules** (read `SCHEMA.md` in the repo root before proposing):
   - **Status**: `ga` only if generally available via API. "Preview", "rolling out", waitlist → `preview`.
   - **Modalities**: only what actually ships. Roadmap features never enter the row.
   - **Price**: from the pricing page only. Unknown → `null`, never estimate. Note cache pricing and promotional pricing separately.
   - **Context window**: from official docs; if providers quote characters instead of tokens, say so in notes rather than converting silently.
   - **Open weights**: weights downloadable from Hugging Face or equivalent → `true`, and record the license name exactly.

4. **Flag uncertainty inline.** Write `notes` like "prices approximate", "context tiered above 200K", "vendor claim — needs third-party confirmation". Approximate values carry an asterisk on the board.

5. **Check for supersession.** Search the board for the provider's previous generation. If the new model clearly replaces an old one, mark the old row for strikethrough instead of deleting it (rule: struck rows stay ~2 generations).

6. **Deliver the proposal** as a filled row in the exact `models.yaml` shape plus the matching README table line, ready for the `update-model-board` skill to insert. Include `source_date` (YYYY-MM of verification).

## Do not

- Do not rank models or aggregate benchmarks — the board tracks capabilities and prices, and the evals/ directory handles qualitative testing.
- Do not import leaderboard numbers into the repo.
- Do not invent model IDs: derive the kebab-case `id` from the market name (`Kimi K2.8 Preview` → `kimi-k2-8-preview`).
