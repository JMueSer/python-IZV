income = float(input("Anual Income: "))
if income <  10000:
    print("Taxes: 5%")
elif 10000 <= income < 20000:
    print("Taxes: 15%")
elif 20000 <= income < 35000:
    print("Taxes: 20%")
elif 35000 <= income < 60000:
    print("Taxes: 30%")
else:
    print("Taxes: 45%")