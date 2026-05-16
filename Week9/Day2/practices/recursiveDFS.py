graph = {
    "A": ["B","C"],
    "B": ["A","D"],
    "C": ["A","D"],
    "D": ["B","C"]
}

def dfs(graph,node,visited):

    if node in visited:
        return

    visited.add(node)
    print(node)

    for neighbor in graph[node]:
        dfs(graph,neighbor,visited)
    

visited = set()
dfs(graph,"A",visited)

