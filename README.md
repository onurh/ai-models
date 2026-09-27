# AI Model Comparison Matrix

A maintained comparison of current models from the major providers (plus specialist speech vendors): pricing, context windows, input/output modalities, and capability classifications. The board is grouped by output type — the axis on which model selection is usually made.

Last updated: September 2026. Prices are USD per 1M tokens (input / output), verified against provider pricing pages and Artificial Analysis in September 2026.

## How to read the board

Column definitions and data rules are in [SCHEMA.md](SCHEMA.md).

- **Input / Output**: text, image, audio, video, file.
- **Capabilities**: reasoning, agent (tool-use and multi-step work), computer-use (GUI control), coding, voice (native speech-to-speech), long-context (500K+), cheap-volume.
- **ID**: normalized kebab-case key used as the join handle across all files in this repository. Platform-specific model strings (OpenRouter, Azure, Bedrock) may differ; verify per platform.
- **Released**: `YYYY-MM` of general API availability; year only when the month is unconfirmed.
- **Status**: struck-through models are discontinued or superseded; the rows stay for reference but must not be selected for new work.

## Ordering

Within each output-type group:

1. Provider blocks in fixed order: OpenAI, Anthropic, Google, xAI, Moonshot, DeepSeek; specialist vendors (e.g. ElevenLabs) last.
2. Within a provider block: tier order, premium first (flagship → mid → budget).
3. Same tier: newest release first.
4. Struck-through rows always sink to the bottom of their group.

---

## Text-output models

| ID | Provider | Model | Released | Context | $ input | $ output | Input | Capabilities / notes |
|---|---|---|---|---|---|---|---|---|
| `gpt-6-astra` | OpenAI | GPT-6 Astra | 2026-09 | 1.05M | 10.00 | 50.00 | text, image, file | reasoning, agent, computer-use, coding; cache reads ~$1 |
| `gpt-6-sol` | OpenAI | GPT-6 Sol | 2026-09 | 1.05M | 2.00 | 10.00 | text, image, file | agent, coding |
| `gpt-6-luna` | OpenAI | GPT-6 Luna | 2026-09 | 1.05M | 0.10 | 0.50 | text, image, file | agent, cheap-volume |
| `gpt-5-6-sol` | OpenAI | GPT-5.6 Sol | 2026-07 | 1.05M | 4.00 | 20.00 | text, image, file | agent, coding; previous-gen flagship coder, still selectable |
| `gpt-5-6-terra` | OpenAI | GPT-5.6 Terra | 2026-07 | 1.05M | 2.00 | 12.00 | text, image, file | agent |
| `gpt-5-6-luna` | OpenAI | GPT-5.6 Luna | 2026-07 | 1.05M | 0.20 | 1.20 | text, image, file | agent, cheap-volume |
| `claude-fable-5-1` | Anthropic | Claude Fable 5.1 | 2026-09 | 1M | 10.00 | 50.00 | text, image, file | reasoning, agent, computer-use, coding; cache reads $0.25 |
| `claude-opus-5-5` | Anthropic | Claude Opus 5.5 | 2026-09 | 1M | 4.00 | 20.00 | text, image, file | agent, computer-use, coding; Claude Code default |
| `claude-sonnet-5` | Anthropic | Claude Sonnet 5 | 2026-06 | 1M | 2.00 | 10.00 | text, image, file | agent, coding |
| `claude-haiku-4-5` | Anthropic | Claude Haiku 4.5 | 2025-10 | 200K | 1.00 | 5.00 | text, image | cheap-volume; fast small tier |
| `gemini-3-1-pro` | Google | Gemini 3.1 Pro | 2026-02 | 200K+ (tiered) | 2.00 | 12.00 | text, image, audio, video, file | reasoning, agent; Search grounding; preview |
| `gemini-3-8-flash` | Google | Gemini 3.8 Flash | 2026-09 | 1M | 0.75 | 3.75 | text, image, audio, video, file | agent, cheap-volume; promo pricing |
| `gemini-3-5-flash-lite` | Google | Gemini 3.5 Flash-Lite | 2026 | 1M | 0.30 | 2.50 | text, image, audio, video, file | cheap-volume; lowest-cost Gemini tier |
| `grok-4-7` | xAI | Grok 4.7 | 2026-09 | 500K | 2.00 | 6.00 | text, image, file | agent, coding; cache hits $0.50 |
| `kimi-k3` | Moonshot AI | Kimi K3 | 2026-07 | 1M | 2.20* | 8.00* | text, image, video, file | reasoning, agent, coding; open weights (2.8T MoE) |
| `kimi-k2-8-preview` | Moonshot AI | Kimi K2.8 Preview | 2026-09 | 1M | 0.60* | 2.50* | text, image, video | agent, coding |
| `deepseek-v4-pro` | DeepSeek | DeepSeek V4 Pro | 2026-08 | 1M | 0.66* | 1.98* | text | reasoning, agent, coding; open weights (1.6T MoE, MIT) |
| `deepseek-v4-1-flash` | DeepSeek | DeepSeek V4.1 Flash | 2026-09 | 1M | 0.15* | 0.60* | text, image | agent, coding, cheap-volume; open weights (552B MoE, MIT); native vision |
| ~~`claude-opus-5`~~ | Anthropic | ~~Claude Opus 5~~ | 2026-07 | 1M | 5.00 | 25.00 | text, image, file | Superseded by Claude Opus 5.5 |

