class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def LIS(root):
    if not root:
        return 0

    sizeExc = LIS(root.left) + LIS(root.right)

    sizeInc = 1
    if root.left:
        sizeInc += LIS(root.left.left) + LIS(root.left.right)
    if root.right:
        sizeInc += LIS(root.right.left) + LIS(root.right.right)

    return max(sizeExc, sizeInc)

def makingTree():
    root = TreeNode(-15)
    five = TreeNode(5)
    six = TreeNode(6)
    root.left = five
    root.right = six
    eight = TreeNode(8, TreeNode(2), TreeNode(6))
    one = TreeNode(1, TreeNode(-11), None)
    five.left = eight
    five.right = one
    nine = TreeNode(9)
    three = TreeNode(3,TreeNode(11),None)
    six.left = three
    six.right = nine
    zero = TreeNode(0)
    nine.left = zero
    minOne = TreeNode(-1, TreeNode(10), None)
    zero.left = TreeNode(4)
    zero.right = minOne

    return root

root = makingTree()
print(LIS(root))
