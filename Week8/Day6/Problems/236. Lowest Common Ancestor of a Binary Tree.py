class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root:
        return None

    if root == p or root == q:
        return root

    left_lca = lowestCommonAncestor(root.left, p, q)
    right_lca = lowestCommonAncestor(root.right, p, q)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca else right_lca

# Example usage:
# Constructing the binary tree:
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
p = root.left  # Node with value 5
q = root.right  # Node with value 1
lca = lowestCommonAncestor(root, p, q)
print(lca.val)  # Output: 3
