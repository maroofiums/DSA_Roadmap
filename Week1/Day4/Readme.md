# Week 1 — Day 4: Hashing with Strings

## Goal

Learn how to use **HashMaps (Python dictionaries)** to solve string problems efficiently.

Many interview problems become **O(n)** instead of **O(n²)** when you use hashing.

Daily target: **3 problems**

---

# 1. Frequency Counting

The most common hashing pattern.

Idea:

* Count how many times each character appears.

Example:

```python
s = "banana"

freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1

print(freq)
```

Output

```
{'b': 1, 'a': 3, 'n': 2}
```

### Why This Is Powerful

Without hashing you might need nested loops.

Time complexity comparison:

Brute force
O(n²)

HashMap solution
O(n)

---

# 2. HashMap Pattern Template

Most string hashing problems follow this pattern.

```python
freq = {}

for char in string:
    freq[char] = freq.get(char, 0) + 1
```

This stores **frequency of each character**.

---

# Practice Problem 1: Valid Anagram

Two strings are anagrams if they contain the **same characters with the same frequency**.

Example

```
Input: s = "anagram"
t = "nagaram"

Output: True
```

### Approach

1. Count characters in first string
2. Count characters in second string
3. Compare dictionaries

### Solution

```python
def is_anagram(s, t):

    if len(s) != len(t):
        return False

    freq = {}

    for c in s:
        freq[c] = freq.get(c, 0) + 1

    for c in t:
        if c not in freq:
            return False
        freq[c] -= 1

    return True
```

Time complexity
O(n)

---

# Practice Problem 2: Group Anagrams

Group words that are anagrams of each other.

Example

```
Input
["eat","tea","tan","ate","nat","bat"]

Output
[
["eat","tea","ate"],
["tan","nat"],
["bat"]
]
```

### Key Idea

Sort characters in each word.

Words with the **same sorted form** belong to the same group.

Example

```
eat -> aet
tea -> aet
ate -> aet
```

### Solution

```python
from collections import defaultdict

def group_anagrams(strs):

    groups = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)

    return list(groups.values())
```

Time complexity
O(n * k log k)

k = word length

---

# Practice Problem 3: Longest Palindrome

Find the **length of the longest palindrome** that can be built using characters.

Example

```
Input
"abccccdd"

Output
7
```

Example palindrome:

```
dccaccd
```

### Idea

A palindrome can use:

* All **even frequency characters**
* Only **one odd frequency character in the center**

### Solution

```python
def longest_palindrome(s):

    freq = {}

    for c in s:
        freq[c] = freq.get(c, 0) + 1

    length = 0
    odd_found = False

    for count in freq.values():

        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            odd_found = True

    if odd_found:
        length += 1

    return length
```

---

# Patterns Learned Today

### 1. Frequency Counting

Count characters using a dictionary.

### 2. HashMap Lookup

Check existence quickly.

```
if char in hashmap
```

### 3. Grouping Pattern

Use **sorted strings or character counts as keys**.

---

# Daily Success Criteria

You should be able to:

* Use a dictionary to count characters
* Solve **Valid Anagram** in under **10 minutes**
* Understand why **Group Anagrams uses sorting**
* Identify when **hashing replaces nested loops**

---
