import HackerrankSolutions.ProblemSolving.DataStructures.LinkedList.Easy.ll_class as c


def insertNodeAtHead(head, data):
    node = c.SinglyLinkedListNode(data)
    node.next = head
    head = node

    return head
