# https://www.youtube.com/watch?v=xUHohVsidLA&t=444s

class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left= left
        self.right =right

def formingTree():
    four = BinaryTreeNode(4, BinaryTreeNode(8), BinaryTreeNode(9))
    two = BinaryTreeNode(2, four, BinaryTreeNode(5))
    three = BinaryTreeNode(3, BinaryTreeNode(6), BinaryTreeNode(7))
    root = BinaryTreeNode(1, two, three)
    return root


max_path = 0
def solve(node):
    global max_path
    if not node.left and not node.right:
        return node.data
    if not node.right:
        return node.data + solve(node.left)
    if not node.left:
        return node.data + solve(node.right)

    a = solve(node.right)
    b = solve(node.left)
    if node.data + a + b > max_path:
        max_path = a + b + node.data
    return node.data + max(a,b)

root = formingTree()
solve(root)
print(max_path)
