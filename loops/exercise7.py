table1 = int(input("Table 1: "))
table2 = int(input("Table 2: "))
for x in range(table1, table2 + 1):
    print(f"Mult table of {x}: ")
    for y in range(1, 11):
        print(f"{x} x {y} = {x * y}")
    print( )