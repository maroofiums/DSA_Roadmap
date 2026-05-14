class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root: 'TreeNode',p:'TreeNode',q:'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q:
        return root
    
    left = lowestCommonAncestor(root.left,p,q)
    right = lowestCommonAncestor(root.right,p,q)

    if left and right:
        return root
    
    return left or right

# Example Usage:
if __name__ == "__main__":
    # Create a sample binary tree:
    #     3
    #    / \
    #   5   1
    #  / \ / \
    # 6  2 0  8
    #   / \
    #  7   4
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    
    # Define nodes for testing
    node5 = root.left
    node1 = root.right
    node6 = root.left.left
    node4 = root.left.right.right
    
    # Test Case 1: LCA of 5 and 1 should be 3
    result1 = lowestCommonAncestor(root, node5, node1)
    expected1 = root
    print("Test 1 - LCA of 5 and 1:")
    print("Result:", result1.val if result1 else None)
    print("Expected:", expected1.val if expected1 else None)
    assert result1 == expected1, f"Test 1 failed: expected {expected1.val}, got {result1.val if result1 else None}"
    print("Test 1 passed!\n")
    
    # Test Case 2: LCA of 5 and 4 should be 5
    result2 = lowestCommonAncestor(root, node5, node4)
    expected2 = node5
    print("Test 2 - LCA of 5 and 4:")
    print("Result:", result2.val if result2 else None)
    print("Expected:", expected2.val if expected2 else None)
    assert result2 == expected2, f"Test 2 failed: expected {expected2.val}, got {result2.val if result2 else None}"
    print("Test 2 passed!\n")
    
    # Test Case 3: LCA of 6 and 4 should be 5
    result3 = lowestCommonAncestor(root, node6, node4)
    expected3 = node5
    print("Test 3 - LCA of 6 and 4:")
    print("Result:", result3.val if result3 else None)
    print("Expected:", expected3.val if expected3 else None)
    assert result3 == expected3, f"Test 3 failed: expected {expected3.val}, got {result3.val if result3 else None}"
    print("Test 3 passed!")