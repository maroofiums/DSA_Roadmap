# Week 1 — Day 7: Weekly Test

## Goal

Test whether you actually **understand the patterns** from Week 1:

* Arrays
* Strings
* Hashing
* Two Pointers
* Sliding Window

You must **solve without help**.

Total problems: **5**

Time per problem: **30 minutes**

---

# Test Problems

## 1. Two Sum

**Pattern:** HashMap

### Idea

You want two numbers whose sum equals a target.

Instead of checking all pairs (O(n²)):

* While traversing the array, store numbers in a **HashMap**.
* For each number, check if its **complement (target − number)** already exists.

This allows solving the problem in **one pass**.

---

## 2. Valid Anagram

**Pattern:** Frequency Counting

### Idea

Two strings are anagrams if they contain:

* Same characters
* Same frequencies

Approach:

1. Count characters in the first string.
2. Reduce counts using the second string.
3. If all counts become zero → valid anagram.

---

## 3. Longest Substring Without Repeating Characters

**Pattern:** Sliding Window

### Idea

We want the **longest substring with unique characters**.

Approach:

1. Expand the window using the **right pointer**.
2. Track characters in a **set or hashmap**.
3. If a duplicate appears:

   * Move the **left pointer** until the duplicate is removed.
4. Track the **maximum window length**.

Key idea:
The window **always contains unique characters**.

---

## 4. Container With Most Water

**Pattern:** Two Pointers

### Idea

Two lines form a container.

Area =

height × width

Where:

* height = **minimum of two heights**
* width = **distance between indices**

Approach:

1. Start pointers at **both ends of the array**.
2. Calculate area.
3. Move the pointer with the **smaller height**.

Why?

Because the smaller height limits the area.

---

## 5. Minimum Size Subarray Sum

**Pattern:** Sliding Window

### Idea

Find the **smallest subarray whose sum ≥ target**.

Approach:

1. Expand the window by moving the **right pointer**.
2. Keep adding elements to the **current sum**.
3. Once sum ≥ target:

   * Try shrinking the window from the **left**.
4. Track the **minimum window length**.

---

# Test Rules

Follow these strictly.

### 1. Max Time

30 minutes per problem.

Total test time: **2.5 hours**

---

### 2. Write Approach First

Before coding write:

```
Pattern:
Idea:
Time Complexity:
Space Complexity:
```

Example:

```
Pattern: Sliding Window
Idea: Expand right pointer, shrink left pointer when condition breaks.
Time Complexity: O(n)
Space Complexity: O(1)
```

---

### 3. Review Mistakes

After solving:

Ask yourself:

* Did I recognize the **pattern quickly**?
* Did I waste time on brute force?
* Could I explain the solution clearly?

---

# Week 1 Completion Checklist

You should now recognize:

Array problems
Hashing problems
Two pointer problems
Sliding window problems

If you can solve **3–4 out of 5 problems without help**, Week 1 is successful.

