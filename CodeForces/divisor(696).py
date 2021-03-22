from math import sqrt

def solve(d):
    x = 1 + d
    while True:
        if all(x % i != 0 for i in range(2, int(sqrt(x)) + 1 if x > 9 else x)):
            break
        x += 1
    y = x + d
    while True:
        if all(y % i != 0 for i in range(2, int(sqrt(y)) + 1 if y > 9 else y)):
            break
        y += 1
    return x * y


for _ in range(int(input())):
    d = int(input())
    print(solve(d))