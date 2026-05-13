from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    diameter = 0

    def depth(node):
        nonlocal diameter
        if not node:
            return 0

        left_depth = depth(node.left)
        right_depth = depth(node.right)

        diameter = max(diameter, left_depth + right_depth)

        return max(left_depth, right_depth) + 1

    depth(root)
    return diameter

if __name__ == "__main__":
    # Example usage:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(diameterOfBinaryTree(root))  # Output: 3