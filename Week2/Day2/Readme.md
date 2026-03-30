# DAY 2 - Grouping with Hashing (Group Anagrams)

## Concept

You are learning a powerful pattern:

> Instead of comparing elements, transform them into a **common representation**, then group them.

This is one of the most important hashing patterns in interviews.

---

# Problem: Group Anagrams

## Goal

Group strings that contain:

* Same characters
* Same frequency
* Different order

---

# Core Idea

All anagrams become identical after applying a transformation.

So the problem becomes:

> “What should be the unique identifier (key) for each group?”

---

# Pattern

> Grouping → HashMap + Canonical Key

---

# Approach 1: Sorting Based Key

## Idea

If two strings are anagrams:

* Sorting both gives the same result

Example:

* "eat" → "aet"
* "tea" → "aet"

## Steps

1. Sort each string
2. Use sorted string as key
3. Add original string to that key’s group

---

## When to use

* Simple problems
* Small constraints
* Easy implementation

---

# Approach 2: Frequency-Based Key (Better Thinking)

## Idea

Instead of sorting, represent string as:

> character frequency signature

Example:

* "eat" → (1a, 0b, 0c...1e...1t)

This becomes a **unique structural fingerprint**

---

## Steps

1. Count frequency of characters
2. Convert into immutable structure (like tuple)
3. Use it as hashmap key
4. Group strings with same signature

---

## Why this is better

* No sorting cost
* More efficient for large strings
* True hashing logic (important for interviews)

---

# Key Insight

You are not grouping strings.

You are grouping:

> “Structural similarity”

---

# What Interviewers are testing

They want to see:

* Can you think beyond direct comparison?
* Can you create a transformation function?
* Do you understand hashing deeply?

---

# Comparison

| Method    | Idea             | Efficiency            | Use case         |
| --------- | ---------------- | --------------------- | ---------------- |
| Sorting   | reorder string   | O(n log n) per string | easy problems    |
| Frequency | count characters | O(n) per string       | optimal approach |

---

# Mental Model

Whenever you see:

* “Group similar items”
* “Find all pairs”
* “Cluster items”

Think:

> HashMap + Custom Key

---

# Task Execution Plan

You should:

1. First solve using sorting (for intuition)
2. Then solve using frequency (for mastery)
3. Compare both mentally

---

# Extra Practice Question (Important)

Try to think:

* How would you group sentences with same words?
* How would you group numbers with same digits?

This is the SAME pattern.

---