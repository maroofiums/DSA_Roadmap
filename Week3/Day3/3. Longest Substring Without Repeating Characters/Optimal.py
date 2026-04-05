def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    max_len = 0
    l = 0

    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        max_len = max(max_len, r - l + 1)
    return max_len

# test cases
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(lengthOfLongestSubstring("pwwkew"))    # Output: 3