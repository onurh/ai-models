---
name: run-benchmark
description: Procedure for running a model against the ai-models eval suite and logging the result. Use when asked to benchmark, evaluate, or test a model on this repo's prompts — covers running prompts (via API or chat UI), saving raw outputs under evals/outputs/, and writing concrete observations to evals/results.md.
---

# Run Benchmark

Single job: get a model's raw outputs for the eval prompts and log observations. Process lives in `evals/`; rules live in `../SCHEMA.md` §Benchmark observations.

## Procedure

1. **Pick the target.** The model must exist as an `id` in `../models.yaml` (add it first via the `update-model-board` skill if not).

2. **Run each prompt in `evals/prompts/`** (skip `README.md`):
   - Read the file; **strip the trailing HTML comment** (`<!-- ... -->`) — it is guidance, not prompt.
   - The body below the frontmatter is the exact prompt. Send it as-is, one user message, no system prompt, no temperature tweaks.
   - Via API when a key is available; via the model's chat UI otherwise. Either is valid — the process is tool-agnostic.

3. **Save every raw output** as `evals/outputs/<model-id>/<prompt-id>.md` with a header:
   ```
   model: <id>
   prompt: <prompt-id>
   date: YYYY-MM-DD

   ---

   <raw output>
   ```
   If the API exposes reasoning content, save it below a `--- reasoning ---` separator — future re-grading may need it.

4. **Write one observation row per prompt** in `evals/results.md`: date, model id, prompt id, and a single concrete sentence — what worked, what broke. Quote the failing constraint, don't editorialize ("broke constraint 2 silently", not "bad").

5. **Commit** with message: `evals: <model-id> — <n> prompts run`.

## Rules

- **No output saved, no observation.** Comparisons happen over preserved raw outputs, never memory.
- **Never edit a saved output.** If a run looks wrong, re-run and save under the same file (overwrite) with a fresh date.
- **Don't aggregate into scores.** The log stays qualitative; patterns emerge across rows over time.
- A single run never moves a tag in the main board — tag changes need a pattern of observations (record them, flag for review).
