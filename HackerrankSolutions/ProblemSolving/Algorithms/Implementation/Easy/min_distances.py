def minimumDistances(a):
    mind = 0
    found_on = False
    for i in range(len(a)-1):
        if a.count(a[i]) > 1:
            for j in range(i+1, len(a)):
                if a[j] == a[i]:
                    if not found_on:
                        found_on = True
                        mind = j-i
                    elif mind > j-i:
                        mind = j-i

    return mind if found_on else -1

print(minimumDistances([7,1,3,4,1,7]))
