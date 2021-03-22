def check(root):
    elements = []
    if root.left:
        elements += check(root.left)

    elements += [root.data]

    if root.right:
        elements += check(root.right)

    return elements


def checkBST(root):
    elements = check(root)
    if elements == sorted(elements):
        for i, element in enumerate(sorted(elements)):
            try:
                if elements[i + 1] == element:
                    return False
            except:
                break
        return True
    return False