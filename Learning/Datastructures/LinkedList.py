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

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        elif index == 0:
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

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
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

    def insert_after(self, data_after, data_to_insert):
        if self.head.data == data_after:
            node = Node(data_to_insert, self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

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

    def delete_list(self):
        self.head = None


ll = LinkedList()
ll.insert_at_beginning(5)
ll.insert_at_end(10)
ll.print()

ll1 = LinkedList()
ll1.insert_values(["orange", "banana", "apple"])
ll1.print()
ll1.remove_at(1)
ll1.print()
ll1.insert_at(1, "banana")
ll1.print()
print(ll1.get_length())
ll1.insert_after("banana", "kiwi")
ll1.print()
ll1.remove_by_value("kiwi")
ll1.print()
