def catalan(n):
    if n==0:
        return 1
    cat = [0] * (n+1)
    cat[0] =1
    for i in range(1, n+1):
        if i%2:
            cat[i] = 2*sum(cat[j]*cat[i-j-1] for j in range(i//2)) + cat[i//2]*cat[i//2]
        else:
            cat[i] = 2*sum(cat[j]*cat[i-j-1] for j in range(i//2))

    return cat[n]

print(catalan(3))
