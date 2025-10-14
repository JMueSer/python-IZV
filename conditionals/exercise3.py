num1 = float(input("Dividend: "))
num2 = float(input("Divisor: "))
if num2 == 0:
    raise ValueError("The divisor can't be zero")
else:
    print (f"Answer: {num1 / num2}")