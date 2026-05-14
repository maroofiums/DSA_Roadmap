from typing import Optional

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return 1 + max(
        left,right
    )

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
    
    # Test the maximum depth
    result = maxDepth(root)
    expected = 3
    
    print("Result:", result)
    print("Expected:", expected)
    assert result == expected, f"Test failed: expected {expected}, got {result}"
    print("Test passed!") 