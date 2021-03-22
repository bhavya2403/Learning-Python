class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        a = (sum(i for i in self.scores)) / len(self.scores)
        if 90 <= a <= 100:
            return 'O'
        elif 80 <= a < 90:
            return 'E'
        elif 70 <= a < 80:
            return 'A'
        elif 55 <= a < 70:
            return 'P'
        elif 40 <= a < 55:
            return 'D'
        else:
            return 'T'
