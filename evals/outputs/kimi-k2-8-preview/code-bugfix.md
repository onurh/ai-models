model: kimi-k2-8-preview
prompt: code-bugfix
date: 2026-09-27
reasoning_tokens_saved_below: yes

---

**The bug:** The tuple update is missing the addition — `a, b = b, a` just swaps the values, so `b` never accumulates the sum.

**Fixed code:**

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

**Explanation:** The original code swapped `a` and `b` each iteration instead of advancing the Fibonacci sequence, because it should assign `b` to `a` and `a + b` to `b` (the tuple assignment evaluates both right-hand expressions *before* any assignment, so the old values are used correctly).

--- reasoning ---

The bug: tuple assignment should be `a, b = b, a + b`. Explain in one sentence.