def bubble_sort(elements):
    size = len(elements)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                swapped = True

        if not swapped:
            break

    return elements


print(bubble_sort([5, 9, 2, 1, 67, 34, 88, 34]))


# EXCERCISE


def bubbleSort(elemments, key):
    size = len(elements)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j][key] > elements[j + 1][key]:
                temp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = temp
                swapped = True

        if not swapped:
            break

    return elements


elements = [
    {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
    {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
    {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
    {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
]

print(bubbleSort(elements, 'transaction_amount'))
