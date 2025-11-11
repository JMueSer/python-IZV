phrase = input("Enter your phrase: ")
letter = input("Enter your letter: ")
count = 0
for x in phrase:
    if x == letter:
        count += 1
print(f"The letter {letter} appears {count} times")