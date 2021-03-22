# using array as stack


a = ['https://www.cnn.com', 'https://www.cnn.com/world', 'https://www.cnn.com/india']
print(a)
a.pop()
print(a[-1])
print(a)

from collections import deque

stack = deque()
stack.append('https://www.cnn.com')
stack.append('https://www.cnn.com/world')
stack.append('https://www.cnn.com/india')
print(stack)
stack.pop()
print(stack)


# other way to use stack


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)

    def is_empty(self):
        return len(self.container) == 0


def reverse_string(string):
    stack = Stack()
    for i in string:
        stack.push(i)
    rstr = ''
    while stack.size() != 0:
        rstr += stack.pop()
    return rstr


print(reverse_string("my name is bhavya"))
s = 'bhavya'
print(s.endswith('a'))
s.replace('y', ' ')
print(s)
