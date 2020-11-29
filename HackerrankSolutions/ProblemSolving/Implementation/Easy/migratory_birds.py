def migratoryBirds(arr):
    uniques = []
    for i in arr:
        if i not in uniques:
            uniques.append(i)

    arr1 = []
    for i in uniques:
        arr1.append(arr.count(i))

    arr2 = []
    index = 0
    for i in arr1:
        if i == max(arr1):
            arr2.append(uniques[index])
        index += 1

    return min(arr2)


print(migratoryBirds([1,2,3,4,5,4,3,2,1,3,4]))
