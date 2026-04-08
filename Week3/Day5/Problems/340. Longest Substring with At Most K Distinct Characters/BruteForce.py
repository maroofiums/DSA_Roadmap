def longestKDistinct(s: str, k: int) -> int:
    longest = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            seen.add(s[j])
            if len(seen) > k:
                break
            longest = max(longest, j - i + 1)
    return longest

# Example Usage
s: str = "eceba"
k: int = 2
print(longestKDistinct(s, k))  # Output: 3