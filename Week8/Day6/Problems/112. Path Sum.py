from typing import Optional

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == targetSum
    
    remaining_sum = targetSum - root.val
    return (
        hasPathSum(root.left, remaining_sum) or
        hasPathSum(root.right, remaining_sum)
    )

# Example usage:
# Constructing the binary tree:
#         5
#        / \
#       4   8
#      /   / \
#     11  13  4
#    /  \      \
#   7    2      1
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
targetSum = 22
print(hasPathSum(root, targetSum))  # Output: True