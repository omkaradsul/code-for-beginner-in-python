a = input("how's the weather? ")

great = ('hot' in a)  # in is used to check the input from a, in returns with boolean value eg true and false
nice = ('cold' in a)

is_hot = great
is_cold = nice

if is_hot:
    print('its hot outside')
    print('drink more water')

elif is_cold:
    print('its cold outside')
    print('wear warm cloths')

else:
    print('its a lovely day')
print("have a good day")

