def preOrder(root):
    def calulate(root):
        elements = [root.info]
        if root.left:
            elements += calulate(root.left)
        if root.right:
            elements += calulate(root.right)

        return elements

    elements = calulate(root)
    for element in elements:
        print(str(element), end=' ')