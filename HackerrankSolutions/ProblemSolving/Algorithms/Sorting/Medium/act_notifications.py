# curr = head
# while curr.next.next:
#     curr = curr.next
# temp = curr.next
# curr.next = None
#
# node = LinkedList(temp.value)
# node.next = head
# head = node

class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    # initializing a list
    def __init__(self, node=None):
        self.head = node

    # method for inserting a new node at the beginning of the Linked List (at the head)
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def remove_by_value(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def insert_at(self, d, index, data):
        if index < 0 or index >= d-1:
            raise Exception("Invalid Index")
        elif index == 0:
            self.insert_at_beginning(data)
            return
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    # we are at previous element of new element and we'll create new node
                    node = Node(data, itr.next)
                    itr.next = node
                    # this itr.next is address to new node
                    break
                itr = itr.next
                count += 1

def activityNotifications(n, expenditure, d):
    not_count = 0
    i = d
    j = d-1
    ll = LinkedList()
    arr = sorted(expenditure[:d])
    while j>=0:
        j -= 1
        ll.insert_at_beginning(arr[j])
    expenditure[:d] = arr
    while True:
        num = expenditure[i]
        if d % 2 == 1:
            median = arr[d // 2]
        else:
            median = (arr[d // 2] + arr[(d // 2) - 1]) / 2

        if num >= 2 * median:
            not_count += 1

        if i == n - 1:
            break

        ll.remove_by_value(expenditure[i-d])
        # arr.remove(expenditure[i - d])
        inserted = False
        for j in range(d - 1):
            if arr[j] > num:
                inserted = True
                ll.insert_at(d, j-1, num)
                # arr.insert(j - 1, num)
        if not inserted:
            # arr.append(num)
            ll.insert_at(d, d-2, num)
        i += 1
        print(not_count)
    return not_count


nd = input().split()

n = int(nd[0])

d = int(nd[1])

expenditure = list(map(int, input().rstrip().split()))


print(activityNotifications(n, expenditure, d))