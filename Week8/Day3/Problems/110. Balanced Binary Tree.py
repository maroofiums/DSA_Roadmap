from typing import Optional

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def dfs(node):
        if not node:
            return 0   # fix here
            
        left = dfs(node.left)
        if left == -1:
            return -1
            
        right = dfs(node.right)
        if right == -1:
            return -1
            
        if abs(left - right) > 1:
            return -1
            
        return 1 + max(left, right)
        
    return dfs(root) != -1

if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    print(isBalanced(None, root1))  # Output: True

    # Example 2
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    root2.right.right = TreeNode(3)
    
    print(isBalanced(None, root2))  # Output: False
    