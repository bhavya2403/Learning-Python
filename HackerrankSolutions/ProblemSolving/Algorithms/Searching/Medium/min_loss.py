def minimumLoss(price):
    sor_price = []
    for i, p in enumerate(price):
        sor_price.append([p, i])
    sor_price.sort()
    d = {}
    for i in range(len(sor_price)):
        d[sor_price[i][0]] = i

    min_loss = 10e16
    for i in range(len(price) - 1):
        buy_val = price[i]
        idx_in_sor_price = d[buy_val] - 1
        sell_val, j = sor_price[idx_in_sor_price]
        if sell_val < buy_val and j > i and buy_val-sell_val < min_loss:
            min_loss = buy_val - sell_val
        if min_loss == 1:
            return 1

    return min_loss


print(minimumLoss([20,7,8,2,5]))