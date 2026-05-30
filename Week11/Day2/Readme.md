# DAY 2 - Heap Operations Deep Dive

## Learning Objectives

By the end of today, you should be able to:

* Understand how insertion works internally
* Understand how deletion works internally
* Perform Sift Up and Sift Down
* Build a heap from an array
* Explain why Heapify is O(n)
* Implement a Min Heap manually

---

# Review From Day 1

A Heap is:

* A Complete Binary Tree
* Stored in an array
* Follows Heap Property

Min Heap:

```text
Parent ≤ Children
```

Max Heap:

```text
Parent ≥ Children
```

---

# 1. Heap Insertion (Push)

Suppose we have:

```text
      10
     /  \
    20   30
```

Array:

```python
[10, 20, 30]
```

Insert:

```python
5
```

---

## Step 1

Add at the end.

```text
      10
     /  \
    20   30
   /
  5
```

Array:

```python
[10, 20, 30, 5]
```

Heap property is broken.

---

## Step 2

Compare with parent.

```text
5 < 20
```

Swap.

```text
      10
     /  \
     5   30
   /
 20
```

Array:

```python
[10, 5, 30, 20]
```

---

## Step 3

Compare again.

```text
5 < 10
```

Swap.

```text
       5
      / \
    10  30
   /
 20
```

Array:

```python
[5, 10, 30, 20]
```

Heap property restored.

---

# 2. Sift Up

The process of moving a node upward until heap property is satisfied.

Also called:

```text
Bubble Up
Percolate Up
Heapify Up
```

---

## Algorithm

```python
while current < parent:
    swap(current, parent)
```

---

## Complexity

Height of heap:

```text
log n
```

Therefore:

```text
O(log n)
```

---

# Manual Sift Up

```python
def sift_up(heap, i):
    while i > 0:
        parent = (i - 1) // 2

        if heap[parent] <= heap[i]:
            break

        heap[parent], heap[i] = heap[i], heap[parent]

        i = parent
```

---

# 3. Heap Deletion (Pop)

Min Heap:

```text
Remove Root
```

Example:

```text
       5
      / \
    10  30
   /
 20
```

Array:

```python
[5, 10, 30, 20]
```

Remove:

```python
5
```

---

## Step 1

Move last element to root.

```text
       20
      / \
    10  30
```

Array:

```python
[20, 10, 30]
```

Heap property broken.

---

## Step 2

Compare with children.

Smallest child:

```python
10
```

Swap.

```text
       10
      / \
    20  30
```

Array:

```python
[10, 20, 30]
```

Heap property restored.

---

# 4. Sift Down

Process of moving root downward until heap property becomes valid.

Also called:

```text
Heapify Down
Bubble Down
Percolate Down
```

---

## Algorithm

```python
while child is smaller:
    swap(parent, child)
```

---

## Complexity

Heap height:

```text
log n
```

Therefore:

```text
O(log n)
```

---

# Manual Sift Down

```python
def sift_down(heap, i):
    n = len(heap)

    while True:

        left = 2 * i + 1
        right = 2 * i + 2

        smallest = i

        if left < n and heap[left] < heap[smallest]:
            smallest = left

        if right < n and heap[right] < heap[smallest]:
            smallest = right

        if smallest == i:
            break

        heap[i], heap[smallest] = heap[smallest], heap[i]

        i = smallest
```

---

# 5. Heapify

Convert an arbitrary array into a valid heap.

Example:

```python
[40, 10, 30, 5, 20]
```

Not a heap.

Heapify transforms it into:

```python
[5, 10, 30, 40, 20]
```

---

# Python Heapify

```python
import heapq

nums = [40, 10, 30, 5, 20]

heapq.heapify(nums)

print(nums)
```

Output:

```python
[5, 10, 30, 40, 20]
```

---

# 6. How Heapify Works

Instead of inserting elements one by one:

```python
for x in arr:
    heappush(heap, x)
```

which costs:

```text
O(n log n)
```

Heapify starts from the last non-leaf node and performs Sift Down.

---

Example:

```text
        40
       /  \
     10    30
    / \
   5  20
```

Start from:

```text
Last non-leaf node
```

Index:

```python
(n // 2) - 1
```

Then perform Sift Down repeatedly.

---

# 7. Why Heapify Is O(n)

This is a famous interview question.

Many beginners think:

```text
n nodes
×
log n work

= O(n log n)
```

Wrong.

---

Reason:

Most nodes are near the bottom.

Bottom nodes require:

```text
0 swaps
```

Nodes above them require:

```text
1 swap
```

Higher nodes require:

```text
2 swaps
```

Only a few nodes are near the root and require many swaps.

---

Mathematical Result

Total work becomes:

```text
n × (1 + 1/2 + 1/4 + 1/8 + ...)
```

Geometric series:

```text
≤ 2n
```

Therefore:

```text
O(n)
```

This is one of the most commonly asked heap interview questions.

---

# 8. Complexity Summary

| Operation | Complexity |
| --------- | ---------- |
| Peek      | O(1)       |
| Insert    | O(log n)   |
| Delete    | O(log n)   |
| Sift Up   | O(log n)   |
| Sift Down | O(log n)   |
| Heapify   | O(n)       |

---

# 9. Manual Min Heap Implementation

```python
class MinHeap:

    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def push(self, val):

        self.heap.append(val)

        self._sift_up(len(self.heap) - 1)

    def pop(self):

        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]

        self.heap[0] = self.heap.pop()

        self._sift_down(0)

        return root

    def peek(self):
        return self.heap[0]

    def _sift_up(self, i):

        while i > 0:

            p = self.parent(i)

            if self.heap[p] <= self.heap[i]:
                break

            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]

            i = p

    def _sift_down(self, i):

        n = len(self.heap)

        while True:

            smallest = i

            left = self.left(i)
            right = self.right(i)

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]

            i = smallest
```

---

# Practice Problems

## Easy

1. Last Stone Weight
2. Kth Largest Element in Stream

---

## Medium

### LeetCode 973

K Closest Points to Origin

Learn:

* Max Heap
* Distance Calculation
* Top K Pattern

---

### LeetCode 451

Sort Characters By Frequency

Learn:

* HashMap
* Heap
* Frequency Counting

---

# Day 2 Checklist

Before moving to Day 3 make sure you can answer:

* Why is insertion O(log n)?
* Why is deletion O(log n)?
* What is Sift Up?
* What is Sift Down?
* Why is Heapify O(n)?
* How does heapq.heapify() work internally?
* Can you implement MinHeap without heapq?

---
