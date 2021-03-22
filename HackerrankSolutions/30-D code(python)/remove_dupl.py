class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        # deleted = False
        # itr = head.next
        # i = 1
        # while itr:
        #     j = 0
        #     curr = head
        #     while True:
        #         if j == i:
        #             break
        #         if itr.next:
        #             if curr.data == itr.next.data:
        #                 deleted = True
        #                 break
        #         elif not itr.next and curr.data == itr.data:
        #             itr = None
        #         curr = curr.next
        #         j += 1
        #     itr = itr.next if not deleted else itr.next.next
        #     i += 1 if not deleted else 2
        #
        # return head

        itr = head
        arr = [itr.data]
        while itr.next:
            if itr.next.data in arr:
                if itr.next:
                    itr.next = itr.next.next
                else:
                    itr.next = None
            else:
                arr.append(itr.next.data)
                itr = itr.next

        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head)