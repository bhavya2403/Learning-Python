class stack:
    def __init__(self, items):
        self.items = items

    def reverse(self):
        return self.items[::-1]


string = stack("Bhavya")
print(string.reverse())
