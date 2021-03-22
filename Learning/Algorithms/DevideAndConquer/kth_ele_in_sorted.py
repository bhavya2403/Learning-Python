# not done yet

def median(a, n, k):
     if k//2 >= n-1:
         if not n%2:
             return n//2-1, True
         return n//2, False
     if not k%2:
         return k//2-1, True
     return k//2, False

def handleOne(num, a, n, k):
    pass
    # if n1 == 1 and n2 == 1:
    #     if a[0] >= b[0]:
    #         return a[0] if k == 1 else b[0]
    #     return b[0] if k == 1 else a[0]

def handleTwo(num1, num2, a, n, k):
    pass

def elementInSorted(a, b, n1, n2, k):
    if not a:
        return b[k]
    elif not b:
        return a[k]
    elif k==0:
        return min(a[0], a[0])
    elif k==1:
        return max(a[0], b[0])
    elif n1==1:
        return handleOne(a[0], b, n2, k)
    elif n2==1:
        return handleOne(b[0], a, n1, k)
    elif n1==2:
        return handleTwo(a[0], a[1], b, n2, k)
    elif n2==2:
        return handleTwo(b[0], b[1], a, n1, k)

    med1, c1 = median(a, n1, k)
    med2, c2 = median(b, n2, k)

    if c1 and c2:
        e, f, g, h = a[med1], a[med1+1], b[med2], b[med2+1]
        if e < h < f or g < f < h:
            if g < e:
                return g
            return e
        if h < e:
            return elementInSorted(a[:med1+2], b[med2+2:], med1+1, n2-med2, k-med2+1)
        return
    elif c1 and not c2:
        pass
    elif c2 and not c1:
        pass
    else:
        if a[med1] > b[med2]:
            return elementInSorted(a[:med1+1], b[med2:], med1+1, n2-med2, k-med2+1)
        return elementInSorted(a[med1:], b[:med2+1], n1-med1, med2+1, k-med1+1)