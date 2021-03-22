for _ in range(int(input())):
    a, b= map(int, input().split())
    if a < b:
        print(1)
    else:
        count = 0
        movesDone = 0
        minMoves = 1000
        lastMoves = 0
        if b == 1:
            movesDone += 1
            b += 1
        while True:
            # if round(c) == int(c):
            #     moves =
            moves = movesDone
            c = a
            while c:
                c = c//b
                moves += 1
            if moves < minMoves:
                minMoves = moves
            if lastMoves < moves and lastMoves:
                print(minMoves)
                break
            movesDone += 1
            b += 1
            lastMoves = moves