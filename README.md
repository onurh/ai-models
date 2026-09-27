# AI Model Comparison Matrix

Current models from 5 major providers: pricing, context windows, input/output modalities, capability tags, and benchmark standing.

> **Last updated: September 2026.** Prices in USD per 1M tokens (input / output). Sources: provider pricing pages + Artificial Analysis, verified September 2026.

## Column semantics (classification schema)

Full definitions and contribution rules in [SCHEMA.md](SCHEMA.md). In short:

- **Input**: text · image · audio · video · file
- **Output**: text · audio (TTS) · image · video
- **Tags**: 🧠 reasoning · 🤖 agent/tool-use · 💻 computer use · ⌨️ coding · 🎙️ native speech · 🔓 open weights

## Legend
✅ = built-in, generally available · 🔶 = partial / preview / higher tier only · — = not supported · ⚠️ = sunset, don't build on it
Benchmark cells: **bold** = independent third-party run · *italic* = vendor self-reported (inflates vs independent)
**ID** = normalized kebab-case key, the join key across all files in this repo and the handle agents should use. Platform-specific strings (OpenRouter, Azure, Bedrock…) may differ — verify per platform.

---

## All models

| ID | Provider | Model | Context | $ in | $ out | Input | Output | Tags / Notes |
|---|---|---|---|---|---|---|---|---|
| `gpt-6-astra` | **OpenAI** | GPT-6 Astra | 1.05M | 10.00 | 50.00 | text, image, file | text | 🧠🤖💻⌨️ cache ~$1 |
| `gpt-6-sol` | OpenAI | GPT-6 Sol | 1.05M | 2.00 | 10.00 | text, image, file | text | 🤖⌨️ half of Astra |
| `gpt-6-luna` | OpenAI | GPT-6 Luna | 1.05M | 0.10 | 0.50 | text, image, file | text | 🤖 high-volume cheap tier |
| `gpt-image-2` | OpenAI | GPT Image 2 | — | per image | per image | text, image | image | AA Image Arena #1 (Elo ~1339) |
| `whisper-v4` | OpenAI | Whisper v4 | — | per minute | — | audio | text | transcription standard |
| `sora-2` ⚠️ | OpenAI | Sora 2 | — | per second | — | text, image | video | API shutdown Sep 24, 2026 |
| `claude-fable-5-1` | **Anthropic** | Claude Fable 5.1 | 1M | 10.00 | 50.00 | text, image, file | text | 🧠🤖💻⌨️ cache $0.25 — cheapest long sessions |
| `claude-opus-5-5` | Anthropic | Claude Opus 5.5 | 1M | 4.00 | 20.00 | text, image, file | text | 🤖💻⌨️ Claude Code default |
| `claude-sonnet-5` | Anthropic | Claude Sonnet 5 | 1M | 2.00 | 10.00 | text, image, file | text | 🤖⌨️ daily driver |
| `gemini-3-1-pro` | **Google** | Gemini 3.1 Pro | 200K+ tiered | 2.00 | 12.00 | text, image, audio, video, file | text | 🧠🤖 Search grounding |
| `gemini-3-8-flash` | Google | Gemini 3.8 Flash | 1M | 0.75 | 3.75 | text, image, audio, video, file | text | 🤖 volume work · promo pricing |
| `gemini-3-8-live` | Google | Gemini 3.8 Live / ET | session | $0.005/min | $0.018/min | audio | audio | 🎙️ S2S quality index #1 (82.6) |
| `imagen-nano-banana-pro` | Google | Imagen (Nano Banana Pro) | — | per image | per image | text, image | image | 4K output, editing |
| `veo-3-1` | Google | Veo 3.1 | — | per second | — | text, image | video + audio | enterprise (GCP, SLA, SynthID) |
| `grok-4-7` | **xAI** | Grok 4.7 | 500K | 2.00 | 6.00 | text, image, file | text | 🤖⌨️ price/performance · cache $0.50 |
| `grok-imagine` | xAI | Grok Imagine | — | per image/sec | — | text, image | image, video | image→video |
| `kimi-k3` | **Moonshot AI** | Kimi K3 | 1M | 2.20* | 8.00* | text, image, video, file | text | 🧠🤖⌨️🔓 2.8T MoE · strongest open weights |
| `kimi-k2-8-preview` | Moonshot AI | Kimi K2.8 Preview | 1M | 0.60* | 2.50* | text, image, video | text | ⌨️🤖 near-K3 coding, much cheaper |

