def insert(min_heap, value):
    min_heap.append(value)
    if len(min_heap) == 2:
        return
    else:
        i = len(min_heap)-1
        while True:
            if i == 1:
                break
            if min_heap[i // 2] > min_heap[i]:
                min_heap[i // 2], min_heap[i] = min_heap[i], min_heap[i // 2]
                i = i // 2
            else:
                break


def delete(min_heap, value):
    i = 0
    for j, element in enumerate(min_heap):
        if element == value:
            i = j
            break
    if i == len(min_heap)-1:
        min_heap.pop()
        return

    min_heap[i] = min_heap.pop()
    while True:
        if len(min_heap) == 2:
            return

        if 2 * i < len(min_heap)-1:
            minimum = min(min_heap[2 * i], min_heap[2 * i + 1])
            if minimum < min_heap[i]:
                if minimum == min_heap[2 * i]:
                    min_heap[2 * i], min_heap[i] = min_heap[i], min_heap[2 * i]
                    i = 2 * i
                else:
                    min_heap[2 * i + 1], min_heap[i] = min_heap[i], min_heap[2 * i + 1]
                    i = 2 * i + 1
            else:
                break
        elif 2 * i == len(min_heap)-1:
            if min_heap[2 * i] < min_heap[i]:
                min_heap[2 * i], min_heap[i] = min_heap[i], min_heap[2 * i]
            break
        else:
            break


heap = [0]
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        insert(heap, arr[1])
    elif arr[0] == 2:
        delete(heap, arr[1])
    else:
        print(heap[1])