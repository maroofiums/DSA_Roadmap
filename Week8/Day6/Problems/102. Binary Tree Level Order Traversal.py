from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []
    
    result = []
    q = deque([root])

    while q:
        qLen = len(q)
        level = []
        for _ in range(qLen):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level)
    return result

if __name__ == "__main__":
    # Example usage:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(levelOrder(root))  # Output: [[1], [2, 3], [4, 5]]