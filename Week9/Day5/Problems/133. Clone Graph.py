from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    if not node:
        return None
    
    old_to_new = {}

    def dfs(node):
        if node in old_to_new:
            return old_to_new[node]
        
        copy = Node(node.val)
        old_to_new[node] = copy

        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy
    
    return dfs(node)

# Example Usage: 

# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Connect graph
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# Clone graph
cloned = cloneGraph(node1)

# Print results
print("Original Node:", node1.val)
print("Cloned Node:", cloned.val)

print("Original neighbors:", [n.val for n in node1.neighbors])
print("Cloned neighbors:", [n.val for n in cloned.neighbors])

# Verify deep copy
print(node1 is cloned)  # False
print(node1.neighbors[0] is cloned.neighbors[0])  # False