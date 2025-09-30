w=input("Weight: ")
h=input("Height: ")
ans=float(w)/float(h)**2
print(f"The result is: {ans}")
if ans<18.5:
    print("You are underweight")
if 18.5<ans<25:
    print("You are in a healthy weight")
if 25<ans<30:
    print("You are overweight")
if 30<ans<35:
    print("You are obese")
if 35<ans:
    print("You are extremely obese")