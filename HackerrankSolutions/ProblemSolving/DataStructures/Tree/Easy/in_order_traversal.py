def inOrder(root):
    def calulate(root):
        elements = []
        if root.left:
            elements += calulate(root.left)
        elements.append(root.info)
        if root.right:
            elements += calulate(root.right)

        return elements

    elements = calulate(root)
    for element in elements:
        print(str(element), end=' ')