class Staff:
    def __init__(self, pPosition, pName, pPay):
        self.position = pPosition
        self.name = pName
        self.pay = pPay
        print('Creating Staff object')

    def __str__(self):
        return "Position = %s,\nName = %s,\nPay = %d" % (self.position, self.name, self.pay)

    def calculatePay(self):
        hours = input('\nEnter the hourly rate for ' + self.name + ': ')
        hourly_rate = input('Enter number of hours worked for %s: ' % self.name)
        self.pay = int(hours) * int(hourly_rate)
        return self.pay


class ManagementStaff(Staff):
    def __init__(self, pName, pPay, pAllowance, pBonus):
        super().__init__('Manager', pName, pPay)
        self.allowance = pAllowance
        self.bonus = pBonus

    def calculatePay(self):
        basicPay = super().calculatePay()
        self.pay = basicPay + self.allowance
        return self.pay

    def calculatePerfBonus(self):
        grade = input('Enter performance grade for %s: ' % self.name)
        if grade == 'A':
            self.bonus = 1000
        else:
            self.bonus = 0
        return self.bonus


class BasicStaff(Staff):
    def __init__(self, pName, pPay):
        super().__init__('Basic', pName, pPay)


peter = BasicStaff('peter', 0)
john = ManagementStaff('john', 0, 1000, 0)

print('Peter\'s Pay = ', peter.calculatePay())
print('John\'s Pay = ', john.calculatePay())
print('John\'s Performance Bonus = ', john.calculatePerfBonus())

print(peter.__str__())
