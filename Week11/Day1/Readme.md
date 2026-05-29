# DAY 1 - Introduction to Heaps

## What is a Heap?

A heap is a special tree-based data structure.

It follows:

* Complete Binary Tree structure
* Heap Property

---

# Complete Binary Tree

A complete binary tree means:

* Every level is completely filled
* Except possibly the last level
* Last level fills from left to right

Example:

```text
        1
      /   \
     4     7
    / \   /
   10 15 9
```

---

# Heap Property

## Min Heap

Parent is always smaller than children.

```text
Parent <= Children
```

Smallest element stays at root.

Example:

```text
        1
      /   \
     4     7
    / \
   10 15
```

---

## Max Heap

Parent is always larger than children.

```text
Parent >= Children
```

Largest element stays at root.

Example:

```text
        15
      /    \
     7      10
    / \
   1   4
```

---

# Array Representation

Heap is usually stored inside arrays.

Example:

```text
Index:  0  1  2  3  4
Value: [1, 4, 7,10,15]
```

Tree:

```text
        1
      /   \
     4     7
    / \
   10 15
```

---

# Parent / Child Formulas

For index i:

Parent:

```
(i - 1) // 2
```

Left child:

```
2 * i + 1
```

Right child:

```
2 * i + 2
```

---

# Python heapq

Python provides built-in heap support.

Import:

```python
import heapq
```

Important:

* Python heapq is MIN HEAP by default.

---

# Basic Min Heap Example

```python
import heapq

heap = []

heapq.heappush(heap,10)
heapq.heappush(heap,4)
heapq.heappush(heap,15)
heapq.heappush(heap,1)
heapq.heappush(heap,7)

print(heap)
```

Output:

```python
[1, 4, 15, 10, 7]
```

---

# Peek Minimum

```python
print(heap[0])
```

Output:

```python
1
```

---

# Pop Minimum

```python
print(heapq.heappop(heap))
```

Output:

```python
1
```

---

# Heapify Existing Array

```python
arr = [9,3,6,1,8,2]

heapq.heapify(arr)

print(arr)
```

Output:

```python
[1,3,2,9,8,6]
```

---

# Heap Sort Using Min Heap

```python
sorted_arr = []

while arr:
    sorted_arr.append(heapq.heappop(arr))

print(sorted_arr)
```

Output:

```python
[1,2,3,6,8,9]
```

---

# Max Heap in Python

Python does not directly support max heaps.

We simulate max heap using negative numbers.

---

# Max Heap Example

```python
import heapq

heap = []

nums = [10,4,15,1,7]

for x in nums:
    heapq.heappush(heap,-x)

print(heap)
```

---

# Peek Maximum

```python
print(-heap[0])
```

---

# Pop Maximum

```python
print(-heapq.heappop(heap))
```

---

# Manual Heap Implementation

Implemented:

* MinHeap
* MaxHeap

Important operations:

* push()
* pop()
* peek()
* heap_sort()

---

# Core Heap Operations

## Bubble Up (Sift Up)

Used during insertion.

Move element upward until heap property is restored.

Complexity:

O(log n)

---

## Bubble Down (Sift Down)

Used during deletion.

Move element downward until heap property is restored.

Complexity:

O(log n)

---

# Time Complexities

Insertion:
O(log n)

Deletion:
O(log n)

Peek:
O(1)

Heapify:
O(n)

Heap Sort:
O(n log n)

---

# Important Observations

## Heap is NOT fully sorted

Example:

```python
[1,4,15,10,7]
```

Only guarantee:

* Parent relation is maintained

Not full ordering.

---

# Difference Between Heap and BST

Heap:

* Fast min/max access
* Not fully sorted

BST:

* Ordered structure
* Better searching

---

# Real World Uses

Heaps are used in:

* Priority queues
* Operating systems scheduling
* Task scheduling
* Dijkstra algorithm
* AI search systems
* Streaming top-k systems

---

# Problems Practiced

Built-in:

* minHeap.py
* maxHeap.py

Scratch:

* minHeap.py
* maxHeap.py

---

# Key Learnings

Today I learned:

* Heap basics
* Min heap vs max heap
* Array representation
* heapq usage
* Max heap trick
* Heap sort
* Manual heap implementation
* Bubble up and bubble down

---
