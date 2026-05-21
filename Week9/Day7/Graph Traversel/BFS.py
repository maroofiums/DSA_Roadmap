from collections import deque

graph = {
    "A":["B","C"],
    "B":["A","C"],
    "C":["D"],
    "D":[]
}

def bfs(start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()

        print(node)

        for nei in graph[node]:
            if nei not in visited:
                queue.append(nei)
                visited.add(nei)

bfs("A")