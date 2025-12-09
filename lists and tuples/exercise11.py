a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for x in range(len(a)):
    product += a[x] * b[x]
print("The product of the vectors " + str(a) + " and " + str(b) + " is " + str(product))   