import heapq

heap = []

nums = [10,4,15,1,7]

for x in nums:
    heapq.heappush(heap,-x)

print(heap)

print(-heap[0])

print(-heapq.heappop(heap))

print(heap)

arr = [9,3,6,1,8,2]

arr = [-x for x in arr]

heapq.heapify(arr)

print(arr)

sorted_arr = []

while arr:
    sorted_arr.append(-heapq.heappop(arr))

print(sorted_arr)