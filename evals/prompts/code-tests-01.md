---
id: code-tests-01
capability: coding
grader: executable
---

The function below is buggy. Fix it so that it satisfies the specification
and passes ALL the asserts. Output only the corrected function, no explanation.

```python
def rle_decode(s):
    """Decode a run-length encoded string.

    Encoding rule: one character followed by its repeat count ('a3b1' -> 'aaab').
    Counts may be multi-digit ('c12' -> 'cccccccccccc').
    Empty input returns ''. Malformed input (a character not followed by a
    positive integer count) raises ValueError.
    """
    out = []
    i = 0
    while i < len(s):
        ch = s[i]
        i += 1
        count = 0
        while i < len(s) and s[i].isdigit():
            count = count + int(s[i])
            i += 1
        out.append(ch * count)
    return ''.join(out)


assert rle_decode('a3b1c10') == 'aaab' + 'c' * 10
assert rle_decode('') == ''
assert rle_decode('x1') == 'x'
assert rle_decode('z25') == 'z' * 25
for bad in ['a', 'a0', '3a', 'ab2']:
    try:
        rle_decode(bad)
        raise AssertionError(f"expected ValueError for {bad!r}")
    except ValueError:
        pass
```

<!-- What to look for: the count-accumulation bug (count * 10 + digit, not count + digit);
whether it also adds the missing ValueError validation; grader is executable — run the
output against the asserts. -->
