for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    not_solved = 0
    slow = False
    bot = True
    at_least_ont_unsolved = False
    for time in arr:
        if time==-1:
            not_solved+=1
            at_least_ont_unsolved = True
        if time >k:
            slow = True
        if time > 1:
            bot = False
    if not_solved>int(n/2):
        print('Rejected')
    elif slow:
        print('Too Slow')
    elif bot and not at_least_ont_unsolved:
        print('Bot')
    else:
        print('Accepted')
