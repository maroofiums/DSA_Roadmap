# DAY 7 - MOCK TEST

## Rules

* No notes
* No retries during solving
* Think first, then code
* Time: 30–45 minutes total

---

# Problem 1 - Container With Most Water

## What is being tested

* Opposite direction two pointers
* Greedy decision making

---

## Expected Thinking

Ask:

* What determines area? → width + min height
* What limits area? → smaller height

---

## Key Decision

> Always move the pointer with smaller height

---

## Failure Signal

If you:

* Try all pairs → wrong approach
* Move both pointers randomly → no understanding

---

## Target Time

8–10 minutes

---

# Problem 2 - Longest Substring Without Repeating

## What is being tested

* Core sliding window
* Pointer coordination

---

## Expected Thinking

Ask:

* Is this substring problem? → Yes
* Constraint? → no duplicates

---

## Core Logic

* Expand window
* If duplicate → shrink until valid
* Track max length

---

## Failure Signal

If you:

* Restart window
* Forget to remove elements when shrinking

---

## Target Time

10–12 minutes

---

# Problem 3 - Minimum Window Substring (HARD)

## What is being tested

* Advanced sliding window
* State tracking + optimization

---

## Expected Thinking

Ask:

* What is required? → all characters of target
* What makes window valid? → all counts satisfied

---

## Core Logic

* Expand → until valid
* Shrink → to minimize window
* Keep best answer

---

## MOST IMPORTANT

> Expand for validity, shrink for optimization

---

## Failure Signal

If you:

* Don’t know when window becomes valid
* Shrink incorrectly
* Lose track of required counts

---

## Target Time

15–20 minutes

---

# Evaluation (Be Honest)

After test, rate yourself:

## 1. Pattern Recognition

* Instant → strong
* Slow → needs revision
* Confused → weak

---

## 2. Execution

* Clean pointer movement → good
* Bugs/confusion → needs practice

---

## 3. Sliding Window Depth

* Understand when to shrink → strong
* Guessing → weak

---

# Result Interpretation

## If you solved all 3 smoothly

You are:

> Ready for next level (Linked List + harder patterns)

---

## If you struggled in Minimum Window

Normal.

It means:

> Sliding window is not fully internalized yet

You should:

* Revisit Day 5
* Do 2–3 more similar problems

---

## If you struggled in basic ones

Then:

> Pattern is not stable yet

Repeat Week 3 again (fast revision)

---

# Final Reality Check

If you can solve these 3 under time:

You are already ahead of most beginners.

---

