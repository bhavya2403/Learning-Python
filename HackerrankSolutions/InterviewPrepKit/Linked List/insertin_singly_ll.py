class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


def insertNodeAtPosition(head, data, position):
    count = 0
    curr = head
    while curr:
        if count == position - 1:
            node = SinglyLinkedListNode(data)
            node.next = curr.next
            curr.next = node
            break
        curr = curr.next
        count += 1

    return head
