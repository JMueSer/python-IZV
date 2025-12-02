lottery = []
for x in range(5):
    lottery.append(int(input("Number of the winned lottery: ")))
lottery.sort()
print("The winning numbers are " + str(lottery))  