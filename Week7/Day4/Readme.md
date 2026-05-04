# 📅 DAY 4 - INORDER TRAVERSAL 

## 🎯 Goal of Today

Until now:

* Day 2 → You were printing nodes
* Day 3 → You were returning numbers/booleans

Today:
You’ll learn how to return an entire **list output**, which is how traversal questions usually appear on LeetCode.

---

# Problem: Binary Tree Inorder Traversal

LeetCode: 94

Return the inorder traversal of a binary tree.

Traversal rule:

Left → Node → Right

---

# Example Tree

```
        1
         \
          2
         /
        3
```

Expected Output:

```python
[1,3,2]
```

Why?

* Left of 1 → none
* Visit 1
* Go right → 2
* Left of 2 → 3
* Visit 3
* Visit 2

---

# Why print() is NOT enough

Earlier:

```python
print(root.val)
```

Interview platforms need:

```python
return [1,3,2]
```

So we store values in a list.

---

# Solution Using Helper Function

```python
def inorderTraversal(root):
    result = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result
```

---

# Step-by-Step Breakdown

## Step 1

Create empty list

```python
result = []
```

Stores final traversal answer.

---

## Step 2

Create helper function

```python
def dfs(node):
```

Why helper?
Because main function must return final result.

---

## Step 3

Base case

```python
if not node:
    return
```

Stop recursion.

---

## Step 4

Traverse left

```python
dfs(node.left)
```

---

## Step 5

Visit current node

```python
result.append(node.val)
```

---

## Step 6

Traverse right

```python
dfs(node.right)
```

---

# Visual Flow

Tree:

```
      1
     / \
    2   3
```

Traversal order:

2 → 1 → 3

Output:

```python
[2,1,3]
```

---

# Dry Run

Start at 1:

Go left → 2

2 has no left
Append 2

Go back to 1
Append 1

Go right → 3
Append 3

Final:

```python
[2,1,3]
```

---

# Common Mistakes

* Forgetting result list
* Returning inside recursion too early
* Mixing traversal order
* Using print instead of append

---

# Practice Tasks

## Task 1

Solve LeetCode 94

## Task 2

Convert preorder traversal to list output

## Task 3

Convert postorder traversal to list output

---

# Pattern You Learned Today

```python
result = []

def dfs(node):
    if not node:
        return

    dfs(left)
    process node
    dfs(right)

return result
```

This pattern appears everywhere.

---

# ✅ End of Day Outcome

You should now be able to:

* Return traversal output properly
* Use helper DFS functions
* Solve traversal questions on LeetCode

---