def inOrder(root):
    def calulate(root):
        elements = []
        if root.left:
            elements += calulate(root.left)
        if root.right:
            elements += calulate(root.right)
        elements.append(root.info)

        return elements

    elements = calulate(root)
    for element in elements:
        print(str(element), end=' ')