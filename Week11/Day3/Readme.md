# DAY 3 - Kth Largest Element (Heap + Sorting)

## Folder Structure

```
Day3
├── Problems
│   ├── 215. Kth Largest Element in an Array
│   │   ├── BruteForce.py
│   │   └── Optimal.py
│   └── 703. Kth Largest Element in a Stream
│       ├── BruteForce.py
│       └── Optimal.py
└── Readme.md
```

---

# 1. Overview

This day focuses on one of the most important interview patterns:

## 👉 Top K Pattern

You learn how to efficiently find:

* Kth largest element
* Streaming Kth largest element
* Optimized heap usage

---

# 2. Problems Covered

## Problem 1: Kth Largest Element in an Array

### LeetCode 215

Goal:
Find the Kth largest element in an unsorted array.

---

### Brute Force Approach

#### Idea:

* Sort the entire array
* Return `nums[-k]`

#### Code:

```python
from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    nums.sort()
    return nums[-k]


nums = [3,2,1,5,6,4]
k = 2

print(findKthLargest(nums, k))
```

---

### Complexity

* Time: O(n log n)
* Space: O(1)

---

### Problem:

Sorting is expensive for large datasets.

---

## Optimal Approach (Min Heap)

### Idea:

* Keep only K largest elements
* Use Min Heap of size K
* Root = Kth largest element

---

### Code:

```python
from typing import List
import heapq

def findKthLargest(nums: List[int], k: int) -> int:
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


nums = [3,2,1,5,6,4]
k = 2

print(findKthLargest(nums, k))
```

---

### Complexity

* Time: O(n log k)
* Space: O(k)

---

### Why this works:

We maintain only the **K largest elements** in the heap.

The smallest among them is the answer.

---

# 3. Problem 2: Kth Largest Element in a Stream

### LeetCode 703

Goal:
Design a system that continuously returns the Kth largest element after each insertion.

---

# Brute Force Approach

### Idea:

* Add value to list
* Sort every time
* Return `nums[-k]`

---

### Code:

```python
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]
```

---

### Complexity

* add(): O(n log n)
* inefficient for streaming data

---

# Optimal Approach (Heap)

### Idea:

* Use Min Heap of size K
* Maintain K largest elements only
* Top of heap = answer

---

### Code:

```python
from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums

        heapq.heapify(self.minHeap)

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]
```

---

### Complexity

* add(): O(log k)
* init(): O(n)

---

# 4. Key Insight (VERY IMPORTANT)

## Why Min Heap?

We want:

* Keep largest K elements
* Remove smaller values automatically

So:

```
Heap stores only top K candidates
```

Root is:

```
Kth largest element
```

---

# 5. Comparison

| Approach    | Time Complexity  | Use Case          |
| ----------- | ---------------- | ----------------- |
| Sorting     | O(n log n)       | Small input       |
| Heap        | O(n log k)       | Large input       |
| Stream Heap | O(log k) per add | Real-time systems |

---

# 6. Pattern Recognition

This is a **Top-K Pattern** problem.

Used in:

* Recommendation systems
* Leaderboards
* Search ranking
* Stream processing

---

# 7. What You Learned Today

You should now understand:

* Sorting vs Heap trade-off
* Min Heap of size K
* Streaming design using heap
* Why heap improves performance
* Core Top-K pattern

---

# 8. Interview Summary

If asked:

### “How do you find Kth largest element?”

Answer:

> Use a Min Heap of size K.
> Push elements one by one.
> If heap size exceeds K, remove smallest.
> The root is the answer.

---
