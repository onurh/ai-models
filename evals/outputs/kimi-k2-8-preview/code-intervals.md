model: kimi-k2-8-preview
prompt: code-intervals
date: 2026-09-27
reasoning_tokens_saved_below: yes

---

```python
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort by start time — O(n log n)
    sorted_intervals = sorted(intervals, key=lambda iv: iv[0])

    merged = [sorted_intervals[0]]
    for start, end in sorted_intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:          # overlap OR adjacency (1,2)+(2,3)
            merged[-1] = (last_start, max(last_end, end))  # handles nesting
        else:
            merged.append((start, end))

    return merged
```

**How it handles the edge cases:**

- **Empty input:** returns `[]` immediately.
- **Adjacent intervals:** the condition `start <= last_end` uses `<=`, so `(1,2)` and `(2,3)` merge into `(1,3)`. (If you wanted adjacency *not* to merge, use `<` instead.)
- **Fully nested:** since we only extend with `max(last_end, end)`, `(1,10)` swallows `(2,3)` and `(4,5)` without growing unnecessarily.

**Complexity:** sorting is O(n log n), the merge pass is O(n), so total is **O(n log n)** time and O(n) space for the output.

Example:

```python
data = [(1, 3), (8, 10), (2, 6), (15, 18), (9, 12), (3, 3), (16, 17)]
print(merge_intervals(data))
# [(1, 6), (8, 12), (15, 18)]
```

Note this works for any 2-element interval representation (tuples, lists) since it only unpacks `start, end`. If your intervals might arrive unsorted with guarantees about validity (e.g., `start <= end`), no extra handling is needed — sorting normalizes everything.

--- reasoning ---

Write the function with explanation.