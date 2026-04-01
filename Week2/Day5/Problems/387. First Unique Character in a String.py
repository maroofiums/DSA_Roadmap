from collections import defaultdict

def firstUniqChar(s:str) -> int:
    freq = defaultdict()

    for c in s:
        freq[c] = freq.get(c,0) + 1

    for i,c in enumerate(freq):
        if freq[c] == 1:
            return i
        
    
    return -1

# Example usage

s:str = "leetcode"
print(firstUniqChar(s))
        