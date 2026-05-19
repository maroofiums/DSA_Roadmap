# Day 5 - Clone Graph

Today’s problem is important because it teaches:

* Real graph traversal
* Deep copying
* HashMap mapping
* Cyclic graph handling

This is one of the first “real graph object” problems on LeetCode.

---

# Problem: Clone Graph

You are given a node in a connected graph.

Create a **deep copy** of the graph.

Meaning:

* Create completely new nodes
* Preserve connections
* Do NOT reuse original nodes

---

# Example Graph

```python id="dvl93p"
1 --- 2
|     |
4 --- 3
```

Cloned graph should look identical:

```python id="a09z0j"
1' --- 2'
|       |
4' --- 3'
```

But nodes are NEW objects.

---

# What Makes This Hard?

Graphs can contain cycles.

Example:

```python id="pk5md0"
1 → 2 → 3 → 1
```

If you clone recursively without tracking:

Infinite recursion.

---

# Key Idea

We need mapping:

```python id="vv38an"
old_node → new_node
```

This is why HashMap (dictionary) is used.

---

# Node Structure

Typical interview structure:

```python id="bjjlwm"
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []
```

Each node contains:

* value
* list of neighboring nodes

---

# Visual Understanding

Original:

```python id="x0e3vz"
1 -> [2,4]
2 -> [1,3]
3 -> [2,4]
4 -> [1,3]
```

Clone:

```python id="9y8w6d"
1' -> [2',4']
2' -> [1',3']
3' -> [2',4']
4' -> [1',3']
```

---

# DFS Cloning Approach

Steps:

1. Create copy of current node
2. Store mapping
3. DFS neighbors
4. Connect cloned neighbors

---

# HashMap Usage

```python id="m1exwp"
old_to_new = {}
```

Example:

```python id="uxq6ri"
{
   old_node_1 : cloned_node_1,
   old_node_2 : cloned_node_2
}
```

---

# DFS Clone Solution

```python id="2lp8yh"
class Solution:
    def cloneGraph(self, node):

        old_to_new = {}

        def dfs(node):

            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)

            old_to_new[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node) if node else None
```

---

# Step-by-Step Dry Run

Graph:

```python id="jlwmq5"
1 --- 2
```

Start:

```python id="l1a0zw"
dfs(1)
```

Create:

```python id="xt3g3f"
1'
```

Store:

```python id="j2h6b7"
{
 1 : 1'
}
```

Visit neighbor `2`

Create:

```python id="fxxe5w"
2'
```

Store:

```python id="g9v1yn"
{
 1 : 1',
 2 : 2'
}
```

Now connect:

```python id="3f12q7"
1'.neighbors = [2']
2'.neighbors = [1']
```

Done.

---

# Why HashMap is Critical

Without it:

* duplicate nodes get created
* cycles cause infinite recursion

HashMap solves both.

---

# Deep Copy vs Shallow Copy

## Shallow Copy

Copies references only.

```python id="6ml0u0"
A -> same object
```

---

## Deep Copy

Creates entirely new objects.

```python id="s2x5lt"
A -> new independent object
```

Clone Graph requires:

```python id="2r6a84"
Deep Copy
```

---

# Time Complexity

Every node and edge visited once:

O(V+E)

---

# Space Complexity

HashMap + recursion stack:

O(V)

---

# BFS Version (Alternative)

Possible using queue.

But DFS is cleaner for interviews.

---

# Recognition Pattern

If question says:

* clone/copy graph
* duplicate nodes
* preserve relationships
* cyclic references

Think:

```python id="e7p2gn"
DFS + HashMap
```

---

# Common Mistake

WRONG:

```python id="sv1d5l"
copy.neighbors = node.neighbors
```

Why wrong?

Because original graph references are reused.

Not a deep copy.

---

# Similar Problems

* Copy linked list with random pointer
* Deep copy nested structures
* Graph serialization/deserialization

---

# Interview Explanation

Strong explanation:

> “I use DFS to traverse the graph and a hashmap to map original nodes to cloned nodes so cycles and duplicate cloning are avoided.”

That sounds interview-level.

---

# Mini Visualization

---

# Homework

1. Rewrite clone graph from memory
2. Dry run on cyclic graph
3. Explain why hashmap is necessary
4. Implement iterative BFS clone version yourself
