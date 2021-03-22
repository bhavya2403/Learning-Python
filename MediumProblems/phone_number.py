phone_numbers = {
    "bhavya": 81539_76915,
    "amish": 9999999999,
    "rupal": 0000000000,
}

while True:
    user_input = input("update your phone number list\nType add, remove, get, check or quit: ")
    if user_input.lower() == "add":
        inp1 = input("Enter the name :  ")
        inp2 = input("Enter phone number : ")
        phone_numbers[inp1] = inp2
    elif user_input.lower() == "remove":
        inp3 = input("Enter the name u want to remove from list : ")
        phone_numbers.pop(inp3)
    elif user_input.lower() == "get":
        inp4 = input("Name of the person:")
        print(phone_numbers.get(inp4))
    elif user_input.lower() == "check":
        print(phone_numbers)
    elif user_input.lower() == 'bhavya':
        inp5 = int(input('phone number'))
        for key in phone_numbers.keys():
            if phone_numbers[key] == inp5:
                print(key)
                break
    elif user_input.lower() == "quit":
        break
    else:
        print("I don't understand the command!!")
