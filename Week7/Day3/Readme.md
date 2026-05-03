# 📅 DAY 3 - TREE PROBLEM SOLVING 

## 🎯 Goal of Today

Today you move from **traversing trees** → to actually **solving tree problems using recursion**.

By the end of today, you should understand:

* How recursion returns values in trees
* How base cases prevent errors
* How to break tree problems into left subtree + right subtree

---

# Problem 1: Max Depth of Binary Tree

LeetCode: 104

## Problem Statement

Find the maximum depth (height) of a binary tree.

Example:

```
        1
       / \
      2   3
     / \
    4   5
```

Max depth = 3

Path:

1 → 2 → 4

---

# Step 1: Think Recursively

At every node ask:

* What is depth of left subtree?
* What is depth of right subtree?
* Take maximum

Formula:

genui{"math_block_widget_always_prefetch_v2": {"content": "depth(root)=1+\max(depth(left),depth(right))"}}

---

# Base Case

If node doesn't exist:

```python
if not root:
    return 0
```

Why?
Because empty tree depth = 0

---

# Solution

```python
def maxDepth(root):
    if not root:
        return 0

    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return 1 + max(left, right)
```

---

# Dry Run

For node 4:

left = 0
right = 0
return 1

For node 2:

left = 1
right = 1
return 2

For node 1:

left = 2
right = 1
return 3

Final answer = 3

---

# Problem 2: Same Tree

LeetCode: 100

## Problem Statement

Check if two trees are identical.

Two trees are same if:

* Values match
* Left subtrees match
* Right subtrees match

---

# Base Cases

### Both None

```python
if not p and not q:
    return True
```

Both trees ended together → valid

---

### One is None

```python
if not p or not q:
    return False
```

Structure mismatch

---

### Values differ

```python
if p.val != q.val:
    return False
```

---

# Solution

```python
def isSameTree(p, q):
    if not p and not q:
        return True

    if not p or not q:
        return False

    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```

---

# Dry Run Example

Tree A:

```
   1
  / \
 2   3
```

Tree B:

```
   1
  / \
 2   3
```

Every node matches → True

---

# Core Recursion Pattern

Almost every tree problem follows:

1. Base case
2. Solve left subtree
3. Solve right subtree
4. Combine result

---

# Difference from Traversals

Day 2:
You were just visiting nodes

Day 3:
You are returning useful values

This is a major shift.

---

# Practice Tasks

## Task 1

Solve Max Depth without looking at notes

## Task 2

Solve Same Tree without looking at notes

## Task 3

Dry run both on paper

---

# Common Mistakes

* Forgetting return statement
* Wrong base case
* Confusing traversal with recursion solving

---

# ✅ End of Day Outcome

You should now be able to:

* Solve beginner tree recursion problems
* Understand recursive returns
* Build answers from subtrees

---