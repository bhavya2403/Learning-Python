def surfaceArea(h, w, a):
    he_or_wi1 = False
    if h == 1 and w == 1:
        return 2 + (4*a[0][0])
    elif h==1 and w!=1:
        count = 2*w + a[0][0] + a[0][w-1]
        he_or_wi1 = True
    elif h!=1 and w==1:
        count = 2*h + a[0][0] + a[h-1][0]
        he_or_wi1 = True
    else:
        count = a[0][0] + a[0][w-1] + a[h-1][0] + a[h-1][w-1] + (2*h*w)

    if he_or_wi1:
        x = 2
    else:
        x=1
    for i in range(h):
        for j in range(w):
            if i == 0 or j==0 or i==h-1 or j == w-1:
                count += x * a[i][j]
            if j > 0:
                count += abs(a[i][j] - a[i][j-1])
            if i > 0:
                count += abs(a[i][j]- a[i-1][j])


    return count


print(surfaceArea(1,1,[[100]]))