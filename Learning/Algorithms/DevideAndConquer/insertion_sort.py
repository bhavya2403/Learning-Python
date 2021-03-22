def insertionSort(arr, n):
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j]= arr[j], arr[j+1]
            else:
                break
    return arr

print(insertionSort([2,45,2,5,6,2,6,8], 8))