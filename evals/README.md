# evals/ — our own benchmark

We don't take leaderboard numbers at face value (vendor scaffolds inflate them — see git history for the removed public-scores matrix). Instead we run every model in the matrix against a **fixed task suite** and grade the outputs ourselves. Results feed back into the `tags` in the main matrix.

## Layout

| File | What |
|---|---|
| `tasks.yaml` | The task suite. Each task = one prompt + one grader + one capability it tests |
| `run.py` | Runner + grader + report. Stdlib + PyYAML only |
| `results.yaml` | One row per (model, task) run. Starts empty — only real runs enter |
| `outputs/<model>/<task>.txt` | Raw model outputs, kept for audit and re-grading |

## The process

1. **Run** — send every task to the model, save raw output:
   ```bash
   export OPENROUTER_API_KEY=...
   python run.py --model kimi-k3                     # all tasks
   python run.py --model kimi-k3 --task code-01      # one task
   ```
   First time only: `python run.py --make-longctx` to generate the long-context prompt (~120K tokens).

2. **Grade** — deterministic graders (exact/contains/regex) run locally; open-ended tasks use LLM-as-judge:
   ```bash
   python run.py --grade --model kimi-k3 --judge-model claude-sonnet-5
   ```

3. **Report** — standings by task:
   ```bash
   python run.py --report
   ```

4. **Feed back** — if a model passes the tasks behind a tag, the tag stays; if it fails, the tag is removed from `models.yaml` with a note. Tags are earned here, not copied from marketing.

## Rules (also in ../SCHEMA.md)

- **Fixed suite.** Don't swap tasks between models mid-comparison. Suite changes bump `version` and reset the matrix.
- **Raw outputs are kept** — every score is re-gradable and auditable.
- **Judge declared.** LLM-graded rows record which judge model graded them.
- **Empty cell ≠ weakness**, but unlike public leaderboards, an empty cell here just means *we haven't run it yet* — the fix is to run it, not to infer.
- **Cost noted**: judge and long-context runs burn tokens; the point of our suite is it's small enough to re-run monthly.

## Task suite v1

| ID | Capability | Grader | What it probes |
|---|---|---|---|
| code-01 | coding | judge | Merge intervals — algorithmic correctness |
| code-02 | coding | contains | Spot and fix a subtle recurrence bug |
| reason-01 | reasoning | exact | Cognitive reflection (bat & ball) |
| reason-02 | reasoning | exact | Rate reasoning |
| math-01 | reasoning | exact | Prime sum |
| instr-01 | instruction-following | judge | Multi-constraint generation (start word, banned letter, end token) |
| longctx-01 | long-context | contains | Anchor phrase buried in ~120K tokens |
| tool-01 | agent | judge | Correct tool-call sequence for a comparative question |
| tr-01 | multilingual | judge | Turkish register rewriting (meaning preserved, more formal) |
