password = input("Password: ")
password2 = input("Confirm Password: ")
if password.lower() == password2.lower():
    print ("The password matches")
else:
    print ("Yhe password doesn't match")