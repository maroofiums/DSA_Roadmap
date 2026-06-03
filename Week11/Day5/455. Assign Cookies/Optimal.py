from typing import List

def findContentChildren(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    i = j = 0
    while i < len(g):
        while j < len(s) and s[j] < g[i]:
            j += 1

        if j == len(s):
            break

        i += 1
        j += 1
    
    return i

g: List[int] = [1,2,3]
s: List[int] = [2,2]

print(findContentChildren(g, s))

