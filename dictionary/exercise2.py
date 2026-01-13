name = input('What is your name? ')
age = input('How old are you? ')
address = input('Where do you live? ')
phone = input('What is your phone number? ')
person = {'name': name, 'age': age, 'address': address, 'phone': phone}
print(person['name'], 'is', person['age'], 'years old, lives in', person['address'], 'and his phone number is', person['phone'])