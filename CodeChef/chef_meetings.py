def checkStart(friend):
    hs, ms = int(friend[0][:2]), int(friend[0][3:5])
    if hs == 12:
        hs = 0
    if hs == h:
        if m >= ms:
            return True
        return False
    elif hs < h:
        return True
    return False

def checkEnd(friend):
    he, me = int(friend[2][:2]), int(friend[2][3:5])
    if he == 12:
        he = 0
    if he == h:
        if m <= me:
            return True
        return False
    elif he > h:
        return True
    return False

def solve():
    friend = input().split()
    if p[1] == 'AM' and friend[1] == 'PM':
        return False
    if p[1] == 'PM' and friend[3] == 'AM':
        return False
    if p[1] == 'AM' and friend[3] == 'PM':
        if checkStart(friend):
            return True
        return False
    if p[1] == 'PM' and friend[1] == 'AM':
        if checkEnd(friend):
            return True
        return False
    else:
        if checkStart(friend) and checkEnd(friend):
            return True
        return False

for _ in range(int(input())):
    p = input().split()
    n = int(input())
    h = int(p[0][:2])
    m = int(p[0][3:5])
    if h==12:
        h = 0
    for _ in range(n):
        if solve():
            print(1, end='')
        else:
            print(0, end='')
    print()
