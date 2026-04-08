def longestKDistinct(s: str, k: int) -> int:
    count = {}
    l = res = 0

    for r in range(len(s)):
        c = s[r]
        count[c] = count.get(c, 0) + 1

        while len(count) > k:
            left_char = s[l]
            count[left_char] -= 1
            if count[left_char] == 0:
                del count[left_char]
            l += 1
        res = max(res, r - l + 1)

    return res

# Example Usage
s: str = "eceba"
k: int = 2
print(longestKDistinct(s, k))  # Output: 3