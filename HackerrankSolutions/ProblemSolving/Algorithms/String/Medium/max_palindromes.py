def fact(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def answerQuery(s, l, r):
    s = s[l-1:r]
    d = {}
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1

    arr = []
    odds = 0
    for i in d:
        if d[i] >= 2:
            if d[i]%2 == 0:
                arr.append(d[i])
            else:
                arr.append(d[i]-1)
                odds += 1
        else:
            odds += 1
    answer = 1
    ans1 = 0
    for i in arr:
        if i>=2:
            answer /= fact(i)
        ans1 += i
    if odds > 0:
        answer = answer*fact(ans1)*odds
    else:
        answer *= fact(ans1)

    return answer % 1000000007


s = input()
for _ in range(int(input())):
    l, r = map(int, input().split())
    print(answerQuery(s, l, r))



# pgtwwxxkduujmmsrrzfaayyoni
# pdubsqfaolv
# print(((fact(26)*11)/128)%1000000007)