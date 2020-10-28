weight = input('what is your weight in pound?  ')


def kilogram():
    kg = int(weight) * float(.45)
    msg = f'{kg} in kilograms'
    return msg


#print(kilogram())