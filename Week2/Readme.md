# WEEK 2 - STRINGS + HASHING (ROADMAP)

## Goal

By the end of this week, you should be able to:

* Build frequency maps quickly
* Recognize string patterns instantly
* Apply sliding window without confusion
* Avoid brute force thinking

---

# DAY 1 - Frequency Map Basics

## Concept

* Character counting
* HashMap for strings

## Problem

Valid Anagram

## Idea

* Count characters in both strings
* Compare frequency maps

## Pattern

Same characters → Frequency Map comparison

## Task

* Solve Valid Anagram
* Practice building frequency dictionary manually

---

# DAY 2 - Grouping with Hashing

## Concept

* Grouping similar items using a transformed key

## Problem

Group Anagrams

## Idea

* Convert each string into a key:

  * sorted string OR
  * frequency tuple
* Use HashMap to group

## Pattern

Grouping → HashMap with custom key

## Task

* Solve Group Anagrams
* Try both sorting and frequency approach

---

# DAY 3 - Sliding Window Introduction

## Concept

* Expand and shrink window
* Track condition dynamically

## Problem

Longest Substring Without Repeating Characters

## Idea

* Expand right pointer
* If duplicate appears → shrink left pointer

## Pattern

Substring with constraint → Sliding Window

## Task

* Dry run pointer movement step by step
* Implement solution from memory

---

# DAY 4 - First Unique Character

## Concept

* Frequency + index tracking

## Problem

First Unique Character in a String

## Idea

* Build frequency map
* Scan string again to find first character with count 1

## Pattern

Frequency map + linear scan

## Task

* Solve using two-pass approach
* Focus on clarity, not speed

---

# DAY 5 - Mixed Practice

## Problems

* Valid Anagram
* Group Anagrams
* First Unique Character

## Goal

* Solve without notes
* Identify pattern before coding

---

# DAY 6 - Sliding Window Mastery

## Problem

Longest Substring Without Repeating Characters

## Focus

* Clean implementation
* Correct pointer movement
* No confusion in window logic

## Goal

Make sliding window automatic

---

# DAY 7 - Mock Test

## Rules

* 3 problems
* 30–40 minutes
* No references

## Test Set

* Valid Anagram
* Group Anagrams
* Longest Substring Without Repeating Characters

---

# WEEK 2 CORE PATTERNS

| Problem Type       | Pattern                 |
| ------------------ | ----------------------- |
| Anagram            | Frequency Map           |
| Grouping           | HashMap with custom key |
| Substring problems | Sliding Window          |
| First occurrence   | Frequency + scan        |

---

# Final Note

Week 2 is about pattern selection speed. The goal is:

* See problem
* Immediately know approach
* Then code