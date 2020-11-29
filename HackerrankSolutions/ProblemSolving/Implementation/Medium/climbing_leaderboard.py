def climbingLeaderborard(ranked, player):
    ar = [1]
    count = 1
    for i in range(1, len(ranked)):
        if ranked[i] != ranked[i-1]:
            count += 1
        ar.append(count)

    for i in range(len(player)):
        j = 0
        while j < len(ranked) - 1:
            if player[i] >= ranked[0]:
                player[i] = 1
                break
            elif player[i] == ranked[j]:
                player[i] = ar[j]
                break
            elif ranked[j] > player[i] > ranked[j+1]:
                player[i] = ar[j+1]
                break
            elif player[i] == ranked[len(ranked) - 1]:
                player[i] = ar[len(ranked) - 1]
                break
            elif player[i] < ranked[len(ranked) - 1]:
                player[i] = ar[len(ranked) - 1] + 1
                break
            j += 1

    print(ranked)
    print(ar)
    print(player)

    return player


print(climbingLeaderborard([100,100,50,40,40,20,10], [5,25,50,120]))
