from math import sqrt

upperBound = 0

def solve(x, xDict):
    pass

def closestPair(points):
    global upperBound
    points.sort()
    (a, b) = points[0][0], points[0][1]
    c, d = points[1][0], points[1][1]
    uppBound = sqrt((a-c)**(a-c) + (b-d)(b-d))
    xDict = {}
    for i in points:
        x,y = i
        if x not in xDict:
            xDict[x] = [y]
        else:
            xDict[x].append(y)