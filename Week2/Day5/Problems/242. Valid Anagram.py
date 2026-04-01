def validAnagram(s:str, t:str) -> bool:
    if len(s) != len(t):
        return False

    freq = {}

    for c in s:
        freq[c] = freq.get(c,0) + 1

    for c in t:
        freq[c] -= 1

    for value in freq.values():
        if value != 0:
            return False

    return True

# Example usage
s:str = "anagram"
t:str = "nagaram"

print(validAnagram(s,t))