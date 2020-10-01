is_goodcredit = True
is_average = False
p = 100000

if is_goodcredit:
    g = 0.1 * p
    g = f'{round(g)} with 10percent downpayment'
    print(g)

elif is_average:
    a = 0.2 * p
    a = f'{round(a)} with 20percent downpayment'
    print(a)

else:
    print('you are not eligible for purchase')