from typing import Optional

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root: Optional[TreeNode]) -> int:
    ans = float("-inf")

    def dfs(node):

        nonlocal ans

        if not node:
            return 0

        left = max(dfs(node.left),0)
        right = max(dfs(node.right),0)

        current = node.val + left + right

        ans = max(ans,current)

        return node.val + max(left,right)
    
    dfs(root)

    return ans

# Example usage:
# Constructing the binary tree:
#         1
#        / \
#       2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(maxPathSum(root))  # Output: 6 (path is 2 -> 1 -> 3)
