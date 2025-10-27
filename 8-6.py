distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption: '))

total_fuel_consumption = round(distance / fuel_consumption,2)
total_cost = round(total_fuel_consumption * fuel_price,2)

print(f'To travel {distance} kilometers with {fuel_consumption}/100km  with {fuel_price}/1L you need {total_fuel_consumption} litres of fuel and {total_cost} PLN to buy it')