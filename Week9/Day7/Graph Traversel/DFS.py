graph = {
    "A":["B","C"],
    "B":["A","C"],
    "C":["D"],
    "D":[]
}

visited = set()

def dfs(node):
    if node in visited:
        return 
    
    print(node)
    visited.add(node)

    for nei in graph[node]:
        dfs(nei)


dfs("A")
