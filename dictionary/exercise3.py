fruits = {'Banana':1.35, 'Apple':0.8, 'Pear':0.85, 'Orange':0.7}
fruit = input("Select a fruit: ").capitalize()
num = float(input("How many would you like to have: "))
if fruit in fruits:
    total = fruits[fruit] * num
    print(f"The {num} kilos of {fruit}s will come to a total of {total}€")
else:
    print(f"The fruit {fruit} is not in the dictionary")