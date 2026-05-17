from collections import deque

graph = {
    1:[2,3],
    2:[4,5],
    3:[],
    4:[],
    5:[]
}

def level_order(graph,start):
    queue = deque([start])
    visited = set([start])

    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            print(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


level_order(graph,1)