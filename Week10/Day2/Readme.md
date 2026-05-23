# Day 2 - Subsets

Today you learn your FIRST real backtracking pattern.

This problem teaches:

* recursion tree
* choose / skip decisions
* backtracking
* copying arrays
* exponential thinking

---

# Problem

Given:

```python
[1,2,3]
```

Generate ALL subsets:

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

# Important Observation

For EVERY number:

You have TWO choices:

1. take it
2. skip it

That creates a binary decision tree.

---

# Decision Tree

```text
                         []
                    /          \
                 take1        skip1
                 [1]            []
               /    \         /    \
          take2   skip2   take2   skip2
          [1,2]    [1]      [2]     []
```

Each level = one index.

---

# Core Backtracking Pattern

```python
choose
recurse
undo choice
```

In subsets:

```python
subset.append(nums[i])   # choose

dfs(i + 1)               # recurse

subset.pop()             # undo
```

That `pop()` is BACKTRACKING.

---

# Full Solution

```python
class Solution:

    def subsets(self, nums):

        result = []
        subset = []

        def dfs(i):

            # base case
            if i >= len(nums):
                result.append(subset[:])
                return

            # TAKE
            subset.append(nums[i])

            dfs(i + 1)

            # BACKTRACK
            subset.pop()

            # SKIP
            dfs(i + 1)

        dfs(0)

        return result
```

---

# Dry Run

Input:

```python
nums = [1,2]
```

---

# Start

```python
dfs(0)
subset = []
```

---

# Take 1

```python
subset = [1]
dfs(1)
```

---

# Take 2

```python
subset = [1,2]
dfs(2)
```

Base case:

```python
result.append([1,2])
```

---

# Backtrack

```python
subset.pop()
subset = [1]
```

Now skip 2:

```python
dfs(2)
```

Add:

```python
[1]
```

---

# Backtrack Again

Return to root:

```python
subset = []
```

Now skip 1.

---

# Final Output

```text
[1,2]
[1]
[2]
[]
```

Order may differ.

---

# Why `subset[:]` ?

VERY IMPORTANT.

Wrong:

```python
result.append(subset)
```

Correct:

```python
result.append(subset[:])
```

Because:

* `subset` changes later
* Python lists are mutable

You need a COPY.

---

# Visualization of Backtracking

Example:

```python
subset.append(1)
```

State:

```text
[1]
```

After recursion:

```python
subset.pop()
```

State becomes:

```text
[]
```

We “undo” the previous choice.

That’s why it’s called BACKTRACKING.

---

# Complexity

For every number:

* take
* skip

So total subsets:

2^n

Time Complexity:

```text
O(2^n)
```

Space Complexity:

```text
O(n)
```

(recursion depth)

---

# Recursive Tree for [1,2,3]

```text
                           []
                    /                \
                 [1]                 []
               /     \             /    \
          [1,2]      [1]       [2]      []
          /   \      /  \      /  \      / \
 [1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] []
```

Leaf nodes = completed subsets.

---

# Pattern Recognition

Subsets problems usually involve:

* include/exclude
* binary decisions
* power set generation

Keywords:

* “all subsets”
* “all combinations”
* “pick or not pick”

---

# Alternative Version (Cleaner)

Another common style:

```python
class Solution:

    def subsets(self, nums):

        result = []

        def backtrack(start, path):

            result.append(path[:])

            for i in range(start, len(nums)):

                path.append(nums[i])

                backtrack(i + 1, path)

                path.pop()

        backtrack(0, [])

        return result
```

This version is VERY important for:

* combinations
* combination sum
* subsets II

---

# Compare Both Approaches

## Approach 1 - Take/Skip

```python
take
skip
```

Good for:

* understanding recursion
* beginners

---

## Approach 2 - Loop Based

```python
for i in range(...)
```

Good for:

* advanced backtracking
* combinations
* interview style

---

# Subsets II (Duplicates)

Input:

```python
[1,2,2]
```

Need unique subsets only.

Main idea:

* sort array
* skip duplicates

---

## Solution

```python
class Solution:

    def subsetsWithDup(self, nums):

        nums.sort()

        result = []

        def backtrack(start, path):

            result.append(path[:])

            for i in range(start, len(nums)):

                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])

                backtrack(i + 1, path)

                path.pop()

        backtrack(0, [])

        return result
```

---

# Important Backtracking Rules

## Rule 1 - Choose

```python
path.append(x)
```

---

## Rule 2 - Recurse

```python
dfs(...)
```

---

## Rule 3 - Undo Choice

```python
path.pop()
```

---

# Common Mistakes

## 1. Forgetting `pop()`

This breaks the state.

---

## 2. Forgetting Copy

Wrong:

```python
result.append(path)
```

Correct:

```python
result.append(path[:])
```

---

## 3. Wrong Base Case

```python
if i == len(nums):
```

or

```python
if i >= len(nums):
```

---

# Homework

## Easy

1. Generate subsets of `[1,2]`
2. Generate subsets of `[1,2,3,4]`

---

## Medium

1. Subsets II
2. Letter combinations of phone number

---

# Main Goal Today

You should now understand:

* binary recursion trees
* choose/skip pattern
* why backtracking needs undo
* how subsets are generated
* exponential recursion structure
