from typing import List
from collections import Counter

def leastInterval(tasks: List[str], n: int) -> int:
    freq = Counter(tasks)

    max_freq = max(freq.values())
    max_count = sum(1 for f in freq.values() if f == max_freq)

    part = (max_freq - 1) * (n + 1) + max_count

    return max(len(tasks), part)

# Example Usage: 
tasks: List[str] = ["A","A","A","B","B","B"]
n: int = 2

print(leastInterval(tasks,n))