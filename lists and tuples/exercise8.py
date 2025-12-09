word = input("Insert a word: ")
reverse_word = word[::-1]
if word == reverse_word:
    print("It's a palindrome")
else:
    print("It isn't a palindrome")   