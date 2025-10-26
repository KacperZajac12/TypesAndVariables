age = int(input('Enter age: '))

if age < 26:
    no_tax = True
else:
    no_tax = False

print(f'Exemption from paying taxes: {no_tax}')