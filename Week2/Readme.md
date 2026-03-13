# Week 2 — Linked Lists & Hashing

## Day 1 — Linked List Fundamentals

### Concepts

* Structure of a linked list
* Node and pointer references
* Traversal
* Reversing a linked list
* Detecting cycles (fast & slow pointers)

### What to Learn

1. How pointers move in a linked list
2. Difference between **iterative vs recursive reverse**
3. Floyd’s **Tortoise & Hare** algorithm

### Practice Problems

* Reverse Linked List
* Linked List Cycle

### Key Pattern

Fast pointer moves **2 steps**
Slow pointer moves **1 step**

If they meet → cycle exists

---

# Day 2 — Linked List Manipulation

### Concepts

* Finding the **middle node**
* Merging sorted linked lists
* Multiple pointer management

### What to Learn

1. Fast/slow pointer to find middle
2. Dummy node technique
3. Handling pointer edge cases

### Practice Problems

* Middle of Linked List
* Merge Two Sorted Lists
* Merge K Sorted Lists (idea understanding)

### Important Trick

**Dummy node**

This simplifies pointer manipulation when building new lists.

---

# Day 3 — HashMap Patterns

### Concepts

* Frequency counting
* Duplicate detection
* Complement lookup
* Tracking counts

### What to Learn

1. HashMap insertion and lookup
2. Counting frequencies efficiently
3. Avoiding nested loops

### Practice Problems

* Two Sum
* Top K Frequent Elements

### Key Idea

HashMap gives **O(1) lookup**.

This replaces **O(n²) brute force**.

---

# Day 4 — HashMap + Prefix Sum

### Concepts

* HashMap with prefix sums
* Sliding window with hashmap
* Tracking previously seen values

### What to Learn

1. Store **prefix sums in a hashmap**
2. Detect if a previous prefix satisfies a condition

### Practice Problems

* Minimum Window Substring
* Subarray Sum Equals K

### Key Pattern

Instead of checking all subarrays:

Store previous prefix sums.

Then check:

```
previous_prefix = current_sum - target
```

---

# Day 5 — Advanced Hashing + Linked Lists

### Concepts

* Data structure design
* Combining HashMap + LinkedList
* Object references

### What to Learn

1. How **LRU cache** works
2. HashMap → O(1) lookup
3. Doubly linked list → O(1) insert/remove

### Practice Problems

* LRU Cache
* Copy List With Random Pointer

### Interview Insight

This problem tests **data structure design thinking**, not just coding.

---

# Day 6 — Practice Day

### Goal

Strengthen recognition of patterns.

Solve **4–5 mixed problems**.

Suggested topics:

* Linked list manipulation
* HashMap tricks
* Prefix sum problems

Examples:

* Intersection of Two Linked Lists
* Remove Nth Node From End
* Subarray Sum Equals K
* Top K Frequent Elements

---

# Day 7 — Weekly Test

Solve **without help**.

### Test Problems

1. Reverse Linked List
2. Middle of Linked List
3. Top K Frequent Elements
4. Subarray Sum Equals K
5. LRU Cache (idea + approach)

### Rules

* Max time per problem: **30 minutes**
* Write **pattern + idea first**
* Review mistakes after solving

---

# Week 2 Success Criteria

By the end of Week 2 you should be able to:

Recognize **linked list pointer problems quickly**

Use **fast & slow pointer technique**

Use **HashMaps to remove nested loops**

Understand **prefix sum + hashmap pattern**

Solve **10+ problems confidently**

---

