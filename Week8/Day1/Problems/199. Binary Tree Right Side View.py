from typing import List,Optional
from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root:Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    
    res = []
    q = deque([root])

    while q:
        qLen = len(q)
        for i in range(qLen):
            node = q.popleft()
            if i == qLen - 1:
                res.append(node.val)

            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)

        
    return res

if __name__ == "__main__":
    # Creating tree:
    #         1
    #        / \
    #       2   3
    #        \   \
    #         5   4

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    result = rightSideView(root)
    print("Right Side View:", result)