\* Approximate or off-peak rates (DeepSeek peak hours are 2×); cached input is cheaper. Kimi K3, DeepSeek V4 Pro, and V4.1 Flash are open-weight and can be self-hosted.

Provider notes:

- **Anthropic** does not offer image generation or TTS. ChatGPT voice mode is a text model with a separate audio layer; OpenAI offers a TTS API separately.
- **xAI** provides live X data access and the most permissive content policy in the frontier tier.
- **Moonshot** rolled K2.8 Preview out automatically to Kimi Code users.
- Deliberately omitted: Gemini 3.5 Pro (announced, not yet shipped — "coming soon" never enters the board) and GPT-5.5 (two generations behind).

## Image-output models

| ID | Provider | Model | Released | Billing | Input | Notes |
|---|---|---|---|---|---|---|
| `gpt-image-2` | OpenAI | GPT Image 2 | 2026 | per image | text, image | Top of the AA Image Arena (Elo ~1339); strongest prompt and text accuracy |
| `imagen-nano-banana-pro` | Google | Imagen (Nano Banana Pro) | 2026 | per image | text, image | Native 4K output, editing, factual text via Gemini grounding |
| `grok-imagine` | xAI | Grok Imagine | 2026-05 | per image | text, image | Image generation and image-to-video |

## Video-output models

| ID | Provider | Model | Released | Billing | Input | Notes |
|---|---|---|---|---|---|---|
| `veo-3-1` | Google | Veo 3.1 | 2026 | per second | text, image | Enterprise option (GCP, SLA, SynthID); native audio |
| ~~`sora-2`~~ | OpenAI | ~~Sora 2~~ | 2026 | per second | text, image | Shut down September 24, 2026 — row kept for reference |

## Audio models

| ID | Provider | Model | Released | Billing | Input | Output | Notes |
|---|---|---|---|---|---|---|---|
| `whisper-v4` | OpenAI | Whisper v4 | 2026 | per minute | audio | text | De facto transcription standard |
| `openai-tts` | OpenAI | OpenAI TTS | 2025 | per 1K chars | text | audio | Low-latency speech synthesis (`gpt-4o-mini-tts`, `tts-1-hd`) |
| `gemini-3-8-live` | Google | Gemini 3.8 Live (Extended Thinking) | 2026-09 | per minute | audio | audio | Native speech-to-speech; #1 on the AA S2S quality index (82.6) |
| `google-chirp3-hd` | Google | Cloud TTS (Chirp 3 HD) | 2025 | per 1M chars | text | audio | Google Cloud voice library, 60+ languages |
| `elevenlabs-v3` | ElevenLabs | ElevenLabs v3 | 2026 | per 1K chars | text | audio | Expressive TTS, voice cloning, dubbing; strong multilingual incl. Turkish |

---

## Benchmark ([evals/](evals/))

The benchmark is a small, manual test bench rather than a leaderboard. Prompts live in [evals/prompts/](evals/prompts/); a prompt is run against a model, the raw output is saved under `evals/outputs/<model-id>/`, and a one-line observation is logged in [evals/results.md](evals/results.md). Over time these observations confirm or adjust the capability classifications above. Process details: [evals/README.md](evals/README.md).

---

## Selection guide

| Requirement | Suggested pick |
|---|---|
| Hardest reasoning tasks | GPT-6 Astra or Claude Fable 5.1 |
| Long-horizon autonomous work | Claude Fable 5.1 (lowest cache-read cost) |
| Everyday coding | Claude Sonnet 5, Kimi K2.8 Preview |
| Coding on a budget | Grok 4.7, DeepSeek V4.1 Flash |
| Voice-first product | Gemini 3.8 Live |
| Image generation | GPT Image 2 (accuracy), Imagen (4K) |
| Video generation | Kling 3.0 (cost), Veo 3.1 (enterprise) |
| Self-hosting / data privacy | Kimi K3 or DeepSeek V4 Pro (open weights) |
| High-volume low-cost work | Gemini 3.5 Flash-Lite, GPT-6 Luna, DeepSeek V4.1 Flash |

## Files

- [models.yaml](models.yaml) — machine-readable version of the pricing and modality matrix
- [evals/](evals/) — benchmark prompts, saved outputs, and observation log
- [SCHEMA.md](SCHEMA.md) — field definitions and data rules

---

Maintained with [Kimi](https://www.kimi.com) (K2.8).
