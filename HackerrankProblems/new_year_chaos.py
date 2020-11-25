def minimumBribes(q):
    a = [0 for i in range(len(q))]
    count = 0
    for i in range(len(q) - 1):
        swapped = False
        for j in range(len(q) - 1 - i):
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
    print(a)
    print(q)
    print(count)
    for i in a:
        if i >= 3:
            print('Too chaotic')
            break


minimumBribes([2,5,1,3,4])
