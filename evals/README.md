# evals — manual benchmark

A small test bench, not a leaderboard. The purpose is to run the same prompts across models, keep the outputs side by side, and observe which approaches hold up on which models. Over time these observations inform the capability tags in the main matrix.

## Process

1. Pick a prompt from [prompts/](prompts/).
2. Run it against the model (chat interface or API).
3. Save the raw output as `outputs/<model-id>/<prompt-id>.md`, e.g. `outputs/kimi-k3/tr-register.md`.
4. Add a one-line observation to [results.md](results.md).

## Principles

- Outputs are always saved. Comparisons are only valid over preserved raw outputs.
- Observations should be concrete ("silently violated constraint 2"), not verdicts ("bad").
- Each prompt file ends with an HTML comment describing what to check; it is not part of the prompt.
- New prompts are welcome: add a file under `prompts/` with `id` and `capability` in the frontmatter.

## Prompts

| ID | Capability | What it probes |
|---|---|---|
| code-bugfix | coding | Finding a subtle recurrence bug |
| code-intervals | coding | Writing a correct merge-intervals algorithm |
| reason-batball | reasoning | Classic cognitive-reflection traps |
| instr-constraints | instruction-following | Multi-constraint generation with a banned letter |
| tool-sequence | agent | Correct tool-call ordering, ignoring irrelevant tools |
| tr-register | multilingual | Turkish register shift and spelling-rule knowledge |
