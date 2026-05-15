
# Day 1 - Graph Fundamentals

## What is a Graph?

A graph is a non-linear data structure used to represent relationships between objects.

It consists of:

- **Vertices (Nodes)** → entities/data points
- **Edges** → connections between vertices

Example:

```
A -- B  
|    |  
C -- D  
```
Real-world examples:

- Social networks → users + friendships
- Google Maps → cities + roads
- Course prerequisites → courses + dependencies
- Web pages → pages + hyperlinks

---

# Vertices and Edges

Example:
```
1 -- 2  
|    |  
3 -- 4  
```
### Vertices:
- 1
- 2
- 3
- 4

### Edges:
- (1,2)
- (1,3)
- (2,4)
- (3,4)

---

# Directed Graph

Edges have direction.

A → B → C

Meaning:
- A points to B
- B points to C

Example:
- Instagram follow system
- Course prerequisites

### Representation

```python
graph = {
    "A": ["B"],
    "B": ["C"],
    "C": []
}
````

---

# Undirected Graph

Edges have no direction.

A — B

If A connects to B, then B connects to A.

Example:

* Friendships
* Two-way roads

### Representation

```python
graph = {
    "A": ["B"],
    "B": ["A"]
}
```

---

# Weighted Graph

Edges contain weights/costs.

```
A --5--> B
A --2--> C
```

Used in:

* Maps
* Delivery routes
* Flight systems

### Representation

```python
graph = {
    "A": [("B",5), ("C",2)],
    "B": [],
    "C": []
}
```

---

# Cyclic Graph

A cycle means returning to the same node.
```
A → B → C → A
```
This creates a loop.

Example:

* Circular dependencies

---

# Acyclic Graph

No loops exist.
```
A → B → C
```
Used in:

* Task scheduling
* Course scheduling
* Build systems

---

# Adjacency List

Most commonly used graph representation.

Example graph:
```
1 -- 2
|
3
```
### Representation

```python
graph = {
    1: [2,3],
    2: [1],
    3: [1]
}
```

### Space Complexity

O(V + E)




```
Where:
- V = Vertices
- E = Edges
```
---

# Adjacency Matrix

Stores graph in matrix form.
```
    1 2 3
1 [ 0 1 1 ]
2 [ 1 0 0 ]
3 [ 1 0 0 ]
```
### Space Complexity

O(V²)

---

# Adjacency List vs Matrix

| Adjacency List | Adjacency Matrix |
|----------------|------------------|
| Space efficient | More space usage |
| Easy traversal | Fast edge lookup |
| Most common in interviews | Less common |

---

# Implement add_edge()

## Directed Graph

```python
graph = {}

def add_edge(u, v):
    if u not in graph:
        graph[u] = []
    graph[u].append(v)
````

---

## Undirected Graph

```python
graph = {}

def add_edge(u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    graph[v].append(u)
```

---

# Manual Traversal

```python
graph = {
    1: [2,3],
    2: [4],
    3: [],
    4: []
}
```

Traversal:

1 → 2 → 4 → 3

---

# Key Takeaways

* Graph = Nodes + Edges
* Directed = One-way connection
* Undirected = Two-way connection
* Weighted = Edge has cost
* Cycle = Loop exists
* Adjacency List = Most important
* Matrix problems often become graph problems later
