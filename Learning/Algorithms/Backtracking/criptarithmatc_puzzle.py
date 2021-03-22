def calcSum(arr, sumStr, auxDict):
    totSum = 0
    for string in arr:
        num = ''
        for char in string:
            num += str(auxDict[char])
        totSum += int(num)
    checkNum = ''
    for char in sumStr:
        checkNum += str(auxDict[char])

    return int(checkNum) == totSum


def solve(cantAssign0, assignedNum, notAssignedChar, arr, sumStr, answer):
    if not notAssignedChar:
        if calcSum(arr, sumStr, answer):
            return True
        return False

    char = notAssignedChar.pop()
    for num in range(0, 10):
        if not num and char in cantAssign0:
            continue

        if num not in assignedNum:
            answer[char] = num
            assignedNum.add(num)

            if solve(cantAssign0, assignedNum, notAssignedChar, arr, sumStr, answer):
                return True

            assignedNum.remove(num)
            answer[char] = 0
    notAssignedChar.append(char)

    return False


def cryptarithmaticPuzzle(arr, sumStr):
    cantAssign0, assignedNum = set(), set()
    uniques = set()
    for string in arr:
        cantAssign0.add(string[0])
        for j in string:
            uniques.add(j)
    cantAssign0.add(sumStr[0])
    for j in sumStr:
        uniques.add(j)

    notAssignedChar, answer = [], {}
    for idx, char in enumerate(uniques):
        answer[char] = 0
        notAssignedChar.append(char)

    if solve(cantAssign0, assignedNum, notAssignedChar, arr, sumStr, answer):
        return answer
    return "No solution exists"


print(cryptarithmaticPuzzle(["cp", "is", "fun"], "true"))
