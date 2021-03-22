def findRootsPoly(coef):
    n = len(coef)-1
    return solve(coef, n)

def solve(coef, n):
    if n==1:
        return [-coef[1]/coef[0]]
    fD = fDash(coef, n)
    ranges = solve(fD, n-1)
    return findRoots(ranges, n, coef)

def findRoots(ranges, n, coef):
    ranges = makeRange(ranges, n, coef)
    roots= []
    for i, (x, fx) in enumerate(ranges[:-1]):
        if abs(ranges[i+1][1]) < 10**(-3):
            continue
        if abs(fx) < 10**(-3):
            roots.append(x)
            continue
        if not ((fx>0 and ranges[i+1][1]<0) or (fx<0 and ranges[i+1][1]>0)):
            continue
        root = binSearch(x, ranges[i+1][0], coef, n)
        roots.append(root)
    return roots

def makeRange(ranges, n, coef):
    ans = [(-1000, fOf(-1000, coef, n))]
    for range in ranges:
        ans.append((range, fOf(range, coef, n)))
    return ans + [(1000, fOf(1000, coef, n))]

def fOf(x, coef, n):
    ans = 0
    for i in range(n+1):
        ans += coef[n-i]*(x**i)
    return ans

def fDash(coef, n):
    ans = []
    for i in range(n):
        ans.append(coef[i]*(n-i))
    return ans

def binSearch(l, r, coef, n):
    mid = (l+r)/2
    for i in range(1000):
        fl = fOf(l, coef, n)
        mid = (l+r)/2
        fMid = fOf(mid, coef, n)
        if fMid == 0:
            return mid
        if (fMid>0 and fl<0) or (fMid<0 and fl>0):
            r = mid
        else:
            l = mid
    return mid


print(findRootsPoly([1, -10, 35, -50, 24]))
