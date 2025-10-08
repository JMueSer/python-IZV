product = input("Product: ")
price = float(input("Price: "))
unit = int(input("Units: "))
total = price * unit
print(f"{product}: {unit:3d} units * {price:9.2f}€ = {total:11.2f}€")