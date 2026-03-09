from typing import List
from collections import defaultdict

def groupAnagrams(s: List[str]) -> List[List[str]]:
    hash_map = defaultdict(list)
    for w in s:
        key = ''.join(sorted(w))
        hash_map[key].append(w)
    return list(hash_map.values())

# Example usage:
s = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(s))  # Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
