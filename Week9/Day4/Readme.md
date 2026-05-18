# Day 4 - Number of Islands

## Problem

Given a grid of:

- `"1"` → land
- `"0"` → water

Return the number of islands.

An island is formed by connecting adjacent lands:

- Up
- Down
- Left
- Right

---

## Example

```python
grid = [
    ["1","1","0","0"],
    ["1","0","0","1"],
    ["0","0","1","1"]
]
````

Output:

```python
2
```

---

## Key Pattern

Grid problems often hide graph problems.

### Convert:

```python
Grid → Graph
```

Each cell = node

Adjacent land cells = connected nodes

---

## Directions

```python
(i-1,j)   # up
(i+1,j)   # down
(i,j-1)   # left
(i,j+1)   # right
```

No diagonal movement.

---

# Approach

Loop through every cell.

If cell == `"1"`:

* Found new island
* Increase count
* Run DFS
* Mark entire island visited

---

## DFS Logic

```python
def dfs(i,j):
    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
        return
    else:
        grid[i][j] = "0"
        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j-1)
        dfs(i,j+1)
```

---

# Full Solution

```python
def numIslands(grid: List[List[str]]) -> int:
    m,n = len(grid),len(grid[0])

    def dfs(i,j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
            return
        else:
            grid[i][j] = "0"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

    island_count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                island_count += 1
                dfs(i,j)

    return island_count
```

---

# Why `grid[r][c] = "0"`?

Acts like visited set.

Instead of:

```python
visited = set()
```

We modify grid directly.

---

# Boundary Check

```python
if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
    return
```

Prevents index errors.

---

# Time Complexity

```python
O(rows * cols)
```

Each cell visited once.

O(rows \times cols)

---

# Pattern Recognition

If problem contains:

* Grid
* Matrix
* Islands
* Regions
* Groups
* Connected cells

Think:

```python
Grid → DFS/BFS
```

---

# Similar Problems

* LeetCode Flood Fill
* LeetCode Max Area of Island
* LeetCode Rotten Oranges
* LeetCode Surrounded Regions
