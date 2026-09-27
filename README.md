# AI Model Comparison Matrix

Current models from 5 major providers: pricing, context windows, input/output modalities, and capability classification.

> **Last updated: September 2026.** Prices in USD per 1M tokens (input / output). Sources: provider pricing pages + Artificial Analysis, verified September 2026.

## Column semantics (classification schema)

Full definitions and contribution rules in [SCHEMA.md](SCHEMA.md). In short:

- **Input**: text · image · audio · video · file
- **Output**: text · audio (TTS) · image · video
- **Tags**: 🧠 reasoning · 🤖 agent/tool-use · 💻 computer use · ⌨️ coding · 🔓 open weights (self-hostable)

### Legend
✅ = built-in, generally available · 🔶 = partial / preview / higher tier only · — = not supported

---

## OpenAI

| Model | Context | $ input | $ output | Input | Output | Tags |
|---|---|---|---|---|---|---|
| **GPT-6 Astra** | 1.05M | 10.00 | 50.00 | text, image, file | text | 🧠🤖💻⌨️ |
| **GPT-6 Sol** | 1.05M | 2.00 | 10.00 | text, image, file | text | 🤖⌨️ |
| **GPT-6 Luna** | 1.05M | 0.10 | 0.50 | text, image, file | text | 🤖 (cheap, high-volume) |
| **GPT Image 2** | — | per image | per image | text, image | image | Top arena score (Elo ~1339) |
| **Whisper v4** | — | per minute | — | audio | text | Transcription standard |
| **Sora 2** ⚠️ | — | per second | — | text, image | video | ⚠️ API shutdown: Sep 24, 2026 |

*ChatGPT voice mode runs a text model + separate audio layer; a TTS API is available.*

## Anthropic

| Model | Context | $ input | $ output | Input | Output | Tags |
|---|---|---|---|---|---|---|
| **Claude Fable 5.1** | 1M | 10.00 | 50.00 | text, image, file | text | 🧠🤖💻⌨️ |
| **Claude Opus 5.5** | 1M | 4.00 | 20.00 | text, image, file | text | 🤖💻⌨️ |
| **Claude Sonnet 5** | 1M | 2.00 | 10.00 | text, image, file | text | 🤖💻⌨️ |

*No image generation, no TTS. Cache reads at $0.25/1M (Fable) — cheapest for long agent sessions.*

## Google

| Model | Context | $ input | $ output | Input | Output | Tags |
|---|---|---|---|---|---|---|
| **Gemini 3.1 Pro** | 200K+ (tiered) | 2.00 | 12.00 | text, image, audio, video, file | text | 🧠🤖 |
| **Gemini 3.8 Flash** | 1M | 0.75 | 3.75 | text, image, audio, video, file | text | 🤖 (volume work) |
| **Gemini 3.8 Live / ET** | session | $0.005/min | $0.018/min | audio | audio | 🎙️ S2S quality index #1 (82.6) |
| **Imagen (Nano Banana Pro)** | — | per image | — | text, image | image | 4K output, editing |
| **Veo 3.1** | — | per second | — | text, image | video + audio | Enterprise/SLA option |

## xAI

| Model | Context | $ input | $ output | Input | Output | Tags |
|---|---|---|---|---|---|---|
| **Grok 4.7** | 500K | 2.00 | 6.00 | text, image, file | text | 🤖⌨️ (price/performance) |
| **Grok Imagine** | — | per image/sec | — | text, image | image, video | Image→video |

*Live X data access. Most permissive content policy in the frontier tier.*

## Moonshot AI (Kimi)

| Model | Context | $ input | $ output | Input | Output | Tags |
|---|---|---|---|---|---|---|
| **Kimi K3** | 1M | 2.20* | 8.00* | text, image, video, file | text | 🧠🤖⌨️🔓 2.8T MoE |
| **Kimi K2.8 Preview** | 1M | 0.60* | 2.50* | text, image, video | text | ⌨️🤖 (near-K3, cheap) |

*\*approximate; cached input cheaper. K3 is open-weight (own license, self-hostable).*

---

## Quick comparison (flagships)

| Capability | Best pick |
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

- [`models.yaml`](models.yaml) — machine-readable version of this data (for agents and scripts)
- [`SCHEMA.md`](SCHEMA.md) — column definitions and rules for adding new models
