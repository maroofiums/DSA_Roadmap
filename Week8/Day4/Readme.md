# Day 4 - Lowest Common Ancestor (LCA)

## Objective

Learn how recursive ancestor search works and understand subtree return logic.

---

# Concepts Learned

## 1. Recursive Ancestor Search

The goal is to find the lowest node where both target nodes exist in different subtrees.

---

## Example Tree

```text
        3
      /   \
     5     1
    / \   / \
   6   2 0   8
```

LCA of:

* 6 and 2 → 5
* 6 and 8 → 3

---

## 2. Left/Right Subtree Reasoning

At every node:

* Search left subtree
* Search right subtree

Cases:

### Both sides return non-null

Current node = LCA

### Only one side returns non-null

Return that subtree result upward

### Both return null

Return null

---

# Problems Solved

## 1. Lowest Common Ancestor of Binary Tree

### Approach

Use DFS recursion to search both subtrees.

### Time Complexity

O(n)

### Space Complexity

O(h)

---

## 2. Lowest Common Ancestor of BST

### Approach

Use BST property:

* both smaller → go left
* both larger → go right
* otherwise current node is answer

### Time Complexity

O(h)

---

# Core Recursive Pattern

```python
if root is None:
    return None

if root == p or root == q:
    return root

left = dfs(root.left)
right = dfs(root.right)
```

---

# Mistakes I Made

* Wrong base case
* Confused subtree returns
* Forgot when current node becomes answer

---

# Key Pattern Learned

When question asks:

* common ancestor
* parent relationship
* tree relation

Think:

👉 **Recursive subtree return problem**

---