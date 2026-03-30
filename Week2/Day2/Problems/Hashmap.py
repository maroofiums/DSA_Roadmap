from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list:
    anagrams = defaultdict(list)

    for ch in strs:
        key = ''.join(sorted(ch))
        anagrams[key].append(ch)
    return list(anagrams.values())

# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
