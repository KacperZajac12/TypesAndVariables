speed = int(input('Enter vehicle speed: '))

if speed > 40 and speed < 140:
    valid = True
else: 
    valid = False

print(f'Speed is valid : {valid}')