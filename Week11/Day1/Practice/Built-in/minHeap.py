import heapq

heap = []

# 10,4,15,1,7

heapq.heappush(heap,10)
heapq.heappush(heap,4)
heapq.heappush(heap,15)
heapq.heappush(heap,1)
heapq.heappush(heap,7)

print(heap)

# peek

print(heap[0])

# pop minimum

print(heapq.heappop(heap))

print(heap)

# heapify existing list

arr = [9,3,6,1,8,2]

heapq.heapify(arr)

print(arr)

# heap sort

sorted_arr = []
while arr:
    sorted_arr.append(heapq.heappop(arr))

print(sorted_arr)
