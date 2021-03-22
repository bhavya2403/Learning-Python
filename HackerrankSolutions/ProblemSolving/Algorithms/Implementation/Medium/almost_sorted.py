def almostSorted(arr):
    s = ''
    n = len(arr)
    i = 0
    swapped = False
    checked = False
    while i < n-1:
        if arr[i+1] < arr[i]:
            if checked:
                return [-1]
            if i==n-2:
                if arr[i-1] < arr[i+1] < arr[i]:
                    s = 'swap ' + str(i+1) + ' ' + str(i+2)
                    break
                else:
                    return [-1]
            elif arr[i+2] > arr[i+1]:
                if i:
                    pass
            for j in range(i+1, n):
                if arr[j] < arr[j-1] and j!=i+1:
                    if i:
                        if arr[i-1] < arr[j] and arr[i] > arr[j-1]:
                           s = 'swap ' + str(i+1) + ' ' + str(j+1)
                           swapped = True
                    else:
                        if arr[i] > arr[j-1]:
                            s = 'swap ' + str(i+1) + ' ' + str(j+1)
                            swapped = True
                    checked = True
                    i = j
                    break
        i += 1
    return s

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    print(almostSorted(arr))

# 5
# 10 20 55 30 40 25
# 55 30 40 25
# 10 20 55 30 40 25 70 60
# 10 20 40 50 30
# 4 2
#
