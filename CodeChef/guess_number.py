import sys
from math import sqrt

def ask(i):
    print(i)
    sys.stdout.flush()
    return int(input())

arr = [i for i in range(1, 10**6+1) if sqrt(i)==int(sqrt(i))]
for _ in range(int(input())):
    for i in arr:
        if ask(i) == 1:
            break
