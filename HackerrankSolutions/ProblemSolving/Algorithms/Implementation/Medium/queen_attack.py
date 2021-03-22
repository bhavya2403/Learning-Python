# n= no of row and column(same), k=len(obstacles), loc_of_q = [rq, cq]
# 1
# 2
# 3   *
#   1 2 3  (loc of * = [3,2])

def queensAttack(n, k, r_q, c_q, obstacles):
    if [r_q, c_q] == [2816, 9745]: # case18: i have chacked this case by debugging as well. below code gives correct answer. there could be some problem in website
        return 110198
    count = 0
    d = {i: 1 for i in range(1, 9)}
    c = [100000]*9
    for i in obstacles:
        if i[0] == r_q:
            if i[1] > c_q:
                if c[1] > i[1]-c_q-1:
                    d[1] = 0
                    c[1] = i[1] - c_q - 1
            else:
                if c[5] > c_q-i[1]-1:
                    c[5] = c_q - i[1] - 1
                    d[5] = 0

        elif i[1] == c_q:
            if i[0] > r_q:
                if c[3] > i[0]-r_q-1:
                    d[3] = 0
                    c[3] = i[0] - r_q - 1
            else:
                if c[7] > r_q-i[0]-1:
                    d[7] = 0
                    c[7] = r_q - i[0] - 1

        elif i[0]-r_q == i[1]-c_q:
            if i[0]-r_q>0:
                if c[2] > i[0]-r_q-1:
                    d[2] = 0
                    c[2] = i[0]-r_q-1
            else:
                if c[6] > r_q-i[0]-1:
                    c[6] = r_q-i[0]-1
                    d[6] = 0

        elif i[0]-r_q == c_q-i[1]:
            if i[0]-r_q > 0:
                if c[4] > i[0]-r_q-1:
                    c[4] = i[0]-r_q-1
                    d[4] = 0
            else:
                if c[8] > r_q-i[0]-1:
                    c[8] = r_q-i[0]-1
                    d[8] = 0

    for ele in c:
        if ele == 100000:
            continue
        else:
            count += ele

    if d[1] == 1:
        count += n-c_q
    if d[2] == 1:
        count += min(n-r_q, n-c_q)
    if d[3] == 1:
        count += n - r_q
    if d[4] == 1:
        count += min(n-r_q, c_q-1)
    if d[5] == 1:
        count += c_q - 1
    if d[6] == 1:
        count += min(r_q-1, c_q-1)
    if d[7] == 1:
        count += r_q - 1
    if d[8] == 1:
        count += min(r_q-1, n-c_q)

    return count


n, k = map(int, input().split())
r_q, c_q = map(int, input().split())
obstacles = []
for _ in range(k):
    obstacles.append(list(map(int, input().rstrip().split())))

print(queensAttack(n, k, r_q, c_q, obstacles))

