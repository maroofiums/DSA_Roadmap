
# Day 2 - DFS (Depth First Search)

## What is DFS?

DFS = Depth First Search

Rule:

- Go as deep as possible first
- Then backtrack

Example:
```
1 → 2 → 4
|
3
```
DFS Traversal:
```
1 → 2 → 4 → 3
```
---

# Real Life Analogy

Maze exploration:

- Pick one path
- Keep moving until dead end
- Return back

This is DFS.

---

# Recursive DFS

```python
def dfs(graph, node, visited):
    if node in visited:
        return
    
    visited.add(node)
    print(node)
    
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)
````

### Example

```python
graph = {
    1:[2,3],
    2:[4],
    3:[],
    4:[]
}

visited = set()
dfs(graph,1,visited)
```

Output:

```python
1
2
4
3
```

---

# How Recursive DFS Works

Call Stack:
```
dfs(1)
→ dfs(2)
→ dfs(4)
```
Then backtrack.

---

# Iterative DFS (Using Stack)

Uses manual stack instead of recursion.

```python
def dfs_iterative(graph,start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node)
            visited.add(node)

            for neighbor in graph[node]:
                stack.append(neighbor)
```

---

# Why Use Visited Set?

Prevents infinite loops in cyclic graphs.

Example:

1 → 2 → 3 → 1

Without visited set:

Infinite recursion

Solution:

```python
visited = set()
```

---

# Time Complexity

DFS visits:

* Every vertex
* Every edge

O(V + E)

---

# Practice Problem 1: Graph Traversal

```python
graph = {
    0:[1,2],
    1:[2],
    2:[3],
    3:[]
}
````

Traversal:

0 → 1 → 2 → 3

---

# Practice Problem 2: Path Exists

Check whether destination exists.

```python
def has_path(graph,src,dst):
    if src == dst:
        return True

    for neighbor in graph[src]:
        if has_path(graph,neighbor,dst):
            return True

    return False
```

---

# Practice Problem 3: Connected Components

Graph:
```
0 -- 1

2 -- 3

4
```
Components:
```
[0,1]
[2,3]
[4]
```
Answer = 3

```python
def count_components(graph):
    visited = set()
    count = 0

    def dfs(node):
        if node in visited:
            return
        
        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor)

    for node in graph:
        if node not in visited:
            count += 1
            dfs(node)

    return count
```

---

# DFS Template

```python
def dfs(node):
    if node in visited:
        return
    
    visited.add(node)

    for neighbor in graph[node]:
        dfs(neighbor)
```

---

# Key Takeaways

* DFS = deep traversal
* Recursion uses call stack
* Iterative DFS uses stack
* Always track visited nodes
* Used in many graph problems

---

# Homework

* Write recursive DFS from memory
* Write iterative DFS from memory
* Solve path exists problem
* Solve connected components
* Dry run on paper
