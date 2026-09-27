# AI Model Comparison Matrix

A maintained comparison of current models from the major providers (plus specialist speech vendors): pricing, context windows, input/output modalities, and capability classifications. The board is grouped by output type — the axis on which model selection is usually made.

Last updated: September 2026. Prices are USD per 1M tokens (input / output), verified against provider pricing pages and Artificial Analysis in September 2026.

## How to read the board

Column definitions and data rules are in [SCHEMA.md](SCHEMA.md).

- **Input / Output**: text, image, audio, video, file.
- **Capabilities**: reasoning, agent (tool-use and multi-step work), computer-use (GUI control), coding, voice (native speech-to-speech), long-context (500K+), cheap-volume.
- **ID**: normalized kebab-case key used as the join handle across all files in this repository. Platform-specific model strings (OpenRouter, Azure, Bedrock) may differ; verify per platform.
- **Status**: struck-through models are discontinued or shut down; the rows stay for reference but must not be selected for new work.

---

## Text-output models

| ID | Provider | Model | Context | $ input | $ output | Input | Capabilities / notes |
|---|---|---|---|---|---|---|---|
| `gpt-6-astra` | OpenAI | GPT-6 Astra | 1.05M | 10.00 | 50.00 | text, image, file | reasoning, agent, computer-use, coding; cache reads ~$1 |
| `gpt-6-sol` | OpenAI | GPT-6 Sol | 1.05M | 2.00 | 10.00 | text, image, file | agent, coding |
| `gpt-6-luna` | OpenAI | GPT-6 Luna | 1.05M | 0.10 | 0.50 | text, image, file | agent, cheap-volume |
| `claude-fable-5-1` | Anthropic | Claude Fable 5.1 | 1M | 10.00 | 50.00 | text, image, file | reasoning, agent, computer-use, coding; cache reads $0.25 |
| `claude-opus-5-5` | Anthropic | Claude Opus 5.5 | 1M | 4.00 | 20.00 | text, image, file | agent, computer-use, coding; Claude Code default |
| `claude-sonnet-5` | Anthropic | Claude Sonnet 5 | 1M | 2.00 | 10.00 | text, image, file | agent, coding |
| `gemini-3-1-pro` | Google | Gemini 3.1 Pro | 200K+ (tiered) | 2.00 | 12.00 | text, image, audio, video, file | reasoning, agent; Search grounding |
| `gemini-3-8-flash` | Google | Gemini 3.8 Flash | 1M | 0.75 | 3.75 | text, image, audio, video, file | agent, cheap-volume; promo pricing |
| `grok-4-7` | xAI | Grok 4.7 | 500K | 2.00 | 6.00 | text, image, file | agent, coding; cache hits $0.50 |
| `kimi-k3` | Moonshot AI | Kimi K3 | 1M | 2.20* | 8.00* | text, image, video, file | reasoning, agent, coding; open weights (2.8T MoE) |
| `kimi-k2-8-preview` | Moonshot AI | Kimi K2.8 Preview | 1M | 0.60* | 2.50* | text, image, video | agent, coding |

\* Approximate; cached input is cheaper. Kimi K3 is open-weight under its own license and can be self-hosted.

Provider notes:

- **Anthropic** does not offer image generation or TTS. ChatGPT voice mode is a text model with a separate audio layer; OpenAI offers a TTS API separately.
- **xAI** provides live X data access and the most permissive content policy in the frontier tier.
- **Moonshot** rolled K2.8 Preview out automatically to Kimi Code users.

## Image-output models

| ID | Provider | Model | Billing | Input | Notes |
|---|---|---|---|---|---|
| `gpt-image-2` | OpenAI | GPT Image 2 | per image | text, image | Top of the AA Image Arena (Elo ~1339); strongest prompt and text accuracy |
| `imagen-nano-banana-pro` | Google | Imagen (Nano Banana Pro) | per image | text, image | Native 4K output, editing, factual text via Gemini grounding |
| `grok-imagine` | xAI | Grok Imagine | per image | text, image | Image generation and image-to-video |

## Video-output models

| ID | Provider | Model | Billing | Input | Notes |
|---|---|---|---|---|---|
| `veo-3-1` | Google | Veo 3.1 | per second | text, image | Enterprise option (GCP, SLA, SynthID); native audio |
| ~~`sora-2`~~ | OpenAI | ~~Sora 2~~ | per second | text, image | Shut down September 24, 2026 — row kept for reference |

## Audio models

| ID | Provider | Model | Billing | Input | Output | Notes |
|---|---|---|---|---|---|---|
| `gemini-3-8-live` | Google | Gemini 3.8 Live (Extended Thinking) | per minute | audio | audio | Native speech-to-speech; #1 on the AA S2S quality index (82.6) |
| `whisper-v4` | OpenAI | Whisper v4 | per minute | audio | text | De facto transcription standard |
| `openai-tts` | OpenAI | OpenAI TTS (`gpt-4o-mini-tts`, `tts-1-hd`) | per 1K chars | text | audio | Low-latency speech synthesis API |
| `elevenlabs-v3` | ElevenLabs | ElevenLabs v3 | per 1K chars | text | audio | Expressive TTS, voice cloning, dubbing |

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
| Self-hosting / data privacy | Kimi K3 (strongest open-weight option) |
| High-volume low-cost work | Gemini 3.8 Flash, GPT-6 Luna |

## Files

- [models.yaml](models.yaml) — machine-readable version of the pricing and modality matrix
- [evals/](evals/) — benchmark prompts, saved outputs, and observation log
- [SCHEMA.md](SCHEMA.md) — field definitions and data rules
