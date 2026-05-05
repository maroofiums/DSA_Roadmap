from typing import Optional,List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    res = []

    def dfs(node):
        if not node:
            return

        res.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return res

def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    res = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        dfs(node.right)
        res.append(node.val)

    dfs(root)
    return res

def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    
    res = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    dfs(root)
    return res

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return max(left_depth, right_depth) + 1

def isSymmetric(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        return isMirror(left.left, right.right) and isMirror(left.right, right.left)

    return isMirror(root.left, root.right)

if __name__ == "__main__":
    # Example usage:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print(preorderTraversal(root))  # Output: [1, 2, 3]
    print(isSameTree(root, root))  # Output: True
    print(maxDepth(root))           # Output: 2
    print(isSymmetric(root))       # Output: False
    