price = float(input("Price: "))
euro = int(price)
cents = int(round((price - euro) * 100))
print(f"{euro} euros and {cents} cents")