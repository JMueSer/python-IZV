phrase = input("Enter a phrase: ")
vocal = input("Enter a vocal: ")
if vocal in 'aeiou':
    mod_phrase = phrase.replace(vocal, vocal.upper())
    print(mod_phrase)