def get_length(head):
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next

    return count


def getNode(head, positionFromTail):
    size = get_length(head)
    count = 0
    index = size - int(positionFromTail) - 1
    curr = head
    while curr:
        if count == index:
            return curr.data
        curr = curr.next
        count += 1
