from play import Card, Deck

d1 = Deck()

x_cards = d1.get_cards(10)

for i in x_cards:
    print(f"{i.get_number()}{i.get_symbol()}")