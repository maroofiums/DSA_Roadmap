# Week 1 — Day 3: String Basics

## Goal

Understand how to **work with strings like arrays of characters** and solve common interview problems involving traversal, comparison, and character counting.

Daily target: **2–3 problems**

---

# 1. String Traversal

Strings can be iterated just like arrays.

### Example

```python
s = "hello"

for char in s:
    print(char)
```

Output

```
h
e
l
l
o
```

You can also access characters by index.

```python
for i in range(len(s)):
    print(s[i])
```

### Key Idea

Strings are **immutable**, meaning you cannot modify characters directly.

Example (invalid):

```python
s[0] = "H"
```

Instead, you create a **new string**.

---

# 2. Palindrome Check

A palindrome reads the **same forward and backward**.

Examples

```
racecar
madam
level
```

### Two Pointer Approach

Use one pointer at the **start** and one at the **end**.

```python
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True
```

Example

```
Input: "racecar"
Output: True
```

### Pattern Learned

**Two pointers moving toward the center**

---

# 3. Reversing a String

### Method 1 — Python Built-in

```python
s = "hello"
print(s[::-1])
```

Output

```
olleh
```

### Method 2 — Two Pointer Swap

```python
def reverse_string(s):
    s = list(s)
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1

    return "".join(s)
```

---

# Practice Problems

## 1. Valid Palindrome

Check if a string is a palindrome **ignoring spaces and punctuation**.

Example

```
Input: "A man a plan a canal Panama"
Output: True
```

Concepts used

* String traversal
* Two pointers
* Character filtering

---

## 2. Reverse String

Reverse characters in a string.

Example

```
Input: "hello"
Output: "olleh"
```

Concepts used

* Two pointers
* Swapping

---

## 3. First Unique Character in String

Find the **first character that appears only once**.

Example

```
Input: "leetcode"
Output: 0
```

Approach

1. Count character frequencies
2. Traverse again to find first unique

Example solution

```python
def first_unique_char(s):
    freq = {}

    for c in s:
        freq[c] = freq.get(c, 0) + 1

    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i

    return -1
```

---

# Pattern Summary

Today you learned **three important patterns**

### 1. String Traversal

Iterate through characters.

### 2. Two Pointer Pattern

Used in palindrome and reverse problems.

### 3. Frequency Counting

Use a dictionary to count characters.

---

# Daily Target

You should be able to:

* Traverse a string confidently
* Implement a palindrome check
* Reverse a string using two pointers
* Count characters using a hashmap

If you can solve the **three problems without looking at solutions**, Day 3 is complete.

---