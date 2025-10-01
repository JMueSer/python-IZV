bread=float(3.49)
discount=60
num=float(input("Non fresh bread sold: "))
total=float(bread*num)
totald=float(total*(discount/100))
print(f"The usual price would be of {total}€, but since it isn't fresh it's of {totald}€")