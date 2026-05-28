# Day 7 - Test + Revision

## Topics Covered

* Backtracking
* Recursion
* DFS (Depth First Search)
* State Space Exploration

---

# Problems Solved

## Easy

### 78. Subsets

Generate all possible subsets (the power set) of a given array.

### Concepts

* Backtracking
* Decision Tree
* Include / Exclude Pattern

### Time Complexity

* `O(2^n)`

### Space Complexity

* `O(n)`

---

## Medium

### 46. Permutations

Generate all possible permutations of distinct integers.

### Concepts

* Backtracking
* Path Building
* Used Elements Tracking

### Time Complexity

* `O(n!)`

### Space Complexity

* `O(n)`

---

### 39. Combination Sum

Find all unique combinations where candidates sum to the target.

### Concepts

* Backtracking
* Reuse Elements
* DFS

### Time Complexity

* Exponential

### Space Complexity

* `O(target)`

---

## Hard

### 51. N-Queens

Place `N` queens on an `N x N` chessboard so that no two queens attack each other.

### Concepts

* Backtracking
* Hash Sets
* Diagonal Tracking
* Constraint Checking

### Time Complexity

* Approximately `O(N!)`

### Space Complexity

* `O(N^2)`

---

# Folder Structure

```bash
Day7
└── Problems
    ├── 39. Combination Sum.py
    ├── 46. Permutation.py
    ├── 51. N-Queens.py
    └── 78. Subsets.py
```

---

# Key Learning Outcomes

* Learned how recursive backtracking explores all possibilities.
* Understood how to build and revert state using:

  * `append()`
  * `pop()`
* Practiced pruning invalid states early.
* Improved understanding of recursion trees.

---

# Patterns Identified

| Problem         | Pattern                 |
| --------------- | ----------------------- |
| Subsets         | Include / Exclude       |
| Permutations    | Used Tracking           |
| Combination Sum | Choose / Skip           |
| N-Queens        | Constraint Backtracking |

---

# Revision Notes

## Backtracking Template

```python
def backtrack(state):
    if goal_reached:
        save_result()
        return

    for choice in choices:
        make_choice()

        backtrack(next_state)

        undo_choice()
```

---

# Progress

* Completed Day 7 Revision
* Solved all problems without notes

✅ Easy<br>
✅ Medium<br>
✅ Hard<br>

---

# Next Goal

* Practice optimized pruning
* Solve Sudoku Solver
* Solve Word Search
* Learn Bitmask Backtracking
