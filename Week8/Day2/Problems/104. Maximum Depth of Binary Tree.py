from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return 1 + max(left_depth, right_depth)

# Example usage:
if __name__ == "__main__":
    optional_tree = TreeNode(1)
    optional_tree.left = TreeNode(2)
    optional_tree.right = TreeNode(3)
    optional_tree.left.left = TreeNode(4)
    optional_tree.left.right = TreeNode(5)

    print(maxDepth(optional_tree))  # Output: 3
    