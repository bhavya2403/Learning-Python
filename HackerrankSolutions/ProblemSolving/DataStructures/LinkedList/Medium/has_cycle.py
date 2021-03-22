def has_cycle(head):
    arr = []
    itr = head
    while itr:
        if itr in arr:
            return 1
        arr.append(itr)
        itr = itr.next
    return 0


def has_cycle1(head):
    if head is None:
        return 0
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return 1

    return 0