\* approximate; cached input cheaper. Kimi K3 is open-weight (own license, self-hostable).

**Notes**
- *Anthropic:* no image generation, no TTS. *ChatGPT voice mode* runs a text model + separate audio layer; a TTS API is available.
- *xAI:* live X data access; most permissive content policy in the frontier tier.
- *Moonshot:* K2.8 Preview auto-rolled out in Kimi Code.

---

## Benchmark matrix (classification step)

Where each model stands on the boards that matter. This is a **classification dimension for the table above**, not a separate leaderboard — use it to confirm a tag, not to rank across different benchmarks. Rows use the same `id` keys.

| ID | SWE-bench Verified (coding) | SWE-bench Pro (hard coding) | Terminal-Bench (agentic) | GPQA Diamond (science) | AA Intelligence Index |
|---|---|---|---|---|---|
| `claude-opus-5-5` | — | — | — | — | — |
| `claude-opus-5` | ***96.5*** | *79.2* | — | — | — |
| `claude-fable-5-1` | — | — | — | — | **65.7** |
| `claude-fable-5` | **95.0** | *80.0* | — | — | — |
| `claude-sonnet-5` | — | *63.2* | — | — | — |
| `gpt-6-astra` | — | — | — | *91.0* | **61.2** |
| `gpt-5-6-sol` | **96.2** | *64.6* | — | — | — |
| `gpt-5-6-luna` | **93.0** | *62.7* | — | — | — |
| `gpt-5-5` | *88.7* | — | *82.7* (TB 2.0) | — | — |
| `kimi-k3` | **93.4** | — | *88.3* | **93.1** | — |
| `kimi-k2-6` | *80.2* | — | — | — | — |
| `kimi-k2-8-preview` | — | — | — | — | — |
| `grok-4-7` | — | — | — | — | **46.3** |
| `grok-4-5` | **86.6** | *64.7* | — | — | — |
| `gemini-3-1-pro` | *80.6* | — | — | — | — |
| `gemini-3-8-flash` | — | — | — | — | **41.0** |
| `deepseek-v4-pro-max`* | *80.6* | — | — | — | — |
| `glm-5-2`* | **80.0** | *62.1* | — | — | — |
| `minimax-m2-5`* | *80.2* | — | — | — | — |

\* reference models tracked on the boards but not in the pricing matrix above.

**Reading rules**
- Cells are **not comparable across columns** — a 93 in Verified says nothing about GPQA.
- Prefer **bold (independent)** rows over *italic (vendor)* when both exist; vendor scaffolds inflate (vendor SWE-Pro board tops at 80%, standardized SEAL harness at 61.5%).
- Empty = not evaluated / no public number. Don't infer weakness.
- Full score data with dates and harnesses: [`benchmarks.yaml`](benchmarks.yaml)

---

## Quick comparison (by job)

| You need… | Best pick |
|---|---|
| Hardest reasoning | GPT-6 Astra ≈ Claude Fable 5.1 |
| Long-horizon autonomous work | Claude Fable 5.1 (cheap cache) |
| Daily coding | Claude Sonnet 5 · Kimi K2.8 Preview |
| Coding on a budget | Grok 4.7 · DeepSeek V4.1 Flash |
| Voice conversation (S2S) | Gemini 3.8 Live — unrivaled |
| Image generation | GPT Image 2 (quality) · Imagen (4K) |
| Video generation | Kling 3.0 (price) · Veo 3.1 (enterprise) |
| Self-host / data privacy | Kimi K3 (strongest open model) |
| Cheap volume work | Gemini 3.8 Flash · GPT-6 Luna |

---

## Files

- [`models.yaml`](models.yaml) — pricing/modality matrix, machine-readable (for agents and scripts)
- [`benchmarks.yaml`](benchmarks.yaml) — benchmark scores with source/harness/date per row
- [`SCHEMA.md`](SCHEMA.md) — field definitions and rules for both datasets
