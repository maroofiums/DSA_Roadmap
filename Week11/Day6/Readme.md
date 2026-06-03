# DAY 6 - Task Scheduler

## Folder Structure

```text
Day6
├── Problems
│   └── 621. Task Scheduler
│       ├── BruteForce.py
│       └── Optimal.py
└── Readme.md
```

---

# Problem

## 621. Task Scheduler

Given a list of tasks represented by capital letters and a cooldown period `n`.

The same task must be separated by at least `n` intervals.

Return the minimum number of CPU intervals needed to finish all tasks.

---

## Example

```python
tasks = ["A","A","A","B","B","B"]
n = 2
```

Output:

```python
8
```

One valid schedule:

```text
A -> B -> idle -> A -> B -> idle -> A -> B
```

Total time:

```text
8
```

---

# Concepts Used

* Frequency Counting
* Greedy Scheduling
* Max Heap
* Queue (Cooldown)
* Simulation

---

# Approach 1: Brute Force

## Idea

At every time unit:

1. Find all tasks that are not cooling down.
2. Pick the task with the highest remaining frequency.
3. Execute it.
4. Put it into cooldown.
5. Repeat until all tasks finish.

---

## Algorithm

```text
Count frequencies

While tasks remain:

    Find available task with highest count

    Execute it

    Put task into cooldown

    Increase time
```

---

## Code

```python
from typing import List

def leastInterval(tasks: List[str], n: int) -> int:

    freq = {}

    for task in tasks:
        freq[task] = freq.get(task, 0) + 1

    cooldown = {}

    time = 0

    while freq:

        time += 1

        candidate = None
        max_count = 0

        for task, count in freq.items():

            if task not in cooldown or cooldown[task] <= time:

                if count > max_count:
                    candidate = task
                    max_count = count

        if candidate:

            freq[candidate] -= 1

            cooldown[candidate] = time + n + 1

            if freq[candidate] == 0:
                del freq[candidate]

    return time
```

---

## Complexity

Let:

```text
m = unique tasks
n = total tasks
```

Time:

```text
O(total_time × m)
```

Worst Case:

```text
O(n²)
```

Space:

```text
O(m)
```

---

# Approach 2: Optimal (Heap + Queue)

## Idea

Always execute the task with the highest remaining frequency.

Use:

* Max Heap → highest frequency task
* Queue → tasks in cooldown

This minimizes idle time.

---

## Key Observation

The tasks causing the most problems are the most frequent ones.

Therefore:

```text
Always execute highest frequency task first
```

---

## Algorithm

```text
Count frequencies

Build max heap

While heap or cooldown queue:

    Increase time

    Execute top task

    Put remaining count into cooldown queue

    Move finished cooldown tasks back to heap
```

---

## Code

```python
from typing import List
from collections import deque
import heapq

def leastInterval(tasks: List[str], n: int) -> int:

    count = {}

    for task in tasks:
        count[task] = count.get(task, 0) + 1

    maxHeap = [-cnt for cnt in count.values()]
    heapq.heapify(maxHeap)

    q = deque()

    time = 0

    while maxHeap or q:

        time += 1

        if maxHeap:

            cnt = 1 + heapq.heappop(maxHeap)

            if cnt:
                q.append([cnt, time + n])

        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])

    return time
```

---

## Dry Run

Input:

```python
tasks = ["A","A","A","B","B","B"]
n = 2
```

Frequencies:

```text
A = 3
B = 3
```

Heap:

```text
[-3, -3]
```

Simulation:

```text
Time 1 -> A
Time 2 -> B
Time 3 -> idle
Time 4 -> A
Time 5 -> B
Time 6 -> idle
Time 7 -> A
Time 8 -> B
```

Answer:

```text
8
```

---

# Complexity

Heap Operations:

```text
Push  -> O(log m)
Pop   -> O(log m)
```

Where:

```text
m = number of unique tasks
```

Overall:

```text
O(n log m)
```

Commonly written as:

```text
O(n log n)
```

Space:

```text
O(m)
```

---

# Why Greedy Works

We always choose:

```text
Task with highest remaining frequency
```

Reason:

* High-frequency tasks are hardest to place.
* Scheduling them early reduces future idle gaps.
* Leads to minimum total execution time.

---

# Pattern Recognition

This problem combines:

## Heap Pattern

```text
Always select highest priority task
```

## Queue Pattern

```text
Manage cooldown period
```

## Greedy Pattern

```text
Do the most urgent task first
```

---

# Interview Takeaway

Whenever you see:

* Frequencies
* Scheduling
* Cooldown periods
* Highest priority first

Think:

```text
Heap + Queue + Greedy
```

This pattern appears in:

* CPU Scheduling
* Job Scheduling
* Task Execution Systems
* Distributed Systems
* Cloud Resource Allocation

```
```
