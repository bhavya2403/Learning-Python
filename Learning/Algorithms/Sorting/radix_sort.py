def radix_sort(arr): # O(n*m) m=len_max_num ~ O(n)
    maximum = max(arr)
    len_max_num = len(str(maximum))

    for raised_to10 in range(len_max_num): # O(m)
        aux = [[] for _ in range(10)]
        for ele in arr: # O(n)
            num = ele//(10**raised_to10) % 10
            aux[num].append(ele)

        # flattening the auxiliary array
        k = 0
        for i in range(10): # O(n)
            for j in aux[i]:
                arr[k] = j
                k += 1

    return arr


from random import shuffle
arr = [i for i in range(101)]
shuffle(arr)
print(radix_sort(arr))
