import HackerrankSolutions.ProblemSolving.DataStructures.LinkedList.Easy.ll_class as c


def insertNodeAtTail(head, data):
    if head is None:
        head = c.SinglyLinkedListNode(data)
    else:
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = c.SinglyLinkedListNode(data)

    return head

