# Day 5 - Diameter of Binary Tree

## Objective

Learn how to calculate the longest path in a binary tree and manage global state during recursion.

---

# Concepts Learned

## 1. Longest Path Logic

Diameter means:

**Longest path between any two nodes in the tree**

The path may or may not pass through the root.

---

## Formula

genui{"math_block_widget_always_prefetch_v2":{"content":"diameter = height(left) + height(right)"}}

At every node:

* calculate left height
* calculate right height
* update maximum diameter

---

## Example

```text
       1
      / \
     2   3
    / \
   4   5
```

Longest path:

4 → 2 → 5 → 1 → 3

Diameter = 4 edges

---

# Concepts Learned (Important)

## 2. Global Variable Tracking

We return height from recursion.

But diameter needs a global maximum update.

That means recursion has two jobs:

* return height
* update diameter

---

# Problems Solved

## 1. Diameter of Binary Tree

### Approach

Use DFS recursion for height calculation.

Update global diameter at every node.

### Time Complexity

O(n)

### Space Complexity

O(h)

---

## 2. Binary Tree Maximum Path Sum (Optional)

Hard variation of diameter logic.

Adds path sum constraints.

---

# Core Pattern

```python
diameter = 0

def dfs(root):
    if not root:
        return 0

    left = dfs(root.left)
    right = dfs(root.right)

    diameter = max(diameter, left + right)

    return 1 + max(left, right)
```

---

# Mistakes I Made

* Forgot global update
* Returned diameter instead of height
* Confused path length with tree height

---

# Key Pattern Learned

When question asks:

* longest path
* maximum path
* tree width/diameter style

Think:

👉 **DFS + height + global variable pattern**

---

# Time Complexity

O(n)
