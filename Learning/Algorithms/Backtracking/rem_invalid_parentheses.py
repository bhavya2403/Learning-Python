def isValid(removed):
    global mainString, n, chars

    lc, rc = 0, 0
    for i in range(n):
        if i not in removed and i not in chars:
            if mainString[i] == '(':
                lc += 1
            else:
                rc += 1
        if rc > lc:
            return False
    return True


def printString(removed):
    global mainString, n

    s = ''
    for i in range(n):
        if i not in removed:
            s += mainString[i]
    print(s, removed)


def solve(count, parCount, removed, idx):
    global mainString, n, chars

    if count == parCount:
        if isValid(removed):
            printString(removed)
            return True
        return False

    answer, tmp = False, False
    for i in range(idx, n):
        tmp = solve(count + 1, parCount, removed | {i}, idx + 1)
        if tmp:
            answer = True

    return answer


def removeInvalidPar():
    global n, mainString, chars

    chars = set()
    for i in range(n):
        if mainString[i] not in {'(', ')'}:
            chars.add(i)

    for parCount in range(n):
        if solve(0, parCount, set(), 0):
            break


mainString = "(v)())()"
n = 7
removeInvalidPar()
