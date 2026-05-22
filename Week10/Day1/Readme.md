# Day 1 - Recursion Foundations

Recursion = a function calling itself to solve smaller versions of the same problem.

The MOST important thing:

* Every recursive function needs a stopping condition.
* Otherwise → infinite recursion.

---

# 1. Base Case

Base case = stopping condition.

Example:

```python
def countdown(n):

    if n == 0:   # base case
        return

    print(n)

    countdown(n - 1)
```

Call:

```python
countdown(3)
```

Execution:

```text
countdown(3)
countdown(2)
countdown(1)
countdown(0) -> stop
```

Output:

```text
3
2
1
```

---

# 2. Recursive Call

This is the line where function calls itself.

```python
countdown(n - 1)
```

You usually:

1. solve smaller problem
2. move toward base case

---

# 3. Call Stack

Python stores function calls in memory using a stack.

Example:

```python
def func(n):

    if n == 0:
        return

    print("Start", n)

    func(n - 1)

    print("End", n)

func(3)
```

---

## Visualization

Calls go IN:

```text
func(3)
func(2)
func(1)
func(0)
```

Then return OUT:

```text
End 1
End 2
End 3
```

---

## Output

```text
Start 3
Start 2
Start 1
End 1
End 2
End 3
```

---

# 4. Decision Tree Thinking

Backtracking starts with recursion trees.

Example:

Binary strings of length 2.

Choices:

* add 0
* add 1

Tree:

```text
              ""
           /      \
         "0"      "1"
        /   \     /   \
     "00" "01" "10" "11"
```

Every recursive call = a new branch.

---

# Problem 1 - Factorial

Factorial:

```text
5! = 5 × 4 × 3 × 2 × 1
```

Recursive idea:

```text
5! = 5 × 4!
```

---

## Recursive Formula

n! = n \times (n-1)!

Base case:

```text
0! = 1
```

---

## Code

```python
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```text
120
```

---

## Call Stack

```text
factorial(5)
5 * factorial(4)

5 * 4 * factorial(3)

5 * 4 * 3 * factorial(2)

...
```

---

# Problem 2 - Fibonacci

Sequence:

```text
0 1 1 2 3 5 8
```

Formula:

F(n)=F(n-1)+F(n-2)

---

## Code

```python
def fib(n):

    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

print(fib(6))
```

Output:

```text
8
```

---

## Decision Tree

```text
fib(4)
├── fib(3)
│   ├── fib(2)
│   └── fib(1)
└── fib(2)
```

This creates MANY repeated calls.

That’s why recursive Fibonacci is slow.

---

# Problem 3 - Sum of Array

Input:

```python
[1,2,3,4]
```

Goal:

```text
10
```

---

## Idea

```text
sum([1,2,3,4])
=
1 + sum([2,3,4])
```

---

## Code

```python
def array_sum(nums, i=0):

    if i == len(nums):
        return 0

    return nums[i] + array_sum(nums, i + 1)

print(array_sum([1,2,3,4]))
```

---

# Problem 4 - Generate Binary Strings

Code:

```python
def generate(n, path):

    if len(path) == n:
        print(path)
        return

    generate(n, path + "0")
    generate(n, path + "1")

generate(3, "")
```

---

# Understanding the Tree

```text
                    ""
               /          \
            "0"            "1"
          /    \         /    \
       "00"   "01"    "10"   "11"
```

Each level:

* choose 0
* choose 1

---

# Important Concepts

## Recursion Depth

Depth = maximum stack height.

For:

```python
factorial(5)
```

Depth = 5

---

## Branching

How many recursive calls happen per function?

### Factorial

```python
factorial(n - 1)
```

Branching factor = 1

---

### Fibonacci

```python
fib(n - 1)
fib(n - 2)
```

Branching factor = 2

---

# Common Mistakes

## 1. Missing Base Case

```python
def bad(n):
    return bad(n - 1)
```

Infinite recursion.

---

## 2. Not Moving Toward Base Case

Wrong:

```python
bad(n)
```

Correct:

```python
bad(n - 1)
```

---

## 3. Modifying Shared State Incorrectly

Important later in backtracking.

---

# Time Complexity Intuition

## Factorial

One recursive call each time.

```text
O(n)
```

---

## Fibonacci

Two recursive calls each time.

```text
O(2^n)
```

Very expensive.

---

# Homework

## Easy

1. Reverse string using recursion
2. Print numbers 1 → n
3. Print numbers n → 1

---

## Medium

1. Generate ternary strings (`0,1,2`)
2. Generate all strings of length n using `a,b`

---

# Main Goal Today

You should now understand:

* how recursion works
* how functions return
* how stack grows/shrinks
* how recursive trees form
* why backtracking uses recursion heavily
