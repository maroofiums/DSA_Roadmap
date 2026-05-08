# Week 8: Advanced Trees

## Overview

This week focuses on advanced binary tree patterns commonly asked in interviews.

### Topics Covered

* BFS (Level Order Traversal)
* Tree Height / Depth
* Tree Properties
* Lowest Common Ancestor (LCA)
* Diameter of Binary Tree

### Goal

Build strong pattern recognition for tree problems and document solutions for GitHub.

---

# Day 1 — BFS (Level Order Traversal)

## Concepts Learned

* Queue data structure (`collections.deque`)
* Level-by-level traversal
* Difference between BFS vs DFS

## Problems Solved

1. Binary Tree Level Order Traversal
2. Binary Tree Right Side View

## Pattern

```python
queue = deque([root])

while queue:
    level_size = len(queue)
    
    for _ in range(level_size):
        node = queue.popleft()
```

## Time Complexity

* O(n)

## Mistakes I Made

* Forgot level_size logic
* Mixed stack logic with queue

---

# Day 2 — Tree Height / Depth

## Concepts Learned

* Recursive depth calculation
* Base case handling

## Formula

`height = 1 + max(left_height, right_height)`

## Problems Solved

1. Maximum Depth of Binary Tree
2. Minimum Depth of Binary Tree

## Time Complexity

* O(n)

## Mistakes I Made

* Incorrect null handling

---

# Day 3 — Tree Properties

## Concepts Learned

* Balanced trees
* Same tree
* Symmetric tree
* Structural validation

## Problems Solved

1. Balanced Binary Tree
2. Same Tree
3. Symmetric Tree

## Time Complexity

* O(n)

## Mistakes I Made

* Returning wrong boolean values

---

# Day 4 — Lowest Common Ancestor

## Concepts Learned

* Recursive ancestor search
* Left/right subtree reasoning

## Problems Solved

1. LCA of Binary Tree
2. LCA of BST

## Time Complexity

* O(n)

## Mistakes I Made

* Wrong base case
* Confused subtree returns

---

# Day 5 — Diameter of Binary Tree

## Concepts Learned

* Longest path logic
* Global variable tracking

## Formula

`diameter = left_height + right_height`

## Problems Solved

1. Diameter of Binary Tree
2. Binary Tree Maximum Path Sum (optional)

## Time Complexity

* O(n)

## Mistakes I Made

* Forgot global update

---

# Day 6 — Mixed Practice

## Problems Solved

* Level Order Traversal
* LCA
* Diameter
* Path Sum

## Goal

Solve without pattern notes.

---

# Day 7 — Test Day

## Mock Test Rules

Solve problems under timed conditions:

* Easy → 15 mins
* Medium → 25 mins

No notes
No solution videos
No ChatGPT help

---

## Test Problems

1. Binary Tree Level Order Traversal
2. Maximum Depth of Binary Tree
3. Balanced Binary Tree
4. Lowest Common Ancestor
5. Diameter of Binary Tree

---

## Evaluation Criteria

### Accuracy

How many problems solved correctly?

### Speed

Did you finish within time?

### Debugging

How quickly did you fix errors?

### Pattern Recognition

Did you know which approach to use instantly?

---

## Score Yourself

```text
Accuracy: __/10
Speed: __/10
Debugging: __/10
Pattern Recognition: __/10

Total Score: __/40
```

---

## If Score is:

* 35+ → Move to Graphs
* 25–34 → Revise weak areas
* Below 25 → Repeat tree practice

---

# Weekly Reflection

## Problems Solved

Write total solved here.

## Biggest Weakness

Write your weakness here.

## Improvement Next Week

Prepare for Graphs/Heaps.
