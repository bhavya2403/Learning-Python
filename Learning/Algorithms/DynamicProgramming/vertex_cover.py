class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def vertexCover(root):
    dataLevel = {}

    def assigning(root):
        if not root.children:
            dataLevel[root.data] = 0
            return
        for child in root.children:
            assigning(child)
        dataLevel[root.data] = 1 + min(dataLevel[child.data] for child in root.children)
    assigning(root)

    ans1 = set()
    ans2 = set()
    for data in dataLevel:
        if dataLevel[data]%2:
            ans1.add(data)
        if not dataLevel[data]%2:
            ans2.add(data)

    return ans1, ans2

def makingTree():
    root = TreeNode(-15)
    five = TreeNode(5)
    six = TreeNode(6)
    root.children = [five, six]
    eight = TreeNode(8)
    one = TreeNode(1)
    five.children = [eight, one]
    one.children = [TreeNode(-11)]
    eight.children = [TreeNode(2), TreeNode(6)]
    nine = TreeNode(9)
    three = TreeNode(3)
    six.children = [three, nine]
    three.children = [TreeNode(11)]
    zero = TreeNode(0)
    nine.children = [zero]
    minOne = TreeNode(-1)
    zero.children = [TreeNode(4), minOne]
    minOne.children = [TreeNode(10)]

    return root

root = makingTree()
print(vertexCover(root))