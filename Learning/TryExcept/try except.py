try:
    number = int(input("Enter a number: "))
    print(number)
    value = 10 / 0
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid Input")
