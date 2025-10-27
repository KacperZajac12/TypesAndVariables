swift = input('Enter SWIFT code: ')
print(f'Bank code: {swift[0:4]}')
print(f'Country Code: {swift[4:6]}')
print(f'Location code: {swift[6:8]}')

if len(swift) == 11:
    print(f'Branch code: {swift[8:11]}')