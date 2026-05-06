# 📅 DAY 6 - MIXED TREE PRACTICE

## 🎯 Goal of Today

Today is your **confidence-building day**.

You already learned:

* Tree structure
* DFS traversals
* Recursive problem solving
* Returning traversal lists
* Revision

Now your job is to solve problems with minimal help.

Think of today as a mini interview practice day.

---

# Problem 1 - Max Depth (Redo)

LeetCode 104

Goal:
Solve without notes.

Core idea:

genui{"math_block_widget_always_prefetch_v2": {"content": "depth(root)=1+\max(depth(left),depth(right))"}}

Checklist:

* Correct base case
* Recursive calls
* Return max depth

Target Time:
5–7 minutes

---

# Problem 2 - Same Tree (Redo)

LeetCode 100

Goal:
Solve without seeing previous code.

Checklist:

* Both None case
* One None case
* Value mismatch case
* Recursive comparison

Target Time:
5–8 minutes

---

# Problem 3 - Inorder Traversal (Redo)

LeetCode 94

Goal:
Return list output.

Traversal rule:

genui{"math_block_widget_always_prefetch_v2": {"content": "Left \rightarrow Node \rightarrow Right"}}

Checklist:

* Empty result list
* Helper DFS function
* Append values

Target Time:
5–8 minutes

---

# Problem 4 - EXTRA TREE PROBLEM

## Invert Binary Tree

LeetCode 226

This is a perfect beginner tree problem.

---

## Problem Statement

Swap every left and right child.

Example:

Before:

```
      4
     / \
    2   7
   / \ / \
  1  3 6  9
```

After:

```
      4
     / \
    7   2
   / \ / \
  9  6 3  1
```

---

# Think Recursively

At each node:

* Swap left and right
* Solve left subtree
* Solve right subtree

---

# Base Case

```python
if not root:
    return None
```

---

# Solution

```python
def invertTree(root):
    if not root:
        return None

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root
```

---

# Why This Problem Matters

It teaches:

* Tree modification
* Recursive mutation
* Pointer swapping

---

# Full Practice Flow

Solve all 4 problems in one session.

Rule:
No notes.

If stuck for more than 15 mins:

* Review
* Retry

---

# Mistake Tracking Sheet

After each problem write:

* What mistake happened?
* Base case issue?
* Forgot return?
* Wrong traversal order?

---

# Time Goal

Complete all problems in:

45–60 minutes

---

# End of Day Self Check

Can you now solve basic tree problems without panic?

Can you recognize recursion patterns quickly?

If yes → ready for Day 7.

---

# ✅ End of Day Outcome

You should now have:

* Speed
* Confidence
* Better debugging ability
* Strong tree fundamentals