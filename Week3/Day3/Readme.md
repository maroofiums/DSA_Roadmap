# DAY 3 - Sliding Window (Core)

## Goal

Make sliding window **automatic and natural**.

You should stop thinking “step-by-step” and start thinking:

> “I maintain a valid window at all times”

---

# Core Concept

A window is just:

> A continuous range [left → right]

You control it using two actions:

* Expand (right pointer)
* Shrink (left pointer)

---

# Pattern

> Subarray/substring + constraint → Sliding Window

---

# The Golden Rule

## ALWAYS maintain this:

> Window is valid at every step

If it becomes invalid → fix it immediately.

---

# Step-by-Step Mental Flow

## 1. Expand

* Move right pointer
* Add new element into window state

---

## 2. Check validity

Ask:

> Does this window still satisfy condition?

Example condition:

* no duplicates
* sum ≤ limit

---

## 3. Shrink (if needed)

If invalid:

* move left pointer
* remove elements
* keep shrinking until valid again

---

## 4. Update answer

At every valid window:

* update max/min result

---

# Problem 1 - Longest Substring Without Repeating Characters

## Goal

Find longest substring with:

> No repeated characters

---

## Core Idea

* Expand window
* If duplicate appears → shrink left until valid

---

## WHY this works

Because:

> Once duplicate exists, current window is useless until fixed

But instead of restarting:

> You adjust it

---

## Key Insight

You never reset.

You only:

> repair the window

---

# Problem 2 - Maximum Average Subarray

## Goal

Find subarray of size k with maximum average

---

## Core Idea

This is simpler sliding window:

* Window size is fixed (k)
* Move window forward one step at a time
* Maintain running sum

---

## Key Insight

Fixed window = no shrinking needed

So:

> Only expand + slide forward

---

# TWO TYPES OF SLIDING WINDOW

## 1. Variable Window

Used when:

* condition changes dynamically
* duplicates, constraints, limits

Example:

* Longest substring

---

## 2. Fixed Window

Used when:

* size is fixed
* we just slide window

Example:

* max average subarray

---

# BIG INSIGHT OF DAY 3

You are learning:

> How to maintain a dynamic system without recomputing everything

Instead of:

* recalculating from scratch

You:

* update incrementally

---

# Common Mistakes

Do NOT:

* Restart window from scratch
* Forget to remove left element when shrinking
* Move pointers without checking condition

---

# Mental Model

Think like this:

* I extend my current solution
* If it breaks → I fix it locally
* I never throw it away

---

# When to Use Sliding Window

Use it when:

* Problem is about subarrays or substrings
* You need “longest”, “shortest”, or “optimal range”
* Brute force is O(n²)

---

# Task (VERY IMPORTANT)

For each problem:

### 1. Explain:

* What is window condition?
* When do I shrink?

### 2. Dry run:

* "abcabcbb"
* "bbbbb"
* "pwwkew"

---

# Final Takeaway

Sliding window is:

> Not about moving pointers
> It is about maintaining a valid state efficiently

---