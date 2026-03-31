def firstUniqChar(s: str) -> int:
    freq = {}

    # Step 1: Count frequency
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Step 2: Find first unique character
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i

    return -1

# Example Usage
s = "leetcode"
print(firstUniqChar(s))