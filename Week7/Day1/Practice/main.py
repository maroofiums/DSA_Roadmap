class TreeNode:
    def __init__(self,val = 0,left = None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    
    def traverse(self):
        print(self.val)
        if self.left:
            self.left.traverse()
        if self.right:
            self.right.traverse()

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.traverse()
    