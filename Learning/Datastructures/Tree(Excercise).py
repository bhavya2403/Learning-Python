
input = input("What do u want to print?\n 1. Names\n 2. Designation\n 3. Both : ")


class TreeNode:
    def __init__(self, data, designation):
        self.data = data
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree_3(self):
        spaces = ' ' * self.get_level() * 3
        prefix = '|--' if self.parent else ''
        print(spaces + prefix + self.data + ' (' + self.designation + ')')
        for child in self.children:
            child.print_tree_3()

    def print_tree_1(self):
        spaces = ' ' * self.get_level() * 3
        prefix = '|--' if self.parent else ''
        print(spaces + prefix + self.data)
        for child in self.children:
            child.print_tree_1()

    def print_tree_2(self):
        spaces = ' ' * self.get_level() * 3
        prefix = '|--' if self.parent else ''
        print(spaces + prefix + self.designation)
        for child in self.children:
            child.print_tree_2()


def build_tree():
    root = TreeNode("Nilpul", "CEO")

    chinmay = TreeNode("Chinmay", "CTO")
    root.add_child(chinmay)
    vishwa = TreeNode("Vishwa", "Infrastructure Head")
    chinmay.add_child(vishwa)
    vishwa.add_child(TreeNode("Dhaval", "Cloud Manager"))
    vishwa.add_child(TreeNode("Abhisek", "App Manager"))

    gels = TreeNode("Gels", "Application Head")
    root.add_child(gels)
    gels.add_child(TreeNode("peter", "Recruitment manager"))
    gels.add_child(TreeNode("Waqas", "Policy Manager"))

    if input == "3":
        root.print_tree_3()
    elif input == "2":
        root.print_tree_2()
    elif input == "1":
        root.print_tree_1()
    else:
        print("Invalid Input")


build_tree()
