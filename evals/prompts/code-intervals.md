---
id: code-intervals
capability: coding
---

In Python, write a function `merge_intervals(intervals)` that merges overlapping
intervals and returns the result sorted by start. Handle: empty input, adjacent
intervals like (1,2)+(2,3), and fully nested intervals. One pass after sorting is
enough — keep it O(n log n) total.

<!-- What to look for: sorts first, compares with last merged item, handles edge cases without being asked twice -->
