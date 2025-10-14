age = int(input("Age: "))
wage = float(input("Monthly wage: "))
if age >= 16 and wage >= 1000:
    print("You must pay taxes")
else:
    print("You don't have to pay taxes")