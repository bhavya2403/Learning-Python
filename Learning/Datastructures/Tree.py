class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = '|--' if self.parent else ''
        print(spaces + prefix + self.data)
        for child in self.children:
            child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        # root don't have parents so won't loop through the code and return value 0
        # laptop has 1 parent so will return 1
        while p:
            level += 1
            p = p.parent

        return level


root = TreeNode("Electronics")
laptop = TreeNode("Laptop")
laptop.add_child(TreeNode("Mac"))
laptop.add_child(TreeNode("Dell"))
cellphone = TreeNode("CellPhone")
cellphone.add_child(TreeNode("Samsung"))
cellphone.add_child(TreeNode("Apple"))
root.add_child(laptop)
root.add_child(cellphone)
root.print_tree()
print(root.get_level())
print(laptop.get_level())

