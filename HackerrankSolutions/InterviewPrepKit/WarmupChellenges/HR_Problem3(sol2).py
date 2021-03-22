# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    # initializing a list
    def __init__(self, node=None):
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        # loop until itr.next has some value
        while itr.next:
            itr = itr.next
        # now itr.next is none so assign it to new node
        itr.next = Node(data, None)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            count = 0
            itr = self.head
            while itr:
                # index-1 is the previous element which is going to get removed from list
                if count == index - 1:
                    # modifying the links
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count += 1

    def remove_3zeros(self):
        try:
            if self.head.data == 0:
                if self.head.next.data == 0 and self.head.next.next.data == 0:
                    self.head = self.head.next
            itr = self.head
            while itr.next:
                if itr.data == 0:
                    if itr.next.data == 0 and itr.next.next.data == 0:
                        itr.next = itr.next.next
                itr = itr.next
        except:
            return 2

    def remove_1s(self):
        if self.head.data == 1:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == 1:
                itr.next = itr.next.next
            itr = itr.next

    def print(self):
        if self.head is None:
            print("list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ","
            itr = itr.next
        print(llstr)


c = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
ll = LinkedList()
ll.insert_values(c)
ll.print()
ll.remove_3zeros()
ll.print()
ll.remove_1s()
ll.print()
print((ll.get_length()) - 1)
