# full binary tree: if height=h, total ele.= 2^(h+1)-1
# complete binary tree: is a full binary tree till height h-1 and array representation
#                       should not have gaps
# heap is a complete binary tree(duplicates allowed)
# array-representation or bin tree: starts from index 1, left: at index 2*i, right at 2*i+1
# max heap: (binary search tree: left < info < right) info > (left and right)
# min heap: info < (left and right)


class MaxHeap:
    def __init__(self):
        self.heap = [0]
        self.deleted = []

    def insert(self, value):  # direction of adjustment upwards(tc : O(1) to O(log(n))
        if self.heap == [0]:
            self.heap.append(value)
        else:
            size = len(self.heap)
            # make value child of left bottom corner (still it is not a heap)
            self.heap.append(value)
            i = size
            while True:
                if self.heap[i] > self.heap[i // 2]:
                    self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
                i = i // 2

                if self.heap[i] <= self.heap[i // 2] or i == 1:
                    break

    def delete(self):  # direction of adjustment downwards (tc: O(1) to O(log(n))
        size = len(self.heap)
        self.deleted.insert(0, self.heap[1])
        self.heap[1] = self.heap[size - 1]
        self.heap.pop()
        i = 1
        if size == 3 or size == 2:
            return
        while True:  # till index is 6
            if 2 * i == size - 2:
                if self.heap[2 * i] > self.heap[i]:
                    self.heap[2 * i], self.heap[i] = self.heap[i], self.heap[2 * i]
                break
            elif 2 * i > size - 2:
                break
            else:
                maxim = max(self.heap[2 * i], self.heap[2 * i + 1])
                if maxim <= self.heap[i]:
                    break
                elif maxim == self.heap[2 * i]:
                    self.heap[2 * i], self.heap[i] = self.heap[i], self.heap[2 * i]
                    i = 2 * i
                elif maxim == self.heap[2 * i + 1]:
                    self.heap[2 * i + 1], self.heap[i] = self.heap[i], self.heap[2 * i + 1]
                    i = 2 * i + 1


def heapify(arr):  # O(n) (converting array to max-heap)
    size = len(arr)
    n = 0
    while True:
        if size < (2 ** (n + 1)) - 1:
            break
        n += 1
    i = (2 ** n) - 1
    arr = [0] + arr

    while i >= 1:
        j = i
        while True:
            if 2 * j > size:
                break
            if 2 * j == size:
                if arr[2 * j] > arr[j]:
                    arr[2 * j], arr[j] = arr[j], arr[2 * j]
                break

            maxim = max(arr[2 * j], arr[2 * j + 1])
            if arr[j] > maxim:
                break
            if maxim == arr[2 * j]:
                arr[2 * j], arr[j] = arr[j], arr[2 * j]
                j = 2 * j
            elif maxim == arr[2 * j + 1]:
                arr[2 * j + 1], arr[j] = arr[j], arr[2 * j + 1]
                j = 2 * j + 1
        i -= 1

    return arr


def heap_sort(arr):  # O(nlog(n))
    # create a heap from array
    heap = heapify(arr)  # O(n), alternatively we can use next 3 lines
    # heap = [0, arr[0]]
    # for i in range(1, len(arr)):  # O(nlog(n))
    #     insert(arr[i])
    size = len(arr)
    # delete one by one and elements will get sorted
    while size>=3:  # O(nlog(n))
        heap[1], heap[size] = heap[size], heap[1]
        i = 1
        if size == 3 or size == 2:
            if heap[1] > heap[2]:
                heap[1], heap[2] = heap[2], heap[1]
            return heap[1:]
        while True:
            if 2 * i == size - 2:
                if heap[2 * i] > heap[i]:
                    heap[2 * i], heap[i] = heap[i], heap[2 * i]
                break
            elif 2 * i > size - 2:
                break
            else:
                maxim = max(heap[2 * i], heap[2 * i + 1])
                if maxim <= heap[i]:
                    break
                elif maxim == heap[2 * i]:
                    heap[2 * i], heap[i] = heap[i], heap[2 * i]
                    i = 2 * i
                elif maxim == heap[2 * i + 1]:
                    heap[2 * i + 1], heap[i] = heap[i], heap[2 * i + 1]
                    i = 2 * i + 1
        size -= 1

heap1 = MaxHeap()
heap1.insert(50)
heap1.insert(30)
heap1.insert(20)
heap1.insert(15)
heap1.insert(10)
heap1.insert(8)
heap1.insert(16)
print(heap1.heap)
heap1.insert(60)
print(heap1.heap)
heap1.delete()
print(heap1.heap)
heap1.delete()
print(heap1.heap)
print(heap1.deleted)

elements2 = [10, 20, 15, 12, 40, 25, 18]
print(heapify(elements2))

arr = [10, 20, 15, 30, 40]
print(heap_sort(arr))

from random import shuffle
arr = [i for i in range(100001)]
shuffle(arr)
print(heap_sort(arr))


# PRIORITY QUEUE:
#   as insertion and deletion takes O(log(n)) time despite O(n) in Array if we have smaller number
#   higher priority or larger num higher priority queue, to perform these operation we should create
#   min heap, max heap respectively
#   O(log(n))(for insertion or deletion)
