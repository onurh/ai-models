model: kimi-k3
prompt: code-intervals
date: 2026-09-27
reasoning_tokens_saved_below: yes

---

```python
def merge_intervals(intervals):
    """
    Merge overlapping or adjacent intervals.

    Args:
        intervals: iterable of (start, end) pairs.

    Returns:
        List of (start, end) tuples, sorted by start, with no overlaps.
        Adjacent intervals (e.g., (1, 2) and (2, 3)) are merged.
    """
    if not intervals:
        return []

    # Sort by start (then end) — O(n log n), dominates total complexity
    sorted_intervals = sorted(intervals, key=lambda iv: (iv[0], iv[1]))

    merged = [tuple(sorted_intervals[0])]

    for start, end in sorted_intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:  # overlaps or is adjacent
            # max() handles fully nested intervals like (1, 10) inside (1, 5)
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged
```

**How it works:**

1. **Empty input** — return `[]` immediately.
2. **Sort by start** — after sorting, any interval that merges with the current one must start at or before the current end, so a single linear pass suffices.
3. **Adjacency** — the condition `start <= last_end` (not `<`) treats touching intervals like `(1, 2)` and `(2, 3)` as mergeable, producing `(1, 3)`.
4. **Nesting** — using `max(last_end, end)` ensures a nested interval like `(2, 4)` inside `(1, 10)` doesn't shrink the merged result.

**Quick verification:**

```python
assert merge_intervals([]) == []
assert merge_intervals([(1, 2), (2, 3)]) == [(1, 3)]              # adjacent
assert merge_intervals([(1, 10), (2, 4), (5, 6)]) == [(1, 10)]    # nested
assert merge_intervals([(4, 5), (1, 3)]) == [(1, 3), (4, 5)]      # sorted output
assert merge_intervals([(1, 4), (0, 2), (3, 5)]) == [(0, 5)]      # unsorted chain
```

**Complexity:** O(n log n) from sorting, plus O(n) for the single merge pass and O(n) space for the output.

--- reasoning ---

Simple task. Provide solution with explanation and tests.