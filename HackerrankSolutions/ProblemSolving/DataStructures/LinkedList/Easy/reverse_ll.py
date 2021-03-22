import HackerrankSolutions.ProblemSolving.DataStructures.LinkedList.Easy.ll_class as c

def reverse(head):
    ll1 = c.SinglyLinkedList()
    curr = head
    while curr:
        node = c.SinglyLinkedListNode(curr.data)
        node.next = ll1.head
        ll1.head = node
        curr = curr.next

    return ll1.head