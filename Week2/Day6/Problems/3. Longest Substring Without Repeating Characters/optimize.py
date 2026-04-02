def longestSubarray(s: str) -> int:
    seen = set()
    l = max_len = 0

    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1

        seen.add(s[r])
        max_len = max(max_len, r - l + 1)
    return max_len

# Test cases
print(longestSubarray("abcabcbb"))  # Output: 3
print(longestSubarray("bbbbb"))     # Output: 1