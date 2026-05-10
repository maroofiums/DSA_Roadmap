# Day 3 - Tree Properties

## Objective

Learn how to validate important binary tree properties and improve recursive decision-making.

---

# Concepts Learned

## 1. Balanced Trees

A tree is balanced if:

```text
|left_height - right_height| <= 1
```

for every node.

### Key Idea

Use DFS to calculate heights while checking balance.

---

## 2. Same Tree

Check whether two trees are structurally identical.

Conditions:

* Values must match
* Left subtree must match
* Right subtree must match

---

## 3. Symmetric Tree

Check whether a tree is a mirror of itself.

Compare:

* left.left ↔ right.right
* left.right ↔ right.left

---

## 4. Structural Validation

These problems teach how to validate:

* tree shape
* tree symmetry
* balance conditions
* recursive boolean checks

---

# Problems Solved

## 1. Balanced Binary Tree

### Approach

* Calculate subtree heights
* Check height difference

### Time Complexity

O(n)

---

## 2. Same Tree

### Approach

* Compare both trees recursively

### Time Complexity

O(n)

---

## 3. Symmetric Tree

### Approach

* Compare mirrored nodes recursively

### Time Complexity

O(n)

---

# Common Recursive Pattern

```python
if not p and not q:
    return True

if not p or not q:
    return False

if p.val != q.val:
    return False
```

---

# Mistakes I Made

* Returning wrong boolean values
* Forgot mirror comparison logic
* Mixed height logic with boolean logic

---

# Key Pattern Learned

When question asks:

* is valid?
* is balanced?
* is symmetric?
* are both same?

Think:

👉 **Recursive validation problem**

---

# Time Complexity

All problems → O(n)

---
