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


def reverse(head):
    head1 = None
    curr = head
    while curr:
        if head1 is None:
            head1 = DoublyLinkedListNode(curr.data)
        else:
            node = DoublyLinkedListNode(curr.data)
            node.next = head1
            head1.prev = node
            node.prev = None
            head1 = node
        curr = curr.next

    return head1