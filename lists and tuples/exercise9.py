word = input("Insert a word: ").lower()
vowels = ['a', 'e', 'i', 'o', 'u']
for vowel in vowels:
    num = 0
    for letter in word:
        if letter == vowel:
            num += 1
    print(f"The vowel {vowel} appears {num} times")   