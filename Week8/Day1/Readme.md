# Day 1 - BFS (Level Order Traversal)

## Objective

Learn how Breadth First Search (BFS) works in binary trees and solve level-based traversal problems.

---

## What I Learned

### BFS in Trees

BFS explores nodes level by level.

Unlike DFS:

* DFS uses recursion/stack
* BFS uses queue

---

## Visual Representation

```text
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
```

Level Order Output:

```python
[[1], [2, 3], [4, 5, 6, 7]]
```

---

## Core Concept

Use `collections.deque` for efficient queue operations.

### BFS Pattern

```python
from collections import deque

queue = deque([root])

while queue:
    level_size = len(queue)
    level = []

    for _ in range(level_size):
        node = queue.popleft()
        level.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)
```

---

# Problems Solved

## 1. Binary Tree Level Order Traversal

### Approach

* Store current level size
* Traverse all nodes of that level
* Push children into queue

### Time Complexity

`O(n)`

### Space Complexity

`O(n)`

---

## 2. Binary Tree Right Side View

### Approach

* Perform BFS
* Take last node from every level

### Time Complexity

`O(n)`

### Space Complexity

`O(n)`

---

# Mistakes I Made

* Forgot to check if root is null
* Mixed DFS recursion logic with BFS
* Forgot `level_size = len(queue)`

---

# Key Pattern Learned

When question says:

* level order
  n- level by level
* nearest nodes first
* shortest path in unweighted graph (future graphs topic)

Think **BFS**.

---