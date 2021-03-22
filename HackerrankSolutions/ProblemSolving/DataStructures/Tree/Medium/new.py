#          1                     1                          1
#         / \                   / \                        / \
#        /   \                 /   \                      /   \
#       2     3    [s]        2     3                    2     3
#      /     /                \     \                    \     \
#     /     /                  \     \                    \     \
#    4     5          ->        4     5          ->        4     5
#   /     / \                  /     / \                  /     / \
#  /     /   \                /     /   \                /     /   \
# 6     7     8   [s]        6     7     8   [s]        6     7     8
# \          / \            /           / \              \         / \
#  \        /   \          /           /   \              \       /   \
#   9      10   11        9           11   10              9     10   11
# [1,2,3,4,-1,5,-1,6,-1,-1,-1,7,8,-1,-1,-1,9,-1,-1,10,11,-1,-1,-1,-1,-1,-1]
# 4,5,8,9,10,11,

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def in_order(self):
        elements = []
        if self.left:
            elements += self.left.in_order()
        elements += self.data
        if self.right:
            elements += self.right.in_order()
        return elements

def swapNodes(n, indexes, queries):
    root = BinaryTree(1)


#
# Write your code here.
#
