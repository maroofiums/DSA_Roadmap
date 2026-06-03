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


tasks = ["A", "A", "A", "B", "B", "B"]
n = 2

print(leastInterval(tasks, n))