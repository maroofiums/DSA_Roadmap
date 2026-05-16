graph = {
    "A": ["B","C"],
    "B": ["A","D"],
    "C": ["A","D"],
    "D": ["B","C"]
}

def dfs(graph,start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)


dfs(graph,"A")