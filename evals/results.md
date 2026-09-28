# Observation log

One row per run: model, prompt, observation. Always include the date; keep observations concrete.

| Date | Model | Prompt | Observation |
|---|---|---|---|
| 2026-09-27 | kimi-k3 | code-bugfix | Found the exact bug (`a, b = b, a` should be `a, b = b, a + b`); explained the 0/1 oscillation correctly |
| 2026-09-27 | kimi-k2-8-preview | code-bugfix | Same correct fix; bonus: correctly explained why tuple assignment evaluates RHS before assigning |
| 2026-09-27 | kimi-k3 | reason-batball | $0.05 with algebra; missing-dollar puzzle resolved via correct ledger ($27 = $25 + $2) |
| 2026-09-27 | kimi-k2-8-preview | reason-batball | Same; explicitly names the "add the $2" step as double-counting |
| 2026-09-27 | kimi-k3 | instr-constraints | All 3 constraints met; sentence 4 genuinely "e"-free; reasoning shows it noticed the END-token vs banned-letter conflict and resolved it |
| 2026-09-27 | kimi-k2-8-preview | instr-constraints | All 3 constraints met; same conflict noticed and resolved identically |
| 2026-09-27 | kimi-k3 | tool-sequence | Correct minimal plan (weather for both cities, no get_time); refused to invent temperatures — final answer given as a formula, not fabricated numbers |
| 2026-09-27 | kimi-k2-8-preview | tool-sequence | Same correct plan and same honesty about missing tool outputs |
| 2026-09-27 | kimi-k3 | tr-register | Clean register shift; spelling answer correct (TDK: "zekâ", circumflex kept, with a fair note on widespread "zeka" usage) |
| 2026-09-27 | kimi-k2-8-preview | tr-register | Clean register shift with useful diff notes; but spelling answer wrong — confidently claimed TDK dropped the circumflex in 2012 (fabricated rule); K3's answer is the correct one |
| 2026-09-27 | kimi-k3 | code-intervals | Output saved; correctness not yet manually verified |
| 2026-09-27 | kimi-k2-8-preview | code-intervals | Output saved; correctness not yet manually verified |
| 2026-09-28 | kimi-k3 | code-tests-01 | **Executable grade: PASS** — found the count-accumulation bug (`count * 10 + digit`), added the missing ValueError validation, all asserts pass when run |
| 2026-09-28 | kimi-k2-8-preview | code-tests-01 | **Executable grade: PASS** — same correct fix and validation; all asserts pass when run |
