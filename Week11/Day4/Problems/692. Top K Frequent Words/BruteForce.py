from typing import List

def topKFrequent(words: List[str], k: int) -> List[str]:

    freq = {}

    for word in words:
        freq[word] = freq.get(word,0) + 1


    return sorted(
        freq.keys(),
        key = lambda x: (-freq[x],x)
    )[:k]

words: List[str] = ["i","love","leetcode","i","love","coding"]
k: int = 2

print(topKFrequent(words, k))