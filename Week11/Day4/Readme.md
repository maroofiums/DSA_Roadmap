# DAY 4 - Top K Frequent Elements

## Folder Structure

```text
Day4
├── Problems
│   ├── 347. Top K Frequent Elements
│   │   ├── BruteForce.py
│   │   └── Optimal.py
│   └── 692. Top K Frequent Words
│       ├── BruteForce.py
│       └── Optimal.py
└── Readme.md
```

---

# 1. Main Problem

## Top K Frequent Elements

### LeetCode 347

### Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

---

### Example

```text
Input:
nums = [1,1,1,2,2,3]
k = 2

Output:
[1, 2]
```

---

# 2. Key Idea

This problem combines:

* HashMap (frequency counting)
* Heap (Top K selection)
* Sorting alternative

---

# 3. Step-by-Step Approach

## Step 1: Count Frequency

We first count how many times each element appears.

```python
freq[num] += 1
```

Example:

```text
nums = [1,1,1,2,2,3]

freq = {
    1: 3,
    2: 2,
    3: 1
}
```

---

## Step 2: Push into Heap

We store elements in heap as:

```python
(count, num)
```

Why?

Because heap sorts by first value (frequency).

```python
heapq.heappush(heap, (count, num))
```

---

## Step 3: Keep Only Top K

We maintain a Min Heap of size K.

If size exceeds K:

```python
heapq.heappop(heap)
```

---

# 4. Brute Force Approach

## Idea

* Count frequency
* Sort all elements by frequency
* Take top K

---

## Code

```python
from typing import List
from collections import Counter

def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq = Counter(nums)

    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return [item[0] for item in sorted_items[:k]]
```

---

## Complexity

* Time: O(n log n)
* Space: O(n)

---

# 5. Optimal Approach (Heap)

## Idea

* Use Min Heap of size K
* Keep only most frequent elements

---

## Code

```python
from typing import List
import heapq
from collections import Counter

def topKFrequent(nums: List[int], k: int) -> List[int]:

    freq = Counter(nums)
    heap = []

    for num, count in freq.items():

        heapq.heappush(heap, (count, num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for count, num in heap]
```

---

## Complexity

* Time: O(n log k)
* Space: O(n + k)

---

# 6. Why Tuple Works in Heap

Python heap compares tuples like this:

```text
(first element → priority)
```

So:

```python
(count, num)
```

Means:

* Higher frequency = higher priority

---

### Example Heap Behavior

```text
(1, 3)
(2, 2)
(3, 1)
```

Heap keeps smallest count at top.

---

# 7. Alternative Approach (Bucket Sort)

## Idea

* Create buckets where index = frequency
* Place elements in those buckets
* Traverse from high frequency to low

---

## Complexity

* Time: O(n)
* Space: O(n)

---

# 8. Pattern Recognition

This is a **Frequency + Heap Pattern**

Used in:

* Recommendation systems
* Search ranking
* Trending topics
* NLP word frequency
* Log analysis

---

# 9. Related Problems

You should practice:

## 1. Top K Frequent Words

* Same logic
* But with lexicographic tie-break

---

## 2. Frequency Sort

* Sort numbers by frequency
* Reverse ordering

---

# 10. Interview Insight

If asked:

### “How do you solve Top K Frequent Elements?”

Answer:

> First, count frequencies using a hashmap.
> Then use a Min Heap of size K to store top frequencies.
> Remove smallest frequency when heap exceeds K.
> Finally, extract elements from heap.

---

# 11. Comparison

| Approach    | Time Complexity | Use Case         |
| ----------- | --------------- | ---------------- |
| Sorting     | O(n log n)      | Simple cases     |
| Heap        | O(n log k)      | Efficient Top-K  |
| Bucket Sort | O(n)            | Optimal solution |

---

# 12. Key Takeaways

You should now understand:

* Frequency counting with HashMap
* Heap of tuples
* Top-K frequency pattern
* Why heap improves performance
* When to use bucket sort

---

