class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    left_tree = isSameTree(p.left, q.left)
    right_tree = isSameTree(p.right, q.right)
    return left_tree and right_tree

# Example usage:
# Create two identical trees
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)
print(isSameTree(tree1, tree2))  # Output: True