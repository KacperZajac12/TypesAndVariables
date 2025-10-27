car_number = input('Enter car registration number: ')
# number = car_number.lower()

if car_number[0:2] == "KR" or car_number[0:2] == "KK":
    is_krakow = True
else:
    is_krakow = False

print(f'Car is from Krakow: {is_krakow}')