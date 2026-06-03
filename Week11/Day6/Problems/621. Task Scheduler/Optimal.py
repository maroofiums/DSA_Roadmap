from typing import List
from collections import deque
import heapq

def leastInterval(tasks: List[str],n:int) -> bool:
    count = {}

    time = 0

    for task in tasks:
        count[task] = count.get(task,0) + 1
    
    maxHeap = [-cnt for cnt in count.values()]

    q = deque()

    heapq.heapify(maxHeap)

    while maxHeap or q:
        time += 1 

        if maxHeap:
            cnt = 1 + heapq.heappop(maxHeap)

            if cnt:
                q.append([cnt,time + n])

        if q and q[0][1] == time:
            heapq.heappush(maxHeap,q.popleft()[0])
    
    return time


tasks: List[str] = ["A","A","A","B","B","B"]
n: int = 2

print(leastInterval(tasks,n))