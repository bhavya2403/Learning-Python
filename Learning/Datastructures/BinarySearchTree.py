class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()

        elements.append(self.data)

        return elements

    def search(self, value): # O(log(n))
        if self.data == value:
            return True
        elif value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        if self.left and self.right:
            return self.data + self.left.calculate_sum() + self.right.calculate_sum()
        elif self.left:
            return self.data + self.left.calculate_sum()
        elif self.right:
            return self.data + self.right.calculate_sum()
        else:
            return self.data
        # left_sum = self.left.calculate_sum() if self.left else 0
        # right_sum = self.right.calculate_sum() if self.right else 0
        # return self.data + left_sum + right_sum

    def getSize(self):
        if self.left and self.right:
            return 1 + self.left.getSize() + self.right.getSize()
        elif self.left:
            return 1 + self.left.getSize()
        elif self.right:
            return 1 + self.right.getSize()
        else:
            return 1

    def getHeight(self):
        if self.left and self.right:
            return 1 + max(self.left.getHeight(), self.right.getHeight())
        elif self.left:
            return 1 + self.left.getHeight()
        elif self.right:
            return 1 + self.right.getHeight()
        else:
            return 1

    def delete(self, value):
        # here if and elif are trying to search the node by recursively calling the func
        # once search is done we move to else
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
            else:
                return None
            # else means the value we wanna delete doesn't exist
            # but python by default will return none so no need to write
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.right is None and self.left is None:
                # means the node is a leaf node
                return None
            if self.right and self.left is None:
                # means the node has only one child which is right one
                return self.right
            if self.left and self.right is None:
                # means the node has only one child which is left one
                return self.left
                # in example below 3 has left sub tree(2) and our last if will return that left subtree

            # now in case 3 where the node has two children which can be solved by 2 methods
            min_val = self.right.find_min()
            self.data = min_val
            # after assigning the data as minimum of right subtree
            # the deleting process is reduced to case 2 or case 1 and we remove
            # the duplicate by recursively calling the function
            self.right = self.right.delete(min_val)

        return self

    def get_level(self, val, level):
        if val < self.data:
            return self.left.get_level(val, level+1)
        elif val > self.data:
            return self.right.get_level(val, level+1)
        else:
            return level

    def level_order_traversal(self):
        # level order
        arr = []
        queue = [self]
        while queue:
            node = queue.pop()
            arr.append(node.data)
            if node.left: queue.insert(0, node.left)
            if node.right: queue.insert(0, node.right)

        return arr

def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


numbers = [17, 4, 3, 2, 5, 6, 10, 21, 23, 41]
tree = build_tree(numbers)
print(tree.level_order_traversal())
print(tree.in_order_traversal())
print(tree.pre_order_traversal())
print(tree.post_order_traversal())
print(tree.calculate_sum())
print(tree.search(5))
print(tree.search(20))
print(tree.find_min())
print(tree.find_max())
tree.delete(5)
print(tree.in_order_traversal())
print(tree.getSize())
print(tree.getHeight())
print(tree.get_level(23, 0))

