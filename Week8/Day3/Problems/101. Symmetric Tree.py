from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return isMirror(left.left, right.right) and isMirror(left.right, right.left)

    return isMirror(root.left, root.right)

# Example usage:
# Constructing a symmetric tree
#         1
#        / \
#       2   2
#      / \ / \
#     3  4 4  3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
print(isSymmetric(root))  # Output: True
