import math

print("Wpisz swój wzrost: ")

h = float(input())
hotel_height = 20


d = 3.57 * math.sqrt(h)

h_with_window = h + hotel_height
d_hotel = 3.57 * math.sqrt(h_with_window)

d_pretty = round(d,2)
d_hotel_pretty = round(d_hotel,2)

print(f"Odległość od horyzontu: {d_pretty} km")
print(f"Odłegość od horyzontu, jeżeli znajduje się w hotelu na wysokości 20 metrów = {d_hotel}")