import random

dice_roll = random.randint(1,6)

if dice_roll == 1 or dice_roll == 6:
    special_number = True
else:
    special_number = False

print(f'Dice rolled: {dice_roll}')
print(f'Special number (1 or 6): {special_number}')