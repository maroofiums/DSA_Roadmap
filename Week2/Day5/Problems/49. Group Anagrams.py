from typing import List
from collections import defaultdict

def groupAnagrams(strs:List[str]) -> List[List[str]]:
    group = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c)-ord('a')] += 1
        
        key = tuple(count)

        group[key].append(s)

    return list(group.values())

# Example Usage

strs: List[str] = ["eat","tea","tan","ate","nat","bat"] 

print(groupAnagrams(strs))

