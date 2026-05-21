# Day 7 - Graph Test Day

Today is not for learning new concepts.

Today is for:

```text id="y1br7g"
Recall + Pattern Recognition + Speed
```

This is where graph concepts become permanent.

---

# Test Rules

## Strict Rules

* No notes
* No ChatGPT
* No YouTube
* No copy-paste
* Use timer

---

# Easy Problems (15 mins each)

## 1) Graph Traversal

### Goal

Implement:

* DFS
* BFS

---

## Input

```python id="74l9yj"
graph = {
    0:[1,2],
    1:[3],
    2:[],
    3:[]
}
```

---

## Tasks

### DFS Output

```python id="g3ql1s"
0 → 1 → 3 → 2
```

---

### BFS Output

```python id="6w45k6"
0 → 1 → 2 → 3
```

---

## Concepts Being Tested

* recursion
* stack/queue
* visited set

---

# 2) Path Exists

## Problem

Return:

```python id="scysux"
True
```

if path exists from source → destination.

---

## Example

```python id="uj9wxq"
A → B → C
|
D
```

Question:

```python id="z5m9w8"
Path from A to D?
```

Answer:

```python id="c0w78n"
True
```

---

## Expected Pattern

DFS

---

## Hint

Base case:

```python id="ryjlwm"
if src == dst:
    return True
```

---

# Medium Problems (25 mins each)

These are real interview-level graph patterns.

---

# 1) Number of Islands

## Concepts Tested

* Grid → graph conversion
* DFS on matrix
* Boundary checking

---

## Pattern

```python id="9xjlwm"
Grid → DFS/BFS
```

---

## Key Question

When should island count increase?

Answer:

```python id="h71nfa"
When unvisited land is found
```

---

## Important Reminder

Directions:

```python id="9nz6a5"
up
down
left
right
```

---

# 2) Clone Graph

## Concepts Tested

* DFS traversal
* HashMap
* Deep copy
* Cyclic graphs

---

## Core Mapping

```python id="u9px3e"
old_node → new_node
```

---

## Key Question

Why hashmap needed?

Answer:

* avoid duplicate cloning
* prevent infinite recursion

---

## Pattern

```python id="ik0djm"
DFS + HashMap
```

---

# 3) Course Schedule

## Concepts Tested

* Directed graph
* Cycle detection
* Dependency systems

---

## Important Concepts

### visiting

Current DFS path

---

### visited

Fully processed safe nodes

---

## Key Pattern

```python id="1u85ic"
Directed Graph + Cycle Detection
```

---

# Recommended Order

Start easiest first:

1. Graph Traversal
2. Path Exists
3. Number of Islands
4. Clone Graph
5. Course Schedule

This builds confidence gradually.

---

# Time Management Strategy

## Easy

If stuck > 5 mins:

* dry run manually
* draw graph

---

## Medium

If stuck:

Ask yourself:

```python id="0hjlwm"
Is this DFS?
Is this BFS?
Is this cycle detection?
Is this grid graph?
```

Pattern recognition is everything.

---

# What You Should Know After This Week

You now understand:

* Graph representation
* DFS
* BFS
* Grid graphs
* Graph cloning
* Cycle detection
* Directed graphs
* Connected components

This is already a strong graph foundation.

---

# Real-World Systems Using These Concepts

* Google web crawling
* Meta social graphs
* Uber shortest path routing
* GitHub dependency graphs

---

# Final Reflection Questions

After solving, ask yourself:

1. When should I use DFS?
2. When should I use BFS?
3. How do I detect cycles?
4. Why do graphs need visited sets?
5. How do matrices become graphs?

If you can answer these comfortably, Week 9 was successful.

---
