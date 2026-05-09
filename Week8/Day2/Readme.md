# Day 2 - Tree Height / Depth

## Objective

Learn how to calculate tree height (depth) using recursion and understand base case handling.

---

# Concepts Learned

## 1. Recursive Depth Calculation

Tree height is naturally solved using recursion.

At every node:

* Compute left subtree height
* Compute right subtree height
* Add 1 for current node

---

## 2. Base Case Handling

Correct base case is critical:

```python
if not root:
    return 0
```

Without this, recursion breaks or gives wrong values.

---

# Core Formula

## Tree Height Definition

genui{"math_block_widget_always_prefetch_v2":{"content":"height(node) = 1 + \max(height(left), height(right))"}}

---

# Problems Solved

## 1. Maximum Depth of Binary Tree

### Approach

* Recursively compute depth
* Return max(left, right) + 1

### Time Complexity

O(n)

### Space Complexity

O(h) where h = height of tree

---

## 2. Minimum Depth of Binary Tree

### Approach

* Handle missing child cases carefully
* Avoid taking minimum of 0 incorrectly

### Key Insight

If one child is null, take the other child path only.

---

# Code Pattern

```python
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
```

---

# Mistakes I Made

* Incorrect null handling in minimum depth
* Returning 0 too early
* Confusing minDepth with maxDepth logic

---

# Key Pattern Learned

When you see:

* height
* depth
* longest path from root

Think:

👉 **Recursive DFS + max(left, right)**

---

# Time Complexity

* Every node visited once → O(n)
