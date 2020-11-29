
# function solution is correct and giving right answer for count in every question
# there is some issue with the test cases website solution

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
            return 'Too chaotic'
    return count


print(minimumBribes([1,2,5,3,4,7,8,6]))
