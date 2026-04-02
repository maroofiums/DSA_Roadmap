# DAY 6 - Sliding Window Mastery

## Problem

Longest Substring Without Repeating Characters

---

# Core Objective

You are not learning new logic today.

You are training your brain to:

> Automatically maintain a valid window

---

# Pattern Reminder

> Substring + constraint → Sliding Window

Constraint here:

> No repeating characters

---

# Mental Model (IMPORTANT)

Always think:

* I will expand the window (right pointer)
* If something breaks the rule → I will fix it immediately by moving left pointer
* Window must ALWAYS stay valid

---

# Step-by-Step Execution Logic

## Step 1: Expand

* Move right pointer
* Add character into current window state

---

## Step 2: Validate

Ask:

> Is the window still valid?

(valid = no duplicates)

---

## Step 3: Fix (if invalid)

If duplicate appears:

* Move left pointer forward
* Remove characters until duplicate is removed

---

## Step 4: Update answer

At every step:

* Measure window size
* Keep maximum

---

# Key Insight (THIS IS THE WHOLE PROBLEM)

You never restart the window.

You only:

> Adjust it

---

# Why this is powerful

Without sliding window:

* O(n²) brute force (check all substrings)

With sliding window:

* O(n) (each character processed at most twice)

---

# Common Confusion Points

## 1. “When do I move left?”

Answer:

> Only when constraint breaks (duplicate found)

---

## 2. “Do I reset window?”

No.

You only shrink it, never reset fully.

---

## 3. “Why not start over?”

Because previous work is still useful.

You are **reusing computation**

---

# Mental Drill (DO THIS)

Try to imagine window movement for:

* "abcabcbb"
* "bbbbb"
* "pwwkew"

For each:
Track:

* left pointer
* right pointer
* current window

---

# What “Mastery” Means Today

You are successful if:

* You don’t think step-by-step anymore
* You directly see:

  * expand
  * fix
  * continue

---

# Self-Test Questions

You should instantly answer:

## Q1

When duplicate appears, what do you do?

→ Shrink left until valid

---

## Q2

Do you ever restart completely?

→ No

---

## Q3

What is time complexity?

→ O(n)

---

# Final Skill You Are Building

This pattern is used in:

* substrings
* arrays with constraints
* real-time tracking problems

Examples:

* Longest substring
* Minimum window substring
* At most K distinct characters

---
