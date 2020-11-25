user_input = input("convert\nA).C to F\nB).F to C\nType A or B: ")
CtoF = ""
if user_input.lower() == "a":
    CtoF = float(input("write a num:"))
    print((1.8*CtoF)+32)
elif user_input.lower() == "b":
    FtoC = float(input("write a num:"))
    print((FtoC-32)/1.8)
else:
    print("invalid input")
