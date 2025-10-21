points = float(input("How many points did you earn: "))
bonus = 2400
if points == 0:
    print("Unacceptable. You have no bonus")
elif points == 0.4:
    print(f"Acceptable. Your bonus is of {bonus * points}€")
elif points >= 0.6:
    print(f"Meritorious. Your bonus is of {bonus * points}€")
else:
    print("You didn't inserted a valid number of points")