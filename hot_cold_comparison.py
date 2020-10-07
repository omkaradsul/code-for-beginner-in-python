b = input("what's the temprature? ")

great = int(b) > 30
nice = int(b) < 10

is_hot = great
is_cold = nice

if is_hot:
    print("it's hot outside")

elif is_cold:
    print("it's cold outside")

else:
    print("it's lovely outside")