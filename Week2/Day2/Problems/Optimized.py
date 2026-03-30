from collections import defaultdict

def groupAnagrams(strs):

    anagrams = defaultdict(list)
    for ch in strs:
        count = [0] * 26
        for c in ch:
            count[ord(c) - ord('a')] += 1
        key = tuple(count)
        anagrams[key].append(ch)
    return list(anagrams.values())


# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))