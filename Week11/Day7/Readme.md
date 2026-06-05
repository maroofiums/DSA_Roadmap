# DAY 7 - TEST DAY

## Week 11 Assessment

Today is not a learning day.

Today is a testing day.

You must solve problems independently and evaluate your understanding of:

* Heaps
* Top-K Pattern
* Frequency Counting
* Greedy Thinking
* Heap + Queue Combinations

---

# TEST RULES

## During the Test

❌ No YouTube

❌ No Notes

❌ No ChatGPT

❌ No Solution Watching

❌ No Copy/Paste

---

## Allowed

✅ Python Documentation

✅ Whiteboard/Paper

✅ Thinking

✅ Debugging Your Own Code

---

## Time Limits

### Problem 1

20 minutes

---

### Problem 2

20 minutes

---

### Problem 3

30–45 minutes

---

## Important

For every problem:

1. Explain your approach aloud
2. Write complexity analysis yourself
3. Identify pattern before coding
4. Write brute force first (mentally)
5. Then optimize

---

# PROBLEM 1

## 215. Kth Largest Element in an Array

### Difficulty

Medium

---

## Concepts Tested

* Min Heap
* Heap Size K
* Top-K Pattern
* Complexity Analysis

---

## Requirements

Use:

```text
Min Heap of Size K
```

---

## Target Complexity

Time:

```text
O(n log k)
```

Space:

```text
O(k)
```

---

## Questions You Must Answer

### Q1

Why is heap better than sorting?

---

### Q2

Why do we pop when heap size exceeds k?

---

### Q3

Why is heap[0] the answer?

---

### Q4

What Top-K pattern is being used?

---

## Self Evaluation

| Check               | Done |
| ------------------- | ---- |
| Solved without help | ☐    |
| Correct complexity  | ☐    |
| Used heap           | ☐    |
| Explained approach  | ☐    |

---

# PROBLEM 2

## 347. Top K Frequent Elements

### Difficulty

Medium

---

## Concepts Tested

* HashMap
* Frequency Counting
* Heap + HashMap
* Tuple Ordering

---

## Requirements

Use:

```text
Frequency Map + Heap
```

---

## Target Complexity

Time:

```text
O(n log k)
```

Space:

```text
O(n)
```

---

## Questions You Must Answer

### Q1

Why do we count frequencies first?

---

### Q2

Why store:

```python
(count, num)
```

inside heap?

---

### Q3

Why maintain heap size k?

---

### Q4

What role does the HashMap play?

---

## Self Evaluation

| Check               | Done |
| ------------------- | ---- |
| Solved without help | ☐    |
| Used HashMap        | ☐    |
| Used Heap           | ☐    |
| Complexity correct  | ☐    |

---

# PROBLEM 3

## 621. Task Scheduler

### Difficulty

Medium

---

## Concepts Tested

* Max Heap
* Greedy Thinking
* Queue + Heap
* Simulation

---

## Requirements

Use:

```text
Max Heap + Queue
```

---

## Target Complexity

Time:

```text
O(n log n)
```

Space:

```text
O(n)
```

---

## Questions You Must Answer

### Q1

Why should the most frequent task run first?

---

### Q2

Why is a queue needed?

---

### Q3

How does cooling time work?

---

### Q4

When do idle slots occur?

---

### Q5

Why is this considered a greedy solution?

---

## Self Evaluation

| Check                  | Done |
| ---------------------- | ---- |
| Solved without help    | ☐    |
| Used Heap              | ☐    |
| Used Queue             | ☐    |
| Complexity correct     | ☐    |
| Explained greedy logic | ☐    |

---

# BONUS CHALLENGE

If you finish early:

## Heap Problems

### 295. Find Median from Data Stream

Concepts:

* Two Heaps
* Running Median

---

### 23. Merge K Sorted Lists

Concepts:

* Heap
* Linked Lists

---

## Greedy Problems

### 55. Jump Game

Concepts:

* Reachability
* Greedy Coverage

---

### 134. Gas Station

Concepts:

* Greedy Reset Strategy

---

# WEEK 11 FINAL CHECKLIST

Can you confidently explain:

### Heap Fundamentals

* Heap Property
* Min Heap
* Max Heap
* Heapify
* Sift Up
* Sift Down

---

### Top-K Pattern

* Kth Largest
* Top K Frequent
* Heap Size K

---

### Frequency Counting

* HashMap
* Counter
* Tuple Ordering

---

### Greedy Concepts

* Local Optimum
* Global Optimum
* Why Greedy Works
* Exchange Argument

---

### Scheduling

* Cooldown
* Queue
* Max Heap
* Simulation

---

# SCORING

## 3 / 3 Problems Solved

Excellent

Ready for:

```text
Week 12
Advanced Heap + Greedy Problems
```

---

## 2 / 3 Problems Solved

Good

Review weak area tomorrow.

---

## 1 / 3 Problems Solved

Needs revision.

Repeat Week 11 practice.

---

# Final Goal

After Week 11 you should immediately recognize:

### Top-K Problems

→ Heap

### Frequency Ranking Problems

→ HashMap + Heap

### Scheduling Problems

→ Heap + Queue + Greedy

### "Most Important First" Problems

→ Max Heap

If these patterns feel automatic, Week 11 is complete.
