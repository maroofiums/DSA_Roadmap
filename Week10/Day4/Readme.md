# **Day 4: Combination Problems**

# Backtracking - Combination Problems

This section covers combination-based backtracking problems.

You will learn:

* subsets
* combinations
* permutations
* repeated choices
* pruning
* recursive decision trees

---

# Concepts Learned

## 1. Subsets

For every element:

* take it
* skip it

Example:

```python
[1,2,3]
```

Subsets:

```text
[]
[1]
[2]
[1,2]
...
```

---

## 2. Combinations

Choose `k` elements from `n`.

Example:

```python
n = 4
k = 2
```

Output:

```text
[1,2]
[1,3]
[1,4]
[2,3]
[2,4]
[3,4]
```

---

## 3. Permutations

Arrange elements in all possible orders.

Example:

```python
[1,2,3]
```

Output:

```text
[1,2,3]
[1,3,2]
[2,1,3]
...
```

---

# Subsets Implementation

```python
from typing import List

def subsets(nums: List[int]) -> List[List[int]]:

    res = []
    sol = []

    def backtrack(i=0):

        if i >= len(nums):
            res.append(sol[:])
            return

        # skip
        backtrack(i + 1)

        # choose
        sol.append(nums[i])

        backtrack(i + 1)

        # backtrack
        sol.pop()

    backtrack()

    return res


nums = [1,2,3]

print(subsets(nums))
```

---

# How It Works

At every index:

* skip current number
* OR choose current number

This creates a binary recursion tree.

Decision Tree:

```text
                 []
             /        \
         skip1       take1
           []          [1]
```

---

# Time Complexity

For every number:

* 2 choices

Total complexity:

O(2^n)

---

# Combinations Implementation

```python
from typing import List

def combine(n: int, k: int) -> List[List[int]]:

    sol = []
    ans = []

    def backtrack(x):

        if len(sol) == k:
            ans.append(sol[:])
            return

        left = x
        still_need = k - len(sol)

        # skip
        if left > still_need:
            backtrack(x - 1)

        # choose
        sol.append(x)

        backtrack(x - 1)

        # backtrack
        sol.pop()

    backtrack(n)

    return ans


n = 4
k = 2

print(combine(n, k))
```

---

# Important Idea - Pruning

This condition:

```python
if left > still_need:
```

avoids unnecessary recursive calls.

This is called PRUNING.

Pruning improves performance by cutting impossible paths early.

---

# Combination Decision Tree

```text
                  []
               /      \
             skip      take4
              []         [4]
```

---

# Permutations Implementation

```python
from typing import List

def permute(nums: List[int]) -> List[List[int]]:

    sol = []
    res = []

    def backtrack():

        if len(nums) == len(sol):
            res.append(sol[:])
            return

        for x in nums:

            if x not in sol:

                # choose
                sol.append(x)

                backtrack()

                # backtrack
                sol.pop()

    backtrack()

    return res


nums = [1,2,3]

print(permute(nums))
```

---

# How Permutations Work

At every step:

* choose ONE unused number

Unlike subsets:

* order matters

Example:

```text
[1,2] != [2,1]
```

---

# Permutation Decision Tree

```text
                    []
            /         |         \
           1          2          3
         /   \      /   \      /   \
```

---

# Time Complexity

Permutations grow factorially.

Total permutations:

n!

Complexity:

```text
O(n!)
```

---

# Core Backtracking Pattern

All three problems follow the same pattern:

```python
choose

recurse

undo choice
```

Example:

```python
sol.append(x)

backtrack()

sol.pop()
```

The `pop()` operation restores the previous state.

This is called BACKTRACKING.

---

# Key Differences

| Problem      | Order Matters | Reuse Allowed |
| ------------ | ------------- | ------------- |
| Subsets      | No            | No            |
| Combinations | No            | No            |
| Permutations | Yes           | No            |

---

# Concepts Practiced

* recursion
* decision trees
* DFS
* backtracking
* pruning
* state restoration
* recursive branching

---

# Problems Practiced

* LeetCode 78 - Subsets
* LeetCode 77 - Combinations
* LeetCode 46 - Permutations

---

# Main Learning Outcome

After Day 4 you should understand:

* how recursive decision trees work
* how backtracking restores state
* difference between subsets/combinations/permutations
* pruning optimization
* recursive search patterns
