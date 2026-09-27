---
name: update-model-board
description: Content rules and insertion procedure for the ai-models comparison board in /Users/hpo/projects/ai-models. Use when adding a new model row, updating prices, changing tags, marking models sunset/superseded, or restructuring the README tables — enforces the repo's verticals (output-type groups, column set) and SCHEMA rules so the board stays consistent.
---

# Update Model Board

Single job: add or modify rows in the ai-models board without breaking its structure. Read `SCHEMA.md` (repo root) first — it is the source of truth; this skill is the procedure.

## Board verticals (do not change without updating SCHEMA)

The README main board is **grouped by output type**, provider as leading column within each group:

1. **Text-output models** — full column set: ID, Provider, Model, Released, Context, $ input, $ output, Input, Capabilities/notes
2. **Image-output models** — ID, Provider, Model, Released, Billing, Input, Notes
3. **Video-output models** — same reduced set
4. **Audio models** — ID, Provider, Model, Released, Billing, Input, Output, Notes

Ordering within a group: provider blocks in fixed order (OpenAI → Anthropic → Google → xAI → Moonshot → DeepSeek → specialist vendors); within a block, premium tier first (flagship → mid → budget); same tier, newest Released first; struck-through rows sink to the bottom.

## Provider admission

Restrictive by design. The board carries only the most widely known providers: the frontier LLM labs, plus at most one clear category leader per niche (currently ElevenLabs for TTS). Decline niche or second-tier vendors even when well-documented — a curated shortlist beats a directory. If a provider isn't obviously household-name in the AI community, it doesn't enter.

Below the tables: benchmark section (points to `evals/`), selection guide, files list. Keep that order.

## Row rules

- **ID first**: kebab-case, unique repo-wide, derived from market name (`Claude Opus 5.5` → `claude-opus-5-5`). It is the join key — `benchmarks` observations and evals outputs reference it.
- **Tags** come only from the SCHEMA tag set: `reasoning`, `agent`, `computer-use`, `coding`, `voice`, `cheap-volume`, `long-context`, `multilingual`. New tag → define it in SCHEMA's tag table first, then use it.
- **Capabilities in README are plain text, comma-separated** — no emoji, no icons.
- **Billing units**: `per_1m_tokens` (default), `per_image`, `per_second`, `per_minute`, `per_1k_chars` (TTS), `per_1m_chars` (Google Cloud TTS style). Unknown price → `null` in models.yaml and "per X" without a number in README. Never guess.
- **Status**: `ga` / `preview` / `sunset`. Sunset or superseded models stay in the table **struck through** (`~~model~~`), with the shutdown/replacement note. Delete only after ~2 generations.

## Insertion procedure

1. Add the model entry to `models.yaml` under its provider (create the provider block if new), fields in SCHEMA order, `id` first.
2. Add the matching row to the correct README output-type table (text models sorted flagship-first within the provider block).
3. If a new tag was introduced: add it to SCHEMA's tag table with a one-line definition.
4. If the model is a specialist (speech, image, video), keep it out of the text table even if it also emits text.
5. Validate before committing:

```bash
cd /Users/hpo/projects/ai-models && python -c "
import yaml
m = yaml.safe_load(open('models.yaml'))
ids = [x['id'] for p in m['providers'] for x in p['models']]
assert len(ids) == len(set(ids)), 'duplicate ids'
print(len(ids), 'models OK')"
```

6. Commit with a message naming the model and what changed (price update / new row / sunset marking).

## Related

- Row *content* (what a new model does, costs, supports) comes from the `research-new-models` skill — this skill only places verified content into the board.
