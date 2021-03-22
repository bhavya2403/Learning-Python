def solve(two, three, four):
    global arr
    arr.sort(reverse=True)
    answer = []
    pizNo = 0
    for t in range(two):
        if pizNo + 1 < n:
            answer.append((2, arr[pizNo][1], arr[pizNo + 1][1]))
        pizNo += 2

    for f in range(four):
        if pizNo+3 < n:
            answer.append((4, arr[pizNo][1], arr[pizNo+1][1], arr[pizNo+2][1], arr[pizNo+3][1]))
        pizNo += 4

    for t in range(three):
        if pizNo + 2 < n:
            answer.append((3, arr[pizNo][1], arr[pizNo + 1][1], arr[pizNo + 2][1]))
        pizNo += 3

    return answer


input = open("b_little_bit_of_everything.in", "r")
n, two, three, four = map(int, input.readline().split())
arr = []
for i in range(n):
    a = input.readline().split()
    a.insert(1, i)
    arr.append(a)
input.close()
answer = solve(two, three, four)


output = open("bOutput", "w")
output.write(str(len(answer)))
output.write('\n')
for ans in answer:
    for i in ans:
        output.write(str(i) + ' ')
    output.write('\n')
output.close()
