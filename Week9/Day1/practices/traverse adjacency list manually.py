graph = {
    "A":["B","C"],
    "B":["A","D"],
    "C":["A"],
    "D":["B"]
}

for node in graph:
    print(f"{node} -> {graph[node]}")