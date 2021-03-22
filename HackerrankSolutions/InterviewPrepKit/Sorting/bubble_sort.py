def countSwaps(a):
    size = len(a)
    swaps = 0
    for i in range(size-1):
        swapped = False
        for j in range(size-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
                swaps += 1
        if not swapped:
            break

    print("Array is sorted in " + str(swaps) + " swaps.\nFirst Element: " +str(a[0])+ "\nLast Element: "+ str(a[size-1]))

print(countSwaps([3,2,1]))