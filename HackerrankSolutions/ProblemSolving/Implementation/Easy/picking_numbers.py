def piclkingNumbers(a):
    ar = []
    a.sort()
    for i in range(len(a)-1):
        ar1 = [a[i]]
        for j in range(i+1, len(a)):
            if a[j] == a[i] or a[j] == a[i] + 1:
                ar1.append(a[j])
            else:
                break
        ar.append(ar1)

    return max(len(i) for i in ar)


print(piclkingNumbers([5,5,5,5,5,5]))
