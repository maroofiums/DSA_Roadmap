# 📅 Day 7 - Tree Mock Test

## 🧭 Overview
This day is a full **mock interview simulation** for binary tree fundamentals.

No learning is done here only testing your ability to recall and apply concepts from Week 7.

---

## 🎯 Objective
By the end of this mock test, you should be able to:

- Solve basic tree problems without notes
- Apply recursion patterns under time pressure
- Identify weaknesses in DFS-based problems
- Build interview confidence

---

## ⏱️ Time Limit
- 45–60 minutes (single session recommended)

---

## 📌 Rules
- No notes
- No internet
- No copying previous solutions
- Solve independently

---

## 🧪 Problems

### 1. Max Depth of Binary Tree
- Type: Recursive DFS
- Core idea:  
  `depth = 1 + max(left, right)`

---

### 2. Same Tree
- Type: Recursive comparison
- Core idea:
  - Check structure
  - Check values
  - Recurse left and right

---

### 3. Inorder Traversal
- Type: DFS traversal
- Order: Left → Node → Right
- Output must be a list

---

## 🧠 Core Patterns Used

### Depth Pattern
```python
return 1 + max(left, right)
````

---

### Tree Comparison Pattern

```python
return isSame(left) and isSame(right)
```

---

### DFS Traversal Pattern

```python
def dfs(node):
    if not node:
        return
    dfs(node.left)
    process(node)
    dfs(node.right)
```

---

## 📊 Self Evaluation (Score /30)

* Max Depth: /10
* Same Tree: /10
* Inorder Traversal: /10

---

## 📈 Performance Levels

* **25–30** → Interview ready for basics
* **18–24** → Needs revision on recursion
* **<18** → Repeat Days 3–5

---

## ⚠️ Common Mistakes

* Forgetting base case
* Mixing traversal order
* Not returning values properly
* Confusing recursion flow

---

## 🧠 Key Insight

Tree problems are not about memorization.

They follow a simple recursion pattern:

1. Base case
2. Left subtree
3. Right subtree
4. Combine result

---
