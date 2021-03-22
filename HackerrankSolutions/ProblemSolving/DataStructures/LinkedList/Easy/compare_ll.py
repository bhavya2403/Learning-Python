def compare_lists(llist1, llist2):
    curr1 = llist1
    curr2 = llist2
    while curr1 and curr2:
        if curr1.data != curr2.data:
            return 0
        curr1 = curr1.next
        curr2 = curr2.next

    if curr1.next is None and curr2.next is None:
        return 1
    else:
        return 0
