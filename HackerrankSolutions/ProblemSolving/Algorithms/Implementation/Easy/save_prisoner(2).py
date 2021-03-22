def saveThePrisoner(n, m, s):
    # n is num of prisonors sitting on round table
    # m is number of sweets
    # s is where we start
    return (m+s-1) % n if (m+s-1) % n != 0 else n
# after (16%10) 6 candies left we need to start from 7th
# after (19%7) 5 candies left we are at 1


print(saveThePrisoner(10,16,7))
print(saveThePrisoner(7,19,2))
