from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    res = []
    q = deque([root])

    while q:
        level = []
        qLen = len(q)

        for _ in range(qLen):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
    
            if node.right:
                q.append(node.right)
        if level:
            res.append(level)

    return res

if __name__ == "__main__":
    # Example usage:
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]
