class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def rotate(self, list, d):
        self.head = None
        for data in list:
            self.insert_at_end(data)

        for i in range(0, d):
            self.insert_at_end(self.head.data)
            self.head = self.head.next

        arr = []
        itr = self.head
        while itr:
            arr.append(itr.data)
            itr = itr.next

        return arr


ll = LinkedList()
print(ll.rotate([1,2,3,4,5], 4))
