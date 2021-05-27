n1 = input('enter first name')
n2 = input('enter last name')
a= list(set(n1)&set(n2))
print(set(n1))
print("common alphabets in name:")
for i in a:
    print(i)