def climbingLeaderboard(ranked, player):
    i = len(set(ranked)) + 1 # rank
    j = len(ranked) - 1 # index counter
    for idx, score in enumerate(player):
        if ranked[j] > score:
            player[idx] = i
            continue

        while j > 0:
            if ranked[j] > score:
                break
            elif ranked[j] == score:
                player[idx] = i-1
            elif ranked[j] < score:
                player[idx] = i-1
            if ranked[j] != ranked[j-1]:
                i -= 1
            j -= 1

        if score >= ranked[0]:
            player[idx] = 1

    return player


ranked_count = int(input().strip())

ranked = list(map(int, input().rstrip().split()))

player_count = int(input().strip())

player = list(map(int, input().rstrip().split()))

print(climbingLeaderboard(ranked, player))
# print(climbingLeaderboard([100,90,90,80,75,60],[50,65,77,90,102]))