card = input('Enter the card notation: ')
card = card.upper()

if len(card) == 2:
    value = card[0]
    suit = card[1]
else:
    value = card[0] + card[1]
    suit = card[2]
if value == 'A':
    value = 'Ace'
if value == 'J':
    value = 'Jack'
if value == 'Q':
    value = 'Queen'
if value == 'K':
    value = 'king'
if suit == 'D':
    suit = 'Diamonds'
if suit == 'H':
    suit = 'Hearts'
if suit == 'S':
    suit = 'Spades'
if suit == 'C':
    suit = 'Clubs'
print(f'{value} of {suit}')