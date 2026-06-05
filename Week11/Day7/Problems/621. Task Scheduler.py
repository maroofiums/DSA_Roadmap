import heapq
from typing import List
from collections import deque

def leastInterval(tasks:List[int],n:int) -> int:

    count = {}

    for task in tasks:
        count[task] = count.get(task,0) + 1

    q = deque()

    heap = [-cnt for cnt in count.values()]

    heapq.heapify(heap)

    time = 0

    while heap or q:
        time += 1
    
        if q and q[0][1] == time:
            heapq.heappush(heap,q.popleft()[0])

        if heap:
            cnt = 1 + heapq.heappop(heap)

            if cnt:
                q.append([cnt,time + n + 1])

    return time


tasks: List[int] = ["A","A","A","B","B","B"]
n : int = 2

print(leastInterval(tasks,n))