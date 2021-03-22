class LinkedListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = LinkedListNode(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = LinkedListNode(data)


def jumpingOnClouds(c, k):
    temp = c.pop()
    ll = LinkedList()
    for i in c:
        ll.insert_at_end(i)

    curr = ll.head
    while curr.next:
        curr = curr.next
    curr.next = LinkedListNode(temp)
    curr.next.next = ll.head

    e = 100
    curr = ll.head
    again = 0
    while again == 0:
        if curr.data == 1:
            e -= 3
        else:
            e -= 1
        for i in range(k):
            curr = curr.next
        if curr == ll.head:
            again = 1

    return e


print(jumpingOnClouds([0,0,1,0,0,1,1,0], 2))