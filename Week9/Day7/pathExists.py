graph = {
    "A":["B","C"],
    "B":["A","C"],
    "C":["D"],
    "D":[]
}

def hasPath(src,dst):
    visited = set()

    def dfs(node):
        if node == dst:
            return True
        visited.add(node)

        for nei in graph[node]:
            if nei not in visited:
                if dfs(nei):
                    return True
        return False
    
    return dfs(src)

print(hasPath("A","B"))
