def deleteNode(head, position):
    if position == 0:
        head = head.next
        return head
    else:
        count = 0
        curr = head
        while curr:
            if count == position-1:
                curr.next = curr.next.next
                return head
            count += 1
            curr = curr.next
