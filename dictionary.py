users = []
new_user = {
    'last': 'fermi',
    'first': 'enrico',
    'username': 'efermi',
}
users.append(new_user)
new_user = {
    'last': 'curie',
    'first': 'marie',
    'username': 'mcurie',
}
users.append(new_user)
for user_dict in users:
    for k, v in user_dict.items():#k and v is used for key and value
        print(k + ": " + v)
print("\n")
