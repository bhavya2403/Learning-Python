class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


def height(root):
    if root.left and root.right:
        return 1 + max(height(root.left), height(root.right))
    elif root.left and not root.right:
        return 1 + height(root.left)
    elif root.right and not root.left:
        return 1 + height(root.right)
    else:
        return 0
