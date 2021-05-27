def divide(num1,num2):
    return num1/num2


def multiply(num1,num2):
    return num1*num2


def add(num1,num2):
    return num1+num2


def subtraction(num1,num2):
    return num1-num2

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    num1 = float(input("enter your first number: "))
    num2 = float(input("enter your second number: "))
    # Take input from the user
    task = input("Enter choice(1/2/3/4): ")
    if task in ('1','2','3','4'):
        if task == '1':
            print(add(num1, num2))
        elif task == '2':
            print(subtraction(num1,num2))
        elif task == '3':
            print(multiply(num1,num2))
        elif task == '4':
            print(divide(num1,num2))
    else:
        print('invalid input')