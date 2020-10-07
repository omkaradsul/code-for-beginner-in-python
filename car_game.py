command = ""
starter: False
while True:
    command = input("> ").lower()
    if command == "start":
        if starter:
            print("car is already started")
        else:
            starter: True
            print("car started")
    elif command == "stop":
        if not starter:
            print("car already stopped")
        else:
            starter: False
            print("car stopped")
    elif command == "help":
        print("""start t go
        stop to stop
        quit to quit""")
    elif command == "quit":
        break
    else:
        print("idk")
