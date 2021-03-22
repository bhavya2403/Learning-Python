def count_sort(elements):  # sc-O(m), tc-O(n+m)
    m = max(elements)
    count = [0] * (m + 1)
    for element in elements:
        count[element] += 1
    i = 0
    j = 0
    while i <= m:
        if count[i] > 0:
            elements[j] = i
            count[i] -= 1
            j += 1
        else:
            i += 1

    return elements


from random import shuffle
arr = [i for i in range(1000001)]
shuffle(arr)
count_sort(arr)
