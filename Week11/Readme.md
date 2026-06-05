# WEEK 11 - Heaps + Greedy

This week is extremely important because heaps appear everywhere:

* Scheduling systems
* Recommendation systems
* Streaming/top-k problems
* AI ranking pipelines
* Operating systems
* Distributed systems

You’ll also start developing “greedy intuition”, which is a major interview skill.

---

# WEEK 11 GOALS

By the end of this week you should be able to:

* Use min-heaps and max-heaps confidently
* Solve Top K problems efficiently
* Understand when greedy works
* Analyze heap complexity quickly
* Combine hashmap + heap patterns
* Solve medium LeetCode heap questions independently

---

# DAY 1 - Introduction to Heaps

## Concepts

Learn:

* What is a heap?
* Complete binary tree
* Min heap vs max heap
* Heap properties
* Array representation
* Parent/child formulas

## Important Formulas

For index `i`:

Parent:

Left child:
2i+1

Right child:
2i+2

---

## Python Learning

Learn:

```python
import heapq
```

Operations:

```python
heapq.heappush(heap, val)
heapq.heappop(heap)
heapq.heapify(arr)
```

Max heap trick:

```python
heapq.heappush(heap, -x)
```

---

## Practice

### Easy

1. Heap basics manually
2. Implement min heap mentally

### LeetCode

* Kth Largest Element in a Stream
* Last Stone Weight

---

## Goal

Understand:

* Why heaps are useful
* Why insertion/removal is efficient

---

# DAY 2 - Heap Operations Deep Dive

## Concepts

Learn:

* Push
* Pop
* Heapify
* Sift up
* Sift down

## Complexity

Insertion:
O(log n)

Deletion:
O(log n)

Peek:
O(1)

Heapify:
O(n)

---

## Learn WHY heapify is O(n)

This is very important interview theory.

---

## Practice Problems

* K Closest Points to Origin
* Sort Characters By Frequency

---

## Extra

Implement heap manually once.

---

# DAY 3 - Kth Largest Element

## Main Problem

### Kth Largest Element in an Array

---

## Concepts

Learn:

* Why heap is better than sorting
* Min heap of size k
* Keep only largest k elements

---

## Key Idea

If heap size exceeds `k`:

```python
heapq.heappop(heap)
```

Final heap top:

```python
heap[0]
```

---

## Complexity

Sorting:
O(nlog n)

Heap approach:
O(nlog k)

---

## Tasks

1. Solve brute force
2. Solve heap version
3. Compare complexities
4. Explain why heap wins

---

## Bonus

Try QuickSelect later (advanced).

---

# DAY 4 - Top K Frequent Elements

## Main Problem

### Top K Frequent Elements

---

## Concepts

This problem combines:

* HashMap
* Frequency counting
* Heap

---

## Learn

Step-by-step:

1. Count frequencies
2. Push into heap
3. Keep top k

---

## Pattern

```python
freq[num] += 1
```

Push:

```python
heapq.heappush(heap, (count, num))
```

---

## Important Skill

Tuple ordering in Python heaps.

---

## Practice

Also solve:

* Top K Frequent Words
* Frequency Sort

---

# DAY 5 - Greedy Algorithms Introduction

## Concepts

Learn:

* What is greedy?
* Local optimum
* Global optimum
* When greedy works
* Greedy vs DP

---

## Learn Through Problems

* Assign Cookies
* Lemonade Change
* Best Time to Buy and Sell Stock II

---

## Key Thinking

Greedy asks:

> “What is the best choice RIGHT NOW?”

---

## Important

Not every problem can use greedy.

Learn:

* Exchange argument intuition
* Why proofs matter

---

# DAY 6 - Task Scheduler

## Main Problem

### Task Scheduler

---

## Concepts

This is one of the most important heap + greedy interview problems.

Learn:

* Frequency counting
* Max heap
* Cooling time
* Simulation

---

## Skills Built

* Heap scheduling
* Greedy ordering
* Queue + heap combination

---

## Visual Understanding

Think:

* Most frequent tasks should run first
* Avoid idle time

---

## Complexity Goal

Target:
O(nlog n)

---

# DAY 7 – TEST DAY (No Learning, Only Solving)

## Rules

1. No videos
2. No notes
3. No solution watching for 30–45 minutes
4. Write complexity analysis yourself
5. Explain your approach aloud

---

# Problem 1 — Kth Largest Element in an Array

### Concepts Tested

* Min Heap
* Heap Size K
* Heap Complexity
* Top K Pattern

### Expected Solution

Heap of size `k`

### Target Complexity

* Time: `O(n log k)`
* Space: `O(k)`

### Questions You Must Answer

1. Why is heap better than sorting?
2. Why do we pop when heap size exceeds `k`?
3. Why is `heap[0]` the answer?

---

# Problem 2 — Top K Frequent Elements

### Concepts Tested

* HashMap
* Frequency Counting
* Heap + HashMap Combination
* Tuple Ordering

### Target Complexity

* Time: `O(n log k)`
* Space: `O(n)`

### Questions You Must Answer

1. Why do we count frequencies first?
2. Why store `(frequency, value)` in heap?
3. Why is heap size maintained at `k`?

---

# Problem 3 — Task Scheduler

### Concepts Tested

* Max Heap
* Greedy Thinking
* Queue + Heap
* Simulation

### Target Complexity

* Time: `O(n log n)`
* Space: `O(n)`

### Questions You Must Answer

1. Why should the most frequent task run first?
2. Why is a queue needed?
3. How does cooling time work?
4. When do idle slots occur?

---

# Test Scoring

### Kth Largest Element

* Correct Solution → 10 Marks
* Complexity Explanation → 5 Marks

**Total: 15 Marks**

---

### Top K Frequent Elements

* Correct Solution → 10 Marks
* Complexity Explanation → 5 Marks

**Total: 15 Marks**

---

### Task Scheduler

* Correct Solution → 15 Marks
* Complexity Explanation → 5 Marks

**Total: 20 Marks**

---

# Final Score

| Score | Level                                    |
| ----- | ---------------------------------------- |
| 0–20  | Need Revision                            |
| 21–35 | Basic Understanding                      |
| 36–45 | Interview Ready for Medium Heap Problems |
| 46–50 | Strong Heap + Greedy Foundation          |

---

# Week 11 Completion Checklist

* <input type=checkbox checked > Understand Min Heap
* <input type=checkbox checked> Understand Max Heap
* <input type=checkbox checked> Know Heap Operations
* <input type=checkbox checked> Know Heapify (`O(n)`)
* <input type=checkbox checked> Solve Kth Largest Element
* <input type=checkbox checked> Solve Top K Frequent Elements
* <input type=checkbox checked> Solve Task Scheduler
* <input type=checkbox checked> Explain Heap Complexities
* <input type=checkbox checked> Understand Greedy Intuition
* <input type=checkbox checked> Complete Test Day
