---
name: contribute-board
description: Pull request workflow for contributing to the ai-models comparison board. Use when preparing a PR that adds a model, updates prices, adjusts tags, or marks a model sunset — defines what a mergeable PR must contain, which files may change, and the evidence standards reviewers will apply.
---

# Contribute Board PR

Single job: turn a model change into a PR that a maintainer can merge without rework. The board's rules are in `../SCHEMA.md` — a PR is a proposal that satisfies them, nothing more.

## Scope rules

- **One model family per PR.** "Add DeepSeek V4.1 Flash" merges; "September refresh of everything" doesn't.
- **Files a PR may touch**: `README.md` (table rows + provider notes), `models.yaml`, `SCHEMA.md` (only when adding a tag), `evals/` (only via the `run-benchmark` process). Anything else is out of scope.
- **No drive-by edits.** Restyling, rewording, or reordering unrelated rows belongs in its own PR.

## What a mergeable PR contains

1. **The row itself**, in both `models.yaml` (full field set, `id` first) and the correct README output-type table (see the ordering rules in SCHEMA — provider order, tier order, struck rows at group bottom).
2. **Evidence in the PR description**, per field:
   - price → link to the provider's pricing page, plus the month checked
   - modalities → link to the model card or API docs
   - context window → official docs
   - open weights → the weights repository + exact license name
3. **`source_date` set to the month the data was verified** (`YYYY-MM`).
4. For **price changes**: old value → new value, and the source. For **sunset marking**: the provider's shutdown notice link.
5. A first-party source beats a third-party article; a third-party article beats a blog. If the only source is a blog, say so in the PR description — don't present it as verified.

## Review standards (what gets a PR rejected)

- Guessed or unsourced prices — unknown means `null`, not an estimate.
- Modalities that haven't shipped ("coming soon" never enters).
- A provider that fails the admission rule (most-widely-known only — see SCHEMA rule 5).
- New tags used without a SCHEMA definition.
- A row added to the wrong output-type group or out of ordering.

## After merge

Maintainers sync the installed skill copies from `.agents/skills/` if rules changed. Contributors don't need to do anything else.
