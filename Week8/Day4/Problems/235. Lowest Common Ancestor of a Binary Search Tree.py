class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root:
        return None

    if root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)

    if root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)

    return root

if __name__ == "__main__":
    # Example usage:
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    p = root.left  # Node with value 2
    q = root.right  # Node with value 8

    lca = lowestCommonAncestor(root, p, q)
    print(f"The lowest common ancestor of {p.val} and {q.val} is: {lca.val}")
    