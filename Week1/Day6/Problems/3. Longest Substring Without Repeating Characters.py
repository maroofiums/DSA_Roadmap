def lengthOfLongestSubstring(s: str) -> int:
    char = set()
    l = 0
    max_len = 0

    for r in range(len(s)):
        while s[r] in char:
            char.remove(s[l])
            l += 1

        char.add(s[r])
        max_len = max(max_len,r-l+1)

    return max_len

# Example Usage
s: str = "pwwkew"

print(lengthOfLongestSubstring(s))