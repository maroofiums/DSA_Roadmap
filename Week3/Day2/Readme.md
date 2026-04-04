# DAY 2 - Two Pointers (Opposite Direction)

## Goal

Master **left-right pointer strategy** and understand **why pointers move**, not just how.

---

# Core Concept

You use two pointers:

* **Left pointer** → starts at beginning
* **Right pointer** → starts at end

They move toward each other based on logic.

---

# Pattern

> Optimization problems on sorted/structured data → Two pointers (opposite direction)

---

# Key Idea (VERY IMPORTANT)

You are not just shrinking an array.

You are:

> Eliminating impossible answers step by step

---

# Problem 1 - Container With Most Water

## Goal

Find two lines that form **maximum area**

---

## Key Insight

Area depends on:

* width (distance between pointers)
* height (minimum of two lines)

---

## WHY pointers move (MOST IMPORTANT PART)

At any step:

You have two lines:

* left height
* right height

The limiting factor is:

> the smaller height

---

## Core Logic

If you move the taller line:

* width decreases
* height does NOT improve
  → area cannot increase

If you move the smaller line:

* you might find a taller boundary
  → potential improvement

---

## Final Insight

> Always move the pointer with the smaller height

Because only that can potentially increase area.

---

# Problem 2 - Two Sum II (Sorted Array)

## Goal

Find two numbers that add to target

---

## Core Idea

Since array is sorted:

* If sum is too small → increase left pointer
* If sum is too large → decrease right pointer

---

## Why it works

* Increasing left → increases sum
* Decreasing right → decreases sum

So you move based on comparison with target.

---

## Pattern

> Sorted array + target condition → Two pointers inward

---

# Problem 3 - Valid Palindrome

## Goal

Check if string reads same forward and backward

---

## Core Idea

* Compare left and right characters
* If equal → move both inward
* If not equal → not palindrome

---

## Extra Thought (Important)

You may need to:

* ignore non-alphanumeric characters
* ignore case

---

## Pattern

> Symmetry check → Two pointers inward

---

# COMMON PATTERN ACROSS ALL 3

| Problem                   | Movement Logic              |
| ------------------------- | --------------------------- |
| Container With Most Water | Move smaller height         |
| Two Sum II                | Move based on sum vs target |
| Palindrome                | Move both inward            |

---

# BIG INSIGHT OF DAY 2

You are learning:

> Pointer movement is decision-based, not fixed

Every move answers:

* What am I trying to eliminate?
* What cannot give better answer anymore?

---

# Mental Model

Think like this:

* I don’t search all pairs
* I eliminate bad regions
* I keep only potential optimal candidates

---

# Common Mistakes

Do NOT:

* Move pointers randomly
* Forget WHY you moved a pointer
* Try brute force pairs inside logic

---

# When to Use This Pattern

Use opposite pointers when:

* You need **pairs**
* You need **max/min optimization**
* Data is sorted or can be interpreted from both ends

---

# Task (IMPORTANT)

For each problem, explain:

1. Why does left move?
2. Why does right move?
3. What case is being eliminated?

---

# Final Takeaway

This day is not about coding.

It is about:

> Learning how to eliminate impossible answers efficiently

---
