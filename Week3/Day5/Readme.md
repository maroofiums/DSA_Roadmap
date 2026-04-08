# DAY 5 — Advanced Sliding Window

## Goal

Handle **interview-level sliding window problems** where you must:

> Find a window that is valid AND optimal (usually minimum or maximum)

---

# Core Upgrade from Day 4

Earlier:

* Just keep window valid

Now:

* First make it **valid**
* Then make it **optimal (smallest or largest)**

---

# Pattern

> Expand → satisfy condition
> Shrink → optimize answer

---

# Mental Model (VERY IMPORTANT)

Think in two phases:

## Phase 1 — Expand (right pointer)

* Keep expanding until condition is satisfied
* Window becomes **valid**

---

## Phase 2 — Shrink (left pointer)

* Once valid, try to shrink
* Reduce size while keeping it valid
* Update best answer

---

# Problem 1 — Minimum Window Substring

## Goal

Find the **smallest substring** that contains all required characters

---

## Core Idea

You must track:

* Required characters (target)
* Current window characters

---

## What is “valid”?

A window is valid when:

> It contains all required characters with correct frequency

---

## Flow

### Expand:

* Add characters until all requirements are met

### Shrink:

* Try removing from left
* Stop shrinking when condition breaks

---

## Key Insight

You are not just finding a valid window.

You are finding:

> The smallest valid window

---

## Most Important Thinking

* Expand → achieve validity
* Shrink → improve answer

---

# Problem 2 — Longest Substring with At Most K Distinct Characters

## Goal

Find longest substring with ≤ k distinct characters

---

## Core Idea

Track:

* Number of distinct characters in window

---

## What is “valid”?

> distinct characters ≤ k

---

## Flow

### Expand:

* Add character
* Update distinct count

### Shrink:

* If distinct > k → shrink until valid

---

## Key Insight

Unlike minimum window:

* Here we maximize length
* So we shrink only when forced

---

# BIG DIFFERENCE BETWEEN BOTH PROBLEMS

| Problem            | Goal          | Shrinking Style         |
| ------------------ | ------------- | ----------------------- |
| Minimum Window     | minimize size | shrink aggressively     |
| At Most K Distinct | maximize size | shrink only when needed |

---

# MOST IMPORTANT RULE OF DAY 5

You must know:

> When to shrink aggressively vs when to shrink lazily

---

# Common Mistakes

Do NOT:

* Forget to update state when shrinking
* Stop shrinking too early (min window)
* Over-shrink (lose valid window)
* Confuse “valid” condition

---

# Pattern Recognition

If problem says:

* “smallest window” → aggressive shrinking
* “longest window” → controlled shrinking
* “contains all” → tracking requirement counts
* “at most k” → tracking distinct count

---

# Mental Checklist Before Solving

1. What is the condition for validity?
2. What state do I track? (freq, count, etc.)
3. When do I expand?
4. When do I shrink?
5. Am I minimizing or maximizing?

---

# Task (IMPORTANT)

For each problem:

## 1. Explain:

* What makes window valid?
* What breaks validity?

## 2. Identify:

* When do you shrink?
* Why are you shrinking?

## 3. Dry run:

* Minimum window → "ADOBECODEBANC"
* K distinct → "eceba", k=2

---

# Final Takeaway

You are now doing:

> Constraint satisfaction + optimization at the same time

This is core of many FAANG problems.

---
