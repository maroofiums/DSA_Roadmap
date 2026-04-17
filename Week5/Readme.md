# WEEK 5 - STACK + QUEUE (COMPLETE ROADMAP)

## Overall Goal

Master:

* LIFO thinking (Stack)
* FIFO thinking (Queue)
* Monotonic stack pattern
* Tracking previous / next greater elements

---

# Core Concepts

## Stack = Last In First Out

Last item added is removed first.

Think:

> Plate stack

---

## Queue = First In First Out

First item added leaves first.

Think:

> Line of people

---

# Why This Week Matters

Many interview problems look hard until you realize:

> “This is just a stack problem”

---

# DAY 1 - Stack Basics + Valid Parentheses

## Goal

Understand push / pop logic

## Concepts

* Opening bracket goes in stack
* Closing bracket must match top

## Problem

* Valid Parentheses

## Focus

* Why top element matters
* Order checking

---

# DAY 2 - Monotonic Stack Introduction

## Goal

Learn next greater / warmer future pattern

## Concepts

* Stack stores unresolved indices
* Pop when better answer found

## Problem

* Daily Temperatures

## Focus

* Why indices are stored
* Why popping happens

---

# DAY 3 - Design Stack Problem

## Goal

Use extra tracking inside stack

## Concepts

* Maintain minimum efficiently
* Parallel state tracking

## Problem

* Min Stack

## Focus

* O(1) minimum retrieval
* Structure design thinking

---

# DAY 4 - Next Greater Element

## Goal

Master monotonic stack pattern

## Concepts

* Previous / next greater
* Decreasing stack

## Problem

* Next Greater Element

## Focus

* Which elements stay in stack
* Why popped elements are resolved

---

# DAY 5 - Queue Basics + Mixed Practice

## Goal

Understand FIFO + revise stack patterns

## Concepts

* Enqueue / dequeue
* When queue is better than stack

## Problems

* Implement Queue using Stack (optional)
* Valid Parentheses
* Daily Temperatures

## Focus

* Stack vs Queue recognition

---

# DAY 6 - Pattern Mastery

## You must know

| Problem            | Pattern           |
| ------------------ | ----------------- |
| Valid Parentheses  | Matching stack    |
| Daily Temperatures | Monotonic stack   |
| Min Stack          | Design + tracking |
| Next Greater       | Monotonic stack   |
| Queue tasks        | FIFO              |

---

## Task

Explain each pattern without code
Dry run manually

---

# DAY 7 - Mock Test

## Rules

* 3 problems
* 30–45 minutes
* No help

## Test Set

* Valid Parentheses
* Daily Temperatures
* Min Stack

---

# BIG INSIGHT OF WEEK 5

Stack is used when you need:

* recent history
* reverse processing
* matching pairs
* unresolved elements

Queue is used when you need:

* ordered processing
* BFS later in trees/graphs
* scheduling

---

# Common Mistakes

Do NOT:

* Use stack when queue needed
* Store values when indices are needed
* Forget empty stack checks
* Ignore order logic

---

# Final Check

You are ready for Week 6 if:

* You recognize monotonic stack quickly
* You understand push/pop meaning
* You know stack vs queue difference instantly

---

# Important Note

This week introduces **monotonic stack**, which many beginners fear.

But once understood:

> Many hard problems become formula-like.

---
