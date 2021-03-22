# swap: 0 1 5 3 4 2 6, 0 1 4 3 2 5 6 (swap + reverse), 0 1 2 3 4 6 5
#       0 1 3 2 4 5 6
# reverse: 0 1 5 4 3 2 6 (i+1, 6 = i+a[i+1]-1)
def almostSorted(arr):
    a = [0] + arr
    size = len(arr)
    once = False
    i = 0
    s = ''
    while i <= size:
        if a[i+1] < a[i]:
            if once:
                return 'no'

            once = True
            if i +1 == size:
                if a[i+1] < a[i-1]:
                    return 'no'
                return 'yes\nswap ' + str(i) + ' ' + str(i+1)
            if a[i+2] > a[i+1]:  # 0 1 4 3 2 5 6, 0 1 5 3 4 2 6
                for j in range(i+2, size+1):
                    if a[i] < a[j] and a[j] > a[j-1]:
                        s = 'yes\nswap ' + str(i) + ' ' + str(j)
                        if j == size:
                            return s

                    if j==size:
                        return 'no'
                i = j+1
                # swap
            elif a[i+2] < a[i+1] < a[i]:
                s = 'yes\nswap ' + str(i) + ' ' + str(i+2)
                i += 3
                if i+2 == size:
                    return s
                if a[i+3] < a[i]:
                    return 'no'
            else: # 0 1 5 4 3 2 6
                for j in range(i+3, size+1):
                    if a[j] > a[j-1]:
                        s = 'yes\nreverse ' + str(i) + ' ' + str(j-1)
                        if a[j] < a[i]:
                            return 'no'
                if j==size:
                    return 'yes\nreverse ' + str(i) + ' ' + str(j)
                j = i+1
        else:
            i +=1
    if not once:
        return 'yes'
    return s

print(almostSorted([1,4,2,2.5,5]))