# WEEK 4 - LINKED LIST (COMPLETE ROADMAP)

## Overall Goal

* Understand pointer movement deeply
* Stop “visual guessing” → start logical tracking
* Master:

  * traversal
  * reversal
  * fast/slow technique

---

# DAY 1 - Linked List Basics + Traversal

## Goal

Understand how linked lists actually work

## Concepts

* Node structure (value + next pointer)
* Traversal using pointer
* Difference from arrays

## Problems

* Print linked list
* Find length of linked list

## Focus

* Move pointer step by step
* Understand `current = current.next` deeply

---

# DAY 2 - Reverse Linked List (MOST IMPORTANT)

## Goal

Master pointer reversal

## Concepts

* Changing direction of links
* Using 3 pointers:

  * previous
  * current
  * next

---

## Problem

Reverse Linked List

---

## Core Idea

At each step:

> Reverse the link of current node

---

## Mental Flow

* Save next
* Reverse current pointer
* Move forward

---

## Focus

* Do NOT lose the rest of list
* Order of operations matters

---

# DAY 3 - Fast & Slow Pointers

## Goal

Understand dual-speed traversal

## Concepts

* Slow moves 1 step
* Fast moves 2 steps

---

## Problem

Detect Cycle in Linked List

---

## Core Idea

If there is a cycle:

> Fast pointer will meet slow pointer

---

## Why it works

* Fast moves faster → catches slow inside cycle

---

## Focus

* Visualize loop behavior
* Understand meeting condition

---

# DAY 4 - Remove Nth Node from End

## Goal

Solve problems without knowing list length

## Concepts

* Two pointers with gap
* One pass solution

---

## Problem

Remove Nth Node From End

---

## Core Idea

* Move first pointer ahead by N
* Then move both together
* Second pointer reaches node before target

---

## Focus

* Maintaining gap correctly
* Edge cases (removing head)

---

# DAY 5 - Merge Two Sorted Lists

## Goal

Merge structures using pointers

## Concepts

* Comparing nodes
* Building new list using pointer

---

## Problem

Merge Two Sorted Lists

---

## Core Idea

* Compare both lists
* Always take smaller node
* Move pointer accordingly

---

## Focus

* Maintain sorted order
* Handle leftover nodes

---

# DAY 6 - Pattern Mastery

## You must know

| Problem      | Pattern            |
| ------------ | ------------------ |
| Reverse List | Pointer reversal   |
| Detect Cycle | Fast & slow        |
| Remove Nth   | Gap pointers       |
| Merge Lists  | Parallel traversal |

---

## Task

* Explain each pattern without code
* Dry run manually

---

# DAY 7 - Mock Test

## Rules

* 3 problems
* 30–40 minutes
* No help

---

## Test Set

* Reverse Linked List
* Detect Cycle
* Remove Nth Node

---

# CORE INSIGHT OF WEEK 4

You are learning:

> How to control pointers safely without losing data

---

# Common Mistakes

Do NOT:

* Lose reference to next node (very common)
* Move pointers blindly
* Ignore edge cases (empty list, single node)

---

# Mental Model

Think like this:

* Each node is a box
* Pointer is your only way to move
* If you lose pointer → data is gone

---

# Final Check

You are ready if:

* You can reverse list without confusion
* You understand fast/slow logic
* You can explain pointer movement step by step

---