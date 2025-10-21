print("Types of pizza:")
print("1- Vegetarian")
print("2- Non-vegetarian")
choice = input("Enter the number corresponding to the type of pizza you want: ")
if choice == "1":
    print("Vegetarian pizza ingredients:")
    print("1- Pepper")
    print("2- Tofu")
    ingredient = input("Choose your ingredient: ")
    print("Vegetarian pizza with mozzarella, tomato sauce and ", end="")
    if ingredient == "1":
        print("pepper")
    else:
        print("tofu")
else:
    print("Non-vegetarian pizza ingredients:")
    print("1- Pepperoni")
    print("2- Ham")
    print("3- Salmon")
    ingredient = input("Choose your ingredient: ")
    print("Non-vegetarian pizza with mozzarella, tomato sauce and ", end="")
    if ingredient == "1":
        print("pepperoni")
    elif ingredient == "2":
        print("ham")
    else:
        print("salmon")   