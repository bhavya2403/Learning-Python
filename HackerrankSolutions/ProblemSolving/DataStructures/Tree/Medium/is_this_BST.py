""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check(root):
    elements = []
    if root.left:
        elements += check(root.left)

    elements += [root.data]

    if root.right:
        elements += check(root.right)

    return elements

def check_binary_search_tree_(root):
    elements = check(root)
    if elements == sorted(elements):
        for i, element in enumerate(sorted(elements)):
            try:
                if elements[i+1] == element:
                    return False
            except:
                break
        return True
    return False