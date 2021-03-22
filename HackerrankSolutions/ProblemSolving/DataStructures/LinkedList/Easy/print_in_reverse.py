import HackerrankSolutions.ProblemSolving.DataStructures.LinkedList.Easy.ll_class as c


def reversePrint(head):
    ll1 = c.SinglyLinkedList()
    curr = head
    while curr:
        node = c.SinglyLinkedListNode(curr.data)
        node.next = ll1.head
        ll1.head = node
        curr = curr.next

    curr = ll1.head
    while curr:
        print(curr.data)
        curr = curr.next


ll = c.SinglyLinkedList()
ll.insert_node(1)
ll.insert_node(2)
ll.insert_node(3)
ll.insert_node(4)
print(reversePrint(ll.head))
