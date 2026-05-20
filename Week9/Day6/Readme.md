# Day 6 - Course Schedule

## Problem

You are given:

- `numCourses`
- `prerequisites`

Each pair `[a, b]` means:

> You must complete course `b` before course `a`.

Return `True` if you can finish all courses, otherwise `False`.

---

## Key Idea

This is a:

> Directed Graph Cycle Detection Problem

If a cycle exists → impossible to complete courses.

---

## Graph Interpretation

Example:

```python
prerequisites = [[1,0]]
````

Means:

```text
0 → 1
```

---

## Core Concept

We track each node using 3 states:

| State | Meaning                        |
| ----- | ------------------------------ |
| 0     | Not visited                    |
| 1     | Visiting (in current DFS path) |
| 2     | Fully processed (safe)         |

---

## Why This Works

* If we revisit a `visiting (1)` node → **cycle detected**
* If node is `visited (2)` → already safe

---

## DFS Solution (Your Code)

```python
from typing import List

def canFinish(numCourses:int, prerequisites:List[List[int]]) -> bool:
    
    graph = [[] for _ in range(numCourses)]
    
    for a, b in prerequisites:
        graph[b].append(a)

    visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited

    def dfs(course):
        if visited[course] == 1:
            return False  # cycle detected
        if visited[course] == 2:
            return True   # already processed safely

        visited[course] = 1  # mark as visiting

        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False

        visited[course] = 2  # mark as fully processed
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False

    return True


# Example
numCourses = 2
prerequisites = [[1,0]]

print(canFinish(numCourses, prerequisites))
```

---

## Time Complexity

We visit each node and edge once:

```text
O(V + E)
```

O(V + E)

---

## Space Complexity

```text
O(V)
```

for recursion + visited array.

O(V)

---

## Pattern Recognition

If you see:

* prerequisites
* dependencies
* scheduling
* ordering tasks

Think:

> Directed Graph + Cycle Detection

---

## Real-World Analogy

* University course planning
* Build systems
* Package dependencies

Example systems like Python Software Foundation package dependencies use similar logic.

---

## Key Takeaway

There are **two correct ways** to solve this problem:

1. DFS cycle detection (this solution)
2. Topological sort (BFS/Kahn’s algorithm)

---

## Practice Next

* Course Schedule II (return ordering)
* Alien Dictionary
* Graph Valid Tree

```

---