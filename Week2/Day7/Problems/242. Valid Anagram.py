def validAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        count[char] = count.get(char, 0) - 1
    
    for value in count.values():
        if value != 0:
            return False
    return True

# Example usage:
s = "anagram"
t = "nagaram"
print(validAnagram(s, t))
