command = ""
started = False
stopped = False
while True:
    command = input("> ")
    if command.lower() == "start":
        if started:
            print("the car has already started.")
        else:
            started = True
            print("The car has started...")
    elif command.lower() == "stop":
        if stopped:
            print("the car has already stopped.")
        elif not started:
            print("The car has not started yet.")
        else:
            stopped = True
            print("The car has stopped")
    elif command.lower() == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to quit the game")
    elif command.lower() == "quit":
        break
    else:
        print("I don't understand the command...")
