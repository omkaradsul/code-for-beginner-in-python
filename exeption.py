#try and exception is used to handle errors
try:
    age = int(input("age: "))
    income = int(input("income: "))
    risk = income / age
    print(age)
except ValueError:
    print("please input valid number")
except ZeroDivisionError:
    print("age can't be 0")