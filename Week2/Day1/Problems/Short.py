from typing import Counter

def validAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

# Example Usage
s: str = "anagram"
t: str = "nagaram"

print(validAnagram(s,t))