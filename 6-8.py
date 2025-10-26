first = input('Enter first letter: ')
last = input('Enter last letter: ')

first_letter_code = ord(first)
last_letter_code = ord(last)

difference = last_letter_code - first_letter_code

if difference == 0:
    number_of_letters = 0
else:
    number_of_letters = difference - 1


print(f"Between {first} and {last} is {number_of_letters} letters")