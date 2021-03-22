def insertion_sort(elements): # O(n2)
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i-1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = anchor

    return elements

from random import shuffle
arr = [i for i in range(10001)]
shuffle(arr)
print(insertion_sort(arr))
# print(insertion_sort([5,9,2,1,67,34,88,34]))
