# AI Model Comparison Matrix

Current models from 5 major providers: pricing, context windows, input/output modalities, and capability tags — grouped by what the model **outputs**, the axis people and agents actually choose on.

> **Last updated: September 2026.** Prices in USD per 1M tokens (input / output). Sources: provider pricing pages + Artificial Analysis, verified September 2026.

## Column semantics (classification schema)

Full definitions and contribution rules in [SCHEMA.md](SCHEMA.md). In short:

- **Input**: text · image · audio · video · file
- **Output**: text · audio (TTS) · image · video
- **Tags**: 🧠 reasoning · 🤖 agent/tool-use · 💻 computer use · ⌨️ coding · 🎙️ native speech · 🔓 open weights

## Legend
✅ = built-in, generally available · 🔶 = partial / preview / higher tier only · — = not supported · ⚠️ = sunset, don't build on it
**ID** = normalized kebab-case key, the join key across all files in this repo and the handle agents should use. Platform-specific strings (OpenRouter, Azure, Bedrock…) may differ — verify per platform.

---

## Text-out (LLMs)

The main comparison block — pricing, context, and tags are comparable across these rows.

| ID | Provider | Model | Context | $ in | $ out | Input | Tags / Notes |
|---|---|---|---|---|---|---|---|
| `gpt-6-astra` | **OpenAI** | GPT-6 Astra | 1.05M | 10.00 | 50.00 | text, image, file | 🧠🤖💻⌨️ cache ~$1 |
| `gpt-6-sol` | OpenAI | GPT-6 Sol | 1.05M | 2.00 | 10.00 | text, image, file | 🤖⌨️ half of Astra |
| `gpt-6-luna` | OpenAI | GPT-6 Luna | 1.05M | 0.10 | 0.50 | text, image, file | 🤖 high-volume cheap tier |
| `claude-fable-5-1` | **Anthropic** | Claude Fable 5.1 | 1M | 10.00 | 50.00 | text, image, file | 🧠🤖💻⌨️ cache $0.25 — cheapest long sessions |
| `claude-opus-5-5` | Anthropic | Claude Opus 5.5 | 1M | 4.00 | 20.00 | text, image, file | 🤖💻⌨️ Claude Code default |
| `claude-sonnet-5` | Anthropic | Claude Sonnet 5 | 1M | 2.00 | 10.00 | text, image, file | 🤖⌨️ daily driver |
| `gemini-3-1-pro` | **Google** | Gemini 3.1 Pro | 200K+ tiered | 2.00 | 12.00 | text, image, audio, video, file | 🧠🤖 Search grounding |
| `gemini-3-8-flash` | Google | Gemini 3.8 Flash | 1M | 0.75 | 3.75 | text, image, audio, video, file | 🤖 volume work · promo pricing |
| `grok-4-7` | **xAI** | Grok 4.7 | 500K | 2.00 | 6.00 | text, image, file | 🤖⌨️ price/performance · cache $0.50 |
| `kimi-k3` | **Moonshot AI** | Kimi K3 | 1M | 2.20* | 8.00* | text, image, video, file | 🧠🤖⌨️🔓 2.8T MoE · strongest open weights |
| `kimi-k2-8-preview` | Moonshot AI | Kimi K2.8 Preview | 1M | 0.60* | 2.50* | text, image, video | ⌨️🤖 near-K3 coding, much cheaper |

## Image-out

| ID | Provider | Model | $ per | Input | Notes |
|---|---|---|---|---|---|
| `gpt-image-2` | OpenAI | GPT Image 2 | image | text, image | AA Image Arena #1 (Elo ~1339); best prompt & text accuracy |
| `imagen-nano-banana-pro` | Google | Imagen (Nano Banana Pro) | image | text, image | Native 4K, editing, factual text via Gemini grounding |
| `grok-imagine` | xAI | Grok Imagine | image/sec | text, image | Image generation + image→video |

## Video-out

| ID | Provider | Model | $ per | Input | Notes |
|---|---|---|---|---|---|
| `veo-3-1` | Google | Veo 3.1 | second | text, image | Enterprise pick (GCP, SLA, SynthID); native audio |
| `sora-2` ⚠️ | OpenAI | Sora 2 | second | text, image | ⚠️ API shutdown Sep 24, 2026 — don't build on it |

## Audio / speech

| ID | Provider | Model | $ per | Input | Output | Notes |
|---|---|---|---|---|---|---|
| `gemini-3-8-live` | Google | Gemini 3.8 Live / ET | minute | audio | audio | 🎙️ Native speech-to-speech; S2S quality index #1 (82.6) |
| `whisper-v4` | OpenAI | Whisper v4 | minute | audio | text | Transcription standard |

---

## Our benchmark ([`evals/`](evals/))

We don't trust leaderboards — we run our own. [`evals/tasks.yaml`](evals/tasks.yaml) is our fixed task suite (coding, reasoning, instruction-following, long-context, tool-use, Turkish); [`evals/run.py`](evals/run.py) runs any model in the matrix against it through one OpenRouter key and grades the outputs; results land in [`evals/results.yaml`](evals/results.yaml) and feed back into the tags above. Details and how to run: [evals/README.md](evals/README.md).

Current standings (from our own runs — empty until we run):

| Task | gpt-6-astra | claude-opus-5-5 | gemini-3-8-flash | kimi-k3 | … |
|---|---|---|---|---|---|
| *see evals/results.yaml* | | | | | |

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
- [`evals/`](evals/) — our own benchmark: tasks, runner, results
- [`SCHEMA.md`](SCHEMA.md) — field definitions and rules for both datasets
