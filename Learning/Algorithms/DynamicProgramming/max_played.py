def maxGamesPlayed(n):
    count = 0
    while n != 1:
        if not n%2:
            n /= 2
        else:
            n = (n+1)/2
        count += 1

    return count

for i in range(1, 21):
    print(maxGamesPlayed(i))
