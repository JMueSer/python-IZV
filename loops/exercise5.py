money = float(input("Money invested: "))
interest = float(input("Interest: "))
years = int(input("Years: "))
for x in range(years):
    money *= 1 + interest / 100
    print("Money after " + str(x+1) + " years " + str(round(money, 2)))