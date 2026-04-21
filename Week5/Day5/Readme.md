# DAY 5 - Queue Basics + Mixed Practice

## Goal

Understand **FIFO thinking** and reinforce when to choose **stack vs queue**.

This day is important because queues become essential later for:

* Trees (Level Order Traversal)
* Graphs (BFS)
* Scheduling systems

---

# Core Concept - Queue

Queue follows:

> First In, First Out (FIFO)

Meaning:

* First element added leaves first

---

# Real-Life Example

Think:

* People standing in a line
* First person enters first
* New people join at the back

---

# Operations

## Enqueue

Add item to back.

## Dequeue

Remove item from front.

## Front / Peek

See front element.

---

# Why Queue Matters

Queue is used when order of arrival matters.

Examples:

* processing tasks
* BFS traversal
* ticket systems
* buffering requests

---

# Stack vs Queue (CRITICAL)

| Structure | Order | Used For                     |
| --------- | ----- | ---------------------------- |
| Stack     | LIFO  | recent history, nested logic |
| Queue     | FIFO  | ordered processing           |

---

# Mixed Practice Problems

## 1. Valid Parentheses

### Pattern

Matching Stack

### Why?

Need most recent opening bracket.

---

## 2. Daily Temperatures

### Pattern

Monotonic Stack

### Why?

Need unresolved previous days waiting for future warmer day.

---

## 3. Implement Queue Using Stacks (Optional but Great)

### Pattern

Data structure transformation

### Why?

Shows deep understanding of order behavior.

---

# Deep Insight

Stack and queue are opposites:

## Stack says:

> Last arrived handled first

## Queue says:

> First arrived handled first

Understanding when order matters is the real skill.

---

# Pattern Recognition Drill

## If problem says:

* nested brackets
* undo history
* next greater element

→ Stack

---

## If problem says:

* level by level
* process in arrival order
* shortest steps BFS later

→ Queue

---

# Mental Models

## Stack

Pile of plates

## Queue

Line of people

Use these images during interviews.

---

# Common Mistakes

Do NOT:

* Use list front pop inefficiently (in implementation contexts)
* Confuse FIFO with LIFO
* Use stack where processing order matters

---

# Mixed Practice Task

For each problem, first answer:

1. Why stack or queue?
2. What ordering rule matters?
3. Could other structure work better?

---

# Quick Test

## Q1

Browser back button

→ Stack

---

## Q2

Printer jobs in arrival order

→ Queue

---

## Q3

Tree level traversal

→ Queue

---

## Q4

Matching brackets

→ Stack

---

# Final Takeaway

Today is not about hard coding.

It is about learning:

> Which structure naturally matches the problem’s order logic.

---

