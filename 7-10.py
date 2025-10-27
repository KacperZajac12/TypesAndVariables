import random

computer = random.randint(1,6)

while True:
    user = int(input('Zgadnij liczbe wylosowaną przez komputer: '))
    if user != computer:
        print('Nie zgadłeś, spróbuj ponownie')
    else:
        print(f'Zgadłeś, była to liczba: {computer}')
        break