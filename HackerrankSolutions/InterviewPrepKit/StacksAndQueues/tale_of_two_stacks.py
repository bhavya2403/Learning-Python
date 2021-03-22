class MyQueue(object):
    def __init__(self):
        self.arr = []

    def peek(self):
        return self.arr[0]

    def pop(self):
        self.arr.remove(self.arr[0])

    def put(self, value):
        self.arr.append(value)
