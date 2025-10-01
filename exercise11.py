money=float(input("Money: "))
interest=float(4)
time=1
while time<=10:
    money=float(money*(1+(interest/100)))
    print(f"Total in year {time}: {money:.2f}€")
    time+=1