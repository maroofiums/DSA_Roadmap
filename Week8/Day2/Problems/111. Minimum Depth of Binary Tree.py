from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    if not root.left:
        return 1 + minDepth(root.right)

    if not root.right:
        return 1 + minDepth(root.left)

    return 1 + min(minDepth(root.left), minDepth(root.right))


# Example usage:
if __name__ == "__main__":
    optional_tree = TreeNode(1)
    optional_tree.left = TreeNode(2)
    optional_tree.right = TreeNode(3)

    print(minDepth(optional_tree))  # Output: 2
