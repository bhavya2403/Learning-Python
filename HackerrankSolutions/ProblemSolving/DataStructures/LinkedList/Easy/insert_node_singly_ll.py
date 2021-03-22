import HackerrankSolutions.ProblemSolving.DataStructures.LinkedList.Easy.ll_class as c


def insertNodeAtPosition(head, data, position):
    count = 0
    curr = head
    while curr:
        if count == position - 1:
            node = c.SinglyLinkedListNode(data)
            node.next = curr.next
            curr.next = node
            break
        curr = curr.next
        count += 1

    return head
