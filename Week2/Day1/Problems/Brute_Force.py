def validAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# Example Usage
s: str = "anagram"
t: str = "nagaram"

print(validAnagram(s,t))