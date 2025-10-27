diameter = int(input('Enter tree circumference in cm: '))

if diameter >= 50:
    cutting = True
else:
    cutting = False

print(f'Tree can be cut down: {cutting}')