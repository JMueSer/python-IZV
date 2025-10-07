email = input("Email: ")
new_email = email[:email.find('@')] + "@ceu.es"
print(new_email)