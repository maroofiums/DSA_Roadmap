# Day 6 - Advanced Backtracking

This section focuses on advanced recursive backtracking patterns used in interview-level problems.

Topics covered:

* pruning
* duplicate handling
* visited arrays
* DFS on grids
* constraint-based recursion

---

# Folder Structure

```text id="bxxk3z"
Day6
├── Problems
│   ├── 37. Sudoku Solver
│   │   ├── Brute Force.py
│   │   └── Optimal.py
│   ├── 131. Palindrome Partitioning.py
│   ├── 78. Subsets.py
│   ├── 79. Word Search.py
│   └── 90. Subsets II.py
└── Readme.md
```

---

# Concepts Learned

## 1. Pruning

Pruning means:

* stopping invalid recursion early
* avoiding useless paths

Example:

```python id="3c4wkn"
if total > target:
    return
```

Benefits:

* fewer recursive calls
* faster execution
* optimized DFS tree

---

# 2. Duplicate Handling

Used when input contains duplicate values.

Main technique:

```python id="d4e3tb"
nums.sort()
```

Then skip duplicates:

```python id="f4wwp8"
if i > idx and nums[i] == nums[i - 1]:
    continue
```

Used in:

* Subsets II
* Combination Sum II
* Permutations II

---

# 3. Visited Arrays / Visited States

Used to:

* prevent reuse
* mark explored states
* avoid cycles

Examples:

* Word Search
* Graph DFS
* Permutations

---

# Problem 1 - 131. Palindrome Partitioning

## Problem

Partition a string into substrings such that every substring is a palindrome.

---

# Example

Input:

```text id="7o5nwv"
"aab"
```

Output:

```text id="n4f7gh"
["a","a","b"]
["aa","b"]
```

---

# Solution

```python id="cw40nn"
from typing import List

def partition(s: str) -> List[List[str]]:

    def isPalindrome(string):

        l = 0
        r = len(string) - 1

        while l < r:

            if string[l] != string[r]:
                return False

            l += 1
            r -= 1

        return True

    res = []
    path = []

    def backtrack(start):

        if start == len(s):
            res.append(path[:])
            return

        for end in range(start + 1, len(s) + 1):

            substring = s[start:end]

            # pruning
            if isPalindrome(substring):

                path.append(substring)

                backtrack(end)

                path.pop()

    backtrack(0)

    return res
```

---

# Key Concepts

* recursion on substrings
* pruning invalid substrings
* partition generation
* DFS branching

---

# Time Complexity

Worst-case:

O(2^n)

---

# Problem 2 - 79. Word Search

## Problem

Search for a word in a 2D board.

Movement allowed:

* up
* down
* left
* right

Cell reuse is NOT allowed.

---

# Solution

```python id="7epm2h"
from typing import List

def wordSearch(board: List[List[str]], word: str) -> bool:

    m = len(board)
    n = len(board[0])

    w = len(word)

    def backtrack(pos, index):

        i, j = pos

        # word completed
        if index == w:
            return True

        # invalid state
        if (
            i < 0 or
            j < 0 or
            i >= m or
            j >= n or
            board[i][j] != word[index]
        ):
            return False

        temp = board[i][j]

        board[i][j] = "#"

        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        for i_off, j_off in directions:

            r = i + i_off
            c = j + j_off

            if backtrack((r, c), index + 1):
                return True

        # backtrack
        board[i][j] = temp

        return False

    for i in range(m):
        for j in range(n):

            if backtrack((i, j), 0):
                return True

    return False
```

---

# Important Fixes

Your original code had:

```python id="l4tdr1"
if board == word[index]:
```

Correct version:

```python id="3qrg6w"
board[i][j] != word[index]
```

Also boundary checks should happen BEFORE accessing board.

---

# Key Concepts

* DFS on grid
* visited marking
* state restoration
* boundary pruning

---

# Complexity

Worst-case:

O(m \times n \times 4^L)

Where:

* `m × n` = board size
* `L` = word length

---

# Problem 3 - 78. Subsets

## Problem

Generate all subsets.

---

# Solution

```python id="mgqah3"
from typing import List

def subsets(nums: List[int]) -> List[List[int]]:

    res = []
    path = []

    def backtrack(idx=0):

        res.append(path[:])

        for i in range(idx, len(nums)):

            path.append(nums[i])

            backtrack(i + 1)

            path.pop()

    backtrack()

    return res
```

---

# Key Concepts

* choose / recurse / undo
* recursion tree
* subset generation

---

# Complexity

Total subsets:

2^n

---

# Problem 4 - 90. Subsets II

## Problem

Generate unique subsets when duplicates exist.

---

# Solution

```python id="j3ryoz"
from typing import List

def subsets(nums: List[int]) -> List[List[int]]:

    nums.sort()

    res = []
    path = []

    def backtrack(idx=0):

        res.append(path[:])

        for i in range(idx, len(nums)):

            # duplicate handling
            if i > idx and nums[i] == nums[i - 1]:
                continue

            path.append(nums[i])

            backtrack(i + 1)

            path.pop()

    backtrack()

    return res
```

---

# Key Concepts

* sorting
* duplicate pruning
* recursion-level skipping

---

# Problem 5 - 37. Sudoku Solver (Brute Force)

## Idea

Try every valid number recursively.

---

# Solution

```python id="n4mtb8"
def isValid(board, row, col, num_char):

    for r in range(9):
        if board[r][col] == num_char:
            return False

    for c in range(9):
        if board[row][c] == num_char:
            return False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):

            if board[r][c] == num_char:
                return False

    return True
```

---

# Brute Force Backtracking

```python id="9e9p5r"
def solver(board):

    for r in range(9):
        for c in range(9):

            if board[r][c] == ".":

                for num in range(1,10):

                    num_char = str(num)

                    if isValid(board, r, c, num_char):

                        board[r][c] = num_char

                        if solver(board):
                            return True

                        board[r][c] = "."

                return False

    return True
```

---

# Problem 6 - 37. Sudoku Solver (Optimal)

## Optimization

Instead of scanning rows/cols repeatedly:

* use sets

---

# Box Formula

For cell `(r,c)`:

(r // 3) \times 3 + (c // 3)

---

# State Tracking

```python id="m14vkw"
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxs = [set() for _ in range(9)]
```

---

# Benefits

Checking validity becomes:

```text id="2h0f94"
O(1)
```

instead of scanning board repeatedly.

---

# Complexity Comparison

| Version     | Validity Check  |
| ----------- | --------------- |
| Brute Force | O(9) scans      |
| Optimal     | O(1) set lookup |

---

# Core Backtracking Pattern

All problems follow:

```python id="gn36xt"
choose

recurse

undo
```

Example:

```python id="9kpx2v"
path.append(x)

backtrack()

path.pop()
```

---

# Concepts Practiced

| Concept             | Problems             |
| ------------------- | -------------------- |
| Pruning             | Sudoku, Partitioning |
| Duplicate Handling  | Subsets II           |
| Visited States      | Word Search          |
| Constraint Tracking | Sudoku               |
| DFS                 | All Problems         |

---

# Main Learning Outcome

After Day 6 you should understand:

* advanced pruning
* duplicate handling
* visited state tracking
* DFS on grids
* recursive constraint solving
* optimized backtracking patterns
