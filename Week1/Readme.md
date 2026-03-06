# Week 1 — Arrays & Strings (DSA Roadmap)

## Goal

Build strong fundamentals in arrays and strings.
Learn **two core patterns** used heavily in interviews:

* Two Pointers
* Sliding Window

Daily time target: **2–4 hours**

Target problems this week: **10–12**

---

# Day 1 — Array Basics

### Concepts

* Array traversal
* Finding max / min
* Prefix sum idea
* Brute force vs optimized solution

### Practice Problems

1. Two Sum
2. Maximum Subarray (Kadane preview)
3. Move Zeroes

### What to Learn

* How to iterate arrays efficiently
* How to track values while looping

### Notes

Important idea:

* **Use variables to track state while iterating**

Example pattern:

```
for num in nums:
    update_state()
```

---

# Day 2 — Array Patterns

### Concepts

* Prefix Sum
* Running Sum
* Product array concept

### Practice Problems

1. Running Sum of Array
2. Product of Array Except Self
3. Best Time to Buy and Sell Stock

### What to Learn

* Avoid nested loops when possible
* Precompute values using prefix logic

---

# Day 3 — String Basics

### Concepts

* String traversal
* Palindrome check
* Reversing strings

### Practice Problems

1. Valid Palindrome
2. Reverse String
3. First Unique Character in String

### Key Idea

Strings behave like arrays of characters.

---

# Day 4 — Hashing with Strings

### Concepts

* Frequency counting
* HashMap / dictionary usage

### Practice Problems

1. Valid Anagram
2. Group Anagrams
3. Longest Palindrome

### Pattern

```
freq = {}

for char in string:
    freq[char] += 1
```

---

# Day 5 — Two Pointer Pattern

### Concept

Two pointers move from **different sides** of an array.

Used when:

* Array is sorted
* Need pairs
* Need optimized scanning

### Practice Problems

1. Two Sum II (Sorted Array)
2. Container With Most Water
3. 3Sum

### Template

```
left = 0
right = len(arr) - 1

while left < right:
    if condition:
        left += 1
    else:
        right -= 1
```

---

# Day 6 — Sliding Window Pattern

### Concept

Used for **subarray / substring problems**

Instead of checking all subarrays:
We **expand and shrink window**.

### Practice Problems

1. Longest Substring Without Repeating Characters
2. Minimum Size Subarray Sum
3. Longest Repeating Character Replacement

### Template

```
left = 0

for right in range(len(nums)):
    expand_window()

    while window_invalid:
        shrink_window()
        left += 1
```

---

# Day 7 — Weekly Test

### Solve without help

1. Two Sum
2. Valid Anagram
3. Longest Substring Without Repeating Characters
4. Container With Most Water
5. Minimum Size Subarray Sum

### Rules

* Max time per problem: **30 minutes**
* Write explanation before coding
* Review mistakes

---

# Week 1 Success Criteria

You should be able to:

✓ Identify **array problems quickly**
✓ Recognize **two pointer pattern**
✓ Recognize **sliding window pattern**
✓ Solve **easy problems in <15 minutes**

---

# End of Week Reflection

Ask yourself:

1. Can I detect sliding window problems instantly?
2. Can I implement two pointers without looking?
3. Do I understand why brute force is slow?

If yes → **Week 1 complete.**
