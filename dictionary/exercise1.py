dic = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
coin = input("Enter a tipe of currency: ").capitalize()
if coin in dic:
    print(dic[coin])
else:
    print(f"The currency {coin} is not in the dictionary")