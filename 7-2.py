password = input('Enter password: ')

if len(password) > 8:
    password_ok = True
else:
    password_ok = False

print(f'Password length is valid: {password_ok}')