import HackerrankSolutions.ProblemSolving.DataStructures.LinkedList.Easy.ll_class as c


def mergeLists(head1, head2):
    curr2 = head2
    while curr2:
        node = c.SinglyLinkedListNode(curr2.data)
        if curr2.data <= head1.data:
            node.next = head1
            head1 = node
        else:
            found = False
            curr1 = head1
            while curr1.next:
                if curr1.data <= curr2.data <= curr1.next.data:
                    node.next = curr1.next
                    curr1.next = node
                    found = True
                    break
                curr1 = curr1.next

            if not found:
                curr1.next = node

        curr2 = curr2.next

    return head1.data


ll1 = c.SinglyLinkedList()
ll1.insert_node(1)
ll1.insert_node(3)
ll1.insert_node(7)

ll2 = c.SinglyLinkedList()
ll2.insert_node(3)
ll2.insert_node(4)

print(mergeLists(ll1.head, ll2.head))
