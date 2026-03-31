def firstUniqChar(s:str) -> int:
    for ch in s:
        if s.count(ch) == 1:
            return s.index(ch)
        return -1

# Example Usage
s = "leetcode"
print(firstUniqChar(s))