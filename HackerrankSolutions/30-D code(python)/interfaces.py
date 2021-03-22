# 64
# 1*64
# 2*32
# 4*16
# 8*8

class Calculator():
    def divisorSum(self, n):
        if n==1:
            return 1
        sumL = 1
        sumR = n
        for j in range(2, n): # j is LHS loop
            if j == 2:
                if n%2 == 0:
                    sumL += 2
                    sumR += n/2
            elif n % j == 0:
                if n/j > j:
                    sumL += j
                    sumR += n / j
                elif n/j == j:
                    sumL += j
                else:
                    break
        return sumL + sumR

obj = Calculator()
print(obj.divisorSum(2))