# https://www.youtube.com/watch?v=8EhxxkHzGew

def solve(num, numToStr, numAtIdx, idxNum, string, answer):
    if idxNum == len(num):
        answer.append(string)
        return

    idxNumToStr = numAtIdx[int(num[idxNum])]
    while idxNumToStr < len(numToStr):
        if numToStr[idxNumToStr] == int(num[idxNum]):
            string += chr(idxNumToStr + ord('A'))

            solve(num, numToStr, numAtIdx, idxNum + 1, string, answer)

            string = string[:len(string) - 1]
        idxNumToStr += 1


def numDict(num):  # best: O(3^n), worst: O(4^n)
    numToStr = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
    numAtIdx = {}
    for idx, number in enumerate(numToStr):
        if number not in numAtIdx:
            numAtIdx[number] = idx
    num = str(num)
    answer = []
    solve(num, numToStr, numAtIdx, 0, '', answer)
    print(answer)


numDict(9797)
