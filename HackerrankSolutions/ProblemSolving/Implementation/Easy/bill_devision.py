def bonAppetit(bill, k, b):
    # b is portion of bill anna paid
    # k is index in bill that anna refuses to eat
    billannahastopay = (sum(bill) - bill[k])/2
    refund = b - billannahastopay
    if refund <= 0:
        print("Bon Appetit")
    else:
        print(int(refund))


print(bonAppetit([3,10,2,9], 1, 7))
