graph = {
    "A":["B","D"],
    "B":["C"],
    "C":[],
    "D":[]
}

def hasPath(graph,src,dst):

    if src == dst:
        return True
    
    for neighbor in graph[src]:
        if hasPath(graph,neighbor,dst):
            return True

    return False

print(hasPath(graph,"A","D"))