from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    res = []

    def dfs(node):
        if not node:
            return
        
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    dfs(root)
    return res

# Example usage:
# Constructing a binary tree:
#         1
#          \
#           2
#          /
#         3

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(inorderTraversal(root))  # Output: [1, 3, 2]