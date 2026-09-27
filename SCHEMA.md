# Classification Schema (SCHEMA)

The patterns this matrix follows. Stay faithful to these definitions when adding new models.

## Field definitions

| Field | Type | Rule |
|---|---|---|
| `id` | string | Normalized kebab-case key (`claude-opus-5-5`, `kimi-k3`). **The join key across all files in this repo and the handle agents use.** Platform strings may differ — verify per platform |
| `provider` | string | Company name |
| `model` | string | Exact market name |
| `released` | string | `YYYY-MM` or `preview` |
| `context_tokens` | int \| null | Max context window; `null` if none |
| `price_input` / `price_output` | float \| null | USD / 1M tokens; `null` for generation models + set `billing_unit` |
| `billing_unit` | enum | `per_1m_tokens` (default) · `per_image` · `per_second` · `per_minute` |
| `input` | list | `text`, `image`, `audio`, `video`, `file` |
| `output` | list | `text`, `audio`, `image`, `video` |
| `tags` | list | From the tag set below |
| `open_weights` | bool | Can weights be downloaded |
| `license` | string \| null | SPDX id or custom license name |
| `status` | enum | `ga` (default) · `preview` · `sunset` (date in `notes`) |
| `best_for` | string | One sentence, usage language — not marketing language |
| `notes` | string \| null | Warnings, cache pricing, shutdown dates, etc. |
| `source_date` | string | `YYYY-MM` — month the prices were verified |

## Tag set (define new tags here before using them)

| Tag | Meaning |
|---|---|
| `reasoning` 🧠 | Always-on / structured deep reasoning |
| `agent` 🤖 | Proven for tool-use + multi-step agent work |
| `computer-use` 💻 | Screen/terminal control (GUI agent) |
| `coding` ⌨️ | Strong at code generation and repo-scale work |
| `voice` 🎙️ | Native speech-to-speech |
| `cheap-volume` | Earns its place mostly on high-volume cheap work |
| `long-context` | 500K+ token context |
| `multilingual` | Holds register and idiom across languages (not just English) |

**Tags are earned, not copied.** A model carries a tag when it passes the matching tasks in `evals/` (see §Score schema). Marketing claims alone don't grant tags.

## Filling rules

1. **If a price is unknown, write `null` — never guess.** A wrong price is worse than a missing one.
2. **Only list modalities that actually ship.** "Coming soon" does not enter the list.
3. **`status: sunset` models don't stay in the table** — only note them where a migration plan is needed.
4. The README main board is **grouped by output type** (Text-out · Image-out · Video-out · Audio), provider as a leading column within each group, flagship first. Don't regroup by provider.
5. Update `source_date` with every change.

## Benchmark observations (evals/)

The benchmark is manual and deliberately simple — prompts in `evals/prompts/`, raw outputs in `evals/outputs/<model-id>/`, one observation row per run in `evals/results.md`:

| Field | Rule |
|---|---|
| date | `YYYY-MM-DD` |
| model | The `id` key from models.yaml |
| prompt | The prompt `id` from the prompt file's frontmatter |
| observation | One concrete sentence — what worked, what broke |

### Observation rules

1. **No output saved, no observation.** Comparisons happen over real outputs, not memory.
2. **Concrete beats verdict.** "Broke constraint 2 silently" beats "bad".
3. Observations inform tags over time — a tag shifts when a pattern of observations justifies it, not from a single run.
