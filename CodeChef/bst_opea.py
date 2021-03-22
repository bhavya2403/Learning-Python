class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def min_val(self):
        if self.left:
            return self.left.min_val()
        else:
            return self.data

    def insert(self, data, p):
        if data < self.data:
            if self.left:
                self.left.insert(data, (2*p))
            else:
                self.left = BinarySearchTree(data)
                print(2*p)

        elif data > self.data:
            if self.right:
                self.right.insert(data, (2*p)+1)
            else:
                self.right = BinarySearchTree(data)
                print((2*p)+1)


    def delete(self, data, once, p):
        if data < self.data:
            self.left = self.left.delete(data, False, (2*p))

        elif data > self.data:
            self.right = self.right.delete(data, False, (2*p)+1)

        else:
            if not once:
                print(p)
            if self.left is None and self.right is None:
                return None
            elif self.left and self.right is None:
                return self.left
            elif self.right and self.left is None:
                return self.right
            else:
                if not once:
                    print(p)
                min_val = self.right.min_val()
                self.data = min_val
                self.right = self.right.delete(min_val, True, p)

        return self

cases = int(input())
init = input().split()
root = BinarySearchTree(int(init[1]))
print(1)

for i in range(cases-1):
    arr = input().split()
    if arr[0] == 'i':
        root.insert(int(arr[1]), 1)
    else:
        root.delete(int(arr[1]), False, 1)

