from typing import Optional

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    diameter = 0

    def height(node):
        
        nonlocal diameter
        if not node:
            return 0
        
        left = height(node.left)
        right = height(node.right)

        diameter = max(diameter, left + right)

        return 1 + max(left, right)
    height(root)
    return diameter

# Example usage:
# Constructing the binary tree:
#         1
#        / \
#       2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(diameterOfBinaryTree(root))  # Output: 2 (path is 2 -> 1 -> 3)
