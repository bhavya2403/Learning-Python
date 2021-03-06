class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self, root):
        if root.left and root.right:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        elif root.left and not root.right:
            return 1 + self.getHeight(root.left)
        elif root.right and not root.left:
            return 1 + self.getHeight(root.right)
        else:
            return 0