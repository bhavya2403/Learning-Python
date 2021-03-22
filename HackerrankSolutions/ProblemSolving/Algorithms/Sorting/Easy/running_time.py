def insertion_sort(l):
    shifts = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           shifts += 1
           j -= 1
        l[j+1] = key

    return shifts

print(insertion_sort([2,1,3,1,2]))