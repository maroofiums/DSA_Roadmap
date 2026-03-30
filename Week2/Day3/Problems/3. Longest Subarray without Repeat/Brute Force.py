def longestSubarray(s: str) -> int:
    n = len(s)
    best = 0

    for i in range(n):
        for j in range(i, n):
            substr = s[i:j+1]
            if len(set(substr)) == len(substr):
                best = max(best, j - i + 1)

    return best

# Example usage:
s = "abcabcbb"
print(longestSubarray(s))  