from collections import deque

def shortest_path(graph,start,target):
    queue = deque([(start,0)])
    visited = set([start])

    while queue:
        node,distance = queue.popleft()

        if node == target:
            return distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor,distance+1))
    
    return -1

graph = {
    "A":["B","C"],
    "B":["D"],
    "C":[],
    "D":[]
}

print(shortest_path(graph,"A","D"))
