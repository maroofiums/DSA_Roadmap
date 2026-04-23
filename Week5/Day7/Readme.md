# DAY 7 - MOCK TEST (STACK + QUEUE)

## Goal

This is your **Week 5 checkpoint**.

These 3 problems test:

* Basic stack logic
* Monotonic stack pattern
* Data structure design thinking

If you do well here, your stack fundamentals are strong.

---

# Rules

* No notes
* No hints
* Think before coding
* Time: **30–45 minutes total**

Suggested split:

* Valid Parentheses → 8 min
* Daily Temperatures → 12–15 min
* Min Stack → 12–15 min

---

# Problem 1 - Valid Parentheses

## What is being tested

* Stack basics
* Push / pop correctness
* Matching logic

---

## Expected Thinking

Ask:

* Opening bracket → what do I do?
* Closing bracket → what must it match?

---

## Success Signs

* Clean logic
* Handles empty stack case
* Correct nesting order

---

## Failure Signals

* Matching wrong bracket
* Forgetting empty stack
* Ignoring leftover openings at end

---

# Problem 2 - Daily Temperatures

## What is being tested

* Monotonic stack understanding
* Using indices instead of just values
* Future resolution logic

---

## Expected Thinking

Ask:

* Which previous days are unresolved?
* Does current temperature solve them?

---

## Success Signs

* Stores indices
* Pops multiple items when needed
* Computes distance correctly

---

## Failure Signals

* Stores only values
* Pops once instead of repeatedly
* Wrong day difference calculation

---

# Problem 3 - Min Stack

## What is being tested

* Data structure design
* O(1) state retrieval
* Parallel tracking logic

---

## Expected Thinking

Ask:

* How can min be known instantly?
* How is previous min restored after pop?

---

## Success Signs

* Push/pop/top/getMin all efficient
* Handles duplicate minimums

---

## Failure Signals

* Recomputes min by scanning
* Uses one global min incorrectly
* Breaks after pop

---

# Evaluation Rubric

## 1. Pattern Recognition

Did you instantly know:

* Parentheses → stack
* Temperatures → monotonic stack
* Min Stack → design tracking

---

## 2. Clean Execution

Did you solve without confusion?

---

## 3. Edge Cases

Did you handle:

* empty stack
* no warmer day
* repeated minimum values

---

# Result Meaning

## If all 3 solved cleanly

You are ready for:

> Binary Search, Trees, harder mediums

---

## If only Daily Temperatures was hard

Normal.

That means monotonic stack needs more reps.

---

## If Min Stack was hard

Need stronger data structure design thinking.

---

## If Parentheses was hard

Need stronger basic stack foundations.

---

# Post-Test Reflection (IMPORTANT)

Write these answers after test:

1. Which problem felt natural?
2. Which problem caused hesitation?
3. Which pattern is weakest right now?

This gives fastest improvement.

---

# Final Takeaway

If you can solve these under time:

> You’re developing real interview instincts, not just memorized solutions.

---
