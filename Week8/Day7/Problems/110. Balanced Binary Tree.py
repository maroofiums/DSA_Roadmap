from typing import Optional

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isBalanced(root: Optional[TreeNode]) -> bool:
    def dfs(node):
        if not node:
            return 0
        
        left = dfs(node.left)
        if left == -1:
            return -1
        
        right = dfs(node.right)
        if right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1
        
        return 1 + max(left,right)
    
    return dfs(root) != -1

# Example Usage:
if __name__ == "__main__":
    # Test Case 1: Balanced Tree
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    result1 = isBalanced(root1)
    expected1 = True
    print("Test 1 - Balanced Tree:")
    print("Result:", result1)
    print("Expected:", expected1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print("Test 1 passed!\n")
    
    # Test Case 2: Unbalanced Tree
    #   1
    #  /
    # 2
    #  \
    #   3
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.right = TreeNode(3)
    
    result2 = isBalanced(root2)
    expected2 = False
    print("Test 2 - Unbalanced Tree:")
    print("Result:", result2)
    print("Expected:", expected2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print("Test 2 passed!\n")
    
    # Test Case 3: Empty Tree
    root3 = None
    result3 = isBalanced(root3)
    expected3 = True
    print("Test 3 - Empty Tree:")
    print("Result:", result3)
    print("Expected:", expected3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print("Test 3 passed!")