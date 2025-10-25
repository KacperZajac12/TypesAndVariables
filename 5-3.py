a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

volume = a*b*c
surface_area = 2*(a*b + b*c + a*c)

print(f"Volume of a cuboid with side a = {a}, side b ={b}, side c {c} is {volume}")
print(f"Surface area of a cuboid with side a = {a}, side b ={b}, side c {c} is {surface_area}")