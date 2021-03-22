def solve(meal_cost, tip_percent, tax_percent):
    print(int(round(meal_cost + (tip_percent+tax_percent)*meal_cost/100)))
