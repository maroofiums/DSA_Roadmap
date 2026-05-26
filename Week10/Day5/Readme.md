# Day 5 - N-Queens

N-Queens is one of the MOST important backtracking problems.

It teaches:

* constraint checking
* pruning
* board recursion
* diagonal logic
* state tracking

This is a REAL backtracking interview problem.

---

# Problem

Place `N` queens on an `N × N` chessboard so that:

* same row ❌
* same column ❌
* same diagonal ❌

---

# Example - 4 Queens

Valid solution:

```text id="a0p5h7"
. Q . .
. . . Q
Q . . .
. . Q .
```

Queens attack:

* horizontally
* vertically
* diagonally

---

# Important Observation

We place:

* ONE queen per row

So:

* rows automatically become unique

We only need to track:

* columns
* diagonals

---

# Board Representation

```python id="o1a4k8"
board = [["."] * n for _ in range(n)]
```

Example:

```text id="q5rq6h"
. . . .
. . . .
. . . .
. . . .
```

---

# Core Backtracking Idea

For each row:

* try every column
* place queen if valid
* recurse to next row
* remove queen (backtrack)

---

# Tracking Attacks

We use sets:

```python id="kkn5o6"
col = set()
posDiag = set()
negDiag = set()
```

---

# Columns

If column already used:

```python id="r2uhqs"
if c in col:
```

Cannot place queen.

---

# Diagonal Logic

This is the MOST important part.

For a cell:

```python id="9ltjlv"
(row, col)
```

---

# Positive Diagonal

Cells with SAME:

r + c

belong to same positive diagonal.

Example:

```text id="4gcn7u"
(0,1)
(1,2)
(2,3)
```

All:

```text id="rllf7o"
r + c = 3
```

---

# Negative Diagonal

Cells with SAME:

r - c

belong to same negative diagonal.

Example:

```text id="1x15v0"
(0,2)
(1,1)
(2,0)
```

All:

```text id="hr0r7t"
r - c = -2
```

---

# Full Solution

```python id="3qowkw"
class Solution:

    def solveNQueens(self, n):

        col = set()
        posDiag = set()
        negDiag = set()

        board = [["."] * n for _ in range(n)]

        result = []

        def backtrack(r):

            # solution found
            if r == n:

                copy = ["".join(row) for row in board]

                result.append(copy)

                return

            for c in range(n):

                # invalid position
                if (
                    c in col or
                    (r + c) in posDiag or
                    (r - c) in negDiag
                ):
                    continue

                # place queen
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                board[r][c] = "Q"

                # recurse
                backtrack(r + 1)

                # BACKTRACK
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

                board[r][c] = "."

        backtrack(0)

        return result
```

---

# Step-by-Step Dry Run

## Start

```text id="e8mt7m"
Row 0
```

Try:

```text id="q2r4t4"
(0,0)
```

Place queen.

---

# Move to Row 1

Cannot place:

* same column
* same diagonals

Try valid column.

---

# Continue

If no valid column exists:

* BACKTRACK
* remove previous queen
* try next possibility

---

# Why Backtracking Works

Example:

```python id="wv4um8"
board[r][c] = "Q"
```

After recursion:

```python id="04z8qq"
board[r][c] = "."
```

We restore previous state.

---

# Visualization

Example board:

```text id="9n4g6o"
Q . . .
. . Q .
. . . .
. . . .
```

If recursion fails:

* remove last queen
* try another column

---

# Recursive Tree

```text id="2tqv3n"
Row 0
├── Col 0
│   ├── Col 2
│   └── Col 3
├── Col 1
├── Col 2
└── Col 3
```

Each node:

* partial board state

---

# Complexity

N-Queens is expensive.

Worst case roughly:

O(N!)

Because:

* branching shrinks each row
* many invalid states

---

# Why Sets Are Important

Checking attacks becomes:

```text id="0r6vlg"
O(1)
```

Without sets:

* board scanning becomes slow

---

# Key Backtracking Pattern

```python id="4d2a8k"
place queen

recurse

remove queen
```

This pattern appears everywhere.

---

# Common Mistakes

## 1. Forgetting Backtrack

Wrong:

```python id="g0k7cl"
board[r][c] = "Q"
backtrack()
```

Correct:

```python id="rb6dmu"
board[r][c] = "Q"

backtrack()

board[r][c] = "."
```

---

## 2. Wrong Diagonal Formula

Positive:

r+c

Negative:

r-c

---

## 3. Forgetting Copy

Wrong:

```python id="5xq2mx"
result.append(board)
```

Correct:

```python id="j4mjlwm"
copy = ["".join(row) for row in board]
```

---

# Optimization Insight

We prune aggressively.

Invalid states are removed EARLY.

That’s why backtracking works efficiently.

---

# Important Learning Outcome

N-Queens teaches:

* recursive board search
* pruning
* state tracking
* constraints
* DFS + backtracking

---

# Related Problems

## Medium

* Word Search
* Palindrome Partitioning

## Hard

* Sudoku Solver

---

# Homework

## Easy

1. Solve N-Queens for `n = 1`
2. Solve for `n = 4`

---

## Medium

1. Count number of solutions
2. Print board visually

---

# Main Goal Today

You should now understand:

* board backtracking
* diagonal tracking
* pruning invalid states
* recursive constraint solving
* how advanced backtracking problems work
