amount = int(input("Podaj kwote: "))
discount = int(input("Podaj % zniżki: "))
discount_amount = amount * (discount/100)

price_with_discount = round(amount - discount_amount, 2)
reduction = amount - price_with_discount

print(f"Enter price: {amount}")
print(f"Enter discount % : {discount}")
print(f"Price with discount: {price_with_discount}")
print(f"Reduction: {reduction} ")
