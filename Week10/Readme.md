# Week 10 - Backtracking

Backtracking = “try a choice → go deeper → undo choice → try next”.

You build a decision tree using recursion.

Core pattern:

```python
def backtrack(path, choices):

    if goal_reached:
        result.append(path[:])
        return

    for choice in choices:

        # choose
        path.append(choice)

        # explore
        backtrack(path, new_choices)

        # unchoose (BACKTRACK)
        path.pop()
```

---

# Main Concepts This Week

## 1. Recursion

Function calling itself.

Example:

```python
def count(n):
    if n == 0:
        return
    print(n)
    count(n - 1)
```

---

## 2. Decision Tree

Example for subsets `[1,2]`

```text
                []
             /      \
           take1   skip1
           /           \
        [1]            []
```

Every node = a decision.

---

## 3. Backtracking

You:

* choose
* recurse
* undo choice

```python
path.append(x)
dfs()
path.pop()
```

That `pop()` is the backtracking step.

---

# Day-by-Day Plan

# Day 1 - Recursion Foundations

## Learn

* Base case
* Recursive call
* Call stack
* Decision tree thinking

## Practice

### Easy

* Factorial
* Fibonacci
* Sum of array

### Medium

* Generate all binary strings

Example:

```python
def generate(n, path):

    if len(path) == n:
        print(path)
        return

    generate(n, path + "0")
    generate(n, path + "1")

generate(3, "")
```

Output:

```text
000
001
010
011
100
101
110
111
```

## Goal

Understand:

* recursion depth
* branching
* base case

---

# Day 2 - Subsets

Problem:
Given `[1,2,3]`

Generate:

```text
[]
[1]
[2]
[3]
[1,2]
[1,3]
[2,3]
[1,2,3]
```

---

## Core Idea

For every number:

* take it
* skip it

Decision tree.

---

## Solution

```python
class Solution:
    def subsets(self, nums):

        result = []
        subset = []

        def dfs(i):

            if i >= len(nums):
                result.append(subset[:])
                return

            # take
            subset.append(nums[i])
            dfs(i + 1)

            # backtrack
            subset.pop()

            # skip
            dfs(i + 1)

        dfs(0)
        return result
```

---

## Visual

```text
              []
           /      \
        [1]       []
       /   \      / \
   [1,2] [1] [2] []
```

---

## Practice

* LeetCode 78 - Subsets
* Subsets II

---

# Day 3 - Permutations

Problem:

```text
Input: [1,2,3]

Output:
[1,2,3]
[1,3,2]
[2,1,3]
...
```

---

## Idea

At each step:
choose one unused number.

---

## Solution

```python
class Solution:
    def permute(self, nums):

        result = []

        def backtrack(path):

            if len(path) == len(nums):
                result.append(path[:])
                return

            for n in nums:

                if n in path:
                    continue

                path.append(n)

                backtrack(path)

                path.pop()

        backtrack([])
        return result
```

---

## Decision Tree

```text
            []
       /      |      \
      1       2       3
    /  \    /  \    /  \
```

---

## Practice

* LeetCode 46 - Permutations
* Permutations II

---

# Day 4 - Combination Problems

## Learn

Difference between:

* subsets
* permutations
* combinations

---

## Combination Sum

```text
target = 7
nums = [2,3,6,7]
```

Output:

```text
[2,2,3]
[7]
```

---

## Solution

```python
class Solution:
    def combinationSum(self, candidates, target):

        result = []

        def dfs(i, cur, total):

            if total == target:
                result.append(cur[:])
                return

            if i >= len(candidates) or total > target:
                return

            # choose
            cur.append(candidates[i])

            dfs(i, cur, total + candidates[i])

            # backtrack
            cur.pop()

            # skip
            dfs(i + 1, cur, total)

        dfs(0, [], 0)

        return result
```

---

## Goal

Learn:

* repeated choices
* pruning
* constraints

---

# Day 5 - N-Queens

Classic hard backtracking problem.

---

## Problem

Place queens so:

* same row ❌
* same column ❌
* same diagonal ❌

---

## Learn

How to track:

* columns
* positive diagonal
* negative diagonal

---

## Important Formula

For diagonals:

r+c\ \text{(positive diagonal)},\quad r-c\ \text{(negative diagonal)}

---

## Core Solution

```python
class Solution:
    def solveNQueens(self, n):

        col = set()
        posDiag = set()
        negDiag = set()

        board = [["."] * n for _ in range(n)]

        result = []

        def backtrack(r):

            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return

            for c in range(n):

                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

                board[r][c] = "."

        backtrack(0)

        return result
```

---

# Day 6 - Advanced Backtracking

## Learn

* pruning
* duplicate handling
* visited arrays

---

## Problems

### Medium

* Word Search
* Palindrome Partitioning

### Hard

* Sudoku Solver

---

# Day 7 - Test + Revision

## Solve Without Notes

### Easy

* Subsets

### Medium

* Permutations
* Combination Sum

### Hard

* N-Queens

---

# Patterns You Must Understand

## Pattern 1 - Choose / Explore / Undo

```python
choose
recurse
undo
```

---

## Pattern 2 - Used Set

```python
if x in used:
    continue
```

Used in:

* permutations
* graph search
* scheduling

---

## Pattern 3 - Pruning

Skip impossible paths early.

```python
if total > target:
    return
```

---

# Complexity Intuition

Backtracking is usually exponential.

Examples:

| Problem      | Complexity |
| ------------ | ---------- |
| Subsets      | (2^n)      |
| Permutations | (n!)       |
| N-Queens     | very large |

---

# Best LeetCode Set

## Easy

* Subsets

## Medium

* Permutations
* Combination Sum
* Letter Combinations

## Hard

* N-Queens
* Sudoku Solver

---

# Final Goal of Week 10

By end of week you should:

* think recursively
* visualize decision trees
* write backtracking templates from memory
* know when to:

  * choose
  * recurse
  * backtrack
  * prune
