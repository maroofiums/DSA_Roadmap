# DAY 4 - Sliding Window (Variable Conditions)

## Goal

Learn how to handle **changing constraints inside a window**.

This is where sliding window becomes **interview-level**.

---

# Core Concept

Now the window is NOT just “valid or invalid”.

Instead:

> Window is valid only if it satisfies a condition that depends on counts or values.

So you must track:

* frequencies
* sums
* counts
* products

---

# Pattern

> Sliding Window + State Tracking (Hashing / Math)

---

# Key Upgrade from Day 3

### Before:

* Simple condition (duplicate / fixed size)

### Now:

* Condition depends on **distribution inside window**

---

# 1. Problem - Longest Repeating Character Replacement

## Goal

Find longest substring where you can replace ≤ k characters to make all same.

---

## Core Idea

Inside window:

* Track frequency of each character
* Find most frequent character count

---

## Key Insight

You don’t need to make window perfect immediately.

You check:

> “How many characters are NOT the majority?”

---

## Valid Condition

A window is valid if:

> window size - max frequency ≤ k

---

## When to shrink?

Shrink when:

> replacements needed > k

---

## Why this works

Because:

* We try to maximize a “dominant character window”
* Everything else can be replaced

---

# 2. Problem - Subarray Product Less Than K

## Goal

Count subarrays where product < k

---

## Core Idea

* Expand window
* Multiply values into product
* Shrink if product becomes too large

---

## Key Insight

Unlike sum, product grows fast:

> So shrinking is mandatory when condition breaks

---

## Valid Condition

Window is valid if:

> product < k

---

## When to shrink?

While:

> product ≥ k

---

## Why this works

Because:

* Removing left element reduces product
* Restores validity

---

# BIG IDEA OF DAY 4

Now window validity depends on:

| Type              | What you track |
| ----------------- | -------------- |
| Character problem | frequency map  |
| Numeric problem   | sum/product    |

---

# WHEN TO SHRINK (MOST IMPORTANT RULE)

You shrink when:

> The window violates the condition

And you keep shrinking until:

> It becomes valid again

---

# Mental Model

Think like this:

* I expand to explore possibilities
* I shrink to fix violations
* I always keep window as close to optimal as possible

---

# COMMON MISTAKES

Do NOT:

* Forget to update frequency when shrinking
* Shrink only once (sometimes you must shrink multiple times)
* Confuse “invalid” with “almost valid”

---

# WHY THIS IS HARDER

Because now:

* You are not just tracking structure
* You are tracking **state inside window**

---

# WHEN TO USE THIS PATTERN

Use it when:

* condition depends on counts or sums
* problem says:

  * “at most k”
  * “maximum frequency”
  * “product/sum constraint”

---

# TASK (IMPORTANT)

For each problem:

## 1. Explain:

* What state are you tracking?
* What makes window invalid?

## 2. Identify:

* When do you shrink?
* What gets updated when shrinking?

---

# FINAL TAKEAWAY

Sliding window now becomes:

> A system that maintains constraints dynamically using state tracking
