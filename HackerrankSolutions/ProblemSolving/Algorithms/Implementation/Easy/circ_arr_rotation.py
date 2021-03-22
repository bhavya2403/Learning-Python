def circularArrayRotation(a, k, queries):
    if k >= len(a):
        k = k % len(a)
    for i in range(k):
        ele = a[len(a)-1]
        a.pop()
        a.insert(0,ele)
        print(a)

    for i in range(len(queries)):
        queries[i] = a[queries[i]]

    return queries


print(circularArrayRotation([1,2,3,4,5], 9, [0]))