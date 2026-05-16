graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}

def dfs(graph,node,visited):
    if node in visited:
        return 
    visited.add(node)
    print(node)

    for neighbor in graph[node]:
        dfs(graph,neighbor,visited)

print("Recursive DFS")
visited = set()
dfs(graph,"A",visited)

def iterativeDFS(graph,start):
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

print("Iterative DFS")
iterativeDFS(graph,"A")