class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LL:
    def __init__(self, head=None):
        self.head = head

def middle(start, end):
    if not start:
        return None

    slow = start
    fast = start.next
    while fast.next!=end or fast.next.next!=end:
        fast = fast.next.next
        slow = slow.next

    return slow

def binarySearch(head, value):
    start, end = head, None
    while True:
        mid = middle(start, end)
        if mid.data == value:
            return mid
        elif mid.data < value:
            start = mid.next
        else:
            end = mid

        if not (not end or end != start):
            return 'Not found'