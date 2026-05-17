# Day 3 - BFS (Breadth First Search)

## Goal
Understand level-by-level traversal and shortest path intuition.

---

# What is BFS?

BFS = Breadth First Search

It explores nodes level by level instead of going deep like DFS.

Example:
```
        1
      /   \
     2     3
    / \
   4   5
````
BFS Traversal:

1 → 2 → 3 → 4 → 5

---

# Why Queue?

BFS uses Queue (FIFO)

FIFO = First In First Out

Example:

Insert:
1,2,3

Remove:
1 first

Python:

```python
from collections import deque

q = deque()

q.append(1)
q.append(2)
q.append(3)

print(q.popleft())
````

Output:

```python
1
```

---

# BFS Traversal Algorithm

1. Put starting node in queue
2. Mark it visited
3. Remove node from queue
4. Visit neighbors
5. Add unvisited neighbors to queue
6. Repeat until queue becomes empty

---

# BFS Code

```python
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

---

# Example

```python
graph = {
    1:[2,3],
    2:[4,5],
    3:[],
    4:[],
    5:[]
}

bfs(graph,1)
```

Output:

```python
1
2
3
4
5
```

---

# Dry Run

Queue:

[1]

Pop → 1

Add neighbors:

[2,3]

Pop → 2

Add neighbors:

[3,4,5]

Continue until queue is empty.

---

# Level Order Traversal

Tree:

```
     1
   /   \
  2     3
 / \
4   5
```

Levels:
```
Level 0 → 1
Level 1 → 2,3
Level 2 → 4,5
```
---

# Level Order Code

```python
from collections import deque

def level_order(graph,start):
    queue = deque([start])
    visited = set([start])

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            print(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
```

---

# Shortest Path in Unweighted Graph

BFS finds shortest path because it explores nearest nodes first.

Example:
```
A → B → D
A → C
```
Shortest path from A to D:
```
A → B → D
```
Distance = 2 edges

---

# Shortest Path Code

```python
from collections import deque

def shortest_path(graph,start,target):
    queue = deque([(start,0)])
    visited = set([start])

    while queue:
        node,distance = queue.popleft()

        if node == target:
            return distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor,distance+1))

    return -1
```

---

# Time Complexity

O(V + E)


```md
V = Vertices
E = Edges
```
---

# BFS vs DFS

| BFS | DFS |
|------|------|
| Queue | Stack/Recursion |
| Level order | Deep traversal |
| Shortest path | Path exploration |

---

# When to Use BFS?

Use BFS when question asks:

- Shortest path
- Minimum steps
- Nearest node
- Level traversal
- Fewest moves

---

# Practice Problems

1. BFS Traversal
2. Minimum steps in grid
3. Shortest path problem

---

# Revision Template

```python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```