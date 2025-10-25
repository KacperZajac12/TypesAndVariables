total = 8000000000
north = 7200000000
south = total - north

print(f"World population: {total} ")
print(f"Northern Hemisphere:{north} ")

north_in_percents = north/total*100
print(f"Northern Hemishphere in %: {north_in_percents}")