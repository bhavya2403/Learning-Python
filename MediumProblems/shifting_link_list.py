# https://www.algoexpert.io/questions/Shift%20Linked%20List

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    if k >= 0:
        for i in range(k):
            curr = head
            while curr.next.next:
                curr = curr.next
            temp = curr.next
            curr.next = None

            node = LinkedList(temp.value)
            node.next = head
            head = node
    else:
        for i in range(k, 0):
            temp = head.value
            head = head.next

            curr = head
            while curr.next:
                curr = curr.next
            obj = LinkedList(temp)
            curr.next = obj
            obj.next = None

        return head.value


ll1 = LinkedList(1)
ll2 = LinkedList(2)
ll3 = LinkedList(3)
ll1.next = ll2
ll2.next = ll3
ll3.next = None

print(shiftLinkedList(ll1, -1))


# This is the class of the input linked list.

