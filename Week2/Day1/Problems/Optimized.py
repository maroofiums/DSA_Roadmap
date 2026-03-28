def validAnagram(s:str,t:str) -> bool:
    freq = {}

    for char in s:
        freq[char] = freq.get(char,0) + 1
    
    for char in t:
        if char not in freq:
            return False

        freq[char] -= 1
    
    for value in freq.values():
        if value != 0:
            return False
        
    
    return True

# Example Usage

s: str = "anagram"
t: str = "nagaram"

print(validAnagram(s,t))