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

# DAY 7 - Revision + Mixed Problems

## Revision Topics

Review:

* Min heap
* Max heap
* Heapify
* Top K pattern
* Greedy intuition
* Frequency maps

---

# Mixed Practice

## Heap Problems

* Find Median from Data Stream
* Merge K Sorted Lists
* K Closest Elements

## Greedy Problems

* Jump Game
* Gas Station
* Partition Labels

---

# END OF WEEK CHECKLIST

You should now know:

* Heap push/pop confidently
* Min vs max heap
* Top K patterns
* Frequency-based heap problems
* Greedy basics
* Scheduling logic

---

# IMPORTANT INTERVIEW PATTERNS THIS WEEK

## Heap Patterns

1. Top K elements
2. Frequency ranking
3. Scheduling
4. Streaming data
5. Merge multiple sorted structures

---

## Greedy Patterns

1. Interval scheduling
2. Local best choice
3. Sorting + greedy
4. Priority-based decisions

---

# RECOMMENDED DAILY STRUCTURE

## 2–4 Hour Plan

### Hour 1

Theory + notes

### Hour 2

Watch/understand examples

### Hour 3

Solve 2–3 problems

### Hour 4

Debug + complexity analysis + revision

---

# VERY IMPORTANT

For heaps:

* Always ask:

  * “Do I need smallest?”
  * “Do I need largest?”
  * “Do I only need top k?”

If yes → heap is probably useful.

For greedy:

* Ask:

  * “Can I make the best local choice safely?”

That mindset becomes critical later in:

* Graph algorithms
* AI optimization
* System scheduling
* Reinforcement learning foundations
