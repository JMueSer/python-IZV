name = input("Name: ").lower()
gender = input("Gender: ").lower()
if (gender[0] == "m" and name[0] > "n") or (gender[0] == "f" and name[0] < "m"):
    print("You are in group A")
else:
    print("You are in group B")