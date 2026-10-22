def first_and_last(s: str) -> str:
    """
    Return a new string made of the first character of `s`
    followed by the last character of `s`.

    - If `s` is empty, return "".
    - If `s` has exactly one character, return that character twice.

    Example: first_and_last("python") -> "pn"
    """
    if len(s) == 0:
        return ""

    a = ""
    a += s[0]
    a += s[-1]
    return a


def reverse_string(s: str) -> str:
    """
    Return a new string containing the characters of `s` in
    reverse order. Use a slice with a negative step.

    Example: reverse_string("python") -> "nohtyp"
    """
    a = s[::-1]
    return a


def every_kth_from(s: str, start: int, k: int) -> str:
    """
    Return the characters of `s` at positions start, start + k,
    start + 2k, ... continuing to the end of the string.
    `start` may be negative (counted from the end). `k` is
    always >= 1. If `start` is out of range, return "".

    Example: every_kth_from("abcdefgh", 1, 3) -> "beh"
    """
    if start < -len(s) or start >= len(s):
        return ""
    a = ""
    if start<0:
        start = start + len(s)

    i = start
    while i < len(s):
        a = a + s[i]
        i = i + k

    return a
