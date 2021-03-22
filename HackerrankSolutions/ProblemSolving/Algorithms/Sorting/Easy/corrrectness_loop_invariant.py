def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key): # error: j > 0 replaced with j >= 0
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

