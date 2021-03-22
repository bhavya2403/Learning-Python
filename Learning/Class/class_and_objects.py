# by using class we can create our own datatype like string, numbers and bullion
class Student:
    def __init__(self, name, gpa, is_male):
        self.Name = name
        self.gpa = gpa
        self.is_male = is_male

    def on_honor_roll(self):
        if self.gpa >= 8.5:
            return True
        else:
            return False
# class is a template that defines what a student is but a student is actual object with parameters


student1 = Student("bhavya", 8.7, True)
print(student1.Name)
print(student1.on_honor_roll())


class ProgStaff:
    companyName = 'ProgrammingLab'

    def __init__(self, pSalary):
        self.salary = pSalary

    def printInfo(self):
        print("Company name is", ProgStaff.companyName)
        print("Salary is", self.salary)

# here companyName is a class variable and salary is an instance variable and
# __init__, printInfo are the methods defined in the class
# __init__ is an instance method which has self as its parameter
# self essentially represents an instance of the class.
# As different instances have different names and we do not know those names yet


bhav = ProgStaff(2000)
print(bhav.companyName)
ProgStaff.companyName = 'ProgrammingSchool'
print(bhav.companyName)
print(bhav.printInfo())
