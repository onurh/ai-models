---
id: code-bugfix
capability: coding
---

This Python function has a bug. Find it, fix it, and explain in one sentence what was wrong:

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a
    return a

<!-- What to look for: recognizes the recurrence is wrong (a, b = b, a + b), not an off-by-one -->
