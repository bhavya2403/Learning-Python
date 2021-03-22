def howManyGames(prize, d, minimum, s):
    count = 0
    s_in_hand = s
    while True:
        if s_in_hand >= prize:
            count += 1
            s_in_hand -= prize
        else:
            break

        if prize != minimum:
            prize -= d
        if prize < minimum:
            prize = minimum


    return count


print(howManyGames(20, 3, 6, 85))