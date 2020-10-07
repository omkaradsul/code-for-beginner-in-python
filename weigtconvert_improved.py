weight = input("what is your weight? ")
unit = input("is it in kg or lbs? ")

k = "kg" in unit
l = "lbs" in unit
if k:
    k = eval(weight) / float(2.2)
    h = f'here is your weight in kg {k}'
    print(h)
elif l:
    l = eval(weight) * float(2.2)
    j = f'here is your weight in lbs {l}'
    print(j)