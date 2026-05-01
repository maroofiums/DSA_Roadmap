# 📅 DAY 1 - TREE FUNDAMENTALS (DETAILED NOTES)

## 🎯 Goal of Today

By the end of this day, you should clearly understand:

* What a tree is in Data Structures
* How a binary tree is structured
* Why trees are recursive by nature
* How to manually build a tree in Python

---

# 🌳 1. WHAT IS A TREE?

A **tree** is a hierarchical data structure used to store data in a parent-child relationship.

Unlike arrays or linked lists:

* Arrays → linear structure
* Linked List → linear chain
* Tree → hierarchical branching structure

---

## 🧠 Real-Life Example

Think of a family tree:

* One ancestor (root)
* Children branch out
* Each child can have their own children

---

# 🌲 2. BASIC TREE TERMINOLOGY

## 🔹 Root

The **top node** of the tree.

Example:

```
      1   ← Root
     / \
    2   3
```

---

## 🔹 Leaf Node

A node with **no children**.

Example:

```
    2   3   ← Leaf nodes
```

---

## 🔹 Parent & Child

* Parent → node that has children
* Child → node below parent

Example:

```
1 is parent of 2 and 3
```

---

## 🔹 Height

Longest path from root to a leaf.

---

# 🌳 3. BINARY TREE STRUCTURE

A **binary tree** means:

* Each node has at most 2 children

  * Left child
  * Right child

---

## 📦 Python Representation

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

## 🧠 What this means

Each node is like an object:

* val → data
* left → pointer to left subtree
* right → pointer to right subtree

---

# 🌲 4. MANUALLY BUILDING A TREE

## Example Tree:

```
        1
       / \
      2   3
     / \
    4   5
```

---

## 🧑‍💻 Code

```python
# Step 1: Create nodes
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

# Step 2: Connect nodes
root.left = node2
root.right = node3

node2.left = node4
node2.right = node5
```

---

# 🔁 5. WHY TREES ARE RECURSIVE?

A tree is recursive because:

👉 Every node is itself a tree

Example:

```
      2
     / \
    4   5
```

Subtree rooted at 2 is still a tree
Subtree rooted at 4 is also a tree

---

## 🧠 Key Insight

If you understand one node operation, you understand the whole tree.

---

# 🧪 6. MINI PRACTICE

## Task 1

Create this tree in Python:

```
    10
   /  \
  20   30
```

## Task 2

Identify:

* Root
* Leaves
* Parent nodes

---

# 🧠 7. INTERVIEW THINKING SHIFT

Before trees:

* You think linearly

After trees:

* You think in branches
* You think recursively

---

# ⚠️ COMMON MISTAKES

* Confusing tree with graph
* Thinking only top-down (trees also work bottom-up)
* Forgetting left/right distinction

---

# ✅ END OF DAY 1 OUTCOME

You should now be able to:

* Explain tree structure
* Understand binary tree nodes
* Build a tree manually in Python
* Understand why recursion is natural for trees

---