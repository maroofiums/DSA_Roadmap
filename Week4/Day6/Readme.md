# DAY 6 - Pattern Mastery (Linked List)

## Goal

You should reach this level:

> Hear problem → instantly know pattern → mentally simulate solution

---

# 1. Reverse Linked List

## Pattern

Pointer Reversal

---

## Explanation (without code)

* You are changing direction of links
* Each node originally points forward
* You make it point backward

---

## Core Logic

At each node:

* Save next
* Reverse link
* Move forward

---

## Why needed

Because:

> If you don’t save next → you lose remaining list

---

## Mental Dry Run

```
1 → 2 → 3
```

Becomes:

```
3 → 2 → 1
```

Think step-by-step:

* break link
* reconnect backward

---

# 2. Detect Cycle

## Pattern

Fast & Slow Pointers

---

## Explanation

* Two pointers move at different speeds
* If there is a loop → fast catches slow

---

## Core Logic

* Slow moves 1
* Fast moves 2
* If they meet → cycle exists

---

## Why it works

> Fast gains 1 step per move → collision is guaranteed inside loop

---

## Mental Dry Run

Cycle case:

```
1 → 2 → 3 → 4 → 2
```

* Both enter loop
* Fast keeps looping faster
* Eventually meets slow

---

# 3. Remove Nth Node from End

## Pattern

Gap (Distance Between Pointers)

---

## Explanation

* Maintain fixed distance between two pointers
* When front pointer reaches end → back pointer is at correct position

---

## Core Logic

* Move first pointer N steps ahead
* Move both together
* Second pointer reaches node before target

---

## Why it works

> Distance stays constant → alignment gives correct position

---

## Mental Dry Run

```
1 → 2 → 3 → 4 → 5
n = 2
```

Remove 4

---

# 4. Merge Two Sorted Lists

## Pattern

Parallel Traversal

---

## Explanation

* Traverse both lists simultaneously
* Compare current nodes
* Take smaller one

---

## Core Logic

* Always choose smallest available node
* Move that pointer
* Continue

---

## Why it works

> Lists are already sorted → greedy choice is correct

---

## Mental Dry Run

```
1 → 3 → 5
2 → 4 → 6
```

Result:

```
1 → 2 → 3 → 4 → 5 → 6
```

---

# FINAL PATTERN SUMMARY (IMPORTANT)

| Problem    | Pattern            | Core Idea                |
| ---------- | ------------------ | ------------------------ |
| Reverse    | Pointer reversal   | Change direction safely  |
| Cycle      | Fast & slow        | Relative speed detection |
| Remove Nth | Gap pointers       | Maintain distance        |
| Merge      | Parallel traversal | Greedy comparison        |

---

# MASTER CHECK (VERY IMPORTANT)

You should be able to answer instantly:

## Q1

“Reverse a list”
→ Pointer reversal

---

## Q2

“Detect loop”
→ Fast & slow

---

## Q3

“Nth from end”
→ Gap pointers

---

## Q4

“Merge sorted lists”
→ Parallel traversal

---

# Final Skill You Built

You now understand:

> How to control and manipulate pointers safely

This is a **major milestone**.

---
