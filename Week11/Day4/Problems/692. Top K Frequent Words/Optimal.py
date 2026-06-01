import heapq
from typing import List

def topKFrequent(words: List[str], k: int) -> List[str]:

    heap = []
    freq = {}

    for word in words:
        freq[word] = freq.get(word,0) + 1
    
    for word,count in freq.items():
        heapq.heappush(heap,(-count,word))

    ans = []

    for _ in range(k):
        ans.append(heapq.heappop(heap)[1])

    return ans


words: List[str] = ["i","love","leetcode","i","love","coding"]
k: int = 2

print(topKFrequent(words, k))