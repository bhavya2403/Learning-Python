class LLNode:
    def __init__(self, data, next=None, wins=0):
        self.data = data
        self.next = next
        self.wins = wins

class LL:
    def __init__(self):
        self.head = None

    # def insertBeg(self, data, wins):
    #     self.head, self.head.next = LLNode(data, wins), self.head

    def insertEnd(self, data, ptrLast, wins):
        ptrLast.next = LLNode(data, None, wins)

    def removeBeg(self):
        self.head = self.head.next

    def makeLL(self, arr):
        self.head = LLNode(arr[0])
        ptrLast = self.head
        for i in range(1, len(arr)):
            self.insertEnd(arr[i], ptrLast, 0)
            ptrLast = ptrLast.next

        return ptrLast

def arrEle(arr, k):
    ll = LL()
    ptrLast = ll.makeLL(arr)

    count = 0
    while True:
        data, wins = ll.head.data, ll.head.wins
        ll.removeBeg()

        if data > ll.head.data:
            data, ll.head.data = ll.head.data, data
            wins, ll.head.wins = ll.head.wins, wins

        ll.head.wins += 1
        ll.insertEnd(data, ptrLast, wins)
        ptrLast = ptrLast.next

        count += 1
        if ll.head.wins == k:
            break

    return count

print(arrEle([2,1,3,4,5], 2))