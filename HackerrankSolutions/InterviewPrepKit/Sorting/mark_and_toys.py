def maximumToys(n, prices, k):
    count = 0
    summ  = 0
    for price in sorted(prices):
        summ += price
        if summ >= k:
            return count
        count += 1
    return n