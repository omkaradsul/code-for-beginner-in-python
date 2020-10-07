name = input("what is your name? ")
na = len(name)

nice = na < 3
so_big = na > 20

if nice:
    print("minimum 3 character's")
elif so_big:
    print("maximum 20 characters")
else:
    print("name look's good")




