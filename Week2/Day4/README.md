# DAY 4 - First Unique Character

## Concept

You are combining two ideas:

* **Frequency tracking (what exists and how many times)**
* **Index/order tracking (where it appears first)**

---

# Problem: First Unique Character

## Goal

Find the **first character in a string** that:

> Appears exactly once

---

# Core Idea

You cannot know “first unique” in one pass alone easily.

So you split the problem into 2 stages:

---

# Pattern

> Frequency Map + Linear Scan

---

# Approach (Two-Pass Thinking)

## Pass 1: Build knowledge

You scan the string and build a frequency map:

* Character → count of occurrences

Now you know:

> which characters are unique

---

## Pass 2: Find order

You scan the string again from left to right:

* Check each character
* If frequency is 1 → return it immediately

---

# Why Two Passes?

Because:

* Frequency tells “WHAT”
* Order tells “WHICH FIRST”

You need both.

---

# Key Insight

HashMap alone is NOT enough for ordering problems.

You always need:

> HashMap + traversal

---

# Pattern Recognition

Whenever you see:

* “first”
* “leftmost”
* “earliest”
* “smallest index satisfying condition”

Think:

> Frequency map + linear scan

---

# Mental Model

You are doing:

1. Understand the whole string (frequency map)
2. Then replay the string in order to find answer

---

# Common Mistake

Do NOT:

* Try to solve in one pass blindly
* Forget ordering requirement
* Return any unique character (not first)

---

# Dry Run Concept

Example:

```
"leetcode"
```

## Step 1: Frequency

* l → 1
* e → 3
* t → 1
* c → 1
* o → 1
* d → 1

---

## Step 2: Scan again

Left to right:

* l → 1 → return immediately

Answer = **l**

---

# Important Insight

Even though multiple characters are unique:

> Only the FIRST one matters

So order is critical.

---

# What you are learning here

This problem teaches:

* Separation of concerns (data vs order)
* Two-pass optimization
* Real interview thinking style

---

# Task Checklist

You should be able to:

* Explain why one-pass is hard
* Explain why two-pass works
* Dry run manually on:

  * "aabbccddeff"
  * "swiss"

---