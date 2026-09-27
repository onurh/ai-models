model: kimi-k3
prompt: code-bugfix
date: 2026-09-27
reasoning_tokens_saved_below: yes

---

**The bug:** Line 4 uses `a, b = b, a` instead of `a, b = b, a + b`.

**Fixed version:**
```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

**What was wrong:** The update `a, b = b, a` just swaps the two values back and forth (oscillating between 0 and 1) instead of computing each new Fibonacci number as the sum of the previous two, so it never actually accumulates the sequence.

--- reasoning ---

The bug: `a, b = b, a` should be `a, b = b, a + b`. Fix and explain in one sentence.