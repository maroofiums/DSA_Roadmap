def longestSubstring(s: str) -> int:
    n = len(s)
    max_len = 0

    for i in range(n):
        for j in range(i + 1, n + 1):
            if len(set(s[i:j])) == j - i:  # Check if all characters are unique
                max_len = max(max_len, j - i)
    return max_len
# Test cases
print(longestSubstring("abcabcbb"))  # Output: 3
print(longestSubstring("bbbbb"))     # Output: 1
