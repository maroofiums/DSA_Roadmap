from typing import Optional

class TreeNode:
    def __init__(self, val = 0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


def inOrderTraversal(root: Optional[TreeNode]) -> list[int]:
    res = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    dfs(root)
    return res

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print(inOrderTraversal(root))
    