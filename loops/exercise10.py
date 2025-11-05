num = int(input("Number: "))
div = 2
while num % div != 0:
    div += 1
if div == num:
    print(f"{num} is prime")
else:
    print(f"{num} isn't prime")