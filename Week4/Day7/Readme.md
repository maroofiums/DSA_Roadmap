# DAY 7 - MOCK TEST (LINKED LIST)

## Rules

* No notes
* No rewatching concepts
* Think first, then act
* Time: 30–40 minutes

---

# Problem 1 - Reverse Linked List

## What is being tested

* Pointer control
* Order of operations
* Not losing nodes

---

## Expected Thinking

Ask:

* How do I avoid losing rest of list?
  → Save next

* How do I reverse direction?
  → Point current to previous

---

## Key Check

> Are you following correct order?

1. Save next
2. Reverse
3. Move

---

## Failure Signals

* You lose part of list
* You confuse pointer movement
* You reverse incorrectly

---

## Target Time

8–10 minutes

---

# Problem 2 - Detect Cycle

## What is being tested

* Fast & slow pointer logic
* Understanding loop behavior

---

## Expected Thinking

Ask:

* If cycle exists → what happens?
  → Fast meets slow

* If no cycle → what happens?
  → Fast reaches None

---

## Key Check

> Are you moving fast twice per step?

---

## Failure Signals

* You move both pointers same speed
* You don’t check for None
* You don’t understand why meeting happens

---

## Target Time

8–10 minutes

---

# Problem 3 - Remove Nth Node from End

## What is being tested

* Gap pointer technique
* Edge case handling

---

## Expected Thinking

Ask:

* How do I avoid counting length?
  → Use gap

* Where should second pointer stop?
  → Just before node to delete

---

## Key Check

> Did you move first pointer N steps first?

---

## Critical Edge Case

* Removing head

If you don’t handle this → solution is incomplete

---

## Failure Signals

* Gap is incorrect
* You remove wrong node
* You ignore head removal

---

## Target Time

12–15 minutes

---

# Evaluation (Be Honest)

## 1. Pointer Confidence

* Smooth → strong
* Slight confusion → improving
* Struggling → revisit

---

## 2. Logic Clarity

* You can explain steps → strong
* You just “did it somehow” → weak

---

## 3. Edge Case Handling

* Covered → good
* Missed → needs work

---

# Result Interpretation

## If you solved all 3 cleanly

You are:

> Ready for next level (Stack, Queue, Trees)

---

## If you struggled in Reverse

→ Pointer fundamentals weak
→ Revisit Day 2

---

## If you struggled in Cycle

→ Fast/slow understanding weak
→ Revisit Day 3

---

## If you struggled in Remove Nth

→ Gap technique not clear
→ Revisit Day 4

---

# Final Reality Check

If you can solve these 3 under time:

> You are already ahead of most beginners in DSA

---