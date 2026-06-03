from typing import List

def findContentChildren(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()

    used = [False] * len(s)
    
    content = 0

    for child in g:
        for i, cookie in enumerate(s):
            if not used[i] and cookie >= child:
                used[i] = True
                content += 1
                break

    return content

g: List[int] = [1,2,3]
s: List[int] = [2,2]
print(findContentChildren(g, s))



def findContentChildren(g, s):
    g.sort()
    s.sort()

    used = [False] * len(s)
    
    content = 0

    for child in g:
        for i, cookie in enumerate(s):
            if not used[i] and cookie >= child:
                used[i] = True
                content += 1
                break

    return content

findContentChildren([1,2,3], [1,3])