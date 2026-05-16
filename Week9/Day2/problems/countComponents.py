graph = {
    0:[1],
    1:[0],
    2:[3],
    3:[2],
    4:[]
}

def count_components(graph):
    visited = set()
    count = 0

    def dfs(node):
        if node in visited:
            return
        
        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor)

    
    for node in graph:
        if node not in visited:
            count += 1
            dfs(node)

    return count


print(count_components(graph))