# Wpisywanie temperatury przez użytkownika w celsiusach
celsius = int(input('Wprowadź temperature w stopniach celsiusa: '))

#  Przeliczanie temperatury na fahrenheity
fahrenheit = (celsius * 1.8) + 32

# Przeliczanie temperatury na kelviny 
kelvin = celsius + 273.15

#  Wypisywanie temperatury w kelvinach i fahrenheitach
print(f'Temperatura {celsius} °C to {kelvin} K i {fahrenheit} °F')