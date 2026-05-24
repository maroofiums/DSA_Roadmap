# Day 3 - Permutations

Today you learn another MAJOR backtracking pattern.

Subsets:

* choose OR skip

Permutations:

* choose ONE unused element each step

This changes the recursion tree completely.

---

# Problem

Input:

```python 
[1,2,3]
```

Output:

```text 
[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]
```

---

# Key Difference From Subsets

## Subsets

Order DOES NOT matter.

```text 
[1,2] == [2,1]
```

---

## Permutations

Order DOES matter.

```text 
[1,2] != [2,1]
```

That’s why permutations are harder.

---

# Core Idea

At every step:

* pick ONE unused number
* recurse deeper
* backtrack

---

# Decision Tree

For `[1,2,3]`

```text 
                    []
            /         |         \
           1          2          3
        /    \      /   \      /   \
       2      3    1     3    1     2
      /        \   ...         ...
```

Each level:

* choose another unused number

---

# Main Pattern

```python 
for choice in choices:

    choose

    recurse

    undo
```

This is the STANDARD permutation template.

---

# Full Solution

```python 
class Solution:

    def permute(self, nums):

        result = []

        def backtrack(path):

            # base case
            if len(path) == len(nums):
                result.append(path[:])
                return

            for n in nums:

                # skip used numbers
                if n in path:
                    continue

                # choose
                path.append(n)

                # recurse
                backtrack(path)

                # undo choice
                path.pop()

        backtrack([])

        return result
```

---

# Dry Run

Input:

```python 
[1,2]
```

---

# Start

```python 
path = []
```

Loop:

```python 
choose 1
```

Now:

```python 
path = [1]
```

Recursive call.

---

# Next Level

Available:

* 2

Choose 2:

```python
path = [1,2]
```

Base case reached.

Add:

```python
[1,2]
```

---

# Backtrack

```python
path.pop()
```

Now:

```python
path = [1]
```

No more choices.

Backtrack again.

---

# Root Level

Choose 2:

```python
path = [2]
```

Then choose 1.

Result:

```text 
[2,1]
```

---

# Final Output

```text 
[1,2]
[2,1]
```

---

# Why `if n in path` ?

This prevents reuse.

Without it:

```text 
[1,1,1]
[2,2,2]
```

would happen.

We only want unused numbers.

---

# Backtracking Visualization

```python 
path.append(1)
```

State:

```text 
[1]
```

After recursion:

```python 
path.pop()
```

State restored:

```text 
[]
```

This restoration is BACKTRACKING.

---

# Complexity

For permutations:

Choices shrink each level.

Count:

n!

For 3:

```text 
3 × 2 × 1 = 6
```

Time Complexity:

```text 
O(n!)
```

Very expensive for large `n`.

---

# Recursion Tree

For `[1,2,3]`

```text 
                    []
           /          |          \
         [1]         [2]         [3]
        /   \       /   \       /   \
    [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]
```

Leaves = completed permutations.

---

# Important Difference

## Subsets

Depth:

n

Choices:

* take
* skip

---

## Permutations

Depth:

n

Choices:

* ALL remaining numbers

Much larger branching factor.

---

# Better Version Using `used`

Instead of:

```python 
if n in path
```

Use boolean array.

More efficient.

---

# Optimized Solution

```python 
class Solution:

    def permute(self, nums):

        result = []

        used = [False] * len(nums)

        def backtrack(path):

            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                used[i] = True

                path.append(nums[i])

                backtrack(path)

                path.pop()

                used[i] = False

        backtrack([])

        return result
```

---

# Why Better?

This:

```python 
if n in path
```

takes:

```text 
O(n)
```

every check.

Boolean array:

```python 
used[i]
```

takes:

```text 
O(1)
```

---

# Permutations II (Duplicates)

Input:

```python 
[1,1,2]
```

Need unique permutations only.

---

# Main Idea

1. sort array
2. skip duplicates carefully

---

# Solution

```python 
class Solution:

    def permuteUnique(self, nums):

        nums.sort()

        result = []

        used = [False] * len(nums)

        def backtrack(path):

            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True

                path.append(nums[i])

                backtrack(path)

                path.pop()

                used[i] = False

        backtrack([])

        return result
```

---

# Common Mistakes

## 1. Forgetting Backtrack

Wrong:

```python 
path.append(x)
dfs()
```

Correct:

```python 
path.append(x)
dfs()
path.pop()
```

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

## 3. Reusing Numbers

Need:

* `used`
* or `if n in path`

---

# Pattern Recognition

Permutation problems usually contain:

* “arrangements”
* “order matters”
* “all possible orders”

Keywords:

* rearrange
* ordering
* unique arrangements

---

# Homework

## Easy

1. Permutations of `[1,2]`
2. Permutations of `[1,2,3]`

---

## Medium

1. Permutations II
2. Letter Tile Possibilities

---

# Main Goal Today

You should now understand:

* permutation recursion trees
* choosing unused elements
* backtracking restoration
* factorial growth
* difference between subsets vs permutations
