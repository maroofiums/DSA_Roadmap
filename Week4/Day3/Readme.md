# DAY 3 - Fast & Slow Pointers

## Goal

Understand how **two pointers moving at different speeds** reveal hidden structure.

---

# Core Concept

You use two pointers:

* **Slow pointer** → moves 1 step
* **Fast pointer** → moves 2 steps

---

# Pattern

> Detect cycle / middle / loop behavior → Fast & Slow pointers

---

# Problem - Detect Cycle in Linked List

## Goal

Check if a linked list has a loop

---

# Core Idea

If there is a cycle:

> Fast pointer will eventually meet slow pointer

---

# Why This Works (IMPORTANT)

Think of a cycle like a circular track:

* Slow moves 1 step
* Fast moves 2 steps

So every step:

> Fast gets closer to slow by 1 step

---

## Key Insight

Inside the cycle:

> Distance between fast and slow keeps shrinking

Eventually:

> They collide

---

# Visualization (CRITICAL)

Imagine:

```id="y4o8qv"
1 → 2 → 3 → 4 → 5
          ↑     ↓
          ← ← ←
```

---

## Movement

* Both enter the cycle
* Fast keeps looping faster
* Slow moves steadily

At some point:

> They land on the same node

---

# Important Condition

## If NO cycle

* Fast pointer reaches `None`
* List ends

## If cycle exists

* Fast never reaches `None`
* It loops forever and meets slow

---

# Mental Model

Think like:

> Two runners on a circular track

* One is faster
* Eventually, faster one laps the slower one

---

# What Interviewer is Testing

* Do you understand pointer movement mathematically?
* Can you visualize behavior over time?

---

# Common Mistakes

Do NOT:

* Move both pointers same speed
* Forget to check if fast or fast.next is None
* Assume meeting happens immediately

---

# Deep Insight (IMPORTANT)

This is not luck.

It’s guaranteed because:

> Relative speed = 1 step per iteration

So meeting is inevitable inside a cycle.

---

# When to Use This Pattern

Use fast/slow pointers when:

* Detect cycle
* Find middle of list
* Find loop entry (advanced)

---

# Task (IMPORTANT)

## 1. Answer this:

Why does fast pointer NOT skip over slow pointer?

---

## 2. Dry run:

Case 1:

```id="p7r2m8"
1 → 2 → 3 → 4 → None
```

Case 2:

```id="l2x6h1"
1 → 2 → 3 → 4 → 2 (cycle)
```

Track:

* slow position
* fast position

---

# Final Takeaway

You are learning:

> How relative motion reveals hidden structure

---