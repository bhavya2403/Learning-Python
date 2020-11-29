class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def sortedInsert(head, data):
    node = DoublyLinkedListNode(data)
    if data < head.data:
        node.next = head
        head.prev = node
        node.prev = None
        head = node
        return head
    curr = head
    while curr:
        if curr.next is None:
            curr.next = node
            node.prev = curr
            node.next = None
            break
        if curr.data < data < curr.next.data or curr.data == data:
            node.next = curr.next
            node.prev = curr
            curr.next = node
            curr.next.prev = node
            break
        curr = curr.next

    return head