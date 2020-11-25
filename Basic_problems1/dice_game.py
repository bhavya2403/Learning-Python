import random
user_command = ""
while True:
    user_command = input("wanna play dice game? type yes or no. : ")
    if user_command.lower() == "yes":
        print(random.randint(1, 6))
    elif user_command.lower() == "no":
        break
    else:
        print("Invalid Input")

