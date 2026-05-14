from collections import deque
from typing import Optional,List

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderTraversal(root:Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    res = []
    q = deque([root])

    while q:
        qLen = len(q)
        level = []

        for _ in range(qLen):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        
        res.append(level)

    return res

# Example Usage:
if __name__ == "__main__":
    # Create a sample binary tree:
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    # Test the level order traversal
    result = levelOrderTraversal(root)
    expected = [[3], [9, 20], [15, 7]]
    
    print("Result:", result)
    print("Expected:", expected)
    assert result == expected, f"Test failed: expected {expected}, got {result}"
    print("Test passed!")
