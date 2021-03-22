class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def get_level(self, root, value, level):
        if value < root.data:
            return self.get_level(root.left, value, level+1)
        elif value > root.data:
            return self.get_level(root.right, value, level+1)
        else:
            return level

    def inOrder(self, root):
        elements = []
        if root.left:
            elements += self.inOrder(root.left)

        elements.append(root.data)

        if root.right:
            elements += self.inOrder(root.right)

        return elements

    def levelOrder(self, root):
        elements = self.inOrder(root)
        levels = []
        for element in elements:
            levels.append(self.get_level(root, element, 0))

        size = len(levels)
        for i in range(size-1):
            swapped = False
            for j in range(size-i-1):
                if levels[j] > levels[j+1]:
                    (levels[j], levels[j+1]) = (levels[j+1], levels[j])
                    (elements[j], elements[j + 1]) = (elements[j + 1], elements[j])
                    swapped = True

            if not swapped:
                break

        s = ''
        for element in elements:
            s += ' ' + str(element)
        print(s[1:])


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)