from typing import Optional

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    diameter = 0

    def dfs(node):
        nonlocal diameter

        if not node:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)

        diameter = max(diameter,left+right)

        return 1 + max(left,right)
    
    dfs(root)
    return diameter

# Example Usage:
if __name__ == "__main__":
    # Create a sample binary tree:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    # Test the diameter
    result = diameterOfBinaryTree(root)
    expected = 3  # Path: 4-2-5 (2 edges between 3 nodes)
    
    print("Result:", result)
    print("Expected:", expected)
    assert result == expected, f"Test failed: expected {expected}, got {result}"
    print("Test passed!") 

