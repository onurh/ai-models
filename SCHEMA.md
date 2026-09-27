# Classification Schema (SCHEMA)

The patterns this matrix follows. Stay faithful to these definitions when adding new models.

## Field definitions

| Field | Type | Rule |
|---|---|---|
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

## Filling rules

1. **If a price is unknown, write `null` — never guess.** A wrong price is worse than a missing one.
2. **Only list modalities that actually ship.** "Coming soon" does not enter the list.
3. **`status: sunset` models don't stay in the table** — only note them where a migration plan is needed.
4. The README is a **single table** sorted by provider (provider in the leading column), flagship first within each provider. Don't split into per-provider tables.
5. Update `source_date` with every change.

## Score schema (benchmarks.yaml)

Benchmarks are a **classification dimension of the main board**, not a separate leaderboard. Each score row:

| Field | Type | Rule |
|---|---|---|
| `benchmark` | string | Board name, e.g. `SWE-bench Verified` |
| `version` | string | Board revision — required, scores across versions are not comparable |
| `category` | enum | `coding` · `reasoning` · `science` · `agentic` · `composite` · `image` · `video` |
| `model` | string | Must match a `model` name in models.yaml, or be added there |
| `score` | float | In `unit` |
| `unit` | string | `%` or `index` |
| `source` | enum | `independent` (third-party run) · `vendor` (self-reported, own scaffold) — **never omit** |
| `harness` | string \| null | Eval harness if known (e.g. `Scale SEAL`, `vals.ai`) |
| `date` | string | `YYYY-MM` the score was published |

### Score rules

1. **`source` is mandatory.** Vendor scores inflate (SWE-Pro vendor board 80% vs SEAL 61.5%); readers must be able to tell them apart at a glance.
2. **Never compare across columns** of the README benchmark matrix — only within one board and version.
3. **Empty cell ≠ weakness.** No public number just means not evaluated; never infer.
4. Benchmarks are prompts/tests: a score classifies a model, it doesn't rank the model absolutely. A model qualifies for a tag (e.g. `coding`) when its board standing supports it — that's the only role scores play here.
