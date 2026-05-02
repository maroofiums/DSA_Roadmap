# 📅 DAY 2 - DFS TRAVERSALS 

## 🎯 Goal of Today

By the end of today, you should understand:

* What DFS means in trees
* Why recursion is commonly used in tree traversal
* The difference between Inorder, Preorder, and Postorder
* How to dry run traversal problems manually

---

# 🌳 1. What is DFS?

DFS = **Depth First Search**

It means:
👉 Go as deep as possible into one branch before moving to another branch.

Example Tree:

```
        1
       / \
      2   3
     / \
    4   5
```

DFS explores one path fully before backtracking.

---

# 🔁 Why Recursion Works Perfectly

Each node asks:

* Process me
* Process my left subtree
* Process my right subtree

Since every subtree is also a tree → recursion fits naturally.

Base case:

```python
if not root:
    return
```

This stops recursion when node becomes None.

---

# 2. Inorder Traversal (Left → Node → Right)

Pattern:

```
Left
Node
Right
```

Code:

```python
def inorder(root):
    if not root:
        return

    inorder(root.left)
    print(root.val)
    inorder(root.right)
```

For tree:

```
        1
       / \
      2   3
     / \
    4   5
```

Output:

```
4 2 5 1 3
```

---

# 3. Preorder Traversal (Node → Left → Right)

Pattern:

```
Node
Left
Right
```

Code:

```python
def preorder(root):
    if not root:
        return

    print(root.val)
    preorder(root.left)
    preorder(root.right)
```

Output:

```
1 2 4 5 3
```

---

# 4. Postorder Traversal (Left → Right → Node)

Pattern:

```
Left
Right
Node
```

Code:

```python
def postorder(root):
    if not root:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.val)
```

Output:

```
4 5 2 3 1
```

---

# 🧠 Easy Memory Trick

### Inorder

LNR

### Preorder

NLR

### Postorder

LRN

Memorize these patterns.

---

# 🔍 Dry Run Example

Tree:

```
        1
       / \
      2   3
```

### Inorder

Visit left → 2
Visit root → 1
Visit right → 3

Output:

```
2 1 3
```

---

# 🧪 Practice Tasks

## Task 1

Write all three traversals from memory.

---

## Task 2

Dry run on this tree:

```
      10
     /  \
    20   30
   / \
  40 50
```

Find:

* Inorder
* Preorder
* Postorder

---

# ⚠️ Common Mistakes

* Forgetting base case
* Mixing traversal order
* Printing before recursion accidentally
* Not understanding backtracking

---

# 🔥 Interview Pattern

Most tree problems follow:

1. Base case
2. Go left
3. Go right
4. Return answer

---

# ✅ End of Day Outcome

You should now be able to:

* Explain DFS clearly
* Implement all traversals
* Dry run tree recursion
* Build confidence for actual tree problems

---