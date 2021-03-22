def minimumBribes(q):
    size = len(q)
    a = [0]* size
    count = 0
    for idx in range(size):
        if abs(q[idx] - idx - 1) > 2 and q[idx] - idx - 1 > 0:
            return 'Too chaotic'
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if q[j] > q[j+1]:
                temp = q[j]
                q[j] = q[j + 1]
                q[j + 1] = temp
                temp1 = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp1
                a[j] += 1
                a[j+1] += 1
                count += 1
                swapped = True

        if not swapped:
            break
    return count

print(minimumBribes([2,5,1,3,4]))