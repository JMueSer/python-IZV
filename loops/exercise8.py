num = int(input("Number: "))
for x in range(1, num * 2, 2):
    for y in range(x, 0, -2):
        print(y, end=" ")
    print( )